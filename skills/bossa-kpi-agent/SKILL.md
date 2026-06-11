---
name: BOSSA KPI Agent
description: Calculate and report BOSSA Asado i Mar's key operating KPIs, including covers, average check, food cost, labor cost, and trend comparisons.
---

# BOSSA KPI Agent

## Purpose

Turn raw sales, cost, and labor data into BOSSA's core KPIs with trend context and clear takeaways.

## When to use

Use for periodic (daily, weekly, monthly) KPI reporting, or when checking performance against targets.

## Inputs needed

- Sales data: covers, revenue, by day or shift if available.
- Cost data: cost of goods sold (food/beverage) and labor hours/cost for the period.
- Prior period figures for comparison, if available.
- KPI targets (e.g., target food cost %, target labor %, target average check).

## Step-by-step workflow

1. Calculate core KPIs: covers, average check, food cost %, labor cost %, and revenue per period.
2. Compare each KPI to the prior period and to target, noting direction and size of change.
3. Identify the one or two KPIs most in need of attention.
4. Suggest a likely driver for any significant change (positive or negative).
5. Recommend one concrete action per flagged KPI.

## Output format

Return: KPI table (metric, value, prior period, target, status), key drivers, and recommended actions.

## BOSSA Asado i Mar example

Report a week where average check rose to $42 (up from $38, target $40 — on track), food cost hit 31% (target 28% — over, likely driven by octopus price increase), and labor cost held at 24% (on target), with a recommendation to review octopus portioning or pricing.

## Test prompt

Calculate this week's KPIs for BOSSA Asado i Mar (covers, average check, food cost %, labor cost %) against last week and targets, and recommend actions for any KPI that's off track.
