import importlib.metadata
import re
import subprocess
import unittest

from apm_cli.models.apm_package import APMPackage
from apm_cli.core.errors import UnknownTargetError

from support import APM_VERSION, CONTRACT, MAINTAINER_SKILL, ROOT, SKILLS, MODE, PLAYBOOKS, reachable_documents, check_links, frontmatter, load_yaml


class StructureTests(unittest.TestCase):
    def test_required_files_and_current_manifest_loader(self):
        for name in ("apm.yml", "apm.lock.yaml", "README.md", "CONTRIBUTING.md",
                     "LICENSE", ".gitignore", "CHANGELOG.md", "docs/research.md",
                     "docs/architecture.md", "docs/validation.md", "evals/scenarios.json",
                     "evals/README.md", "examples/workflows.md", ".github/workflows/validate.yml"):
            self.assertTrue((ROOT / name).is_file(), name)
        self.assertEqual(importlib.metadata.version("apm-cli"), APM_VERSION)
        package = APMPackage.from_apm_yml(ROOT / "apm.yml", create_config=False)
        self.assertEqual(package.name, "pg-pstack")
        manifest = load_yaml(ROOT / "apm.yml")
        self.assertRegex(manifest["version"], r"^0\.\d+\.\d+$")
        self.assertEqual(manifest["targets"], ["codex", "claude", "copilot", "agent-skills"])
        self.assertEqual(manifest["license"], "PostgreSQL")
        self.assertEqual((ROOT / "LICENSE").read_bytes(),
                         (ROOT / ".apm/instructions/LICENSE").read_bytes())
        self.assertEqual(manifest["dependencies"], {})
        self.assertNotIn("devDependencies", manifest)
        self.assertEqual(manifest["includes"], [".apm/instructions/", ".apm/skills/"])
        self.assertEqual(package.get_apm_dependencies(), [])

    def test_lock_closure_and_schema_rejection(self):
        lock = load_yaml(ROOT / "apm.lock.yaml")
        self.assertEqual(lock["dependencies"], [])
        self.assertEqual(lock["deployments"], [])
        self.assertEqual(lock["apm_version"], APM_VERSION)
        manifest = load_yaml(ROOT / "apm.yml")
        for mutation in ({"targets": ["imaginary-agent"]}, {"$schema": "https://invalid.test/schema"}):
            with self.subTest(mutation=mutation), self.assertRaises((ValueError, UnknownTargetError)):
                APMPackage.from_mapping({**manifest, **mutation}, package_path=ROOT, create_config=False)

    def test_skill_metadata_and_progressive_references(self):
        paths = list((ROOT / ".apm/skills").glob("*/SKILL.md"))
        names = []
        for path in paths:
            metadata, body = frontmatter(path)
            name = metadata["name"]
            names.append(name)
            self.assertEqual(name, path.parent.name)
            self.assertRegex(name, r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
            self.assertLessEqual(len(name), 64)
            self.assertIsInstance(metadata["description"], str)
            self.assertTrue(1 <= len(metadata["description"]) <= 1024)
            self.assertEqual(set(metadata), {"name", "description", "disable-model-invocation"}
                             if name == MODE else {"name", "description"})
            self.assertLess(len(body.splitlines()), 120)
            self.assertIn("../../instructions/postgresql-contributor.instructions.md", body)
            self.assertNotRegex(body, r"TODO|\[INSERT|!`")
        self.assertEqual(set(names), SKILLS)
        self.assertEqual(len(names), len(set(names)))
        all_docs = set((ROOT / ".apm/skills").rglob("*.md"))
        reached = reachable_documents(paths, ROOT / ".apm")
        self.assertTrue({p.resolve() for p in all_docs} <= reached,
                        sorted(str(p) for p in all_docs if p.resolve() not in reached))
        metadata, body = frontmatter(CONTRACT)
        self.assertEqual(metadata["applyTo"], "**")
        self.assertLess(len(body.splitlines()), 80)

    def test_mode_invocation_and_routing_resources(self):
        mode = ROOT / ".apm/skills" / MODE
        self.assertTrue(frontmatter(mode / "SKILL.md")[0]["disable-model-invocation"])
        self.assertFalse(load_yaml(mode / "agents/openai.yaml")["policy"]["allow_implicit_invocation"])
        self.assertEqual({p.stem for p in (mode / "playbooks").glob("*.md")}, PLAYBOOKS)
        self.assertTrue((mode / "references/delegation.md").is_file())
        for name in SKILLS - {MODE}:
            path = ROOT / ".apm/skills" / name / "SKILL.md"
            metadata, body = frontmatter(path)
            self.assertNotIn("disable-model-invocation", metadata)
            self.assertFalse((path.parent / "agents/openai.yaml").exists())
            self.assertNotIn("pgsql-hackers-mode", body)
        reached = reachable_documents([mode / "SKILL.md"], ROOT / ".apm")
        self.assertTrue({(ROOT / ".apm/skills" / n / "SKILL.md").resolve()
                         for n in SKILLS} <= reached)

    def test_links_and_no_provider_source_duplication(self):
        paths = []
        for folder in (".apm", "docs", "examples", "evals"):
            paths.extend((ROOT / folder).rglob("*.md"))
        paths.extend(ROOT.glob("*.md"))
        paths.extend((ROOT / MAINTAINER_SKILL).rglob("*.md"))
        self.assertEqual(check_links(paths, ROOT), [])
        self.assertEqual({p.name for p in (ROOT / ".apm").iterdir()}, {"skills", "instructions"})
        self.assertEqual(len(list((ROOT / ".apm/instructions").glob("*.instructions.md"))), 1)
        tracked = subprocess.run(["git", "ls-files", "-z"], cwd=ROOT,
                                 capture_output=True, check=True).stdout.decode().split("\0")
        for path in tracked:
            if path.startswith(MAINTAINER_SKILL.as_posix() + "/"):
                continue
            self.assertFalse(re.match(r"^(AGENTS.md|CLAUDE.md|plugin.json|apm_modules/|build/|dist/|\.agents/|\.claude/|\.codex/|\.claude-plugin/|\.codex-plugin/)", path), path)
            self.assertFalse(re.match(r"^\.github/(copilot-instructions\.md|instructions/|skills/|agents/|prompts/|hooks/)", path), path)
        for path in (ROOT / ".apm").rglob("*"):
            self.assertFalse(path.is_symlink(), path)

    def test_maintenance_skill_metadata_and_ignore_boundary(self):
        metadata, body = frontmatter(ROOT / MAINTAINER_SKILL / "SKILL.md")
        self.assertEqual(metadata["name"], MAINTAINER_SKILL.name)
        self.assertEqual(set(metadata), {"name", "description"})
        self.assertTrue(1 <= len(metadata["description"]) <= 1024)
        self.assertNotIn(metadata["name"], SKILLS)
        self.assertNotRegex(body, r"TODO|\[INSERT|!`")
        ignored = {".agents/skills/research-postgresql/SKILL.md",
                   ".agents/skills/another-maintainer/SKILL.md", ".agents/state.json"}
        visible = {str(MAINTAINER_SKILL / "SKILL.md"),
                   str(MAINTAINER_SKILL / "references/check.md")}
        result = subprocess.run(["git", "check-ignore", "--no-index", "--stdin"],
                                cwd=ROOT, input="\n".join(sorted(ignored | visible)) + "\n",
                                text=True, capture_output=True, check=True)
        self.assertEqual(set(result.stdout.splitlines()), ignored)

    def test_example_manifests_use_release_and_targets(self):
        version = load_yaml(ROOT / "apm.yml")["version"]
        for path in (ROOT / "examples").glob("*/apm.yml"):
            manifest = load_yaml(path)
            APMPackage.from_apm_yml(path, create_config=False)
            self.assertEqual(manifest["dependencies"]["apm"],
                             [f"k-zshiba/pg-pstack#v{version}"])
            self.assertTrue(set(manifest["targets"]) <= {"codex", "claude", "copilot", "agent-skills"})
        copilot = load_yaml(ROOT / "examples/copilot/apm.yml")
        self.assertEqual(copilot["targets"], ["copilot"])


if __name__ == "__main__":
    unittest.main()
