---
name: pgsql-hackers-mode
description: Coordinate PostgreSQL upstream/core work through task playbooks when the user explicitly invokes pgsql-hackers-mode. Existing specialist skills remain directly usable.
disable-model-invocation: true
---

# PostgreSQL hackers mode

Read the [common contributor contract](../../instructions/postgresql-contributor.instructions.md).

Use this coordinator only when the user explicitly invokes pgsql-hackers-mode.
It covers PostgreSQL upstream/core development, not application SQL or operations.
Keep the user's requested stopping point, including research-only, design-only,
validation-only and draft-only work.

## Choose the work

State the intended outcome and resolve the checkout/revision and working state.
Read the selected playbook before starting. For a mixed request, sequence the
needed playbooks and reuse evidence instead of restarting completed investigation.

| Request | Playbook |
| --- | --- |
| Understand source, history or a hypothesis | [Investigation](playbooks/investigation.md) |
| Reproduce and fix a defect | [Bug fix](playbooks/bug-fix.md) |
| Add or change behavior | [Feature](playbooks/feature.md) |
| Improve structure while preserving behavior | [Refactoring](playbooks/refactoring.md) |
| Investigate or improve measured performance | [Performance](playbooks/performance.md) |
| Critically assess a patch | [Review](playbooks/review.md) |
| Revise a patch from feedback | [Revision](playbooks/revision.md) |
| Prepare a posting draft or attachments | [Submission](playbooks/submission.md) |

For design-only requests, use [design-pg-patch](../design-pg-patch/SKILL.md)
directly and stop at the design. For validation-only requests, use
[test-pg-patch](../test-pg-patch/SKILL.md) directly and return the results or plan.
An explicit mode invocation outside core development does not expand its scope.

## Run and finish

Keep a short task list from the selected procedure. Mark skipped or blocked work
with its reason. Load the referenced specialist skills and only the principles
needed at the current step. Apply evidence-first to investigation, invariants to
semantic risks, minimal-change to edits, verify-behavior to validation and
measure-before-optimizing to performance comparisons.

Use [delegation](references/delegation.md) when independent investigation or
review, or a separable implementation task, would help. The parent owns scope,
integration and final verification. Without available and authorized delegation,
perform the same procedure alone and identify self-review as such.

Stop at the requested deliverable. Resolve attributable failures where authorized;
otherwise name the blocker and missing evidence. Report outcome, source/patch
revision, actual validation and limitations. Do not attach submission preparation
to every task, claim unrun checks, or treat completion as permission to commit,
send mail, change CommitFest or publish.
