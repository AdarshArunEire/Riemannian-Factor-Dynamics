#!/usr/bin/env Rscript

# Run the cloned parent RFM implementation on one externally generated BW
# panel.  The Python orchestrator owns data generation and scoring so RFM and
# RFD receive exactly the same observations and the same declared rank.

args <- commandArgs(trailingOnly = TRUE)
if (length(args) != 10) {
  stop(paste(
    "usage: parent_rfm_bw_worker.R input.csv verified_mean.csv output_dir",
    "n m rank h seed batch_size budget_iter"
  ))
}

input_path <- normalizePath(args[[1]], mustWork = TRUE)
verified_mean_path <- normalizePath(args[[2]], mustWork = TRUE)
output_dir <- args[[3]]
n <- as.integer(args[[4]])
m <- as.integer(args[[5]])
rank <- as.integer(args[[6]])
h <- as.integer(args[[7]])
seed <- as.integer(args[[8]])
batch_size <- as.integer(args[[9]])
budget_iter <- as.integer(args[[10]])

if (any(is.na(c(n, m, rank, h, seed, batch_size, budget_iter)))) {
  stop("integer worker arguments must be finite")
}
if (n < 2 || m < 2 || rank < 1 || h < 1 || h >= n) {
  stop("invalid sample, matrix, rank, or lag dimension")
}

dir.create(output_dir, recursive = TRUE, showWarnings = FALSE)

script_path <- sub("^--file=", "", grep("^--file=", commandArgs(), value = TRUE)[1])
repo_root <- normalizePath(file.path(dirname(script_path), ".."), mustWork = TRUE)
parent_dir <- file.path(repo_root, "reference", "Riemannian_factor_model-main")
source(file.path(parent_dir, "BWS_util.R"), chdir = TRUE)

flat <- as.matrix(read.csv(input_path, header = FALSE, check.names = FALSE))
if (!identical(dim(flat), c(n, m * m))) {
  stop(sprintf("input has shape %s; expected %d x %d", paste(dim(flat), collapse = "x"), n, m * m))
}
if (any(!is.finite(flat))) {
  stop("input contains NaN or Inf")
}
verified_mean_flat <- as.numeric(read.csv(
  verified_mean_path, header = FALSE, check.names = FALSE
))
if (length(verified_mean_flat) != m * m || any(!is.finite(verified_mean_flat))) {
  stop("verified mean has the wrong size or contains NaN/Inf")
}
verified_mean <- matrix(verified_mean_flat, nrow = m, ncol = m, byrow = TRUE)

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

write_status <- function(prefix, status, message = "") {
  message <- gsub("[\r\n]", " ", message)
  writeLines(c(status, message), file.path(output_dir, paste0(prefix, "_status.txt")))
}

write_fit <- function(prefix, model) {
  log_rows <- log_vec_construct(x, model$mu_hat, model$E_lyapunov)
  fitted_rows <- predict_fm(model$A, model$factor_model$mean, log_rows)
  reconstruction <- array(NA_real_, dim = c(n, m, m))
  for (index in seq_len(n)) {
    tangent <- log_to_tangent(fitted_rows[index, ], model$E)
    reconstruction[index, , ] <- Exp_BWS(tangent, model$mu_hat)
  }

  loading_tangents <- array(NA_real_, dim = c(rank, m, m))
  for (index in seq_len(rank)) {
    loading_tangents[index, , ] <- log_to_tangent(model$A[, index], model$E)
  }
  row_mean_tangent <- log_to_tangent(model$factor_model$mean, model$E)

  write_matrix(matrix(as.vector(t(model$mu_hat)), nrow = 1), file.path(output_dir, paste0(prefix, "_mean.csv")))
  write_matrix(log_rows, file.path(output_dir, paste0(prefix, "_log_rows.csv")))
  write_matrix(model$f_hat, file.path(output_dir, paste0(prefix, "_scores.csv")))
  write_array_rows(loading_tangents, file.path(output_dir, paste0(prefix, "_loadings.csv")))
  write_matrix(matrix(as.vector(t(row_mean_tangent)), nrow = 1), file.path(output_dir, paste0(prefix, "_row_mean_tangent.csv")))
  write_array_rows(reconstruction, file.path(output_dir, paste0(prefix, "_reconstruction.csv")))
  write_status(prefix, "ok")
}

run_variant <- function(prefix, expression) {
  tryCatch(
    {
      model <- force(expression)
      write_fit(prefix, model)
    },
    error = function(error) {
      write_status(prefix, "error", conditionMessage(error))
    }
  )
}

set.seed(seed)
run_variant(
  "budget",
  rfm_bws(
    x, r = rank, h = h, batch_size = batch_size,
    max.iter = budget_iter, mu_hat = NULL
  )
)

run_variant(
  "converged",
  rfm_bws(
    x, r = rank, h = h, batch_size = NULL,
    max.iter = budget_iter, mu_hat = verified_mean
  )
)
