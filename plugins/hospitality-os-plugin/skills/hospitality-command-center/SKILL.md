---
name: hospitality-command-center
description: Produce evidence-controlled daily or weekly hospitality owner reviews, KPIs, priorities, decisions, and follow-ups; use for BOSSA, Sea Horizon, or another supplied client profile.
---

# Hospitality Command Center

Turn current operating evidence into a concise owner decision view. Use generic hospitality, BOSSA, or Sea Horizon mode only when the corresponding authoritative profile is available.

Before working, read:

- [Evidence and source policy](../../references/evidence-and-source-policy.md)
- [Owner gate policy](../../references/owner-gate-policy.md)
- [Common output contract](../../references/common-output-contract.md)

## Inputs

- Period and business
- Sales, covers or occupancy, average check or ADR, reservations, costs, reviews, inventory, staffing, and incidents
- Targets, prior-period values, sources, and verification dates
- Current gate and owner decisions

## Workflow

1. Validate period, units, source dates, and comparable baselines.
2. Calculate only supported KPIs; label missing inputs instead of estimating silently.
3. Explain movement, material variance, risks, and dependencies.
4. Prioritize no more than five actions by safety, deadline, dependency, and value.
5. Assign owner, due date, evidence, and required gate to every action.
6. Record unresolved matters using the common decision-log fields: decision, options, rationale, owner, review date, and reversal trigger.

Do not edit dashboards, production records, or schedules without the exact owner gate.

## Output

Return executive status, KPI table, verified evidence, assumptions/conflicts, risks, decisions, five prioritized actions, and next gate.

## Test prompt

Build BOSSA’s weekly owner review from supplied current and prior-period data. One revenue value conflicts with the source and inventory data is missing. Do not update Notion.
