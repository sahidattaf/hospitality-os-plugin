#!/usr/bin/env python3
"""Validate v0.5 video fixtures without third-party runtime dependencies."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "skills/video-production-operator/schemas/video-job.schema.json"
FIXTURES = ROOT / "tests/fixtures"


def basic_errors(instance: dict, schema: dict) -> list[str]:
    errors: list[str] = []
    required = set(schema.get("required", []))
    properties = schema.get("properties", {})
    missing = required - set(instance)
    extra = set(instance) - set(properties)
    if missing:
        errors.append(f"missing required properties: {sorted(missing)}")
    if schema.get("additionalProperties") is False and extra:
        errors.append(f"unexpected properties: {sorted(extra)}")
    for key, definition in properties.items():
        if key not in instance:
            continue
        value = instance[key]
        if "enum" in definition and value not in definition["enum"]:
            errors.append(f"{key}: value is outside enum")
        if definition.get("type") == "array" and not isinstance(value, list):
            errors.append(f"{key}: expected array")
        if definition.get("type") == "string" and not isinstance(value, str):
            errors.append(f"{key}: expected string")
    return errors


def main() -> int:
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    valid = json.loads((FIXTURES / "video-job-valid.json").read_text(encoding="utf-8"))
    invalid = json.loads((FIXTURES / "video-job-invalid-unauthorized.json").read_text(encoding="utf-8"))
    valid_errors = basic_errors(valid, schema)
    invalid_errors = basic_errors(invalid, schema)
    if valid_errors:
        print("Valid fixture failed:", *valid_errors, sep="\n- ")
        return 1
    if not invalid_errors:
        print("Invalid fixture unexpectedly passed.")
        return 1
    print("Video schema fixture checks passed (valid accepted; invalid rejected).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
