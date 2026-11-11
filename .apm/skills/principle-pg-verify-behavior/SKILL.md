---
name: principle-pg-verify-behavior
description: Use when validating or reviewing a PostgreSQL core patch before claiming it works, is fixed or is ready for submission.
---

# Verify the changed behavior

Read the [common contributor contract](../../instructions/postgresql-contributor.instructions.md).

Bind evidence to the tested revision, build configuration and rebuilt executable.
Start with a reproducer that distinguishes expected from incorrect behavior;
compare suitable baseline and patched builds for a bug fix. Use isolated test
instances and inspect actual test registrations and supported commands.

Cover relevant normal, boundary and error paths. Broaden coverage according to
risk, including concurrency, recovery and portability when affected. A green
build or another agent's report is insufficient evidence of the claimed behavior.

Record commands, working directories, configuration, exit status and surviving
logs. Separate patch defects, baseline failures, environment failures and skips.
If reproduction fails, report that limit instead of declaring a fix verified.
Later source changes require proportionate revalidation. Passing tests establish
observed results, not a proof of correctness or community readiness.
