# Hospitality OS Plugin v0.5 — Owner Review Package

## Review status

- Branch: `feature/hospitality-os-v0.5`
- Base commit: `b59f7ca6ee00087d81c12c28ac59d553d595a15a`
- Version: `0.5.0`
- Scope: repository implementation and local validation only
- Operational effect: none; the plugin is not installed, published, merged, or deployed

## Owner decision summary

Version 0.5 replaces 30 overlapping workflow agents with 12 focused Skills and introduces shared evidence controls and owner gates. The result is a smaller operating surface with explicit separation between analysis or drafting and external execution.

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

## Material changes

- Reorganized the repository as a valid local marketplace with the plugin under `plugins/hospitality-os-plugin/`.
- Updated the plugin manifest and marketplace metadata for v0.5.
- Added shared policies for owner gates, evidence, privacy, connectors, localization, currency, time, and output contracts.
- Consolidated examples into controlled, non-production demonstrations.
- Updated reusable prompts for the 12-Skill structure.
- Strengthened video workflow controls for drafting, production, scheduling, and publication.
- Expanded the video-job schema with authorization, evidence, and approval records.
- Added structural validation, dependency-free fixtures, behavioral tests, and GitHub Actions validation.

## Execution boundaries

The Skills may research, analyze, plan, calculate, and draft within supplied authorization. Separate owner approval remains mandatory before:

- Contacting prospects, guests, vendors, staff, or partners
- Creating or confirming reservations or events
- Placing orders, making payments, or changing commercial terms
- Editing production systems or controlled master data
- Producing, scheduling, or publishing media
- Deploying software, changing access, or installing the plugin

## Connector position

The repository does not bundle account access. Skills may route to available Notion, Google, GitHub, or Vercel connectors only when the connector is present and the action is separately authorized. WhatsApp, POS, reservation, purchasing, and inventory systems remain draft-or-evidence workflows unless a future approved integration is added.

## Validation evidence

The following local checks passed before commit:

- Hospitality OS structural validator: 12 Skills passed
- Video fixture validator: valid fixture accepted and invalid fixture rejected
- Codex plugin validator: passed
- Codex Skill quick validator: 12 of 12 passed
- Git whitespace and conflict-marker check: passed

## Owner review checklist

- [ ] Approve the 12-Skill consolidation
- [ ] Approve the shared owner-gate and evidence-control model
- [ ] Approve the connector boundaries
- [ ] Approve the repository marketplace layout
- [ ] Approve proceeding to pull-request and CI review
- [ ] Keep installation, merge, and deployment separately gated

## Recommended next gate

`OWNER GATE HOSPITALITY-PLUGIN-V05-4 — APPROVE PULL REQUEST CREATION, REMOTE CI OBSERVATION, AND OWNER REVIEW ONLY.`

This proposed gate must not authorize merge, installation, publication, deployment, or operational-system changes.
