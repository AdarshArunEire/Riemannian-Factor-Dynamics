# B3.4b step 2 -- assemble sp500_12bySector.RData in the shape their code reads.
#
# Run experiments/export_for_parent.py first; this reads what it wrote.
#
#   Rscript R/make_panel_rdata.R
#
# WHAT sp500_reproduce.R EXPECTS, read off lines 138-152:
#
#   covariances                  4-D array, (year, month, asset, asset).
#                                Line 141 does
#                                  array(aperm(dta, c(2,1,3,4)), c(d1*d2, q, q))
#                                and R is column-major, so the flattened row
#                                index is month + 12*(year-1). Year MUST be
#                                axis 1 or the panel is silently shuffled in
#                                time -- it still runs, it still prints
#                                plausible numbers, and they are wrong.
#   selected_companies           character vector; gives q and the plot labels.
#   overall_covariance_training  loaded, scaled at line 149, and then NEVER
#                                READ AGAIN in either sp500 script. Dead. Set
#                                to the training-period mean because that is
#                                what the name says; nothing depends on it.
#
# Their line 148 multiplies by 10000. The CSV written by the exporter is
# therefore UNSCALED. Do not "fix" that here.
#
# Their original file was (25, 12, 12, 12) -- the full 2000-2024 download.
# This one is (20, 12, 12, 12), 2000-2019. Equivalent by their own line 155,
# `dta = dta[1:240,,]`, which is the identity on 240 rows. We do not fabricate
# 2020-2024 months that their analysis discards.

root <- getwd()
if (!dir.exists(file.path(root, "reference")))
  stop("run from the repo root:  Rscript R/make_panel_rdata.R")

dest_dir <- file.path(root, "reference", "Riemannian_factor_model-main",
                      "sp500_covariance")
stopifnot(dir.exists(dest_dir))

flat    <- read.csv(file.path(dest_dir, "panel_flat.csv"), stringsAsFactors = FALSE)
tickers <- read.csv(file.path(dest_dir, "tickers.csv"), stringsAsFactors = FALSE)$ticker

months <- flat$month
V      <- as.matrix(flat[, -1])
q      <- length(tickers)
n      <- nrow(V)

stopifnot(n == 240, ncol(V) == q * q, q == 12)
stopifnot(months[1] == "2000-01", months[n] == "2019-12")

n_years <- n %/% 12
covariances <- array(NA_real_, dim = c(n_years, 12, q, q))

for (t in seq_len(n)) {
  y  <- (t - 1) %/% 12 + 1
  mo <- (t - 1) %%  12 + 1
  # the exporter ravels in C order, so index = i*q + j -> fill by ROW
  covariances[y, mo, , ] <- matrix(V[t, ], nrow = q, ncol = q, byrow = TRUE)
}

selected_companies <- tickers
overall_covariance_training <-
  apply(array(aperm(covariances, c(2, 1, 3, 4)), c(n, q, q))[1:(n - 36), , ],
        c(2, 3), mean)

# ---- verify the reshape THEIR way, not ours -------------------------------
# This is the whole point of the file. Replicate lines 141-143 exactly and
# check that row t is month t.
chk <- array(aperm(covariances, c(2, 1, 3, 4)), c(n, q, q))
worst <- 0
for (t in seq_len(n)) {
  worst <- max(worst, max(abs(chk[t, , ] - matrix(V[t, ], q, q, byrow = TRUE))))
}
cat(sprintf("aperm round-trip, worst |diff| over 240 months: %.3e\n", worst))
stopifnot(worst == 0)

sym_err <- max(abs(chk - aperm(chk, c(1, 3, 2))))
eig_min <- min(apply(chk, 1, function(m) min(eigen(m, symmetric = TRUE,
                                                   only.values = TRUE)$values)))
cat(sprintf("symmetry, worst |S - S'|:   %.3e\n", sym_err))
cat(sprintf("smallest eigenvalue anywhere: %.6e  (must be > 0)\n", eig_min))
stopifnot(eig_min > 0)

out <- file.path(dest_dir, "sp500_12bySector.RData")
save(covariances, selected_companies, overall_covariance_training, file = out)

cat(sprintf("\ncovariances dim: (%s)\n", paste(dim(covariances), collapse = ", ")))
cat(sprintf("companies: %s\n", paste(selected_companies, collapse = " ")))
cat(sprintf("written -> %s\n", out))
