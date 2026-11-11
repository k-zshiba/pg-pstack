---
name: principle-pg-evidence-first
description: Ground PostgreSQL core investigation and patch decisions in checkout source, history and discussion; use when resolving internals claims or conflicting evidence.
---

# Evidence first

Read the [common contributor contract](../../instructions/postgresql-contributor.instructions.md).

Use the recorded checkout revision as the source of implemented behavior. Read
complete relevant functions, analogous code, callers, tests, subsystem README
files and comments. Trace history before explaining why a design exists.

Match documentation and discussion to the branch and date. Read relevant replies
and attachments; distinguish a proposal, a participant's opinion and established
agreement. Search failure or shallow history leaves an unknown.

Tie concrete claims to paths, symbols and lines at the recorded revision or exact
source URLs. Separate observations, inference and open questions. Test the smallest
discriminating hypothesis when practical within the requested scope. Research-only
work returns evidence and limitations without implementation changes.
