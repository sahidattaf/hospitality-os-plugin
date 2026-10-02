# Hospitality OS Plugin

Hospitality OS is an evidence-controlled Codex plugin for restaurants, boutique hotels, beach clubs, catering teams, event venues, tourist experiences, and BOSSA Asado i Mar operations.

Version 0.5 consolidates 30 overlapping v0.4 agents into 12 focused Skills. The 0.5.1 candidate repairs packaging and routing while retaining those workflows. It drafts by default and requires an explicit owner gate before external communication, bookings, financial commitments, production-data changes, publication, deployment, or access changes.

## Repository layout

This repository is a repo-local marketplace root:

```text
.agents/plugins/marketplace.json
plugins/hospitality-os-plugin/
  plugin.json
  .codex-plugin/plugin.json
  assets/
  skills/
  references/
  examples/
  prompts/
  scripts/
  tests/
```

The marketplace entry resolves to `./plugins/hospitality-os-plugin`. Marketplace identity `hospitality-os` and plugin identity `hospitality-os-plugin` are unchanged; the installation key is `hospitality-os-plugin@hospitality-os`. The marketplace display label is **GPT Innovation by Attaf**.

The plugin root includes a portable manifest with OpenAI listing metadata in `extensions.com.openai.interface`, plus the supported native Codex manifest. The portable OpenAI extension takes precedence; these interfaces are not merged. Local checks require matching identity, version, shared metadata, and interface values. The package supplies light and dark SVG artwork and the 29-character subtitle **Hospitality planning & drafts**.

## Included Skills

1. Hospitality Command Center
2. Hospitality Sales Operator
3. Events and Catering Operator
4. Guest Sales and Reservations
5. Guest Experience Operator
6. Menu and Product Operator
7. Inventory and Forecast Operator
8. Revenue Optimizer
9. Hospitality Market Intelligence
10. Hospitality Delivery Manager
11. SOP and Training Operator
12. Video Production Operator

Business-specific modes include generic hospitality, BOSSA Asado i Mar, Sea Horizon Apartments, and a future named client when an authoritative client profile is supplied. Business facts are not hard-coded as current truth.

## Safety model

- Classify facts as Verified, Owner-provided, Assumption, Conflict, or Missing evidence.
- Use `BOSSA Menu Items — Master` as the sole editable BOSSA menu source when available.
- Research, analysis, planning, and drafting do not authorize execution.
- Require a fresh owner gate before sending, confirming, ordering, paying, publishing, deploying, or changing live data.
- Verify every material result and stop at the approved boundary.
- Keep guest, staff, client, investor, and credential data out of this public repository.

Shared policies are in `plugins/hospitality-os-plugin/references/`.

## Connector model

The plugin contains Skills, not bundled account access. It can route to Notion, Google Contacts, Gmail, Google Calendar, Google Drive, GitHub, and Vercel only when those connectors are available in the current session and the requested action is authorized.

No WhatsApp, POS, reservation, purchasing, or inventory connector is bundled. For those systems, the plugin prepares drafts or analyzes supplied evidence.

## Validation

From the repository root:

```bash
python3 plugins/hospitality-os-plugin/scripts/validate_hospitality_plugin.py
python3 -m unittest discover -s plugins/hospitality-os-plugin/tests -p 'test_*.py' -v
python3 plugins/hospitality-os-plugin/scripts/validate_video_fixtures.py
```

For full Draft 2020-12 video-schema validation, install the development dependency and run:

```bash
python3 -m pip install 'jsonschema>=4.18,<5'
python3 plugins/hospitality-os-plugin/scripts/validate_video_schema.py
git diff --check
```

On Windows PowerShell, use `py` in place of `python3` when appropriate. These commands run from the repository root and do not require external validator scripts, account access, or secrets.

CI runs the same package checks, 17 regression tests, and both fixture checks. The package validator enforces this repository's listing limits, safe asset paths, native/portable agreement, SemVer, current routing links, and exactly 12 skills. It is a local project check; installed behavior and platform acceptance still require separate verification. See [test instructions](plugins/hospitality-os-plugin/tests/README.md).

## Local marketplace installation

Use the [getting-started guide](docs/GETTING-STARTED.md) for the verified CLI and workspace routes. The 0.5.1 changes are a local candidate until separately accepted and made available remotely. Adding `main` before that step retrieves the existing 0.5.0 package.

Installation, refresh, workspace import, and public submission are outside `HOSPITALITY-PLUGIN-MARKETPLACE-2`. After a separately approved install or refresh, start a new Codex thread and run synthetic acceptance checks before using live business evidence.

## Release records

See [CHANGELOG.md](CHANGELOG.md). [The v0.5 owner review](HOSPITALITY_OS_V0.5_OWNER_REVIEW.md) is a historical pre-merge record; PR #3 subsequently merged the consolidation on September 7, 2026. It is not evidence that the 0.5.1 candidate has been installed or approved for release.

## License

The existing manifests declare MIT. A standalone license file and copyright statement remain an owner-confirmation item before distribution.
