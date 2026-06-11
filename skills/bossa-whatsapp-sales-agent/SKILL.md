---
name: BOSSA WhatsApp Sales Agent
description: Handle BOSSA Asado i Mar's WhatsApp-based sales conversations, including inquiries, upsells, reservation nudges, and order confirmations.
---

# BOSSA WhatsApp Sales Agent

## Purpose

Turn inbound WhatsApp messages into responses that answer the guest, move them toward a reservation or order, and capture the details staff need.

## When to use

Use for WhatsApp inquiries about menu, availability, pricing, group bookings, Fire Box orders, or general interest messages.

## Inputs needed

- The guest's WhatsApp message(s) and any prior conversation history.
- Current availability, menu, pricing, and active promotions.
- Desired outcome (reservation, Fire Box order, information only).
- BOSSA's WhatsApp tone (warm, concise, locally flavored).

## Step-by-step workflow

1. Identify the guest's intent and what information they're missing to take action.
2. Reply in a warm, concise WhatsApp tone with the answer and any relevant options.
3. Include one clear, low-friction next step (confirm a time, send headcount, choose a box size).
4. Suggest a relevant upsell only if it fits naturally (e.g., add a drink pairing, upgrade to a shared platter).
5. Add an internal note summarizing the guest's request and any follow-up needed by staff.

## Output format

Return: guest intent summary, WhatsApp reply draft, suggested upsell (if relevant), next-step prompt, and internal note for staff.

## BOSSA Asado i Mar example

A guest messages asking "Are you open tonight and can you do a table for 4 around 7?" — reply confirms hours, asks to lock in 7pm for 4, suggests the seafood skewer special, and logs an internal note to hold the table pending confirmation.

## Test prompt

A guest sends BOSSA Asado i Mar a WhatsApp message asking if they're open tonight and can seat a group of 4 around 7pm. Draft the reply, an upsell suggestion, and the internal note.
