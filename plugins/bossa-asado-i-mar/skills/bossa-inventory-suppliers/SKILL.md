---
name: bossa-inventory-suppliers
description: "Review BOSSA stock evidence, ingredient purchasing, reorder scenarios and supplier setup; prepare purchase proposals without inventing inventory or ordering."
---

# BOSSA Inventory & Suppliers

Read [operating boundaries](references/operating-boundaries.md) and [source navigation](references/source-navigation.md) before producing material recommendations. Apply current owner authorization; the plugin itself grants no external action permission.

## Inputs

Use the owner request, exact action scope/gate, relevant dated source records and the domain inputs below. Complete supported work when inputs are missing; identify only the missing inputs needed for the remaining conclusion.

## Procedure and output

1. Read current stock counts, units, count timestamps, recipes, demand, supplier setup and evidence/invoices. Separate demo, planned, on-order, received and physically counted stock.
2. Normalize units and identify spoilage, expiry and usable yield. Calculate projected consumption only for an explicit verified booking/sales horizon or a labeled scenario. Avoid counting the same ingredient in multiple component summaries.
3. Calculate projected usable stock = counted usable stock + confirmed receipts within horizon − expected consumption; proposed order = max(0, approved target − projected stock), adjusted for evidenced pack size. Treat missing counts/lead times as gaps, not zero.
4. Compare supplier quotes by dated unit cost, pack size, availability, minimum order, delivery and quality evidence. Do not infer a supplier relationship or available credit from a name in a legacy row.
5. Produce a receiving checklist and financial/menu impact. Prepare a concrete purchase proposal; place an order or message a supplier only with explicit current authorization and verified recipient.

Return: stock/risk table with date/unit/evidence; reorder scenario and assumptions; supplier comparison; cost and approval boundary; assigned/UNASSIGNED owner and next action. Stop claims of availability where physical counts or receipt evidence are missing.
