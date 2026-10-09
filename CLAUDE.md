# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

A Codex/Claude plugin (currently v0.4.0) that packages reusable hospitality-operations skills for restaurants, boutique hotels, beach clubs, catering teams, tourist experiences, and a BOSSA Asado i Mar specialization layer. There is no application code — the repo is a collection of Markdown skill definitions, prompts, examples, and a JSON schema for video jobs.

The skill set has grown in versioned waves:

- **v0.1** — core operations: Sales Operator, Demo Producer, Delivery Manager, Market Intelligence, Weekly AI Brief, Decision Log, SOP Builder, Review Generator, Menu Engineer, Revenue Optimizer, AI Concierge.
- **v0.2** — outreach/finance/ops additions: Restaurant Outreach, Hotel Outreach, Catering Sales, Event Booking, Investor Deck, Social Media, Menu Costing, Inventory, Staff Training, Customer Recovery agents.
- **v0.3** — BOSSA Asado i Mar specialization layer: Fire Chef, Fire Box, Tourist Experience, WhatsApp Sales, Owner Dashboard, KPI, Inventory Forecast, Reservation agents.
- **v0.4** — Multilingual Video Production Agent (`skills/video-production-agent/`), with `references/`, `templates/`, and `schemas/video-job.schema.json`.

## Structure

- `.codex-plugin/plugin.json` — plugin manifest (name, version, skill registration, keywords, default prompts).
- `.agents/plugins/marketplace.json` — repo-local marketplace metadata referencing this plugin as a local source.
- `skills/<skill-name>/SKILL.md` — one skill per workflow, each following the same template (frontmatter `name`/`description`, then Purpose, When to use, Inputs needed, Step-by-step workflow, Output format, BOSSA Asado i Mar example, Test prompt). The video production agent additionally has `references/`, `templates/`, and `schemas/` subfolders.
- `examples/` — sample inputs and expected outputs per skill, including `examples/video-production/`.
- `prompts/hospitality-os-prompts.md` and `prompts/video-production-agent.md` — reusable prompt starters.
- `tests/` — validation notes (`README.md`), a lightweight `yaml.py` checker, and `video-production-agent-validation.md`.

## Validation

Run the plugin validator (Python from the Codex runtime):

```powershell
C:\Users\sahid\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe C:\Users\sahid\.codex\skills\.system\plugin-creator\scripts\validate_plugin.py C:\Users\sahid\OneDrive\Documents\hospitality-os-plugin
```

Expected output: `Plugin validation passed`.

> Note: the validator path above points at `OneDrive\Documents\hospitality-os-plugin`. Confirm this still matches wherever the validator expects the plugin to live before relying on it from this clone (`C:\Users\sahid\plugins\hospitality-os-plugin`).

Manual smoke test for any skill change: run that skill's "Test prompt" (including the v0.2/v0.3 outreach and BOSSA agents, and the v0.4 video production agent — see `tests/video-production-agent-validation.md`) and confirm the response matches its "Output format," and that BOSSA-specific examples stay grounded in the facts provided in the prompt.

## Editing skills

When adding or editing a `skills/*/SKILL.md`, keep the existing section order and frontmatter shape (`name`, `description`) consistent with the other skills — the validator and other tooling expect this structure. Each skill should include a BOSSA Asado i Mar example and a Test prompt. When adding a new skill, also update `.codex-plugin/plugin.json` (keywords/defaultPrompt as relevant) and add a corresponding entry under `examples/` and a smoke-test prompt in `tests/`.
