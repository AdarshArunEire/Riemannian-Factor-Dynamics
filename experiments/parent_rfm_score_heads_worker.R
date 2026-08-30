#!/usr/bin/env Rscript

# Export the exact parent projected-score representation at every expanding
# APP-FIN origin.  Python applies both the parent's OLS VAR head and the new
# Kalman head to these same scores.  The first global BW centre is retained at
# every later origin, exactly as dyn_RFM does.

args <- commandArgs(trailingOnly = TRUE)
if (length(args) != 11) {
  stop(paste(
    "usage: parent_rfm_score_heads_worker.R panel.csv output_dir n m rank h",
    "forecast_months seed batch_size max_iter resume"
  ))
}

input_path <- normalizePath(args[[1]], mustWork = TRUE)
output_dir <- args[[2]]
n <- as.integer(args[[3]])
m <- as.integer(args[[4]])
rank <- as.integer(args[[5]])
h <- as.integer(args[[6]])
forecast_months <- as.integer(args[[7]])
seed <- as.integer(args[[8]])
batch_size <- as.integer(args[[9]])
max_iter <- as.integer(args[[10]])
resume <- identical(toupper(args[[11]]), "TRUE")

if (any(is.na(c(n, m, rank, h, forecast_months, seed, batch_size, max_iter)))) {
  stop("integer worker arguments must be finite")
}
if (n < 3 || m < 2 || rank < 1 || h < 1 || forecast_months < 1 ||
    forecast_months >= n) {
  stop("invalid sample, matrix, rank, lag, or forecast dimension")
}

script_path <- sub("^--file=", "", grep("^--file=", commandArgs(), value = TRUE)[1])
repo_root <- normalizePath(file.path(dirname(script_path), ".."), mustWork = TRUE)
parent_dir <- file.path(repo_root, "reference", "Riemannian_factor_model-main")
source(file.path(parent_dir, "main_func.R"), chdir = TRUE)
source(file.path(parent_dir, "BWS_util.R"), chdir = TRUE)

flat <- as.matrix(read.csv(input_path, header = FALSE, check.names = FALSE))
if (!identical(dim(flat), c(n, m * m)) || any(!is.finite(flat))) {
  stop("input panel has the wrong shape or contains NaN/Inf")
}
x <- array(NA_real_, dim = c(n, m, m))
for (index in seq_len(n)) {
  x[index, , ] <- matrix(flat[index, ], nrow = m, ncol = m, byrow = TRUE)
}

write_matrix <- function(value, path) {
  write.table(
    as.matrix(value), file = path, sep = ",", row.names = FALSE,
    col.names = FALSE, quote = FALSE, na = "NaN"
  )
}

write_array_rows <- function(value, path) {
  rows <- matrix(NA_real_, nrow = dim(value)[1], ncol = prod(dim(value)[-1]))
  for (index in seq_len(dim(value)[1])) {
    rows[index, ] <- as.vector(t(value[index, , ]))
  }
  write_matrix(rows, path)
}

read_square <- function(path) {
  flat_value <- as.numeric(as.matrix(read.csv(
    path, header = FALSE, check.names = FALSE
  )))
  if (length(flat_value) != m * m || any(!is.finite(flat_value))) {
    stop(paste("invalid cached square matrix:", path))
  }
  matrix(flat_value, nrow = m, ncol = m, byrow = TRUE)
}

dir.create(output_dir, recursive = TRUE, showWarnings = FALSE)
set.seed(seed)
mu_hat <- NULL

for (offset in 0:(forecast_months - 1)) {
  target_index <- n - forecast_months + offset
  origin_dir <- file.path(output_dir, sprintf("target_%03d", target_index))
  dir.create(origin_dir, recursive = TRUE, showWarnings = FALSE)
  status_path <- file.path(origin_dir, "status.txt")
  required <- file.path(origin_dir, c(
    "scores.csv", "loadings.csv", "row_mean_tangent.csv", "mean.csv",
    "var_score.csv", "var_forecast.csv", "rng_state.rds", "status.txt"
  ))
  status_ok <- file.exists(status_path) &&
    identical(readLines(status_path, n = 1, warn = FALSE), "ok")
  if (resume && status_ok && all(file.exists(required))) {
    if (is.null(mu_hat)) {
      mu_hat <- read_square(file.path(origin_dir, "mean.csv"))
    }
    assign(".Random.seed", readRDS(file.path(origin_dir, "rng_state.rds")),
           envir = .GlobalEnv)
    cat("parent score origin", target_index, "reused\n")
    next
  }
  tryCatch(
    {
      model <- main_BWS(
        x, r = rank, test_size = forecast_months - offset, h = h,
        batch_size = batch_size, max.iter = max_iter, mu_hat = mu_hat
      )
      if (is.null(mu_hat)) {
        mu_hat <- model$mu_hat
      }
      scores <- model$Factors
      transition <- VAR1(scores)
      var_score <- as.vector(c(1, tail(scores, 1)) %*% transition)
      loading_tangents <- array(NA_real_, dim = c(rank, m, m))
      for (index in seq_len(rank)) {
        loading_tangents[index, , ] <- log_to_tangent(model$V[, index], model$E)
      }
      row_mean_tangent <- log_to_tangent(model$z_bar, model$E)
      forecast_tangent <- row_mean_tangent
      for (index in seq_len(rank)) {
        forecast_tangent <- forecast_tangent + var_score[index] * loading_tangents[index, , ]
      }
      var_forecast <- Exp_BWS(forecast_tangent, mu_hat)

      write_matrix(scores, file.path(origin_dir, "scores.csv"))
      write_array_rows(loading_tangents, file.path(origin_dir, "loadings.csv"))
      write_matrix(
        matrix(as.vector(t(row_mean_tangent)), nrow = 1),
        file.path(origin_dir, "row_mean_tangent.csv")
      )
      write_matrix(
        matrix(as.vector(t(mu_hat)), nrow = 1),
        file.path(origin_dir, "mean.csv")
      )
      write_matrix(matrix(var_score, nrow = 1), file.path(origin_dir, "var_score.csv"))
      write_matrix(
        matrix(as.vector(t(var_forecast)), nrow = 1),
        file.path(origin_dir, "var_forecast.csv")
      )
      saveRDS(.Random.seed, file.path(origin_dir, "rng_state.rds"))
      writeLines(c("ok", ""), status_path)
    },
    error = function(error) {
      writeLines(c("error", gsub("[\r\n]", " ", conditionMessage(error))), status_path)
      quit(status = 1)
    }
  )
  cat("parent score origin", target_index, "complete\n")
}
