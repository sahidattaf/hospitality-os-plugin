"""Regression checks use temporary source copies, never an installed plugin."""

import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from validate_hospitality_plugin import PLUGIN_ROOT, REPO_ROOT, validate


class PackageValidationTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.repo = Path(self.temporary.name)
        self.plugin = self.repo / "plugins/hospitality-os-plugin"
        shutil.copytree(PLUGIN_ROOT, self.plugin, ignore=shutil.ignore_patterns("__pycache__"))
        self.marketplace = self.repo / ".agents/plugins/marketplace.json"
        self.marketplace.parent.mkdir(parents=True)
        shutil.copyfile(REPO_ROOT / ".agents/plugins/marketplace.json", self.marketplace)
        self.native = self.plugin / ".codex-plugin/plugin.json"
        self.portable = self.plugin / "plugin.json"

    def edit(self, path, change):
        data = json.loads(path.read_text(encoding="utf-8"))
        change(data)
        path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")

    def errors(self):
        return validate(self.plugin, self.repo)

    def assert_rejected(self, fragment):
        errors = self.errors()
        self.assertTrue(any(fragment in error for error in errors), errors)

    def test_baseline(self):
        self.assertEqual(self.errors(), [])

    def test_future_semver_releases_are_not_hard_coded(self):
        for version in ("0.5.2", "1.0.0-rc.1+review.7", "2.10.0"):
            with self.subTest(version=version):
                for path in (self.native, self.portable):
                    self.edit(path, lambda data: data.update(version=version))
                self.assertEqual(self.errors(), [])

    def test_malformed_semver_is_rejected(self):
        for version in ("v0.5.1", "0.5", "01.5.1", "1.0.0-01", "1.0.0+", 1):
            with self.subTest(version=version):
                self.edit(self.native, lambda data: data.update(version=version))
                self.assert_rejected("valid SemVer")

    def test_version_drift_is_rejected(self):
        self.edit(self.native, lambda data: data.update(version="0.5.2"))
        self.assert_rejected("version differs")

    def test_portable_override_drift_is_rejected(self):
        self.edit(self.portable, lambda data: data["extensions"]["com.openai"]["interface"].update(
            defaultPrompt=["Prepare a hospitality owner review."]))
        self.assert_rejected("OpenAI interface differs")

    def test_listing_limit_is_enforced(self):
        self.edit(self.native, lambda data: data["interface"].update(shortDescription="x" * 31))
        self.assert_rejected("shortDescription")

    def test_missing_artwork_is_rejected(self):
        (self.plugin / "assets/logo.svg").unlink()
        self.assert_rejected("logo: referenced asset is missing")

    def test_escaping_asset_path_is_rejected(self):
        self.edit(self.native, lambda data: data["interface"].update(logo="./../../outside.svg"))
        self.assert_rejected("asset path escapes")

    def test_undersized_svg_is_rejected(self):
        path = self.plugin / "assets/logo.svg"
        path.write_text('<svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 32 32"/>')
        self.assert_rejected("at least 48 pixels")

    def test_malformed_manifest_is_reported_without_crashing(self):
        for content, fragment in (("[]", "JSON object"), ("{", "cannot read JSON")):
            with self.subTest(content=content):
                self.native.write_text(content, encoding="utf-8")
                self.assert_rejected(fragment)

    def test_missing_portable_manifest_is_rejected(self):
        self.portable.unlink()
        self.assert_rejected("missing required file")

    def test_identities_cannot_change(self):
        self.edit(self.native, lambda data: data.update(name="renamed-plugin"))
        self.assert_rejected("plugin identity must remain")
        self.edit(self.marketplace, lambda data: data.update(name="renamed-marketplace"))
        self.assert_rejected("marketplace identity must remain")

    def test_marketplace_source_cannot_escape_or_change_type(self):
        for source in ({"source": "local", "path": "./../../elsewhere"},
                       {"source": "github", "path": "./plugins/hospitality-os-plugin"}):
            with self.subTest(source=source):
                self.edit(self.marketplace, lambda data: data["plugins"][0].update(source=source))
                self.assert_rejected("marketplace source must name")

    def test_exact_twelve_skill_baseline_is_enforced(self):
        (self.plugin / "skills/phantom-agent").mkdir()
        self.assert_rejected("skill set mismatch")
        shutil.rmtree(self.plugin / "skills/phantom-agent")
        shutil.rmtree(self.plugin / "skills/revenue-optimizer")
        self.assert_rejected("skill set mismatch")

    def test_phantom_integrations_are_rejected(self):
        self.edit(self.native, lambda data: data.update(mcpServers="./mcp.json"))
        self.assert_rejected("unbundled integrations")
        (self.plugin / "mcp.json").write_text("{}", encoding="utf-8")
        self.assert_rejected("unreviewed integration")

    def test_broken_skill_route_is_rejected(self):
        path = self.plugin / "skills/video-production-operator/SKILL.md"
        with path.open("a", encoding="utf-8") as stream:
            stream.write("\n[missing-workflow](../missing-workflow/SKILL.md)\n")
        self.assert_rejected("broken or escaping local reference")

    def test_retired_agent_route_is_rejected(self):
        path = self.plugin / "skills/video-production-operator/SKILL.md"
        with path.open("a", encoding="utf-8") as stream:
            stream.write("\n- Catering offer → Catering Sales Agent\n")
        self.assert_rejected("retired routing label")


if __name__ == "__main__":
    unittest.main()
