# Refactoring

Start when: A PostgreSQL core structural change intended to preserve observable behavior.

1. Use [principle-pg-evidence-first](../../principle-pg-evidence-first/SKILL.md) and [research-postgresql](../../research-postgresql/SKILL.md) to identify concrete change difficulty, callers and existing behavior.

2. Use [principle-pg-preserve-invariants](../../principle-pg-preserve-invariants/SKILL.md) and [design-pg-patch](../../design-pg-patch/SKILL.md) to state preserved semantics and compare the current structure with plausible alternatives.

3. Use [principle-pg-minimal-change](../../principle-pg-minimal-change/SKILL.md) and [implement-pg-patch](../../implement-pg-patch/SKILL.md) to change structure without mixing in unrelated semantics or formatting.

4. Use [principle-pg-verify-behavior](../../principle-pg-verify-behavior/SKILL.md), [test-pg-patch](../../test-pg-patch/SKILL.md) and [review-pg-patch](../../review-pg-patch/SKILL.md) to compare relevant baseline and final behavior, including error paths.

Completion and output: Return the structural benefit, preserved behavior, comparison evidence and coverage limits. Reclassify a necessary behavior change explicitly before implementing it.
