# Example tasks

Supply the checkout path, reproducer, thread/CommitFest URL and patches as needed.

## Coordinated work

Use `$pgsql-hackers-mode` in Codex or `/pgsql-hackers-mode` in Claude/Copilot.
The existing specialist examples below continue to work without the mode.

```text
$pgsql-hackers-mode Fix this PostgreSQL core crash in /path/to/postgresql.
First reproduce and isolate the cause, then implement and validate a focused fix.
```

```text
$pgsql-hackers-mode Refactor this PostgreSQL core ownership path. Establish the
behavior and invariants to preserve, compare designs, then verify equivalence.
```

```text
$pgsql-hackers-mode Investigate this measured PostgreSQL core performance
regression. Compare equivalent baseline and patched workloads, check correctness
and report repetitions, variability and the bottleneck. Diagnosis only for now.
```

```text
$pgsql-hackers-mode Design this PostgreSQL core interface change only.
Return semantics, alternatives and validation plans; stop before implementation.
```

```text
$pgsql-hackers-mode Review this PostgreSQL core patch. Delegation is unavailable;
perform a self-review and report its coverage and validation limits.
```

The mode also provides investigation, feature, review, revision and submission
playbooks. It prepares mail or attachments only when requested and does not send
or publish them without authorization. See the
[playbook index](../.apm/skills/pgsql-hackers-mode/SKILL.md#choose-the-work).

## Planner bug

```text
Use research-postgresql in /path/to/postgresql. Find the source, callers,
tests and discussions relevant to this unexpected plan. Explain the
evidence, hypothesis and next experiment before editing.
```

## New GUC

```text
Research existing mechanisms and prior proposals for this core GUC.
Design scope, defaults, semantics, compatibility and tests. Draft open
questions for pgsql-hackers before substantial implementation.
```

## Find a topic for design practice

```text
Use research-postgresql in /path/to/postgresql to find bounded core refactoring
or feature topics for architecture design practice. Investigate change
propagation, duplication and variation, extension cost, state/lifetime and
testability. Ground candidates in source, change history and prior discussions.
Compare the design decisions they expose, constraints and validation options,
including keeping the current structure. Recommend a manageable starting topic
and identify missing evidence; do not change the code yet.
```

## CommitFest review

```text
Review this entry and patch. Verify the latest thread, version, base and
prerequisites. Check applicability in an isolated tree and run relevant
tests. Report findings and coverage limits; draft a review email.
```

## Revised patch

```text
Use revise-pg-patch for this series and feedback, including later replies.
Make the agreed changes, test the final tree and prepare v3 attachments
with a reply explaining changes and unresolved questions.
```

## Backpatch assessment

```text
Research this fix on the requested stable branches. Check support status,
bug introduction, corresponding code, compatibility risks and tests.
Recommend whether to backpatch; do not switch or cherry-pick my tree.
```

Application index creation and production query tuning are outside these Skills.
Mail drafts and local attachments do not authorize external submission.
