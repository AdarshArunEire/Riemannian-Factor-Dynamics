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
# FVU vectors each fit returns are discarded. So highest_value_check needs its
# own loop, and DO_FVU below pays for fifteen more fits. Run once with
# DO_FVU <- FALSE to time it before committing to that.
#
# THE CHECK TO READ FIRST, before RFM. Their script computes LOCF and EWMA
# itself (lines 295-307, 246-262) from the panel we hand it. We already
# computed both in Python. Same input, two independent harnesses, so those
# eight numbers must agree to round-off. If they do not, the fault is in OUR
# evaluation code and not in the data -- and without this check we would have
# read that as a data problem and gone looking in the wrong place.
# experiments/check_parent_run.py does the comparison.

DO_FVU    <- TRUE
FVU_MAX_R <- 15
FVU_CORES <- 1      # 1 = serial. See "PARALLELISM" below before raising it.
FVU_SHARE_MU <- TRUE   # read "THE FRECHET MEAN DOES NOT DEPEND ON r" first

# THE FRECHET MEAN DOES NOT DEPEND ON r, AND THIS IS WHERE ALL THE TIME GOES.
#
#   rfm_bws (BWS_util.R:445) computes mu_hat by mean_on_BWS ONLY when it is not
#   supplied, and mean_on_BWS takes no r. It is called with tol = -1, so the
#   early-exit test `loss_old - loss < tol` never fires and it always runs the
#   full max.iter = 100 iterations. Each iteration draws a 30-matrix batch for
#   the gradient but then evaluates `mean(geod_BWS(X, mu_new))` on ALL 204
#   training matrices (BWS_util.R:252). That full pass, a hundred times, is the
#   expensive part of a fit. The r-dependent part, LYB_fm, is an eigenproblem on
#   a 78-dimensional vech and is comparatively free.
#
#   So their k = 1:15 loop recomputes the same r-independent Frechet mean
#   fifteen times, and every fit costs about the same. main_BWS takes a `mu_hat`
#   argument (main_func.R:73) and forwards it, precisely so you need not.
#
#   FVU_SHARE_MU computes it ONCE on the training block and passes it to all
#   fifteen. That is roughly a 15x saving on this loop -- more than any core
#   count buys -- and it uses their own parameter, with no edit to their code.
#
#   IT IS ALSO THE BETTER EXPERIMENT. mean_on_BWS is stochastic, so recomputing
#   per r confounds the factor-count axis with mean-estimation noise. Holding
#   mu_hat fixed makes r the only thing varying between the fifteen fits, which
#   is what a comparison across r is supposed to mean. It does differ from what
#   their loop does -- declare it -- but their loop discards these vectors, so
#   there is no published FVU-by-r number it could disagree with.
#
# PARALLELISM. The FVU loop is embarrassingly parallel -- fifteen independent
# main_BWS calls, one per r, sharing nothing. Three things to know before
# raising FVU_CORES:
#
#   THE FLOOR IS NOT ZERO. Their own k = 1:15 loop (line 156) is fifteen serial
#   fits inside a file we do not edit, and it is sunk cost no matter what we do
#   here. Parallelising our loop takes the total from ~30 fits to ~16, not to
#   two. Roughly a 45% saving, not a 15x one.
#
#   IT CHANGES THE NUMBERS, AND THAT IS FINE HERE. main_BWS is stochastic:
#   mean_on_BWS draws `idx = sample(n, batch_size)` every iteration
#   (BWS_util.R:242). Run serially after their set.seed(1), r = 1..15 consume
#   one RNG stream in order; run in parallel, each worker gets its own. So the
#   parallel FVU numbers are NOT the serial ones. That is acceptable *for this
#   loop only*, because their script discards the FVU vectors and no published
#   FVU-by-r figure exists to match. It would NOT be acceptable for the
#   Figure 3/4 numbers, which is why nothing above this point is parallelised.
#   clusterSetRNGStream makes our streams reproducible, so re-runs still agree
#   with each other -- just not with the serial run. Say which you did.
#
#   WINDOWS HAS NO fork. PSOCK workers start empty, so each one sets its own
#   working directory and sources main_func.R and BWS_util.R itself. BLAS
#   threads are pinned to 1 per worker: these are 12x12 matrices, threaded BLAS
#   buys nothing at that size, and fifteen workers each spawning threads only
#   fight each other for cache.
#
#   HOW MANY WORKERS. With FVU_SHARE_MU the fits are near-equal in cost, so
#   this is wave arithmetic, not load balancing: 15 tasks over p workers takes
#   ceil(15/p) waves. p=5 and p=7 both take 3; p=8 takes 2. Going from 7 to 8
#   removes a whole wave and 7 buys nothing over 5. So do NOT reflexively
#   reserve a core -- on an 8-physical-core machine the right answer is 8.
#
# MEASURE BEFORE YOU BOTHER. Run once with DO_FVU <- FALSE and read the
# "their script finished in X s" line: X/15 is one fit. If FVU_SHARE_MU already
# collapses the loop to a fraction of that, cores are moot -- take the simple
# serial run and keep the RNG story clean.

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

# ---- highest_value_check --------------------------------------------------
# main_BWS returns FVU_RFM_BWS, FVU_RFM_Euc, FVU_LYB_BWS, FVU_LYB_Euc from one
# call -- both metrics, both models. The P1-LOSS question is whether the
# BW-ranked and Frobenius-ranked orderings of RFM against LYB ever disagree
# along the factor-count axis. No reimplementation: read the four vectors.
#
# CAVEAT that must travel with any disagreement found (AUDIT 4): before a BW
# distance is taken of an LYB prediction it is pushed onto the cone by
# project_to_SPD(x_hat, 1e-6), while the Frobenius comparison uses the raw
# prediction. The two losses are not scoring identical objects, and the repair
# can only help the linear model on the BW side.
if (DO_FVU) {
  cat(sprintf("\nFVU loop, r = 1..%d (another %d fits, %d core%s)\n",
              FVU_MAX_R, FVU_MAX_R, FVU_CORES, if (FVU_CORES > 1) "s" else ""))

  mu_shared <- NULL
  if (FVU_SHARE_MU) {
    n_train <- dim(dta)[1] - 36          # main_BWS slices this way internally
    set.seed(1)
    t_mu <- proc.time()[["elapsed"]]
    mu_shared <- mean_on_BWS(dta[1:n_train, , ], tau = 0.5, tol = -1,
                             max.iter = 100, batch_size = 30, verbose = FALSE)
    cat(sprintf("  shared Frechet mean computed once in %.1f s\n",
                proc.time()[["elapsed"]] - t_mu))
  }

  one_fit <- function (k) {
    res <- main_BWS(dta, r = k, test_size = 36, h = 6, batch_size = 30,
                    max.iter = 100, return_predictions = TRUE,
                    mu_hat = mu_shared)
    data.frame(
      r = k,
      FVU_RFM_BWS = mean(res$FVU_RFM_BWS), FVU_LYB_BWS = mean(res$FVU_LYB_BWS),
      FVU_RFM_Euc = mean(res$FVU_RFM_Euc), FVU_LYB_Euc = mean(res$FVU_LYB_Euc),
      r_hat_RFM = as.numeric(res$r_hat_RFM)[1],
      r_hat_LYB = as.numeric(res$r_hat_LYB)[1])
  }

  t_fvu <- proc.time()[["elapsed"]]
  if (FVU_CORES > 1) {
    library(parallel)
    # capped at physical cores, NOT physical-minus-one: with equal-cost tasks
    # that reservation can cost a full extra wave (see the note above).
    n_cores <- min(FVU_CORES, detectCores(logical = FALSE), FVU_MAX_R)
    cat(sprintf("  using %d workers (PSOCK)\n", n_cores))
    cl <- makeCluster(n_cores)

    # deterministic across re-runs, different from the serial stream -- declare it
    clusterSetRNGStream(cl, iseed = 1)
    clusterExport(cl, c("dta", "one_fit", "parent", "mu_shared"),
                  envir = environment())
    clusterEvalQ(cl, {
      Sys.setenv(OMP_NUM_THREADS = "1", OPENBLAS_NUM_THREADS = "1",
                 MKL_NUM_THREADS = "1")
      setwd(parent)
      source("./main_func.R"); source("./BWS_util.R")
      NULL
    })
    # descending r: cost grows with r, so start the long pole first
    out <- parLapplyLB(cl, rev(seq_len(FVU_MAX_R)), one_fit)
    stopCluster(cl)
    rows <- do.call(rbind, out)
    rows <- rows[order(rows$r), ]
  } else {
    rows <- NULL
    for (k in seq_len(FVU_MAX_R)) {
      tk <- proc.time()[["elapsed"]]
      rows <- rbind(rows, one_fit(k))
      cat(sprintf("  r=%2d  %.1f s\n", k, proc.time()[["elapsed"]] - tk))
    }
  }
  cat(sprintf("  FVU loop total %.1f s  (rng: %s; mu_hat: %s)\n",
              proc.time()[["elapsed"]] - t_fvu,
              if (FVU_CORES > 1) "per-worker streams, iseed=1" else "serial, their set.seed(1)",
              if (FVU_SHARE_MU) "shared, computed once" else "recomputed per r, as they do"))
  rows$BWS_favours <- ifelse(rows$FVU_RFM_BWS < rows$FVU_LYB_BWS, "RFM", "LYB")
  rows$Euc_favours <- ifelse(rows$FVU_RFM_Euc < rows$FVU_LYB_Euc, "RFM", "LYB")
  rows$disagree    <- rows$BWS_favours != rows$Euc_favours

  write.csv(rows, file.path(outdir, "fvu_by_factor.csv"), row.names = FALSE)
  cat("\n-- highest_value_check: does the loss change the ranking? --\n")
  print(format(rows, digits = 4))
  cat(sprintf("\ndisagreements at %d of %d factor counts\n",
              sum(rows$disagree), nrow(rows)))
}

dev.off()
setwd(old_wd)
cat(sprintf("\nwritten -> %s\n", outdir))
