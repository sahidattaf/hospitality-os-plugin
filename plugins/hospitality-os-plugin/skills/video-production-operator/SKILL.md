---
name: video-production-operator
description: Plan and package multilingual hospitality campaigns and videos with factual, identity, language, production, release, and measurement gates; publication remains separately authorized.
---

# Video Production Operator

## Purpose
Turn a hospitality business objective into a production-ready multilingual video package with a controlled approval workflow and measurable commercial outcome.

Before working, read:

- [Owner gate policy](../../references/owner-gate-policy.md)
- [Evidence and source policy](../../references/evidence-and-source-policy.md)
- [Privacy and public repository policy](../../references/privacy-and-public-repo-policy.md)
- [Connector routing](../../references/connector-routing.md)
- [Localization, currency, and time](../../references/localization-currency-time.md)

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
3. Route missing commercial information to `hospitality-sales-operator` for prospecting, `events-catering-operator` for event or catering terms, or the client owner for authoritative facts.
4. Generate three hooks and one production-ready spoken script.
5. Produce on-screen text, subtitles, visual direction, B-roll requirements, caption, and thumbnail copy.
6. Localize for the requested market instead of translating word-for-word.
7. Run the factual, language, avatar-consent, brand, subtitle, and CTA approval gates.
8. Package the approved script for HeyGen or another approved production tool.
9. Record draft and, only after an explicit publication gate, published asset URLs in the operating cockpit.
10. Measure views, completion, clicks, qualified leads, bookings, and attributed revenue.
11. Save the winning hook, audience, language, CTA, and next experiment.

## Routing

Use the current skill identifiers below. A handoff carries the brief, evidence status, missing inputs, and authorization boundary; it grants no account access or execution permission.

| Need | Current workflow |
| --- | --- |
| Video captions, thumbnail copy, and channel packaging | Continue in `video-production-operator`; a dated, multi-channel social calendar is outside the packaged workflow |
| Restaurant or hotel prospecting | [hospitality-sales-operator](../hospitality-sales-operator/SKILL.md) |
| Catering offer or private event terms | [events-catering-operator](../events-catering-operator/SKILL.md) |
| Demo delivery, broken CTA, or lead flow | [hospitality-delivery-manager](../hospitality-delivery-manager/SKILL.md) |
| Staff explainer or training content | [sop-training-operator](../sop-training-operator/SKILL.md) |
| Guest welcome, concierge content, or complaint recovery | [guest-experience-operator](../guest-experience-operator/SKILL.md) |
| Booking inquiry or reservation qualification | [guest-sales-reservations](../guest-sales-reservations/SKILL.md) |
| BOSSA product or menu facts | [menu-product-operator](../menu-product-operator/SKILL.md) |
| BOSSA stock or forecast facts | [inventory-forecast-operator](../inventory-forecast-operator/SKILL.md) |
| BOSSA campaign priorities or owner decisions | [hospitality-command-center](../hospitality-command-center/SKILL.md) |

For an unsupported workflow, return the missing scope to the owner instead of naming an unavailable agent.

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

A production package is complete when its draft and approval evidence are ready. Scheduling, publication, and measurement are separately gated stages. A released video is complete only when:

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
