#!/usr/bin/env python3
"""Full Draft 2020-12 validation of the existing synthetic video fixtures."""

import json
from pathlib import Path

try:
    from jsonschema import Draft202012Validator
except ImportError:
    raise SystemExit("Install the validation dependency with: python3 -m pip install 'jsonschema>=4.18,<5'")


def main():
    root = Path(__file__).resolve().parents[1]
    schema = json.loads((root / "skills/video-production-operator/schemas/video-job.schema.json").read_text())
    Draft202012Validator.check_schema(schema)
    validator = Draft202012Validator(schema)
    valid = json.loads((root / "tests/fixtures/video-job-valid.json").read_text())
    invalid = json.loads((root / "tests/fixtures/video-job-invalid-unauthorized.json").read_text())
    validator.validate(valid)
    if not list(validator.iter_errors(invalid)):
        raise SystemExit("Unauthorized negative fixture unexpectedly passed the full schema.")
    print("Video Draft 2020-12 schema fixtures passed (valid accepted; unauthorized rejected).")


if __name__ == "__main__":
    main()
