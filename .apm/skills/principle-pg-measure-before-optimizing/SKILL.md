---
name: principle-pg-measure-before-optimizing
description: Use for PostgreSQL core performance investigations and before accepting or reporting a measured optimization or regression.
---

# Measure before optimizing

Read the [common contributor contract](../../instructions/postgresql-contributor.instructions.md).

Define the claim, metric, workload and correctness checks before measuring.
Capture a baseline and identify the limiting work with a separate profiling run.
Inspect the driver as well as the server; verify the intended work actually ran.

Compare the intended revisions using equivalent configuration, data, settings,
hardware and load. Separate profiling overhead from reported timings. Repeat
and interleave comparisons, report variability and examine errors and results.
A configuration difference or a saturated driver cannot establish an improvement
in the patched server code.

Use the [measurement procedure](../test-pg-patch/references/performance-measurement.md)
for concrete comparisons. Report inconclusive evidence when runs are incomparable,
variation hides the difference or correctness was not checked. Keep the raw
measurements and commands so another contributor can reproduce the claim.
