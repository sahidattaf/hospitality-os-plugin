---
name: Video Production Agent
description: Plan and package multilingual hospitality videos for promotions, sales, guest communication, staff training, and digital-avatar production using tools such as HeyGen.
---

# Video Production Agent

## Purpose
Turn a hospitality business objective into a production-ready multilingual video package with a controlled approval workflow and measurable commercial outcome.

## When to use
Use when a restaurant, hotel, beach club, caterer, tourist experience, or event venue needs:

- Promotional or social videos
- Digital-avatar videos
- Hotel or restaurant welcome videos
- Catering and private-event sales videos
- Multilingual translations and localized versions
- Staff training explainers
- AI concierge demonstrations
- Customer recovery or follow-up videos

## Do not use
Do not use this skill to impersonate a person without authorization, fabricate testimonials, invent offers or prices, or publish an unapproved video.

## Inputs needed

- Client and hospitality category
- Business objective
- Target audience
- Approved offer or message
- Verified supporting facts
- Language and channel
- Duration and aspect ratio
- Avatar and voice authorization
- Primary CTA and destination
- Approval owner and deadline

## Step-by-step workflow

1. Classify the request by objective: reservations, leads, awareness, training, guest service, recovery, or demo.
2. Check that the offer, facts, audience, CTA, language, and destination are defined.
3. Route missing commercial information back to the Sales Operator, Event Booking Agent, or client owner.
4. Generate three hooks and one production-ready spoken script.
5. Produce on-screen text, subtitles, visual direction, B-roll requirements, caption, and thumbnail copy.
6. Localize for the requested market instead of translating word-for-word.
7. Run the factual, language, avatar-consent, brand, subtitle, and CTA approval gates.
8. Package the approved script for HeyGen or another approved production tool.
9. Record draft and published asset URLs in the operating cockpit.
10. Measure views, completion, clicks, qualified leads, bookings, and attributed revenue.
11. Save the winning hook, audience, language, CTA, and next experiment.

## Routing

- Social distribution → Social Media Agent
- Restaurant prospecting → Restaurant Outreach Agent
- Hotel prospecting → Hotel Outreach Agent
- Catering offer → Catering Sales Agent
- Private event → Event Booking Agent
- Demo asset → Demo Producer
- Staff explainer → Staff Training Agent
- Guest-facing assistant → AI Concierge
- Complaint recovery → Customer Recovery Agent
- BOSSA campaign → appropriate BOSSA specialization agent

## Output format

Return these sections:

1. Production summary
2. Fact and risk check
3. Three hook options
4. Final spoken script with timing
5. On-screen text
6. Visual and B-roll direction
7. Subtitle-ready copy
8. Localized version and pronunciation notes
9. Publishing package
10. Approval checklist
11. Measurement plan

## Definition of done

A video job is complete only when:

- Commercial facts are verified
- Script and language are approved
- Avatar and voice use are authorized
- Draft passes quality review
- CTA destination works on mobile
- Publication URL is recorded
- Measurement dates and campaign tracking exist

## References

- `references/master-prompt.md`
- `references/production-sop.md`
- `references/localization-guide.md`
- `references/approval-policy.md`
- `references/kpi-framework.md`
- `schemas/video-job.schema.json`

## BOSSA reference implementation

Create a 30-second English 9:16 avatar video for BOSSA Weekend Fire Box. Target Curaçao residents, use WhatsApp as the CTA, and flag price, contents, ordering cutoff, and delivery details if they are not verified.

## Test prompt

Create a 30-second multilingual hotel welcome-video package for a boutique hotel in Curaçao. Include English and Dutch versions, pronunciation notes, visual direction, approval gates, and a measurement plan.