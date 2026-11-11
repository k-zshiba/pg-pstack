# Revision

Start when: A request to revise an existing PostgreSQL core patch from reviewer feedback.

1. Use [principle-pg-evidence-first](../../principle-pg-evidence-first/SKILL.md) and [revise-pg-patch](../../revise-pg-patch/SKILL.md) to identify the patch, later discussion and an issue ledger. Verify rather than automatically accept each requested change.

2. Route changed semantics through [research-postgresql](../../research-postgresql/SKILL.md) and [design-pg-patch](../../design-pg-patch/SKILL.md). Apply [principle-pg-preserve-invariants](../../principle-pg-preserve-invariants/SKILL.md) and [principle-pg-minimal-change](../../principle-pg-minimal-change/SKILL.md) to focused edits.

3. Use [principle-pg-verify-behavior](../../principle-pg-verify-behavior/SKILL.md), [test-pg-patch](../../test-pg-patch/SKILL.md) and [review-pg-patch](../../review-pg-patch/SKILL.md) on the final revision. Inspect changes from the prior version as well as the whole patch.

4. Generate versioned attachments through the revision skill only when requested; use the submission playbook for a requested response draft.

Completion and output: Return the feedback ledger, material version changes, validation, requested artifacts and unresolved points. Do not claim every comment is resolved when questions remain.
