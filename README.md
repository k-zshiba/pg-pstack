# pg-pstack

AI agent workflows for PostgreSQL core development: an explicit coordinator mode,
eight task playbooks, seven specialist Skills and five supporting principles.

Supports Codex, Claude Code, GitHub Copilot and portable Agent Skills through
[Agent Package Manager (APM)](https://github.com/microsoft/apm).
Application SQL, query tuning and database administration are outside its scope.

## Install

Install the tested APM CLI into your Python user directory on Linux or macOS,
without creating or activating a venv. Use Python 3.11+ with pip:

```bash
python3.11 -m pip install --user apm-cli==0.33.0
export PATH="$(python3.11 -m site --user-base)/bin:$PATH"
apm --version
```

This uses the [official pip installation method](https://microsoft.github.io/apm/getting-started/installation/#pip-install)
with a pinned version and a user-owned installation. `apm --version` should report
`0.33.0`; use `type -a apm` if a different installation takes precedence.

Alternatively, on macOS or Linux with glibc 2.38+, install the standalone binary.
It requires no Python installation:

```bash
curl -fsSL https://raw.githubusercontent.com/microsoft/apm/v0.33.0/install.sh | APM_NO_DIRECT_FALLBACK=1 sh -s -- @v0.33.0
export PATH="$HOME/.local/bin:$PATH"
apm --version
```

The [versioned official installer](https://github.com/microsoft/apm/blob/v0.33.0/install.sh)
selects the platform binary and verifies its checksum. Linux systems with older
glibc should use the Python installation above. The installer refuses to replace
an existing pip-owned APM; use its original Python installer to manage it. If
Python reports an externally managed environment, respect that restriction and
use a compatible standalone installation. See the
[official platform options](https://microsoft.github.io/apm/getting-started/installation/).

Install directly from the remote repository in a separate workspace:

```bash
mkdir my-postgresql-workspace
cd my-postgresql-workspace
apm install k-zshiba/pg-pstack#v0.2.0 --target codex
apm compile --single-agents --target codex
export PG_SOURCE=/absolute/path/to/postgresql
```

APM creates `apm.yml` and `apm.lock.yaml`. Commit both to pin the resolved revision.
Choose `--target claude`, `--target copilot`, `--target agent-skills` or a
combination such as `--target codex,copilot`; compile only when Codex is selected.

For local development, clone this repository beside the workspace and replace
`k-zshiba/pg-pstack#v0.2.0` with `../pg-pstack`. Use a clean source clone: local
APM installation rejects symlinks that escape the package, such as interpreter
links in a leftover `.venv` directory.
The `v0.2.0` tag predates the rename and still contains the old package metadata.
To try the renamed package and current workflows before the next release, install
`../pg-pstack` from a local clone of this branch. Existing consumers should update
the old repository dependency to `k-zshiba/pg-pstack#v0.2.0`, run
`apm install --update`, inspect the lock and deployed files, and recompile for Codex. Preserve
handwritten instructions when migrating; do not edit lockfiles by hand.

Use source packages; packed ZIP installation has
[known limitations](docs/validation.md#apm-0330-constraints).

For existing workspaces, inspect `apm compile --dry-run` and preserve handwritten
agent instructions before compiling. Keep generated files out of PostgreSQL patches
and keep `apm_modules/` available for linked instructions.

## GitHub Copilot

Install with `--target copilot` and omit compilation. Open the workspace in
VS Code's Copilot agent mode or start Copilot CLI there. In VS Code, give the
absolute checkout path if the agent does not inherit `PG_SOURCE`.

In Copilot CLI, inspect `/skills list` and `/instructions`; use `/skills reload`
after installation. In VS Code, use Chat: Open Customizations to inspect Skills
and Instructions. Invoke `/research-postgresql` or describe a core-development task.
GitHub-hosted cloud/review sessions need their own APM setup and source access.

## Use

Start or restart your agent in the workspace and check its available Skills.
Provide a PostgreSQL checkout path in the task or set `PG_SOURCE`; otherwise,
the workspace root must be a PostgreSQL source tree. Relative `PG_SOURCE` paths
resolve from the workspace. Configure agent access to that checkout as needed.

For coordinated work, explicitly invoke the mode:

```text
$pgsql-hackers-mode Investigate and fix this PostgreSQL core planner bug in
/path/to/postgresql. Reproduce it first, then make a focused patch and verify it.
```

Use `/pgsql-hackers-mode` in Claude Code or Copilot. The mode selects investigation,
bug-fix, feature, refactoring, performance, review, revision or submission playbooks.
It stops at the requested deliverable; design-only and test-only requests go
straight to their specialist. Submission preparation happens only when requested.
See the [mode](.apm/skills/pgsql-hackers-mode/SKILL.md) and
[architecture](docs/architecture.md#workflow-layers).

The mode is explicit-only: its frontmatter disables automatic invocation for
Claude/Copilot, and its `agents/openai.yaml` disables implicit invocation for
Codex. Portable Agent Skills hosts must honor the corresponding settings; otherwise
manual-only selection is an instruction convention, not an enforced guarantee.
Existing specialist Skills keep automatic discovery and direct invocation:

| Skill | Purpose |
| --- | --- |
| [research-postgresql](.apm/skills/research-postgresql/SKILL.md) | Investigate source, history, discussions and backpatch suitability |
| [design-pg-patch](.apm/skills/design-pg-patch/SKILL.md) | Define behavior, scope and tests |
| [implement-pg-patch](.apm/skills/implement-pg-patch/SKILL.md) | Implement a scoped change with docs and tests |
| [test-pg-patch](.apm/skills/test-pg-patch/SKILL.md) | Run validation appropriate to the checkout |
| [review-pg-patch](.apm/skills/review-pg-patch/SKILL.md) | Review correctness, compatibility and coverage |
| [revise-pg-patch](.apm/skills/revise-pg-patch/SKILL.md) | Address feedback and retest |
| [prepare-pgsql-hackers-post](.apm/skills/prepare-pgsql-hackers-post/SKILL.md) | Draft proposals, submissions, reviews and replies |

Use `$research-postgresql` in Codex or `/research-postgresql` in Claude/Copilot
to invoke research explicitly. See [task examples](examples/workflows.md).

The [shared instructions](.apm/instructions/postgresql-contributor.instructions.md)
require current evidence, preservation of user changes and honest test results.
Mail and CommitFest updates require explicit authorization. Agent permissions
remain responsible for enforcing access; automatic Skill routing needs live evaluation.

## Documentation

- [Consumer examples and updates](examples/README.md)
- [Development, tests and releases](CONTRIBUTING.md)
- [Package structure](docs/architecture.md)
- [Research sources](docs/research.md)
- [Validation and limitations](docs/validation.md)
- [Behavioral evaluation](evals/README.md)
- [Changelog](CHANGELOG.md)

Licensed under the [PostgreSQL License](LICENSE).
