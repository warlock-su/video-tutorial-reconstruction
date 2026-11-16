"""Regression gates for the portable skill bundle (stdlib only)."""
from pathlib import Path
import ipaddress
import re
import unittest
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]


class BundleTests(unittest.TestCase):
    def test_frontmatter_and_public_identity(self):
        text = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        self.assertTrue(text.startswith("---\n"))
        frontmatter, body = text[4:].split("\n---\n", 1)
        self.assertIn("name: video-tutorial-reconstruction", frontmatter)
        self.assertIn("license: MIT", frontmatter)
        self.assertRegex(frontmatter, r"(?m)^version: \d+\.\d+\.\d+$")
        description = re.search(r'(?m)^description: "([^"]+)"$', frontmatter).group(1)
        self.assertTrue(description.startswith("Use when "))
        self.assertLessEqual(len(description), 60)
        self.assertTrue(body.strip())
        self.assertLessEqual(len(text), 100_000)

    def test_all_explicit_reference_paths_exist(self):
        for file in [ROOT / "SKILL.md", *(ROOT / "references").glob("*.md")]:
            for relative in re.findall(r"references/[\w-]+\.md", file.read_text(encoding="utf-8")):
                with self.subTest(file=file.name, reference=relative):
                    self.assertTrue((ROOT / relative).is_file())

    def test_relative_markdown_links_stay_in_bundle_and_resolve(self):
        for file in [*ROOT.glob("*.md"), *(ROOT / "references").glob("*.md")]:
            for link in re.findall(r"\]\(([^)]+)\)", file.read_text(encoding="utf-8")):
                parsed = urlsplit(link)
                if parsed.scheme or parsed.netloc or not parsed.path:
                    continue
                target = (file.parent / unquote(parsed.path)).resolve()
                with self.subTest(file=file.name, link=link):
                    self.assertTrue(target.is_relative_to(ROOT))
                    self.assertTrue(target.is_file())

    def test_workflow_is_one_unbroken_numbered_sequence(self):
        text = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        workflow = text.split("## Required workflow\n", 1)[1].split("\n## ", 1)[0]
        numbers = [int(n) for n in re.findall(r"(?m)^(\d+)\. ", workflow)]
        self.assertEqual(numbers, list(range(1, 16)))

    def test_preserves_evidence_and_verification_gates(self):
        text = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        for gate in (
            "full-duration uniform coarse visual pass", "exactly one inference request at a time",
            "Treat VLM text as OCR, not authority", "dependency-safe intermediate listing",
            "later dependencies only after", "source application's exact version",
            "Map published screenshots back to source frames by checksum", "byte-for-byte",
            "first-import errors as packaging failures", "Only after the final archive passes",
            "Do **not** use cloud subagents merely to reread", "Do not silently send private footage",
        ):
            with self.subTest(gate=gate):
                self.assertIn(gate, text)

    def test_godot_packaging_preserves_import_descriptors_not_cache(self):
        skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        step = re.search(r"(?m)^15\. .+$", skill).group(0)
        reference = (ROOT / "references/local-first-and-godot-packaging.md").read_text(
            encoding="utf-8"
        ).split("## Godot release packaging\n", 1)[1]
        for location, text in (("workflow step 15", step), ("packaging reference", reference)):
            with self.subTest(location=location):
                self.assertNotRegex(
                    text,
                    r"(?i)(?:do not ship|exclude(?: generated)?|without)[^.\n]*`\*\.import`",
                    "Import descriptors must not be blanket-excluded with regenerated cache",
                )
                self.assertRegex(text, r"(?i)(?:keep|preserve|retain)[^.\n]*`\*\.import`")
                self.assertIn("import settings", text)
                self.assertIn("original source assets", text)
                self.assertRegex(text, r"`\.godot/`[^.\n]*Godot 4")
                self.assertRegex(text, r"(?i)diagnose[^.\n]*import errors")
        self.assertIn(
            "https://docs.godotengine.org/en/stable/tutorials/assets_pipeline/import_process.html",
            reference,
        )

    def test_keeps_all_original_procedure_topics(self):
        for name in (
            "code-transition-and-package-verification", "godot-runtime-verification",
            "local-first-and-godot-packaging", "repeat-blocker-audits",
            "session-evidence-and-transport-pitfalls", "source-acquisition-and-preflight",
            "unity-project-archive-reconciliation", "upstream-and-maintenance",
            "video-first-gui-tutorials",
        ):
            with self.subTest(topic=name):
                self.assertTrue((ROOT / "references" / (name + ".md")).is_file())

    def test_installable_attribution_retains_mit_notice(self):
        license_text = (ROOT / "LICENSE").read_text(encoding="utf-8")
        attribution = (ROOT / "references/attribution.md").read_text(encoding="utf-8")
        self.assertIn(license_text, attribution)
        self.assertIn("https://github.com/WeiminXiong/Video2GUI", attribution)
        self.assertIn("Apache-2.0", attribution)

    def test_markdown_has_no_private_machine_paths_or_addresses(self):
        for file in [*ROOT.glob("*.md"), *(ROOT / "references").glob("*.md")]:
            text = file.read_text(encoding="utf-8")
            with self.subTest(file=file.name):
                self.assertNotRegex(text, r"/(?:home|Users)/[^\s/`]+/")
                self.assertNotRegex(text, r"[A-Za-z]:\\Users\\")
                self.assertNotIn("RTX 5090", text)
                for raw in re.findall(r"\b(?:\d{1,3}\.){3}\d{1,3}\b", text):
                    try:
                        address = ipaddress.ip_address(raw)
                    except ValueError:
                        continue
                    self.assertFalse(address.is_private and not address.is_loopback, raw)


if __name__ == "__main__":
    unittest.main()
