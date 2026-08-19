# R/run_parent_victory_lap.R
#
# ONE-OFF FAST FOLLOW-UP AFTER run_parent_reproduce.R HAS ALREADY COMPLETED.
#
# This deliberately:
#   1. keeps the already-saved Figure 3/4 CSVs;
#   2. does NOT source all of sp500_reproduce.R;
#   3. evaluates only its setup section (before the k=1:15 loop) to recover dta;
#   4. computes ONE shared Frechet mean;
#   5. calls main_BWS once at r=15 and retains its four complete rank curves.
#
# The former version called main_BWS at every r and stored mean(FVU[1:r]).
# Those were prefix means, not rank-r FVU values. The corrected result is the
# vector returned by the single r=15 fit. A legacy prefix-mean file can be
# recovered exactly by v_r = r * mean_r - (r - 1) * mean_{r-1}, provided the
# same mu_hat was supplied to every fit, as it was in the recorded run.

FVU_MAX_R <- 15

# From the audited parent script: expensive k=1:15 loop begins at line 156.
SETUP_LAST_LINE <- 155L

root <- getwd()
if (!dir.exists(file.path(root, "reference")))
  stop("run from the repo root:  Rscript R/run_parent_victory_lap.R")

parent <- file.path(root, "reference", "Riemannian_factor_model-main")
outdir <- file.path(root, "results", "raw", "parent_run")

summary_file <- file.path(outdir, "summary.csv")
if (!file.exists(summary_file))
  stop("saved parent_run/summary.csv not found -- the earlier reproduction must finish first")

for (f in c("sp500_covariance/sp500_12bySector.RData",
            "sp500_covariance/VIXCLS.csv",
            "sp500_reproduce.R", "main_func.R", "BWS_util.R")) {
  if (!file.exists(file.path(parent, f)))
    stop(sprintf("missing %s", f))
}

cat("\n============================================================\n")
cat("VICTORY LAP: USING THE ALREADY-SAVED PARENT HARVEST\n")
cat("NO 15-FIT PARENT REPRODUCTION WILL BE RUN\n")
cat("============================================================\n\n")

cat("-- saved Figure 3/4 summary --\n")
summ <- read.csv(summary_file, stringsAsFactors = FALSE)
print(format(summ, digits = 4))

old_wd <- getwd()
setwd(parent)

# -------------------------------------------------------------------------
# Recreate ONLY the setup/data objects from their script.
#
# We cannot get dta from summary.csv because the old harness saved only the
# harvested errors/summary, not the in-memory training panel. But we also do
# not need to rerun the expensive fitting loop just to recover it.
# -------------------------------------------------------------------------
src <- readLines("sp500_reproduce.R", warn = FALSE)

if (length(src) < SETUP_LAST_LINE)
  stop("sp500_reproduce.R is shorter than expected; check the audited loop boundary")

cat(sprintf(
  "\nrebuilding data/setup only from sp500_reproduce.R lines 1:%d ...\n",
  SETUP_LAST_LINE
))

setup_code <- paste(src[seq_len(SETUP_LAST_LINE)], collapse = "\n")
eval(parse(text = setup_code), envir = .GlobalEnv)

if (!exists("dta", envir = .GlobalEnv, inherits = FALSE))
  stop("setup section did not create `dta`; check SETUP_LAST_LINE against parent script")

dta <- get("dta", envir = .GlobalEnv)

# Ensure their functions are available. Cheap: this sources definitions only.
source("./main_func.R")
source("./BWS_util.R")

# -------------------------------------------------------------------------
# THE ONLY FRECHET-MEAN CALCULATION IN THIS SCRIPT.
#
# The previous parent reproduction did not save mu_hat to disk, so if that R
# process is already gone there is nothing to reload. One recomputation is
# therefore necessary. Crucially, it is done ONCE, not once per r.
# -------------------------------------------------------------------------
n_train <- dim(dta)[1] - 36

set.seed(1)
cat("\ncomputing ONE shared Frechet mean ...\n")
t_mu <- proc.time()[["elapsed"]]

mu_shared <- mean_on_BWS(
  dta[1:n_train, , ],
  tau = 0.5,
  tol = -1,
  max.iter = 100,
  batch_size = 30,
  verbose = FALSE
)

cat(sprintf(
  "shared Frechet mean finished in %.1f s\n",
  proc.time()[["elapsed"]] - t_mu
))

# One r=15 call returns all four curves at ranks 1,...,15. Calling once per
# rank is both redundant and the source of the old prefix-mean reporting bug.
cat(sprintf("\nFVU victory lap: one r=%d fit with shared mu_hat\n", FVU_MAX_R))
t_fvu <- proc.time()[["elapsed"]]
res <- main_BWS(
  dta,
  r = FVU_MAX_R,
  test_size = 36,
  h = 6,
  batch_size = 30,
  max.iter = 100,
  return_predictions = TRUE,
  mu_hat = mu_shared
)

curves <- list(
  FVU_RFM_BWS = as.numeric(res$FVU_RFM_BWS),
  FVU_LYB_BWS = as.numeric(res$FVU_LYB_BWS),
  FVU_RFM_Euc = as.numeric(res$FVU_RFM_Euc),
  FVU_LYB_Euc = as.numeric(res$FVU_LYB_Euc)
)
curve_lengths <- vapply(curves, length, integer(1))
if (any(curve_lengths != FVU_MAX_R))
  stop(sprintf("unexpected FVU curve lengths: %s",
               paste(curve_lengths, collapse = ",")))
if (any(!is.finite(unlist(curves, use.names = FALSE))))
  stop("main_BWS returned a non-finite FVU")

rows <- data.frame(
  r = seq_len(FVU_MAX_R),
  FVU_RFM_BWS = curves$FVU_RFM_BWS,
  FVU_LYB_BWS = curves$FVU_LYB_BWS,
  FVU_RFM_Euc = curves$FVU_RFM_Euc,
  FVU_LYB_Euc = curves$FVU_LYB_Euc
)

cat(sprintf(
  "FVU curve fit finished in %.1f s\n",
  proc.time()[["elapsed"]] - t_fvu
))

rows$BWS_favours <- ifelse(
  rows$FVU_RFM_BWS < rows$FVU_LYB_BWS, "RFM", "LYB"
)
rows$Euc_favours <- ifelse(
  rows$FVU_RFM_Euc < rows$FVU_LYB_Euc, "RFM", "LYB"
)
rows$disagree <- rows$BWS_favours != rows$Euc_favours

fvu_file <- file.path(outdir, "fvu_by_factor.csv")
write.csv(rows, fvu_file, row.names = FALSE)

cat("\n-- highest_value_check: does the loss change the ranking? --\n")
print(format(rows, digits = 4))

cat(sprintf(
  "\ndisagreements at %d of %d factor counts\n",
  sum(rows$disagree), nrow(rows)
))

setwd(old_wd)

cat(sprintf("\nDONE. FVU written -> %s\n", fvu_file))
