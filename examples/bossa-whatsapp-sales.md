# Example: BOSSA WhatsApp Sales Reply

## Input

```text
Guest WhatsApp message: "Are you open tonight and can you do a table for 4 around 7?"
Context: BOSSA is open tonight, 7pm has availability, seafood skewer is a featured special
```

## Expected output

- Guest intent summary.
- WhatsApp reply draft confirming hours and proposing 7pm for 4.
- Suggested upsell (seafood skewer special), only if it fits naturally.
- Next-step prompt (e.g., confirm headcount or any dietary notes).
- Internal note for staff to hold the table pending confirmation.
