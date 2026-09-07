---
name: menu-product-operator
description: Design, cost, price, validate, and prepare hospitality menu products and BOSSA Fire Box or fire-grill concepts without changing the menu master or publishing.
---

# Menu and Product Operator

Use for menu engineering, recipe costing, product concepts, portioning, bundles, packaging, reheating guidance, upsells, and BOSSA Fire Box or fire-grill development.

Read [Evidence policy](../../references/evidence-and-source-policy.md), [Owner gate policy](../../references/owner-gate-policy.md), [Localization and currency](../../references/localization-currency-time.md), and [Common output contract](../../references/common-output-contract.md).

## Workflow

1. Resolve the canonical item and current master record. For BOSSA, use `BOSSA Menu Items — Master` when available.
2. Separate concept fields from approved product fields.
3. Calculate ingredient cost, yield, waste, portion cost, food-cost percentage, contribution, and price scenarios from supplied evidence.
4. Evaluate clarity, guest appeal, operational complexity, packaging, holding, reheating, upsells, and channel fit.
5. Flag unverified allergens, food-safety claims, ingredients, counts, prices, taxes, or delivery fees for human verification.
6. Draft the exact proposed changes and validate calculations.
7. Stop before menu-master edits, purchasing, image approval, QR changes, website output, or publication unless separately gated.

Never present a concept image or example as an approved product record.

## Output

Return current state, cost table, scenarios, product specification, operational notes, proposed master changes, evidence gaps, and next gate.

## Test prompt

Cost and evaluate a proposed seven-piece BOSSA box with three sides and XCG 49.50 when recipe yields are missing. Do not edit the master menu.
