# Hospitality OS Plugin

Hospitality OS is a local Codex plugin for restaurants, boutique hotels, beach clubs, catering teams, tourist experiences, and BOSSA Asado i Mar operations.

It packages reusable skills for sales, outreach, events, demos, delivery, market intelligence, weekly AI briefs, decision logs, SOPs, reviews, menu engineering and costing, inventory, revenue optimization, investor materials, social media, staff training, customer recovery, and AI concierge workflows.

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

### v0.2 additions

- Restaurant Outreach Agent
- Hotel Outreach Agent
- Catering Sales Agent
- Event Booking Agent
- Investor Deck Agent
- Social Media Agent
- Menu Costing Agent
- Inventory Agent
- Staff Training Agent
- Customer Recovery Agent

### v0.3 additions: BOSSA Asado i Mar specialization layer

v0.3 adds a BOSSA-specific layer of agents that apply the Hospitality OS workflows directly to BOSSA Asado i Mar's fire-grill menu, Curaçao tourist audience, WhatsApp-based sales, and day-to-day operating rhythm.

- BOSSA Fire Chef Agent
- BOSSA Fire Box Agent
- BOSSA Tourist Experience Agent
- BOSSA WhatsApp Sales Agent
- BOSSA Owner Dashboard Agent
- BOSSA KPI Agent
- BOSSA Inventory Forecast Agent
- BOSSA Reservation Agent

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
