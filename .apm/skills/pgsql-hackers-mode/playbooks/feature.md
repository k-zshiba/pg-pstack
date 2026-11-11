# Feature

Start when: A request for new or changed PostgreSQL core behavior.

1. Use [principle-pg-evidence-first](../../principle-pg-evidence-first/SKILL.md) and [research-postgresql](../../research-postgresql/SKILL.md) to inspect analogous code and prior/rejected proposals.

2. Use [principle-pg-preserve-invariants](../../principle-pg-preserve-invariants/SKILL.md) and [design-pg-patch](../../design-pg-patch/SKILL.md) to settle semantics, compatibility and distinguishing tests. Stop at a proposal or bounded prototype if foundational questions remain unresolved.

3. For justified implementation within the requested scope, use [principle-pg-minimal-change](../../principle-pg-minimal-change/SKILL.md) and [implement-pg-patch](../../implement-pg-patch/SKILL.md).

4. Use [principle-pg-verify-behavior](../../principle-pg-verify-behavior/SKILL.md), [test-pg-patch](../../test-pg-patch/SKILL.md) and [review-pg-patch](../../review-pg-patch/SKILL.md) on the final revision.

Completion and output: Return chosen behavior, implementation or design deliverable, actual validation, tradeoffs and open discussion points. Do not claim community acceptance.
