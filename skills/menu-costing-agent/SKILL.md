---
name: Menu Costing Agent
description: Calculate food cost percentages, suggest menu pricing, and identify margin risks for hospitality menu items.
---

# Menu Costing Agent

## Purpose

Turn ingredient and recipe data into accurate food cost percentages, pricing recommendations, and margin insights.

## When to use

Use when adding a new menu item, reviewing pricing, or investigating why a dish isn't hitting margin targets.

## Inputs needed

- Recipe ingredients with quantities and unit costs.
- Portion size and yield (including waste/trim factors if known).
- Current or proposed menu price.
- Target food cost percentage or margin goal.

## Step-by-step workflow

1. Calculate total recipe cost from ingredient quantities and unit costs.
2. Compute cost per portion, accounting for yield and waste.
3. Calculate food cost percentage at the current or proposed price.
4. Compare against the target food cost percentage and flag gaps.
5. Recommend a price, portion adjustment, or ingredient substitution to hit target margin.

## Output format

Return: recipe cost breakdown, cost per portion, food cost percentage, comparison to target, and pricing/portion recommendations.

## BOSSA Asado i Mar example

Cost out the seafood skewer using shrimp, octopus, peppers, and marinade quantities, compute cost per portion, and recommend a menu price to hit a 28% food cost target.

## Test prompt

Calculate the food cost percentage for BOSSA's seafood skewer given ingredient costs and portion size, and recommend a menu price for a 28% food cost target.
