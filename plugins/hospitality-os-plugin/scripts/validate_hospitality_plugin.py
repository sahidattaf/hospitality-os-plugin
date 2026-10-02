#!/usr/bin/env python3
"""Local package, routing, and safety checks; not an official runtime validator."""

from __future__ import annotations

import json
import math
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path


PLUGIN_ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = PLUGIN_ROOT.parents[1]
EXPECTED_SKILLS = {
    "events-catering-operator",
    "guest-experience-operator",
    "guest-sales-reservations",
    "hospitality-command-center",
    "hospitality-delivery-manager",
    "hospitality-market-intelligence",
    "hospitality-sales-operator",
    "inventory-forecast-operator",
    "menu-product-operator",
    "revenue-optimizer",
    "sop-training-operator",
    "video-production-operator",
}
HIGH_RISK_TERMS = re.compile(
    r"publish|publication|send|book|reservation|order|purchase|payment|schedule|production|external",
    re.IGNORECASE,
)
SECRET_PATTERNS = {
    "OpenAI key": re.compile(r"sk-[A-Za-z0-9_-]{20,}"),
    "GitHub token": re.compile(r"gh[pousr]_[A-Za-z0-9]{20,}"),
    "private key": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
}
SEMVER = re.compile(
    r"(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)"
    r"(?:-(?:0|[1-9][0-9]*|[0-9]*[A-Za-z-][0-9A-Za-z-]*)"
    r"(?:\.(?:0|[1-9][0-9]*|[0-9]*[A-Za-z-][0-9A-Za-z-]*))*)?"
    r"(?:\+[0-9A-Za-z-]+(?:\.[0-9A-Za-z-]+)*)?"
)
SHARED_MANIFEST_FIELDS = (
    "name", "version", "description", "author", "homepage", "repository", "license", "keywords"
)
RETIRED_ROUTES = (
    "Social Media Agent", "Restaurant Outreach Agent", "Hotel Outreach Agent",
    "Catering Sales Agent", "Event Booking Agent", "Demo Producer",
    "Staff Training Agent", "Customer Recovery Agent", "BOSSA specialization agent",
)


def read_object(path: Path, errors: list[str]) -> dict:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"cannot read JSON object {path.name}: {exc}")
        return {}
    if not isinstance(value, dict):
        errors.append(f"{path.name}: manifest must be a JSON object")
        return {}
    return value


def asset_errors(value: object, plugin_root: Path) -> list[str]:
    if not isinstance(value, str) or not value.startswith("./") or "\\" in value:
        return ["asset path must start with ./ and use forward slashes"]
    path = (plugin_root / value).resolve()
    if not path.is_relative_to(plugin_root.resolve()):
        return ["asset path escapes the plugin root"]
    if not path.is_file():
        return ["referenced asset is missing"]
    if path.stat().st_size > 5 * 1024 * 1024:
        return ["asset exceeds 5 MiB"]
    if path.suffix.lower() != ".svg":
        return ["this package's artwork must be SVG"]
    try:
        svg = ET.parse(path).getroot()
        width, height = float(svg.get("width", "0")), float(svg.get("height", "0"))
        box = [float(n) for n in svg.get("viewBox", "").split()]
        if svg.tag != "{http://www.w3.org/2000/svg}svg":
            return ["asset is not an SVG document"]
        if not (all(math.isfinite(n) for n in (width, height, *box))
                and width == height and width >= 48 and len(box) == 4
                and box[2] == box[3] and box[2] >= 48):
            return ["SVG must be square and at least 48 pixels"]
    except (ET.ParseError, ValueError, OSError):
        return ["invalid SVG artwork"]
    return []


def manifest_errors(manifest: dict, portable: bool, plugin_root: Path) -> list[str]:
    errors: list[str] = []
    if manifest.get("name") != "hospitality-os-plugin":
        errors.append("plugin identity must remain hospitality-os-plugin")
    version = manifest.get("version")
    if not isinstance(version, str) or not SEMVER.fullmatch(version):
        errors.append("manifest version must be valid SemVer")
    if not isinstance(manifest.get("description"), str) or not manifest["description"].strip():
        errors.append("manifest description is missing")
    author = manifest.get("author")
    if not isinstance(author, dict) or not isinstance(author.get("name"), str) or not author["name"].strip():
        errors.append("manifest author name is missing")
    openai: dict = {}
    if portable:
        if manifest.get("$schema") != "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json":
            errors.append("portable schema reference mismatch")
        extensions = manifest.get("extensions")
        if isinstance(extensions, dict) and isinstance(extensions.get("com.openai"), dict):
            openai = extensions["com.openai"]
        else:
            errors.append("portable OpenAI extension is missing")
        if "skills" in manifest:
            errors.append("portable format discovers the existing skills directory")
        ui = openai.get("interface")
    else:
        if manifest.get("skills") != "./skills/":
            errors.append("native skills path must be ./skills/")
        ui = manifest.get("interface")
    # This release contains instructions and resources only. New integration
    # declarations need their own implementation and review, not metadata stubs.
    if any(key in obj for obj in (manifest, openai) for key in ("apps", "mcpServers", "mcp", "hooks")):
        errors.append("skills-only package must not declare unbundled integrations")
    if not isinstance(ui, dict):
        errors.append("OpenAI interface must be an object")
        return errors
    for field, maximum in (("displayName", 30), ("shortDescription", 30),
                           ("longDescription", 4000), ("developerName", 80)):
        value = ui.get(field)
        if not isinstance(value, str) or not value.strip() or len(value) > maximum:
            errors.append(f"{field} must contain 1-{maximum} characters")
    if ui.get("category") != "Productivity":
        errors.append("listing category must remain Productivity")
    capabilities = ui.get("capabilities")
    if (not isinstance(capabilities, list) or len(capabilities) > 20
            or any(not isinstance(item, str) or not item.strip() or len(item) > 120 for item in capabilities)):
        errors.append("capabilities must be a list of at most 20 labels of at most 120 characters")
    prompts = ui.get("defaultPrompt")
    if (not isinstance(prompts, list) or not 1 <= len(prompts) <= 3
            or any(not isinstance(item, str) or not item.strip() or len(item) > 128 or "@" in item for item in prompts)):
        errors.append("defaultPrompt must contain 1-3 prompts, each at most 128 characters without @")
    elif len(set(prompts)) != len(prompts):
        errors.append("defaultPrompt must not contain duplicates")
    for field in ("brandColor", "brandColorDark"):
        if not isinstance(ui.get(field), str) or not re.fullmatch(r"#[0-9A-Fa-f]{6}", ui[field]):
            errors.append(f"{field} must be a six-digit hex color")
    for field in ("composerIcon", "logo", "composerIconDark", "logoDark"):
        errors.extend(f"{field}: {error}" for error in asset_errors(ui.get(field), plugin_root))
    return errors


def parse_frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        return {}
    parts = text.split("---\n", 2)
    if len(parts) != 3:
        return {}
    block = parts[1]
    result: dict[str, str] = {}
    for line in block.splitlines():
        if ":" in line and not line.startswith((" ", "\t")):
            key, value = line.split(":", 1)
            result[key.strip()] = value.strip().strip("\"'")
    return result


def validate(plugin_root: Path = PLUGIN_ROOT, repo_root: Path = REPO_ROOT) -> list[str]:
    errors: list[str] = []
    plugin_root, repo_root = plugin_root.resolve(), repo_root.resolve()
    manifest_path = plugin_root / ".codex-plugin" / "plugin.json"
    portable_path = plugin_root / "plugin.json"
    marketplace_path = repo_root / ".agents" / "plugins" / "marketplace.json"

    for path in (manifest_path, portable_path, marketplace_path):
        if not path.is_file():
            errors.append(f"missing required file: {path.relative_to(repo_root)}")
    if errors:
        return errors

    manifest = read_object(manifest_path, errors)
    portable = read_object(portable_path, errors)
    errors.extend(manifest_errors(manifest, False, plugin_root))
    errors.extend(manifest_errors(portable, True, plugin_root))
    for field in SHARED_MANIFEST_FIELDS:
        if manifest.get(field) != portable.get(field):
            errors.append(f"{field} differs between native and portable manifests")
    extensions = portable.get("extensions")
    openai = extensions.get("com.openai") if isinstance(extensions, dict) else None
    if not isinstance(openai, dict) or openai.get("interface") != manifest.get("interface"):
        errors.append("OpenAI interface differs between native and portable manifests")

    marketplace = read_object(marketplace_path, errors)
    if marketplace.get("name") != "hospitality-os":
        errors.append("marketplace identity must remain hospitality-os")
    entries = marketplace.get("plugins", [])
    if not isinstance(entries, list) or len(entries) != 1 or not isinstance(entries[0], dict):
        errors.append("marketplace must contain exactly one real plugin entry")
    else:
        match = entries[0]
        if match.get("name") != "hospitality-os-plugin":
            errors.append("marketplace plugin identity mismatch")
        source = match.get("source", {})
        if source != {"source": "local", "path": "./plugins/hospitality-os-plugin"}:
            errors.append("marketplace source must name the existing local plugin root")
        elif (repo_root / source["path"]).resolve() != plugin_root:
            errors.append("marketplace source does not resolve to the plugin root")
        if match.get("policy") != {"installation": "AVAILABLE", "authentication": "ON_INSTALL"}:
            errors.append("marketplace policy mismatch")
        if match.get("category") != "Productivity":
            errors.append("marketplace category mismatch")

    for relative in ("mcp.json", ".mcp.json", ".app.json", "hooks.json", "mcp", "hooks"):
        if (plugin_root / relative).exists():
            errors.append(f"skills-only package contains an unreviewed integration: {relative}")

    skills_root = plugin_root / "skills"
    if not skills_root.is_dir():
        return errors + ["missing skills directory"]
    found = {p.name for p in skills_root.iterdir() if p.is_dir()}
    if found != EXPECTED_SKILLS:
        errors.append(
            f"skill set mismatch; missing={sorted(EXPECTED_SKILLS-found)}, extra={sorted(found-EXPECTED_SKILLS)}"
        )

    names: list[str] = []
    for folder in sorted(found):
        skill_file = skills_root / folder / "SKILL.md"
        agent_file = skills_root / folder / "agents" / "openai.yaml"
        if not skill_file.is_file():
            errors.append(f"{folder}: missing SKILL.md")
            continue
        text = skill_file.read_text(encoding="utf-8")
        frontmatter = parse_frontmatter(text)
        name = frontmatter.get("name")
        names.append(name or "")
        if name != folder:
            errors.append(f"{folder}: frontmatter name must match folder")
        if not name or len(name) > 64 or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name):
            errors.append(f"{folder}: invalid skill name")
        description = frontmatter.get("description", "")
        if not description or len(description) > 1024 or "<" in description or ">" in description:
            errors.append(f"{folder}: description must contain 1-1024 characters without angle brackets")
        if "## Test prompt" not in text:
            errors.append(f"{folder}: Test prompt section is missing")
        if HIGH_RISK_TERMS.search(text) and "owner-gate-policy.md" not in text:
            errors.append(f"{folder}: high-risk workflow lacks owner-gate policy reference")
        if not agent_file.is_file():
            errors.append(f"{folder}: missing agents/openai.yaml")

    duplicate_names = sorted({name for name in names if name and names.count(name) > 1})
    if duplicate_names:
        errors.append(f"duplicate skill names: {duplicate_names}")

    text_files = [p for p in plugin_root.rglob("*") if p.is_file() and p.suffix.lower() in {".md", ".yaml", ".yml", ".json", ".py"}]
    for path in text_files:
        content = path.read_text(encoding="utf-8")
        unfinished_words = ("TO" + "DO", "T" + "BD")
        if any(re.search(rf"\b{word}\b", content) for word in unfinished_words):
            errors.append(f"unfinished marker in {path.relative_to(plugin_root)}")
        for label, pattern in SECRET_PATTERNS.items():
            if pattern.search(content):
                errors.append(f"possible {label} in {path.relative_to(plugin_root)}")
        if path.suffix.lower() == ".md":
            for target in re.findall(r"\]\(([^)\s]+)\)", content):
                if target.startswith(("https://", "http://", "mailto:", "#")):
                    continue
                resolved = (path.parent / target.split("#", 1)[0]).resolve()
                if not resolved.is_relative_to(plugin_root) or not resolved.is_file():
                    errors.append(f"{path.relative_to(plugin_root)}: broken or escaping local reference {target}")

    for relative in ("skills/video-production-operator/SKILL.md",
                     "skills/video-production-operator/references/production-sop.md",
                     "tests/video-production-agent-validation.md"):
        path = plugin_root / relative
        if path.is_file():
            content = path.read_text(encoding="utf-8")
            for retired in RETIRED_ROUTES:
                if retired in content:
                    errors.append(f"{relative}: retired routing label {retired}")

    examples_path = plugin_root / "examples" / "controlled-examples.md"
    examples = examples_path.read_text(encoding="utf-8") if examples_path.is_file() else ""
    if not examples_path.is_file():
        errors.append("controlled examples are missing")
    pii_patterns = [
        re.compile(r"\b[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}\b"),
        re.compile(r"(?:\+\d{1,3}[ .-]?)?(?:\(?\d{3}\)?[ .-]?)\d{3}[ .-]?\d{4}"),
    ]
    if any(pattern.search(examples) for pattern in pii_patterns):
        errors.append("controlled examples contain email-address or phone-number shaped data")

    for path in plugin_root.rglob("*.json"):
        try:
            json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            errors.append(f"invalid JSON in {path.relative_to(plugin_root)}: {exc}")

    return errors


def main() -> int:
    errors = validate()
    if errors:
        print("Hospitality OS validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    version = json.loads((PLUGIN_ROOT / "plugin.json").read_text(encoding="utf-8"))["version"]
    print(f"Hospitality OS {version} local package validation passed (12 skills).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
