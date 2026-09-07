#!/usr/bin/env python3
"""Local structural and safety validation for Hospitality OS v0.5."""

from __future__ import annotations

import json
import re
import sys
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


def parse_frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        return {}
    try:
        block = text.split("---\n", 2)[1]
    except IndexError:
        return {}
    result: dict[str, str] = {}
    for line in block.splitlines():
        if ":" in line and not line.startswith((" ", "\t")):
            key, value = line.split(":", 1)
            result[key.strip()] = value.strip().strip("\"'")
    return result


def validate() -> list[str]:
    errors: list[str] = []
    manifest_path = PLUGIN_ROOT / ".codex-plugin" / "plugin.json"
    marketplace_path = REPO_ROOT / ".agents" / "plugins" / "marketplace.json"

    for path in (manifest_path, marketplace_path):
        if not path.is_file():
            errors.append(f"missing required file: {path.relative_to(REPO_ROOT)}")
    if errors:
        return errors

    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    if manifest.get("name") != "hospitality-os-plugin":
        errors.append("manifest name must be hospitality-os-plugin")
    if manifest.get("version") != "0.5.0":
        errors.append("manifest version must be 0.5.0")
    prompts = manifest.get("interface", {}).get("defaultPrompt", [])
    if not isinstance(prompts, list) or not 1 <= len(prompts) <= 3:
        errors.append("manifest defaultPrompt must contain 1-3 prompts")

    marketplace = json.loads(marketplace_path.read_text(encoding="utf-8"))
    entries = marketplace.get("plugins", [])
    match = next((p for p in entries if p.get("name") == "hospitality-os-plugin"), None)
    if not match:
        errors.append("marketplace entry hospitality-os-plugin is missing")
    else:
        source = match.get("source", {})
        resolved = (REPO_ROOT / source.get("path", "")).resolve()
        if not resolved.is_dir() or resolved != PLUGIN_ROOT:
            errors.append("marketplace source does not resolve to the plugin root")

    skills_root = PLUGIN_ROOT / "skills"
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
        if not frontmatter.get("description"):
            errors.append(f"{folder}: description is missing")
        if "## Test prompt" not in text:
            errors.append(f"{folder}: Test prompt section is missing")
        if HIGH_RISK_TERMS.search(text) and "owner-gate-policy.md" not in text:
            errors.append(f"{folder}: high-risk workflow lacks owner-gate policy reference")
        if not agent_file.is_file():
            errors.append(f"{folder}: missing agents/openai.yaml")
        for ref in re.findall(r"\]\((\.\./\.\./references/[^)]+)\)", text):
            if not (skill_file.parent / ref).resolve().is_file():
                errors.append(f"{folder}: broken shared reference {ref}")

    duplicate_names = sorted({name for name in names if name and names.count(name) > 1})
    if duplicate_names:
        errors.append(f"duplicate skill names: {duplicate_names}")

    text_files = [p for p in PLUGIN_ROOT.rglob("*") if p.is_file() and p.suffix.lower() in {".md", ".yaml", ".yml", ".json", ".py"}]
    for path in text_files:
        content = path.read_text(encoding="utf-8")
        unfinished_words = ("TO" + "DO", "T" + "BD")
        if any(re.search(rf"\b{word}\b", content) for word in unfinished_words):
            errors.append(f"unfinished marker in {path.relative_to(PLUGIN_ROOT)}")
        for label, pattern in SECRET_PATTERNS.items():
            if pattern.search(content):
                errors.append(f"possible {label} in {path.relative_to(PLUGIN_ROOT)}")

    examples = (PLUGIN_ROOT / "examples" / "controlled-examples.md").read_text(encoding="utf-8")
    pii_patterns = [
        re.compile(r"\b[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}\b"),
        re.compile(r"(?:\+\d{1,3}[ .-]?)?(?:\(?\d{3}\)?[ .-]?)\d{3}[ .-]?\d{4}"),
    ]
    if any(pattern.search(examples) for pattern in pii_patterns):
        errors.append("controlled examples contain email-address or phone-number shaped data")

    for path in PLUGIN_ROOT.rglob("*.json"):
        try:
            json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            errors.append(f"invalid JSON in {path.relative_to(PLUGIN_ROOT)}: {exc}")

    return errors


def main() -> int:
    errors = validate()
    if errors:
        print("Hospitality OS validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print("Hospitality OS v0.5 structural validation passed (12 skills).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
