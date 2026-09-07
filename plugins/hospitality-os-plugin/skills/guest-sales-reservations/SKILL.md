---
name: guest-sales-reservations
description: Prepare guest inquiry, reservation, waitlist, modification, cancellation, WhatsApp sales, and upsell workflows for hospitality businesses; live confirmations require explicit approval.
---

# Guest Sales and Reservations

Use for inbound guest messages, table or room requests, waitlists, changes, cancellations, availability alternatives, and appropriate upsells.

Read [Owner gate policy](../../references/owner-gate-policy.md), [Evidence policy](../../references/evidence-and-source-policy.md), [Privacy policy](../../references/privacy-and-public-repo-policy.md), and [Connector routing](../../references/connector-routing.md).

## Workflow

1. Identify intent, date, time, timezone, party/guest count, preferences, accessibility, allergies, and contact channel.
2. Verify current availability, hours, inventory, price, policy, and promotion from an authoritative source.
3. Draft the answer, closest alternatives, one relevant upsell, and internal note.
4. Distinguish **draft**, **hold requested**, **confirmed**, **waitlisted**, **modified**, and **cancelled** states.
5. Validate the guest identity and exact record before any change.
6. Stop before sending or changing a live reservation, waitlist, calendar, order, or guest record without an exact owner gate.

Never claim a booking is confirmed from a draft response. Do not expose other guests’ information.

## Output

Return intent, verified availability, missing evidence, guest-facing draft, upsell, internal note, target status, validation, and next gate.

## Test prompt

A guest asks by WhatsApp for a Friday table for six, but availability data is missing. Draft a warm reply and alternatives without confirming or sending.
