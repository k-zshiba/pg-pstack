# Bug Fix

Start when: A reported defect in PostgreSQL core with a request to fix it.

1. Use [principle-pg-evidence-first](../../principle-pg-evidence-first/SKILL.md) and [research-postgresql](../../research-postgresql/SKILL.md) to reproduce the symptom and isolate the failing mechanism. Record baseline revision and configuration.

2. If it will not reproduce, tighten the probe or instrument an isolated instance. Report a reproduction blocker when evidence remains insufficient; do not declare a speculative fix verified.

3. Use [design-pg-patch](../../design-pg-patch/SKILL.md) for a brief justified fix, reading [principle-pg-preserve-invariants](../../principle-pg-preserve-invariants/SKILL.md) for affected lifetimes, error paths or concurrency.

4. Use [principle-pg-minimal-change](../../principle-pg-minimal-change/SKILL.md) and [implement-pg-patch](../../implement-pg-patch/SKILL.md) for the focused change, tests and docs.

5. Use [principle-pg-verify-behavior](../../principle-pg-verify-behavior/SKILL.md) and [test-pg-patch](../../test-pg-patch/SKILL.md) to repeat the original reproducer against the final patch and cover relevant wider behavior. Use [review-pg-patch](../../review-pg-patch/SKILL.md) for final review.

Completion and output: Return the observed failure, root cause, change, failing/passing evidence and limits. A non-reproduced symptom remains unverified.
