# Metric calibration, step 1 of 2.
#
# Generates a fixed set of SPD pairs and scores them with the PARENT'S OWN
# geod_BWS_core, then writes both the matrices and the answers to CSV. A
# pytest (py/tests/test_parity_with_parent.py) reads that file and checks our
# bw_dist2 agrees.
#
# This is deliberately the first thing done in the reproduction: it needs no
# price data, takes seconds, and if it fails then every comparison downstream
# is meaningless. Two implementations of the same formula, one number.
#
#   Rscript R/calib_bw_metric.R
#
# Requires their BWS_util.R, which needs: maotai, expm, deSolve.

set.seed(20260816)

parent <- "./reference/Riemannian_factor_model-main/BWS_util.R"
if (!file.exists(parent)) {
  stop(paste("cannot find", parent, "-- see reference/PROVENANCE.md"))
}
source(parent)

out_dir <- "./results/final"
dir.create(out_dir, showWarnings = FALSE, recursive = TRUE)

#' random SPD with a controlled condition number, log-spaced spectrum
rand_spd <- function (m, cond) {
  Q <- qr.Q(qr(matrix(rnorm(m * m), m, m)))
  lam <- exp(seq(log(1), log(cond), length.out = m))
  Q %*% diag(lam) %*% t(Q)
}

# Cases chosen to stress the two things that can differ between the
# implementations: conditioning (they sqrtm a NON-symmetric product; we do
# not), and cancellation (d2 is a difference of large traces, so nearly-equal
# pairs are where relative accuracy dies).
cases <- list()
k <- 0
for (m in c(3, 12)) {
  for (cond in c(1e1, 1e3, 1e5)) {
    k <- k + 1; cases[[k]] <- list(tag = "generic", m = m, cond = cond,
                                   X = rand_spd(m, cond), Y = rand_spd(m, cond))
    X <- rand_spd(m, cond)
    k <- k + 1; cases[[k]] <- list(tag = "identical", m = m, cond = cond,
                                   X = X, Y = X)
    E <- matrix(rnorm(m * m), m, m); E <- (E + t(E)) / 2
    k <- k + 1; cases[[k]] <- list(tag = "near", m = m, cond = cond,
                                   X = X, Y = X + 1e-6 * norm(X, "F") * E / norm(E, "F"))
  }
}

rows <- list()
for (i in seq_along(cases)) {
  cs <- cases[[i]]
  d  <- geod_BWS_core(cs$X, cs$Y)      # THEIR function. Returns the distance.
  rows[[i]] <- data.frame(
    case = i, tag = cs$tag, m = cs$m, cond = cs$cond,
    d2_parent = Re(d)^2,
    d2_imag   = Im(as.complex(d)^2),   # nonzero would mean their sqrtm went complex
    X = paste(format(as.vector(cs$X), digits = 17), collapse = ";"),
    Y = paste(format(as.vector(cs$Y), digits = 17), collapse = ";"),
    stringsAsFactors = FALSE
  )
}

res <- do.call(rbind, rows)
write.csv(res, file.path(out_dir, "parent_bw_reference.csv"), row.names = FALSE)

cat("wrote", file.path(out_dir, "parent_bw_reference.csv"), "\n")
cat("cases:", nrow(res), "\n")
cat("any complex leakage:", any(abs(res$d2_imag) > 0), "\n")
print(res[, c("case", "tag", "m", "cond", "d2_parent")])
