---
name: bossa-menu-costing
description: "Cost BOSSA recipes, breads and Fire Boxes from the authoritative workbook and menu master; reconcile units, yields, item status and proposed margins."
---

# BOSSA Menu & Costing

Read [operating boundaries](references/operating-boundaries.md) and [source navigation](references/source-navigation.md) before producing material recommendations. Apply current owner authorization; the plugin itself grants no external action permission.

## Inputs

Use the owner request, exact action scope/gate, relevant dated source records and the domain inputs below. Complete supported work when inputs are missing; identify only the missing inputs needed for the remaining conclusion.

## Procedure and output

1. Retrieve the current Menu Items — Master, authoritative costing workbook and dated ingredient invoices/test yields. Use spreadsheet skills for workbook analysis/edits. Preserve the legacy workbook read-only.
2. Trace Ingredients → Recipe Ingredient Lines → Recipe Components → Menu Assembly/Direct Purchase → Menu Summary. Identify missing pack size, cost, usable yield, recipe quantities, batch portions and unit conversions before producing totals.
3. Convert compatible units explicitly. Usable unit cost = pack cost / usable quantity; recipe cost = sum(line quantities × unit costs); component portion cost = batch cost / verified portions. Handle yield loss once, not twice. Flag incompatible units and zero denominators.
4. Add evidenced packaging, delivery and other applicable costs separately. Distinguish food cost percentage, gross margin and markup. Label taxes, labor allocation and target margins as assumptions unless approved; never claim profit from food-cost arithmetic alone.
5. Reconcile displayed/approved price and item availability with the master, not legacy ANG exports. Separate proposed selling price from approved customer price. Preserve formulas and inspect current workbook structure before a scoped edit; recalculate and verify using the spreadsheet workflow.

Return: costing table with source/cell, units, yields and line costs; missing inputs; reproducible totals/scenarios; proposed price and approval status; menu alignment conflicts. Stop final pricing when source costs/yields are missing or when the owner authorized costing only.
