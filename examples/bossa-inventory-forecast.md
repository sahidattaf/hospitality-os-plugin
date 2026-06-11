# Example: BOSSA Inventory Forecast

## Input

```text
Venue: BOSSA Asado i Mar
Forecast period: upcoming holiday weekend
Expected reservations: 30% higher than a normal weekend
Current stock: octopus and ribeye levels at normal-weekend par
Supplier lead time: 2 days
```

## Expected output

- Covers forecast with assumptions (30% uplift applied to normal weekend baseline).
- Ingredient demand estimate for octopus and ribeye based on historical mix.
- Stock-vs-forecast comparison.
- Shortage flags (e.g., octopus won't cover Saturday night).
- Recommended order plan with timing (order placed 2 days ahead) and confidence note.
