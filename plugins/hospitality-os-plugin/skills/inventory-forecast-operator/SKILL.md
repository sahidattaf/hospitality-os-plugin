---
name: inventory-forecast-operator
description: Analyze hospitality inventory, par levels, yields, waste, stockout risk, and demand forecasts, and prepare order plans without placing purchases or editing stock records.
---

# Inventory and Forecast Operator

Use for stock counts, par levels, waste patterns, purchase planning, weekend demand, reservations-driven forecasts, and BOSSA ingredient requirements.

Read [Evidence policy](../../references/evidence-and-source-policy.md), [Owner gate policy](../../references/owner-gate-policy.md), and [Common output contract](../../references/common-output-contract.md).

## Workflow

1. Validate units, pack sizes, usable yields, lead times, supplier minimums, stock on hand, committed demand, safety stock, and data date.
2. Separate observed sales, reservations, seasonality, promotions, and assumptions.
3. Calculate expected usage, reorder point, recommended quantity, projected ending stock, and waste risk.
4. Provide base, low, and high demand scenarios when uncertainty is material.
5. Draft a purchase plan with supplier, item, unit, quantity, price evidence, and approval status.
6. Stop before placing orders, sending suppliers, or changing inventory records without an exact gate.

Do not infer food safety, shelf life, or storage limits without a verified source and qualified human review.

## Output

Return source/freshness check, forecast table, exceptions, draft order plan, assumptions, validation, and next gate.

## Test prompt

Forecast BOSSA chicken needs for the weekend using supplied reservations and old sales data with mismatched units. Resolve or flag the conflict and do not order.
