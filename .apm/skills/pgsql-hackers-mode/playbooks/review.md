# Review

Start when: A request to review a PostgreSQL core patch or series.

1. Use [principle-pg-evidence-first](../../principle-pg-evidence-first/SKILL.md), [principle-pg-preserve-invariants](../../principle-pg-preserve-invariants/SKILL.md) and [review-pg-patch](../../review-pg-patch/SKILL.md) to establish intent, latest supplied version, base, discussion and applicability in isolation.

2. Use [principle-pg-verify-behavior](../../principle-pg-verify-behavior/SKILL.md) and [test-pg-patch](../../test-pg-patch/SKILL.md) for discriminating probes; keep confirmed defects separate from questions and untested risks.

3. Prefer an independent review delegate when available and useful. Otherwise perform and label self-review. Review permission alone does not authorize implementation edits.

Completion and output: Return findings ordered by impact, reproduction evidence, questions, inspected revision and coverage limits. Draft a review email only if asked.
