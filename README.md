# Hospitality OS Plugin

Hospitality OS is a local Codex plugin for restaurants, boutique hotels, beach clubs, catering teams, tourist experiences, and BOSSA Asado i Mar operations.

It packages reusable skills for sales, demos, delivery, market intelligence, weekly AI briefs, decision logs, SOPs, reviews, menu engineering, revenue optimization, and AI concierge workflows.

## Included Skills

- Sales Operator
- Demo Producer
- Delivery Manager
- Market Intelligence
- Weekly AI Brief
- Decision Log
- SOP Builder
- Review Generator
- Menu Engineer
- Revenue Optimizer
- AI Concierge

## Structure

- `.codex-plugin/plugin.json` contains the plugin manifest.
- `skills/` contains one Codex skill per Hospitality OS workflow.
- `examples/` contains sample inputs and outputs.
- `prompts/` contains reusable prompt starters.
- `tests/` contains validation notes and lightweight checks.
- `.agents/plugins/marketplace.json` contains repo-local marketplace metadata.

## Validation

```powershell
C:\Users\sahid\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe C:\Users\sahid\.codex\skills\.system\plugin-creator\scripts\validate_plugin.py C:\Users\sahid\OneDrive\Documents\hospitality-os-plugin
```

Expected result:

```text
Plugin validation passed
```
