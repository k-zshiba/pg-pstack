# Performance

Start when: A PostgreSQL core performance symptom or a request to improve measured server behavior.

1. Use [principle-pg-measure-before-optimizing](../../principle-pg-measure-before-optimizing/SKILL.md) and the [measurement procedure](../../test-pg-patch/references/performance-measurement.md) to define the workload, correctness checks and baseline before editing.

2. Use [research-postgresql](../../research-postgresql/SKILL.md) to connect separate profiling evidence to source and investigate the limiter. Inspect the workload driver too.

3. If improvement is requested and evidence justifies it, use [design-pg-patch](../../design-pg-patch/SKILL.md), [principle-pg-minimal-change](../../principle-pg-minimal-change/SKILL.md) and [implement-pg-patch](../../implement-pg-patch/SKILL.md). A diagnosis-only request stops before implementation.

4. Use [principle-pg-verify-behavior](../../principle-pg-verify-behavior/SKILL.md) and [test-pg-patch](../../test-pg-patch/SKILL.md) for correctness and repeated comparable baseline/final measurements. Use [review-pg-patch](../../review-pg-patch/SKILL.md) for the resulting patch.

Completion and output: Return the limiter, metric and units, revisions/configuration, raw artifact locations, repeats and variability. Say inconclusive when correctness, comparability or signal is insufficient.
