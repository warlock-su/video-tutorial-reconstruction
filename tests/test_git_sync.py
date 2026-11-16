"""Prove the documented Git update path using local disposable repositories."""
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]


@unittest.skipUnless(shutil.which("git"), "Git is required for update tests")
class GitSyncTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(dir=os.getenv("TMPDIR"))
        self.addCleanup(self.tmp.cleanup)
        self.base = Path(self.tmp.name)
        self.env = {
            key: value for key in ("PATH", "TMPDIR", "SYSTEMROOT", "WINDIR", "TEMP", "TMP")
            if (value := os.getenv(key)) is not None
        }
        home = self.base / "home"
        home.mkdir()
        self.env.update(HOME=str(home), USERPROFILE=str(home),
                        GIT_CONFIG_NOSYSTEM="1", GIT_CONFIG_GLOBAL=os.devnull)
        self.origin = self.base / "origin.git"
        self.writer = self.base / "writer"
        self.consumer = self.base / "consumer"
        self.git("init", "--bare", "--initial-branch=main", str(self.origin))
        self.git("clone", str(self.origin), str(self.writer))
        self.git("config", "user.name", "Test Fixture", cwd=self.writer)
        self.git("config", "user.email", "fixture@example.invalid", cwd=self.writer)
        self.original = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        (self.writer / "SKILL.md").write_text(self.original, encoding="utf-8")
        self.git("add", "SKILL.md", cwd=self.writer)
        self.git("commit", "-m", "Seed skill fixture", cwd=self.writer)
        self.git("push", "-u", "origin", "main", cwd=self.writer)
        self.git("clone", str(self.origin), str(self.consumer))

    def git(self, *args, cwd=None, check=True):
        return subprocess.run(
            ["git", *args], cwd=cwd or self.base, env=self.env,
            capture_output=True, text=True, check=check, timeout=20,
        )

    def publish_fixture_update(self):
        updated = self.original + "\n<!-- Git-sync regression fixture update. -->\n"
        (self.writer / "SKILL.md").write_text(updated, encoding="utf-8")
        self.git("add", "SKILL.md", cwd=self.writer)
        self.git("commit", "-m", "Update fixture", cwd=self.writer)
        self.git("push", "origin", "main", cwd=self.writer)
        return updated

    def test_fast_forward_updates_same_checkout_path(self):
        installed_file = self.consumer / "SKILL.md"
        self.assertEqual(installed_file.read_text(encoding="utf-8"), self.original)
        expected = self.publish_fixture_update()
        self.git("pull", "--ff-only", cwd=self.consumer)
        self.assertEqual(installed_file.read_text(encoding="utf-8"), expected)
        self.assertEqual(self.git("rev-parse", "HEAD", cwd=self.consumer).stdout,
                         self.git("rev-parse", "HEAD", cwd=self.writer).stdout)
        self.assertEqual(self.git("status", "--porcelain", cwd=self.consumer).stdout, "")

    def test_conflicting_local_lesson_is_not_overwritten(self):
        installed_file = self.consumer / "SKILL.md"
        local = self.original + "\n<!-- Local uncommitted fixture lesson. -->\n"
        installed_file.write_text(local, encoding="utf-8")
        before = self.git("rev-parse", "HEAD", cwd=self.consumer).stdout
        self.publish_fixture_update()
        result = self.git("pull", "--ff-only", cwd=self.consumer, check=False)
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(installed_file.read_text(encoding="utf-8"), local)
        self.assertEqual(self.git("rev-parse", "HEAD", cwd=self.consumer).stdout, before)


if __name__ == "__main__":
    unittest.main()
