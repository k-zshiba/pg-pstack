---
name: principle-pg-minimal-change
description: Use when sizing or implementing a PostgreSQL core patch or refactoring; keep changes focused and consistent with the touched subsystem.
---

# Make the smallest justified change

Read the [common contributor contract](../../instructions/postgresql-contributor.instructions.md).

Name the behavior or structural problem and its evidence. Prefer existing
subsystem conventions and analogous implementations. Include the tests and docs
needed for the change, while keeping unrelated formatting, abstractions and
speculative improvements out of the diff.

For refactoring, state which observable behavior must stay the same. Separate
behavioral changes from structural changes so a reviewer can assess each. Read
generator inputs before editing generated output and check branch practices.

Inspect the checkout's coding conventions and pgindent prerequisites. Format
only intended files or hunks, then review the full diff and working state.
Preserve user changes and useful explanatory comments.
