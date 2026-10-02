# Tests

From the repository root, run:

```bash
python3 plugins/hospitality-os-plugin/scripts/validate_hospitality_plugin.py
python3 -m unittest discover -s plugins/hospitality-os-plugin/tests -p 'test_*.py' -v
python3 plugins/hospitality-os-plugin/scripts/validate_video_fixtures.py
python3 -m pip install 'jsonschema>=4.18,<5'
python3 plugins/hospitality-os-plugin/scripts/validate_video_schema.py
git diff --check
```

The structural and regression checks need only Python 3.10 or newer. The 17 regression tests use temporary source copies to verify successful future SemVer releases and rejection of version or interface drift, identity changes, escaping or missing artwork, invalid SVG dimensions, malformed manifests, changed skill sets, phantom integrations, and broken or retired routes.

`validate_video_fixtures.py` is the dependency-free fixture smoke check. `validate_video_schema.py` uses `jsonschema` for the full Draft 2020-12 schema, accepts the valid synthetic fixture, and rejects the unauthorized fixture. CI runs both. No test result here is an official OpenAI package certification.

The Skill Creator quick validator may also be run when that helper is available in the developer's environment. It is not bundled or required by these repository commands.

Manual behavior checks are defined in:

- [All-skill behavioral matrix](behavioral-test-matrix.md)
- [Video production validation](video-production-agent-validation.md)

The suite is local and read-only with respect to operational systems. It must not contact prospects or guests, create bookings, place orders, schedule content, publish assets, or mutate production data.

Source-level behavior exercises, if run, must be labeled separately from installed-plugin acceptance. The BOSSA and Sea Horizon pilot cases remain pending until installation and synthetic acceptance are separately authorized.
