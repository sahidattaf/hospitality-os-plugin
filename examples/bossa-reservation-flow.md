# Example: BOSSA Reservation Flow

## Input

```text
Venue: BOSSA Asado i Mar
Request: table for 6 at 8pm Friday
Availability: 8pm fully booked, 8:30pm open
Policy: deposit required for parties of 6+
```

## Expected output

- Availability result (8pm unavailable, 8:30pm open).
- Guest-facing message proposing the 8:30pm alternative.
- Policy note on the large-party deposit requirement.
- Internal note for the floor team (table assignment, e.g., sunset-view table if available).
