# PostgreSQL core performance measurement

Use for a performance claim about core source behavior, not routine application
query tuning. Discover commands and supported tools in the actual checkout.

1. Define the metric with units and the expected useful effect. Record revisions,
   workload/data, scale, concurrency, duration, hardware, platform, compiler,
   build options, installed binary paths and server settings. Separate correctness
   builds (for example assertions) from comparable measurement builds.
2. Use disposable instances and isolated data/build/install locations. Keep both
   sides equivalent, including cache/warmup policy, durability and transaction
   settings. Check that each instance runs its intended rebuilt executable.
3. Read the workload driver. Verify that requests reached the intended server and
   completed the intended work. Count errors, retries and timeouts, and check
   returned results or durable effects. A fast failure is not an optimization.
4. Capture baseline measurements before changing code. Profile separately to
   identify the limiting server path and check whether CPU, I/O, locks, the driver
   or another resource limits throughput. Do not include profiling overhead in
   unprofiled timing comparisons.
5. Repeat comparable baseline and patched runs, interleaving their order. Start
   with at least five runs per side for a comparative claim; extend when noise
   or warmup obscures the result. Record individual samples, median and range,
   plus workload-relevant latency/throughput. A requested single-run estimate
   must be labeled as such and cannot establish a comparative win.
6. Recheck correctness on the final revision. Explain the scope of microbenchmarks
   and measure a relevant wider path before asserting an end-to-end benefit.
   Preserve scripts, exact commands, settings and raw logs after cleanup.

Report faster, slower, no measurable difference or inconclusive, with the metric,
units, revisions, configuration, repetitions, variability and limiting work.
Do not claim a win if configurations differ, errors explain the number, the
intended work was skipped or variation masks the effect. Name the missing evidence
and a reproducible next experiment rather than choosing favorable samples.
