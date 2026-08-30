# N-00 / B3.2 -- run the parent's SPD simulation suite without editing upstream.
#
# From the repository root:
#
#   Rscript R/run_parent_simulations.R --check   # no numerical results
#   Rscript R/run_parent_simulations.R           # recorded 300-replicate sweep
#
# Why a wrapper is necessary:
#   1. the parent scripts require their own directory as the working directory;
#   2. ./save/ is absent from the upstream repository;
#   3. BWS_simulation.R contains one bare sink() inside each worker, which fails
#      when no worker sink is active;
#   4. sim_do.R sources the complete four-case sweep four times even though its
#      `type` variable is unused by BWS_simulation.R. The same files are
#      overwritten each time, so only the fourth pass survives.
#
# The wrapper copies the four consumed upstream files into results/raw/n00,
# removes exactly the one proven stray sink() in that disposable copy, and runs
# the complete four-case sweep once with the final driver seed (5566 + 4).
# Upstream files remain byte-for-byte untouched. Parallel workers remain
# unseeded, exactly as in the parent implementation, so this is distributional
# reproduction rather than bitwise reproduction.

args <- commandArgs(trailingOnly = TRUE)
unknown <- setdiff(args, "--check")
if (length(unknown))
  stop(sprintf("unknown argument(s): %s", paste(unknown, collapse = ", ")))
check_only <- "--check" %in% args

root <- normalizePath(getwd(), winslash = "/", mustWork = TRUE)
root_markers <- c("pyproject.toml", "R", "py", "reference")
if (!all(file.exists(file.path(root, root_markers))))
  stop("run from the repository root: Rscript R/run_parent_simulations.R")

parent <- file.path(root, "reference", "Riemannian_factor_model-main")
needed_files <- c(
  "BWS_simulation.R",
  "BWS_util.R",
  "main_func.R",
  "sim_do.R",
  "sim_summary.R"
)
missing_files <- needed_files[!file.exists(file.path(parent, needed_files))]
if (length(missing_files))
  stop(sprintf("missing upstream file(s): %s", paste(missing_files, collapse = ", ")))

needed_packages <- c("foreach", "doParallel", "maotai", "expm", "deSolve")
package_ok <- vapply(needed_packages, requireNamespace, logical(1), quietly = TRUE)
blas <- unname(extSoftVersion()[["BLAS"]])
if (is.null(blas) || !nzchar(blas))
  blas <- "bundled Rblas.dll (see VERSIONS.md)"
cat("R:", R.version.string, "\n")
cat("BLAS:", blas, "\n")
cat("Packages:\n")
for (i in seq_along(needed_packages))
  cat(sprintf("  %-12s %s\n", needed_packages[[i]], if (package_ok[[i]]) "OK" else "MISSING"))
if (!all(package_ok))
  stop(sprintf(
    "install missing packages with: Rscript -e \"renv::install(c(%s)); renv::snapshot()\"",
    paste(sprintf("'%s'", needed_packages[!package_ok]), collapse = ", ")
  ))

# Parse every consumed script before any result directory is created.
invisible(lapply(file.path(parent, needed_files), parse))

sim_lines <- readLines(file.path(parent, "BWS_simulation.R"), warn = FALSE)
sink_line <- grep("^[[:space:]]*sink\\(\\)[[:space:]]*$", sim_lines)
if (length(sink_line) != 1L)
  stop(sprintf("expected exactly one bare sink() in BWS_simulation.R; found %d", length(sink_line)))

driver <- paste(readLines(file.path(parent, "sim_do.R"), warn = FALSE), collapse = "\n")
if (!grepl("for \\(type in c\\(1:4\\)\\)", driver) ||
    !grepl("source\\(\"\\./BWS_simulation.R\"\\)", driver))
  stop("sim_do.R no longer has the audited four-pass structure; re-audit before running")
sim_expr <- parse(text = sim_lines)
if ("type" %in% all.vars(sim_expr)) {
  stop("BWS_simulation.R now appears to consume `type`; re-audit before running")
}

if (check_only) {
  cat("\nCHECK PASSED: inputs parse, packages exist, and audited patch points match.\n")
  quit(status = 0L)
}

outdir <- file.path(root, "results", "raw", "n00")
savedir <- file.path(outdir, "save")
workdir <- file.path(outdir, "upstream_work")
existing <- c(
  list.files(savedir, pattern = "\\.RData$", full.names = TRUE),
  file.path(outdir, c("simulation.log", "simulation_plots.pdf", "summary_plots.pdf"))
)
existing <- existing[file.exists(existing)]
if (length(existing))
  stop("N-00 raw output already exists; preserve or move it before starting a new recorded run")

dir.create(savedir, recursive = TRUE, showWarnings = FALSE)
dir.create(workdir, recursive = TRUE, showWarnings = FALSE)
copied <- file.copy(
  file.path(parent, needed_files),
  file.path(workdir, needed_files),
  overwrite = FALSE
)
if (!all(copied))
  stop("could not create the disposable upstream work copy")

patched <- sim_lines
patched[sink_line] <- "                          # HARNESS: removed stray bare sink()"
writeLines(patched, file.path(workdir, "BWS_simulation.R"), useBytes = TRUE)

# The parent scripts write to ./save relative to their working directory.
if (!dir.create(file.path(workdir, "save"), showWarnings = FALSE))
  stop("could not create work/save")

upstream_md5 <- tools::md5sum(file.path(parent, needed_files))
runner_md5 <- unname(tools::md5sum(file.path(root, "R", "run_parent_simulations.R")))
package_versions <- vapply(
  needed_packages,
  function(pkg) as.character(utils::packageVersion(pkg)),
  character(1)
)
manifest <- c(
  sprintf("generated_utc=%s", format(Sys.time(), tz = "UTC", usetz = TRUE)),
  sprintf("R=%s", R.version.string),
  sprintf("BLAS=%s", blas),
  sprintf("upstream=%s", parent),
  "execution=one complete four-case pass; final sim_do seed 5570",
  "patch=removed exactly one worker-side bare sink() from disposable copy",
  "parallel_rng=upstream unseeded PSOCK workers; distributional, not bitwise reproduction",
  sprintf("runner_md5=%s", runner_md5),
  "package_versions:",
  paste(names(package_versions), package_versions, sep = "="),
  "upstream_md5:",
  paste(names(upstream_md5), upstream_md5, sep = "=")
)
writeLines(manifest, file.path(outdir, "manifest.txt"))

old_wd <- getwd()
setwd(workdir)
on.exit(setwd(old_wd), add = TRUE)

log_path <- file.path(outdir, "simulation.log")
log_con <- file(log_path, open = "wt")
sink(log_con, split = TRUE)
sink(log_con, type = "message")
on.exit({
  if (sink.number(type = "message") > 0L) sink(type = "message")
  if (sink.number() > 0L) sink()
  close(log_con)
}, add = TRUE)

# Small matrices plus twelve PSOCK workers: nested BLAS threads only contend.
Sys.setenv(
  OMP_NUM_THREADS = "1",
  OPENBLAS_NUM_THREADS = "1",
  MKL_NUM_THREADS = "1"
)

cat("Starting parent SPD sweep at", format(Sys.time(), tz = "UTC", usetz = TRUE), "\n")
cat("Raw output:", outdir, "\n")
set.seed(5566 + 4)

pdf(file.path(outdir, "simulation_plots.pdf"), width = 11, height = 8.5)
source("BWS_simulation.R", echo = FALSE)
dev.off()

generated <- list.files("save", pattern = "\\.RData$", full.names = TRUE)
if (length(generated) != 192L)
  stop(sprintf("expected 192 .RData files (24 cells x 8 objects); found %d", length(generated)))

pdf(file.path(outdir, "summary_plots.pdf"), width = 11, height = 8.5)
source("sim_summary.R", echo = FALSE)
dev.off()

# Move after summarising so only one copy of the 192 raw arrays remains.
if (!all(file.rename(generated, file.path(savedir, basename(generated)))))
  stop("failed to move one or more raw result files")

cat("Completed parent SPD sweep at", format(Sys.time(), tz = "UTC", usetz = TRUE), "\n")
cat("Recorded files:", length(list.files(savedir, pattern = "\\.RData$")), "\n")
cat("Log:", log_path, "\n")
