# Hospitality OS Plugin

Hospitality OS is an evidence-controlled Codex plugin for restaurants, boutique hotels, beach clubs, catering teams, event venues, tourist experiences, and BOSSA Asado i Mar operations.

Version 0.5 consolidates 30 overlapping v0.4 agents into 12 focused Skills. It drafts by default and requires an explicit owner gate before external communication, bookings, financial commitments, production-data changes, publication, deployment, or access changes.

## Repository layout

This repository is a repo-local marketplace root:

```text
.agents/plugins/marketplace.json
plugins/hospitality-os-plugin/
  .codex-plugin/plugin.json
  skills/
  references/
  examples/
  prompts/
  scripts/
  tests/
```

The marketplace entry resolves to `./plugins/hospitality-os-plugin`.

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
python3 /path/to/plugin-creator/scripts/validate_plugin.py plugins/hospitality-os-plugin
python3 plugins/hospitality-os-plugin/scripts/validate_hospitality_plugin.py
```

Validate each Skill with the Skill Creator quick validator:

```bash
for skill in plugins/hospitality-os-plugin/skills/*; do
  python3 /path/to/skill-creator/scripts/quick_validate.py "$skill"
done
```

On Windows PowerShell, replace `python3` and helper paths with the installed Codex runtime paths.

CI runs structural validation and JSON fixtures without calling production systems or requiring secrets.

## Local marketplace installation

This is a non-default repo marketplace. Configure the repository marketplace root according to the installed Codex version, then add `hospitality-os-plugin@hospitality-os`. Installation or reinstallation is intentionally outside the v0.5 implementation gate.

After a separately approved reinstall, start a new Codex thread so updated Skills are loaded.

## License

MIT
