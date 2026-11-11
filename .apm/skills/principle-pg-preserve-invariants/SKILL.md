---
name: principle-pg-preserve-invariants
description: Use when designing, changing or reviewing PostgreSQL core ownership, error handling, shared state, locking or persistence paths.
---

# Preserve subsystem invariants

Read the [common contributor contract](../../instructions/postgresql-contributor.instructions.md).

Identify the invariants of the touched path before changing it. Follow resource
and memory ownership across callers, successful returns and error cleanup. Read
local conventions rather than imposing generic C patterns.

For shared state, trace synchronization, visibility, lock ordering and relevant
interleavings. For persistence paths, inspect WAL/recovery and replication
implications. Review interfaces, storage/catalog compatibility and portability
only where the change touches them.

Keep comments that explain intent, lifetime or concurrency constraints beyond
what code expresses. Validate a claimed invariant with source and discriminating
tests; do not invent risks to fill a checklist. Unresolved foundational semantics
call for discussion or a bounded prototype, not a large speculative patch.
