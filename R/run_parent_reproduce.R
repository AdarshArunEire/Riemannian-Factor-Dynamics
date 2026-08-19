# B3.4b step 3 -- run THEIR script on OUR panel, and harvest the numbers.
#
#   Rscript R/run_parent_reproduce.R            # from the repo root
#
# THEIR CODE IS NOT MODIFIED. This harness sources sp500_reproduce.R verbatim
# and then reads the objects it leaves in the global environment. That matters:
# a reproduction where we edited the thing being reproduced proves nothing.
#
# WHY A HARVEST IS NEEDED AT ALL. The published means and medians -- the ones
# in Figures 3 and 4 -- are never printed. They are computed inside sprintf()
# calls that build PLOT LEGEND LABELS (lines 330-336, 379-385, 461-467) and
# then thrown away with the graphics device. So the numbers we want exist for
# microseconds inside a legend. What survives in the global env is the three
# arrays they are computed from:
#
#   BWS_errors  4 x 36   SQUARED BW distance      -- legend reports sqrt()
#   Euc_errors  4 x 36   Frobenius norm           -- legend reports it directly
#   risk_error  4 x 36   already sqrt()'d at 442  -- legend reports it directly
#
# Rows are RFM, LFM, LOCF, EWMA (their model_names, lines 330 / 379 / 461).
# Getting the sqrt convention wrong on BWS_errors is the easy mistake here:
# it is the only one of the three stored squared.
#
# WHAT THIS COSTS. Sourcing their script runs the k = 1:15 loop at line 156 --
# fifteen full main_BWS fits -- and keeps only k = 15 for the factor plots. The
# FVU vectors each fit returns are discarded. The matched-rank follow-up is
# R/run_parent_victory_lap.R: one main_BWS call at r = 15 returns the complete
# rank-1-through-15 curves and writes them beside this harvest.
#
# THE CHECK TO READ FIRST, before RFM. Their script computes LOCF and EWMA
# itself (lines 295-307, 246-262) from the panel we hand it. We already
# computed both in Python. Same input, two independent harnesses, so those
# eight numbers must agree to round-off. If they do not, the fault is in OUR
# evaluation code and not in the data -- and without this check we would have
# read that as a data problem and gone looking in the wrong place.
# experiments/check_parent_run.py does the comparison.

root <- getwd()
if (!dir.exists(file.path(root, "reference")))
  stop("run from the repo root:  Rscript R/run_parent_reproduce.R")

parent <- file.path(root, "reference", "Riemannian_factor_model-main")
outdir <- file.path(root, "results", "raw", "parent_run")
dir.create(outdir, recursive = TRUE, showWarnings = FALSE)

# Clear stale outputs FIRST. An interrupted run leaves a valid-looking
# summary.csv from a previous attempt, and check_parent_run.py would read it
# without complaint -- a reproduction judged on numbers from a different run.
# Their own script writes nothing anywhere, so this directory is the only state
# either half of this pipeline creates.
unlink(list.files(outdir, pattern = "[.](csv|pdf)$", full.names = TRUE))

for (f in c("sp500_covariance/sp500_12bySector.RData",
            "sp500_covariance/VIXCLS.csv",
            "sp500_reproduce.R", "main_func.R", "BWS_util.R")) {
  if (!file.exists(file.path(parent, f)))
    stop(sprintf("missing %s -- run the exporter and make_panel_rdata.R first", f))
}

# NOTE: no on.exit() anywhere in this file. At top level it fires when the
# enclosing top-level expression finishes -- which is immediately -- so
# `on.exit(setwd(old_wd))` would put us back before their script ever ran.
# Cleanup is explicit at the bottom. If this errors midway the working
# directory stays inside their repo, which is what you want for debugging.
old_wd <- getwd()
setwd(parent)                       # their source() calls are all "./"-relative

pdf(file.path(outdir, "parent_plots.pdf"), width = 11, height = 5)

cat("sourcing sp500_reproduce.R  (15 main_BWS fits inside; this is the slow part)\n")
t0 <- proc.time()[["elapsed"]]
source("sp500_reproduce.R", echo = FALSE)
cat(sprintf("their script finished in %.1f s\n\n", proc.time()[["elapsed"]] - t0))

models <- c("RFM", "LFM", "LOCF", "EWMA")

stopifnot(exists("BWS_errors"), exists("Euc_errors"), exists("risk_error"))
stopifnot(all(dim(BWS_errors) == c(4, 36)))

# geod_BWS_core returns NaN on near-identical inputs -- reference/AUDIT.md 7b.
# Count them BEFORE any mean is taken; na.rm would hide a real failure as a
# slightly different average.
nan_count <- c(BWS = sum(!is.finite(BWS_errors)),
               Euc = sum(!is.finite(Euc_errors)),
               risk = sum(!is.finite(risk_error)))
cat("non-finite entries:", paste(names(nan_count), nan_count, sep = "=",
                                 collapse = "  "), "\n")

emit <- function (name, mat) {
  df <- data.frame(model = rep(models, each = ncol(mat)),
                   month = rep(seq_len(ncol(mat)), times = 4),
                   value = as.vector(t(mat)))
  write.csv(df, file.path(outdir, paste0(name, ".csv")), row.names = FALSE)
}
emit("bws_errors_squared", BWS_errors)     # SQUARED -- python takes the sqrt
emit("euc_errors",        Euc_errors)
emit("risk_error",        risk_error)

summ <- data.frame(
  model     = models,
  bw_mean   = rowMeans(sqrt(BWS_errors)),
  bw_median = apply(sqrt(BWS_errors), 1, median),
  frob_mean = rowMeans(Euc_errors),
  frob_median = apply(Euc_errors, 1, median),
  risk_mean = rowMeans(risk_error),
  risk_median = apply(risk_error, 1, median))
write.csv(summ, file.path(outdir, "summary.csv"), row.names = FALSE)

cat("\n-- as their legends would print them (Figures 3 and 4) --\n")
print(format(summ, digits = 4))

dev.off()
setwd(old_wd)
cat(sprintf("\nwritten -> %s\n", outdir))
