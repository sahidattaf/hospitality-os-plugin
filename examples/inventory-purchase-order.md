# Example: Inventory Purchase Order

## Input

```text
Venue: BOSSA Asado i Mar
Counts vs. par (this week):
- Octopus: 6kg on hand / 15kg par
- Shrimp: 12kg on hand / 12kg par
- Ribeye: 20kg on hand / 18kg par
- House cocktail spirits: low on one SKU
Context: busy weekend ahead, next delivery in 2 days
```

## Expected output

- Stock-vs-par table.
- Purchase order list with quantities needed to reach par.
- Flags for items at risk of stockout before next delivery (e.g., octopus).
- Waste/variance notes and likely causes, if any.
- Par level recommendations based on the upcoming busy weekend.
