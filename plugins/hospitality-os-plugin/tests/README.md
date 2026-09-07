# Tests

From the repository root, run:

```bash
python3 plugins/hospitality-os-plugin/scripts/validate_hospitality_plugin.py
python3 plugins/hospitality-os-plugin/scripts/validate_video_fixtures.py
python3 /path/to/plugin-creator/scripts/validate_plugin.py plugins/hospitality-os-plugin
```

Then validate every `skills/*/SKILL.md` with the skill-creator quick validator and validate the two video-job fixtures against `skills/video-production-operator/schemas/video-job.schema.json`.

Manual behavior checks are defined in:

- [All-skill behavioral matrix](behavioral-test-matrix.md)
- [Video production validation](video-production-agent-validation.md)

The suite is local and read-only with respect to operational systems. It must not contact prospects or guests, create bookings, place orders, schedule content, publish assets, or mutate production data.
