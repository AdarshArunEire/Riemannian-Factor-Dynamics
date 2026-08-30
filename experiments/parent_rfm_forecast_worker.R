#!/usr/bin/env Rscript

# Exact parent APP-FIN forecast arm. This deliberately calls the cloned
# dyn_RFM implementation so the global-centre and VAR(1) conventions remain
# those of the published repository.

args <- commandArgs(trailingOnly = TRUE)
if (length(args) != 11) {
  stop(paste(
    "usage: parent_rfm_forecast_worker.R input.csv output.csv",
    "n m rank h test_size seed batch_size max_iter source_file"
  ))
}

input_path <- normalizePath(args[[1]], mustWork = TRUE)
output_path <- args[[2]]
n <- as.integer(args[[3]])
m <- as.integer(args[[4]])
rank <- as.integer(args[[5]])
h <- as.integer(args[[6]])
test_size <- as.integer(args[[7]])
seed <- as.integer(args[[8]])
batch_size <- as.integer(args[[9]])
max_iter <- as.integer(args[[10]])
source_path <- normalizePath(args[[11]], mustWork = TRUE)
status_path <- paste0(output_path, ".status")

if (any(is.na(c(n, m, rank, h, test_size, seed, batch_size, max_iter)))) {
  stop("integer worker arguments must be finite")
}
if (n < 3 || m < 2 || rank < 1 || h < 1 || h >= n ||
    test_size < 1 || test_size >= n) {
  stop("invalid sample, matrix, rank, lag, or test dimension")
}

flat <- as.matrix(read.csv(input_path, header = FALSE, check.names = FALSE))
if (!identical(dim(flat), c(n, m * m)) || any(!is.finite(flat))) {
  stop("forecast input has the wrong shape or contains NaN/Inf")
}

x <- array(NA_real_, dim = c(n, m, m))
for (index in seq_len(n)) {
  x[index, , ] <- matrix(flat[index, ], nrow = m, ncol = m, byrow = TRUE)
}

parent_dir <- dirname(source_path)
source(file.path(parent_dir, "main_func.R"), chdir = TRUE)
source(source_path, chdir = TRUE)
set.seed(seed)

tryCatch(
  {
    forecast <- dyn_RFM(
      x, r = rank, test_size = test_size, h = h,
      batch_size = batch_size, max.iter = max_iter
    )
    rows <- matrix(NA_real_, nrow = test_size, ncol = m * m)
    for (index in seq_len(test_size)) {
      rows[index, ] <- as.vector(t(forecast[index, , ]))
    }
    if (any(!is.finite(rows))) {
      stop("parent forecast contains NaN/Inf")
    }
    write.table(
      rows, file = output_path, sep = ",", row.names = FALSE,
      col.names = FALSE, quote = FALSE, na = "NaN"
    )
    writeLines(c("ok", ""), status_path)
  },
  error = function(error) {
    writeLines(c("error", gsub("[\r\n]", " ", conditionMessage(error))), status_path)
    quit(status = 1)
  }
)
