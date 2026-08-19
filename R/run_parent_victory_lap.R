# R/run_parent_victory_lap.R
#
# ONE-OFF FAST FOLLOW-UP AFTER run_parent_reproduce.R HAS ALREADY COMPLETED
# WITH DO_FVU <- FALSE.
#
# This deliberately:
#   1. keeps the already-saved Figure 3/4 CSVs;
#   2. does NOT source all of sp500_reproduce.R;
#   3. evaluates only its setup section (before the k=1:15 loop) to recover dta;
#   4. computes ONE shared Frechet mean;
#   5. passes that same mu_hat into r = 1:15.
#
# So the 15 expensive Frechet-mean calculations from the parent reproduction
# are NOT repeated.

DO_FVU    <- TRUE
FVU_MAX_R <- 15
FVU_CORES <- 1

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
# The previous DO_FVU=FALSE run did not save mu_hat to disk, so if that R
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

# -------------------------------------------------------------------------
# r = 1..15 with mu_hat supplied.
# This is the cheap r-dependent part.
# -------------------------------------------------------------------------
one_fit <- function(k) {
  res <- main_BWS(
    dta,
    r = k,
    test_size = 36,
    h = 6,
    batch_size = 30,
    max.iter = 100,
    return_predictions = TRUE,
    mu_hat = mu_shared
  )

  data.frame(
    r = k,
    FVU_RFM_BWS = mean(res$FVU_RFM_BWS),
    FVU_LYB_BWS = mean(res$FVU_LYB_BWS),
    FVU_RFM_Euc = mean(res$FVU_RFM_Euc),
    FVU_LYB_Euc = mean(res$FVU_LYB_Euc),
    r_hat_RFM = as.numeric(res$r_hat_RFM)[1],
    r_hat_LYB = as.numeric(res$r_hat_LYB)[1]
  )
}

cat(sprintf(
  "\nFVU victory lap, r = 1..%d; shared mu_hat supplied to every fit\n",
  FVU_MAX_R
))
t_fvu <- proc.time()[["elapsed"]]

if (FVU_CORES > 1) {
  library(parallel)

  n_cores <- min(FVU_CORES, detectCores(logical = FALSE), FVU_MAX_R)
  cat(sprintf("using %d PSOCK workers\n", n_cores))

  cl <- makeCluster(n_cores)
  clusterSetRNGStream(cl, iseed = 1)
  clusterExport(
    cl,
    c("dta", "one_fit", "parent", "mu_shared"),
    envir = environment()
  )

  clusterEvalQ(cl, {
    Sys.setenv(
      OMP_NUM_THREADS = "1",
      OPENBLAS_NUM_THREADS = "1",
      MKL_NUM_THREADS = "1"
    )
    setwd(parent)
    source("./main_func.R")
    source("./BWS_util.R")
    NULL
  })

  out <- parLapplyLB(cl, rev(seq_len(FVU_MAX_R)), one_fit)
  stopCluster(cl)

  rows <- do.call(rbind, out)
  rows <- rows[order(rows$r), ]

} else {
  rows <- NULL

  for (k in seq_len(FVU_MAX_R)) {
    tk <- proc.time()[["elapsed"]]
    rows <- rbind(rows, one_fit(k))
    cat(sprintf("  r=%2d  %.1f s\n",
                k, proc.time()[["elapsed"]] - tk))
  }
}

cat(sprintf(
  "FVU r-loop finished in %.1f s\n",
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

cat(sprintf(
  "\nDONE. Existing parent results were left untouched.\nFVU written -> %s\n",
  fvu_file
))
