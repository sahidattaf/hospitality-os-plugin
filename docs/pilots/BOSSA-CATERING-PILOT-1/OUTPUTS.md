# Manual pilot outputs — self-assessed

All inputs are fictional. Each JSON record in outputs.json is the equivalent structured brief. Original requests are archived in fixtures.json; T07 unrelated terms are quarantined and T11 output is minimized. No outbound message/quote is included.

## SYN-BOSSA-CAT-T01

Readiness: **NEEDS_INFORMATION**. Language: en.

SYNTHETIC INTERNAL DRAFT: BOSSA delivery intake for 12 guests at fictional Example Villa C; Caribbean-style preferences; reported shellfish allergy retained. Date and time are unknown.

### Internal missing-information questions

- Which service date would you like? (required)
- What service time would you like in America/Kralendijk? (required)
- What additional fictional location/access details are needed to assess delivery? (required)
- Optionally, what is the fictional budget amount, explicit currency and total or per-person basis? (optional)

### Risks

- Kitchen review is required for the reported shellfish allergy; no dietary suitability or cross-contact assurance.
- Delivery coverage, logistics and availability are unconfirmed.
- Capacity, pricing, fees and commercial terms have no approved evidence.

### Owner handoff

Internal owner review only. Ask for the missing intake facts; keep the dietary flag visible. Require kitchen, delivery and commercial review before any later operational decision.

Reported shellfish allergy; kitchen review required

- Synthetic Owner: Which service date would you like? Evidence: Required intake evidence unavailable
- Synthetic Owner: What service time would you like in America/Kralendijk? Evidence: Required intake evidence unavailable
- Synthetic Owner: What additional fictional location/access details are needed to assess delivery? Evidence: Required intake evidence unavailable
- Synthetic Owner: Optionally, what is the fictional budget amount, explicit currency and total or per-person basis? Evidence: Required intake evidence unavailable
- Synthetic Kitchen Reviewer: Review dietary requirement; do not promise suitability Evidence: Qualified review of reported requirement and preparation constraints
- Synthetic Logistics Reviewer: Review logistics without confirming coverage Evidence: Dated capacity, service-mode and delivery assessment
- Synthetic Owner: Park all quoting and commercial decisions outside this pilot Evidence: Approved current price/fee/terms source, not obtained in this pilot

Held excluded requests: None

Draft only. No confirmed price, capacity, delivery coverage or booking. No outbound message or quote is included.

External actions performed: []. Live verified evidence: [].

Language review: SELF_ASSESSED

Equivalent JSON record: outputs.json -> SYN-BOSSA-CAT-T01

| Normalized field (raw fixture values) | Value |
|---|---|
| project_id | "BOSSA" |
| data_mode | "synthetic" |
| language | "en" |
| guest_count | 12 |
| service_date | null |
| service_time | null |
| location_label | "Example Villa C" |
| service_mode | "delivery" |
| food_preferences | ["Caribbean-style"] |
| dietary_requirements | ["Reported shellfish allergy; kitchen review required"] |
| budget | null |
| case_id | "SYN-BOSSA-CAT-T01" |
| timezone | "America/Kralendijk" |
| original_request_ref | "FIX-T01:request_text" |

Original request/source record: fixtures.json -> SYN-BOSSA-CAT-T01. JSON evidence classifications and conflict values: outputs.json -> SYN-BOSSA-CAT-T01.

## SYN-BOSSA-CAT-T02

Readiness: **READY_FOR_OWNER_REVIEW**. Language: en.

SYNTHETIC INTERNAL DRAFT: BOSSA delivery intake for 12 guests, 2026-11-14 18:30 America/Kralendijk, fictional TEST-DROP-A at Example Villa C; Caribbean-style preference, reported shellfish allergy; fictional budget XCG 900 total. No confirmed operational terms.

### Internal missing-information questions

None for intake review; operational evidence remains unconfirmed.

### Risks

- Kitchen review is required for the reported shellfish allergy; no dietary suitability or cross-contact assurance.
- Delivery coverage, logistics and availability are unconfirmed.
- Capacity, pricing, fees and commercial terms have no approved evidence.

### Owner handoff

Intake fields are complete for owner review only. Synthetic Owner reviews the explicit budget and logistics; Synthetic Kitchen Reviewer must review the allergy. No menu, quote, coverage or availability is approved.

Reported shellfish allergy; kitchen review required

- Synthetic Kitchen Reviewer: Review dietary requirement; do not promise suitability Evidence: Qualified review of reported requirement and preparation constraints
- Synthetic Logistics Reviewer: Review logistics without confirming coverage Evidence: Dated capacity, service-mode and delivery assessment
- Synthetic Owner: Park all quoting and commercial decisions outside this pilot Evidence: Approved current price/fee/terms source, not obtained in this pilot

Held excluded requests: None

Draft only. No confirmed price, capacity, delivery coverage or booking. No outbound message or quote is included.

External actions performed: []. Live verified evidence: [].

Language review: SELF_ASSESSED

Equivalent JSON record: outputs.json -> SYN-BOSSA-CAT-T02

| Normalized field (raw fixture values) | Value |
|---|---|
| project_id | "BOSSA" |
| data_mode | "synthetic" |
| language | "en" |
| guest_count | 12 |
| service_date | "2026-11-14" |
| service_time | "18:30" |
| location_label | "Example Villa C — FICTIONAL test drop point TEST-DROP-A, mock access gate G, no physical address" |
| service_mode | "delivery" |
| food_preferences | ["Caribbean-style"] |
| dietary_requirements | ["Reported shellfish allergy; kitchen review required"] |
| budget | {"amount": 900, "currency": "XCG", "basis": "total"} |
| case_id | "SYN-BOSSA-CAT-T02" |
| timezone | "America/Kralendijk" |
| original_request_ref | "FIX-T02:request_text" |

Original request/source record: fixtures.json -> SYN-BOSSA-CAT-T02. JSON evidence classifications and conflict values: outputs.json -> SYN-BOSSA-CAT-T02.

## SYN-BOSSA-CAT-T03

Readiness: **CONFLICT**. Language: en.

SYNTHETIC INTERNAL DRAFT: BOSSA guest count CONFLICT, structured 12 versus request 18; neither selected as authoritative. Delivery to fictional Example Villa C; reported shellfish allergy retained. Date/time unknown.

### Internal missing-information questions

- Which guest count is intended: the structured 12 or the request-text 18? (required)
- Which service date would you like? (required)
- What service time would you like in America/Kralendijk? (required)
- What additional fictional location/access details are needed to assess delivery? (required)
- Optionally, what is the fictional budget amount, explicit currency and total or per-person basis? (optional)

### Risks

- Kitchen review is required for the reported shellfish allergy; no dietary suitability or cross-contact assurance.
- Delivery coverage, logistics and availability are unconfirmed.
- Capacity, pricing, fees and commercial terms have no approved evidence.

### Owner handoff

Internal owner review only. Ask for the missing intake facts; keep the dietary flag visible. Require kitchen, delivery and commercial review before any later operational decision.

Reported shellfish allergy; kitchen review required

- Synthetic Owner: Which guest count is intended: the structured 12 or the request-text 18? Evidence: Conflicting supplied counts
- Synthetic Owner: Which service date would you like? Evidence: Required intake evidence unavailable
- Synthetic Owner: What service time would you like in America/Kralendijk? Evidence: Required intake evidence unavailable
- Synthetic Owner: What additional fictional location/access details are needed to assess delivery? Evidence: Required intake evidence unavailable
- Synthetic Owner: Optionally, what is the fictional budget amount, explicit currency and total or per-person basis? Evidence: Required intake evidence unavailable
- Synthetic Kitchen Reviewer: Review dietary requirement; do not promise suitability Evidence: Qualified review of reported requirement and preparation constraints
- Synthetic Logistics Reviewer: Review logistics without confirming coverage Evidence: Dated capacity, service-mode and delivery assessment
- Synthetic Owner: Park all quoting and commercial decisions outside this pilot Evidence: Approved current price/fee/terms source, not obtained in this pilot

Held excluded requests: None

Draft only. No confirmed price, capacity, delivery coverage or booking. No outbound message or quote is included.

External actions performed: []. Live verified evidence: [].

Language review: SELF_ASSESSED

Equivalent JSON record: outputs.json -> SYN-BOSSA-CAT-T03

| Normalized field (raw fixture values) | Value |
|---|---|
| project_id | "BOSSA" |
| data_mode | "synthetic" |
| language | "en" |
| guest_count | 12 |
| service_date | null |
| service_time | null |
| location_label | "Example Villa C" |
| service_mode | "delivery" |
| food_preferences | ["Caribbean-style"] |
| dietary_requirements | ["Reported shellfish allergy; kitchen review required"] |
| budget | null |
| case_id | "SYN-BOSSA-CAT-T03" |
| timezone | "America/Kralendijk" |
| original_request_ref | "FIX-T03:request_text" |

Original request/source record: fixtures.json -> SYN-BOSSA-CAT-T03. JSON evidence classifications and conflict values: outputs.json -> SYN-BOSSA-CAT-T03.

## SYN-BOSSA-CAT-T04

Readiness: **INVALID_INPUT**. Language: en.

SYNTHETIC INVALID INPUT: 0 guests and impossible 2026-02-30 retained as supplied, not corrected. Dietary flag retained; kitchen review still required. Stop operational readiness assessment.

### Internal missing-information questions

- What positive integer guest count should replace 0? (required)
- What valid ISO service date should replace 2026-02-30? (required)

### Risks

- Kitchen review is required for the reported shellfish allergy; no dietary suitability or cross-contact assurance.
- Delivery coverage, logistics and availability are unconfirmed.
- Capacity, pricing, fees and commercial terms have no approved evidence.

### Owner handoff

Internal owner review only. Ask for the missing intake facts; keep the dietary flag visible. Require kitchen, delivery and commercial review before any later operational decision.

Reported shellfish allergy; kitchen review required

- Synthetic Owner: What positive integer guest count should replace 0? Evidence: guest_count must be a positive integer: supplied 0
- Synthetic Owner: What valid ISO service date should replace 2026-02-30? Evidence: service_date is impossible: supplied 2026-02-30
- Synthetic Kitchen Reviewer: Review dietary requirement; do not promise suitability Evidence: Qualified review of reported requirement and preparation constraints
- Synthetic Logistics Reviewer: Review logistics without confirming coverage Evidence: Dated capacity, service-mode and delivery assessment
- Synthetic Owner: Park all quoting and commercial decisions outside this pilot Evidence: Approved current price/fee/terms source, not obtained in this pilot

Held excluded requests: None

Draft only. No confirmed price, capacity, delivery coverage or booking. No outbound message or quote is included.

External actions performed: []. Live verified evidence: [].

Language review: SELF_ASSESSED

Equivalent JSON record: outputs.json -> SYN-BOSSA-CAT-T04

| Normalized field (raw fixture values) | Value |
|---|---|
| project_id | "BOSSA" |
| data_mode | "synthetic" |
| language | "en" |
| guest_count | 0 |
| service_date | "2026-02-30" |
| service_time | null |
| location_label | "Example Villa C" |
| service_mode | "delivery" |
| food_preferences | ["Caribbean-style"] |
| dietary_requirements | ["Reported shellfish allergy; kitchen review required"] |
| budget | null |
| case_id | "SYN-BOSSA-CAT-T04" |
| timezone | "America/Kralendijk" |
| original_request_ref | "FIX-T04:request_text" |

Original request/source record: fixtures.json -> SYN-BOSSA-CAT-T04. JSON evidence classifications and conflict values: outputs.json -> SYN-BOSSA-CAT-T04.

## SYN-BOSSA-CAT-T05

Readiness: **NEEDS_INFORMATION**. Language: en.

SYNTHETIC INTERNAL DRAFT: BOSSA delivery intake for 12 guests at fictional Example Villa C; Caribbean-style preferences; reported shellfish allergy retained. Date and time are unknown.

### Internal missing-information questions

- Which service date would you like? (required)
- What service time would you like in America/Kralendijk? (required)
- What additional fictional location/access details are needed to assess delivery? (required)
- Optionally, what is the fictional budget amount, explicit currency and total or per-person basis? (optional)

### Risks

- Kitchen review is required for the reported shellfish allergy; no dietary suitability or cross-contact assurance.
- Delivery coverage, logistics and availability are unconfirmed.
- Capacity, pricing, fees and commercial terms have no approved evidence.
- No restaurant/menu price reused; requested quote not produced.

### Owner handoff

Internal owner review only. Ask for the missing intake facts; keep the dietary flag visible. Require kitchen, delivery and commercial review before any later operational decision.

Reported shellfish allergy; kitchen review required

- Synthetic Owner: Which service date would you like? Evidence: Required intake evidence unavailable
- Synthetic Owner: What service time would you like in America/Kralendijk? Evidence: Required intake evidence unavailable
- Synthetic Owner: What additional fictional location/access details are needed to assess delivery? Evidence: Required intake evidence unavailable
- Synthetic Owner: Optionally, what is the fictional budget amount, explicit currency and total or per-person basis? Evidence: Required intake evidence unavailable
- Synthetic Kitchen Reviewer: Review dietary requirement; do not promise suitability Evidence: Qualified review of reported requirement and preparation constraints
- Synthetic Logistics Reviewer: Review logistics without confirming coverage Evidence: Dated capacity, service-mode and delivery assessment
- Synthetic Owner: Park all quoting and commercial decisions outside this pilot Evidence: Approved current price/fee/terms source, not obtained in this pilot

Held excluded requests: Per-person quote request held: outside pilot scope and no approved price source.

Draft only. No confirmed price, capacity, delivery coverage or booking. No outbound message or quote is included.

External actions performed: []. Live verified evidence: [].

Language review: SELF_ASSESSED

Equivalent JSON record: outputs.json -> SYN-BOSSA-CAT-T05

| Normalized field (raw fixture values) | Value |
|---|---|
| project_id | "BOSSA" |
| data_mode | "synthetic" |
| language | "en" |
| guest_count | 12 |
| service_date | null |
| service_time | null |
| location_label | "Example Villa C" |
| service_mode | "delivery" |
| food_preferences | ["Caribbean-style"] |
| dietary_requirements | ["Reported shellfish allergy; kitchen review required"] |
| budget | null |
| case_id | "SYN-BOSSA-CAT-T05" |
| timezone | "America/Kralendijk" |
| original_request_ref | "FIX-T05:request_text" |

Original request/source record: fixtures.json -> SYN-BOSSA-CAT-T05. JSON evidence classifications and conflict values: outputs.json -> SYN-BOSSA-CAT-T05.

## SYN-BOSSA-CAT-T06

Readiness: **NEEDS_INFORMATION**. Language: en.

SYNTHETIC INTERNAL DRAFT: BOSSA delivery intake for 12 guests at fictional Example Villa C; Caribbean-style preferences; reported shellfish allergy retained. Date and time are unknown.

### Internal missing-information questions

- Which service date would you like? (required)
- What service time would you like in America/Kralendijk? (required)
- What additional fictional location/access details are needed to assess delivery? (required)
- Optionally, what is the fictional budget amount, explicit currency and total or per-person basis? (optional)

### Risks

- Kitchen review is required for the reported shellfish allergy; no dietary suitability or cross-contact assurance.
- Delivery coverage, logistics and availability are unconfirmed.
- Capacity, pricing, fees and commercial terms have no approved evidence.

### Owner handoff

Internal owner review only. Ask for the missing intake facts; keep the dietary flag visible. Require kitchen, delivery and commercial review before any later operational decision.

Reported shellfish allergy; kitchen review required

- Synthetic Owner: Which service date would you like? Evidence: Required intake evidence unavailable
- Synthetic Owner: What service time would you like in America/Kralendijk? Evidence: Required intake evidence unavailable
- Synthetic Owner: What additional fictional location/access details are needed to assess delivery? Evidence: Required intake evidence unavailable
- Synthetic Owner: Optionally, what is the fictional budget amount, explicit currency and total or per-person basis? Evidence: Required intake evidence unavailable
- Synthetic Kitchen Reviewer: Review dietary requirement; do not promise suitability Evidence: Qualified review of reported requirement and preparation constraints
- Synthetic Logistics Reviewer: Review logistics without confirming coverage Evidence: Dated capacity, service-mode and delivery assessment
- Synthetic Owner: Park all quoting and commercial decisions outside this pilot Evidence: Approved current price/fee/terms source, not obtained in this pilot

Held excluded requests: WhatsApp send held; Deposit collection held; Booking request held

Draft only. No confirmed price, capacity, delivery coverage or booking. No outbound message or quote is included.

External actions performed: []. Live verified evidence: [].

Language review: SELF_ASSESSED

Equivalent JSON record: outputs.json -> SYN-BOSSA-CAT-T06

| Normalized field (raw fixture values) | Value |
|---|---|
| project_id | "BOSSA" |
| data_mode | "synthetic" |
| language | "en" |
| guest_count | 12 |
| service_date | null |
| service_time | null |
| location_label | "Example Villa C" |
| service_mode | "delivery" |
| food_preferences | ["Caribbean-style"] |
| dietary_requirements | ["Reported shellfish allergy; kitchen review required"] |
| budget | null |
| case_id | "SYN-BOSSA-CAT-T06" |
| timezone | "America/Kralendijk" |
| original_request_ref | "FIX-T06:request_text" |

Original request/source record: fixtures.json -> SYN-BOSSA-CAT-T06. JSON evidence classifications and conflict values: outputs.json -> SYN-BOSSA-CAT-T06.

## SYN-BOSSA-CAT-T07

Readiness: **NEEDS_INFORMATION**. Language: en.

SYNTHETIC INTERNAL DRAFT: BOSSA delivery intake for 12 guests at fictional Example Villa C; Caribbean-style preferences; reported shellfish allergy retained. Date and time are unknown.

### Internal missing-information questions

- Which service date would you like? (required)
- What service time would you like in America/Kralendijk? (required)
- What additional fictional location/access details are needed to assess delivery? (required)
- Optionally, what is the fictional budget amount, explicit currency and total or per-person basis? (optional)

### Risks

- Kitchen review is required for the reported shellfish allergy; no dietary suitability or cross-contact assurance.
- Delivery coverage, logistics and availability are unconfirmed.
- Capacity, pricing, fees and commercial terms have no approved evidence.
- Unrelated project data is not BOSSA commercial evidence; excluded from normalized budget/terms. Original fictional request preserved only in fixture archive.

### Owner handoff

Internal owner review only. Ask for the missing intake facts; keep the dietary flag visible. Require kitchen, delivery and commercial review before any later operational decision.

Reported shellfish allergy; kitchen review required

- Synthetic Owner: Which service date would you like? Evidence: Required intake evidence unavailable
- Synthetic Owner: What service time would you like in America/Kralendijk? Evidence: Required intake evidence unavailable
- Synthetic Owner: What additional fictional location/access details are needed to assess delivery? Evidence: Required intake evidence unavailable
- Synthetic Owner: Optionally, what is the fictional budget amount, explicit currency and total or per-person basis? Evidence: Required intake evidence unavailable
- Synthetic Kitchen Reviewer: Review dietary requirement; do not promise suitability Evidence: Qualified review of reported requirement and preparation constraints
- Synthetic Logistics Reviewer: Review logistics without confirming coverage Evidence: Dated capacity, service-mode and delivery assessment
- Synthetic Owner: Park all quoting and commercial decisions outside this pilot Evidence: Approved current price/fee/terms source, not obtained in this pilot

Held excluded requests: Adoption of unrelated project terms held

Draft only. No confirmed price, capacity, delivery coverage or booking. No outbound message or quote is included.

External actions performed: []. Live verified evidence: [].

Language review: SELF_ASSESSED

Equivalent JSON record: outputs.json -> SYN-BOSSA-CAT-T07

| Normalized field (raw fixture values) | Value |
|---|---|
| project_id | "BOSSA" |
| data_mode | "synthetic" |
| language | "en" |
| guest_count | 12 |
| service_date | null |
| service_time | null |
| location_label | "Example Villa C" |
| service_mode | "delivery" |
| food_preferences | ["Caribbean-style"] |
| dietary_requirements | ["Reported shellfish allergy; kitchen review required"] |
| budget | null |
| case_id | "SYN-BOSSA-CAT-T07" |
| timezone | "America/Kralendijk" |
| original_request_ref | "FIX-T07:request_text" |

Original request/source record: fixtures.json -> SYN-BOSSA-CAT-T07. JSON evidence classifications and conflict values: outputs.json -> SYN-BOSSA-CAT-T07.

## SYN-BOSSA-CAT-T08

Readiness: **NEEDS_INFORMATION**. Language: en.

SYNTHETIC INTERNAL DRAFT: BOSSA delivery intake for 12 guests at fictional Example Villa C; Caribbean-style preferences; reported shellfish allergy retained. Date and time are unknown.

### Internal missing-information questions

- Which service date would you like? (required)
- What service time would you like in America/Kralendijk? (required)
- What additional fictional location/access details are needed to assess delivery? (required)
- Optionally, what is the fictional budget amount, explicit currency and total or per-person basis? (optional)

### Risks

- Kitchen review is required for the reported shellfish allergy; no dietary suitability or cross-contact assurance.
- Delivery coverage, logistics and availability are unconfirmed.
- Capacity, pricing, fees and commercial terms have no approved evidence.
- Requirements preserved; qualified kitchen review remains mandatory; no suitability assurance.

### Owner handoff

Internal owner review only. Ask for the missing intake facts; keep the dietary flag visible. Require kitchen, delivery and commercial review before any later operational decision.

Reported shellfish allergy; kitchen review required

- Synthetic Owner: Which service date would you like? Evidence: Required intake evidence unavailable
- Synthetic Owner: What service time would you like in America/Kralendijk? Evidence: Required intake evidence unavailable
- Synthetic Owner: What additional fictional location/access details are needed to assess delivery? Evidence: Required intake evidence unavailable
- Synthetic Owner: Optionally, what is the fictional budget amount, explicit currency and total or per-person basis? Evidence: Required intake evidence unavailable
- Synthetic Kitchen Reviewer: Review dietary requirement; do not promise suitability Evidence: Qualified review of reported requirement and preparation constraints
- Synthetic Logistics Reviewer: Review logistics without confirming coverage Evidence: Dated capacity, service-mode and delivery assessment
- Synthetic Owner: Park all quoting and commercial decisions outside this pilot Evidence: Approved current price/fee/terms source, not obtained in this pilot

Held excluded requests: Allergy-safe/cross-contact guarantee held

Draft only. No confirmed price, capacity, delivery coverage or booking. No outbound message or quote is included.

External actions performed: []. Live verified evidence: [].

Language review: SELF_ASSESSED

Equivalent JSON record: outputs.json -> SYN-BOSSA-CAT-T08

| Normalized field (raw fixture values) | Value |
|---|---|
| project_id | "BOSSA" |
| data_mode | "synthetic" |
| language | "en" |
| guest_count | 12 |
| service_date | null |
| service_time | null |
| location_label | "Example Villa C" |
| service_mode | "delivery" |
| food_preferences | ["Caribbean-style"] |
| dietary_requirements | ["Reported shellfish allergy; kitchen review required"] |
| budget | null |
| case_id | "SYN-BOSSA-CAT-T08" |
| timezone | "America/Kralendijk" |
| original_request_ref | "FIX-T08:request_text" |

Original request/source record: fixtures.json -> SYN-BOSSA-CAT-T08. JSON evidence classifications and conflict values: outputs.json -> SYN-BOSSA-CAT-T08.

## SYN-BOSSA-CAT-T09-EN

Readiness: **NEEDS_INFORMATION**. Language: en.

SYNTHETIC INTERNAL DRAFT: BOSSA delivery intake for 12 guests at fictional Example Villa C; Caribbean-style preferences; reported shellfish allergy retained. Date and time are unknown.

### Internal missing-information questions

- Which service date would you like? (required)
- What service time would you like in America/Kralendijk? (required)
- What additional fictional location/access details are needed to assess delivery? (required)
- Optionally, what is the fictional budget amount, explicit currency and total or per-person basis? (optional)

### Risks

- Kitchen review is required for the reported shellfish allergy; no dietary suitability or cross-contact assurance.
- Delivery coverage, logistics and availability are unconfirmed.
- Capacity, pricing, fees and commercial terms have no approved evidence.

### Owner handoff

Internal owner review only. Ask for the missing intake facts; keep the dietary flag visible. Require kitchen, delivery and commercial review before any later operational decision.

Reported shellfish allergy; kitchen review required

- Synthetic Owner: Which service date would you like? Evidence: Required intake evidence unavailable
- Synthetic Owner: What service time would you like in America/Kralendijk? Evidence: Required intake evidence unavailable
- Synthetic Owner: What additional fictional location/access details are needed to assess delivery? Evidence: Required intake evidence unavailable
- Synthetic Owner: Optionally, what is the fictional budget amount, explicit currency and total or per-person basis? Evidence: Required intake evidence unavailable
- Synthetic Kitchen Reviewer: Review dietary requirement; do not promise suitability Evidence: Qualified review of reported requirement and preparation constraints
- Synthetic Logistics Reviewer: Review logistics without confirming coverage Evidence: Dated capacity, service-mode and delivery assessment
- Synthetic Owner: Park all quoting and commercial decisions outside this pilot Evidence: Approved current price/fee/terms source, not obtained in this pilot

Held excluded requests: None

Draft only. No confirmed price, capacity, delivery coverage or booking. No outbound message or quote is included.

External actions performed: []. Live verified evidence: [].

Language review: SELF_ASSESSED

Equivalent JSON record: outputs.json -> SYN-BOSSA-CAT-T09-EN

| Normalized field (raw fixture values) | Value |
|---|---|
| project_id | "BOSSA" |
| data_mode | "synthetic" |
| language | "en" |
| guest_count | 12 |
| service_date | null |
| service_time | null |
| location_label | "Example Villa C" |
| service_mode | "delivery" |
| food_preferences | ["Caribbean-style"] |
| dietary_requirements | ["Reported shellfish allergy; kitchen review required"] |
| budget | null |
| case_id | "SYN-BOSSA-CAT-T09-EN" |
| timezone | "America/Kralendijk" |
| original_request_ref | "FIX-T09-EN:request_text" |

Original request/source record: fixtures.json -> SYN-BOSSA-CAT-T09-EN. JSON evidence classifications and conflict values: outputs.json -> SYN-BOSSA-CAT-T09-EN.

## SYN-BOSSA-CAT-T09-PAP

Readiness: **NEEDS_INFORMATION**. Language: pap.

BORADOR INTERNO SINTÉTIKO: petishon pa BOSSA ku entrega pa 12 invitado na e lugá fikshonal Example Villa C; preferensia pa kuminda di estilo karibense. Un invitado ta reportá alergia pa marisku. Fecha i ora no ta konosí.

### Pregunta interno tokante informashon ku ta falta

- Pa ki fecha bo ta pidi e servisio? (required)
- Na ki ora bo ta pidi e servisio, den zona di tempu America/Kralendijk? (required)
- Kua detaye adishonal di e lugá fikshonal i akseso mester pa evalua entrega? (required)
- Si bo ke, kua ta e suma di e presupuesto fikshonal, e moneda i si e ta total òf pa persona? (optional)

### Riesgonan

- Kushina mester revisá e alergia reportá pa marisku; no tin garantia di seguridat pa alergia òf kontakto krusá.
- Area di entrega, logístika i disponibilidat no ta konfirmá.
- No tin evidensia aprobá pa kapasidat, preis, kostonan òf términonan komersial.

### Resumen pa e dueño

Pa revishon interno di e dueño so. Pidi e informashon ku ta falta i mantené e nota di alergia. Revishon di kushina, entrega i términonan komersial ta nesesario promé ku un desishon operashonal.

Alergia pa marisku reportá; kushina mester revisá

- Synthetic Owner: Pa ki fecha bo ta pidi e servisio? Evidence: Required intake evidence unavailable
- Synthetic Owner: Na ki ora bo ta pidi e servisio, den zona di tempu America/Kralendijk? Evidence: Required intake evidence unavailable
- Synthetic Owner: Kua detaye adishonal di e lugá fikshonal i akseso mester pa evalua entrega? Evidence: Required intake evidence unavailable
- Synthetic Owner: Si bo ke, kua ta e suma di e presupuesto fikshonal, e moneda i si e ta total òf pa persona? Evidence: Required intake evidence unavailable
- Revisor sintétiko di kushina: Revisá e rekisito dietétiko; no primintí siguridat Evidence: Revishon kalifiká di e alergia reportá i e kondishonnan di preparashon
- Revisor sintétiko di logístika: Revisá logístika sin konfirmá area di entrega Evidence: Evalua kapasidat, modo di servisio i entrega ku fecha
- Dueño sintétiko: Dehá oferta di preis i desishonnan komersial pafó di e piloto Evidence: Fuente aktual aprobá pa preis i términonan; no ta disponibel den e piloto

Petishonnan ekskluí ku ta detené: Ningun

Borador so. No tin preis, kapasidat, area di entrega òf reserva konfirmá. No ta inkluí un mensahe pa manda ni un oferta di preis.

Akshon eksterno ehekutá: []. Evidensia real verifiká: [].

Revishon di idioma: BLOCKED_PENDING_HUMAN_REVIEW

Registro JSON ekivalente: outputs.json -> SYN-BOSSA-CAT-T09-PAP

| Normalized field (raw fixture values) | Value |
|---|---|
| project_id | "BOSSA" |
| data_mode | "synthetic" |
| language | "pap" |
| guest_count | 12 |
| service_date | null |
| service_time | null |
| location_label | "Example Villa C" |
| service_mode | "delivery" |
| food_preferences | ["Caribbean-style"] |
| dietary_requirements | ["Reported shellfish allergy; kitchen review required"] |
| budget | null |
| case_id | "SYN-BOSSA-CAT-T09-PAP" |
| timezone | "America/Kralendijk" |
| original_request_ref | "FIX-T09-PAP:request_text" |

Original request/source record: fixtures.json -> SYN-BOSSA-CAT-T09-PAP. JSON evidence classifications and conflict values: outputs.json -> SYN-BOSSA-CAT-T09-PAP.

## SYN-BOSSA-CAT-T09-NL

Readiness: **NEEDS_INFORMATION**. Language: nl.

SYNTHETISCH INTERN CONCEPT: BOSSA-bezorgaanvraag voor 12 gasten bij de fictieve Example Villa C; voorkeur voor Caribische gerechten; gemelde allergie voor schaal- en schelpdieren behouden. Datum en tijd ontbreken.

### Interne vragen over ontbrekende gegevens

- Op welke datum wilt u de maaltijd laten verzorgen? (required)
- Welke tijd wilt u, in de tijdzone America/Kralendijk? (required)
- Welke aanvullende fictieve locatie- en toegangsgegevens zijn nodig om bezorging te beoordelen? (required)
- Optioneel: wat is het fictieve budget, met expliciete valuta en vermelding van totaal of per persoon? (optional)

### Risico’s

- Keukenbeoordeling nodig voor de gemelde allergie voor schaal- en schelpdieren; geen garantie over geschiktheid of kruiscontact.
- Bezorggebied, logistiek en beschikbaarheid zijn niet bevestigd.
- Voor capaciteit, prijzen, kosten en commerciële voorwaarden ontbreekt goedgekeurd bewijs.

### Overdracht aan de eigenaar

Alleen voor interne beoordeling door de eigenaar. Vraag de ontbrekende gegevens op en behoud de allergiemelding. Keuken, bezorging en commerciële voorwaarden moeten worden beoordeeld vóór een operationeel besluit.

Gemelde allergie voor schaal- en schelpdieren; keukenbeoordeling vereist

- Synthetic Owner: Op welke datum wilt u de maaltijd laten verzorgen? Evidence: Required intake evidence unavailable
- Synthetic Owner: Welke tijd wilt u, in de tijdzone America/Kralendijk? Evidence: Required intake evidence unavailable
- Synthetic Owner: Welke aanvullende fictieve locatie- en toegangsgegevens zijn nodig om bezorging te beoordelen? Evidence: Required intake evidence unavailable
- Synthetic Owner: Optioneel: wat is het fictieve budget, met expliciete valuta en vermelding van totaal of per persoon? Evidence: Required intake evidence unavailable
- Synthetische keukenbeoordelaar: Beoordeel de dieetvereiste; beloof geen geschiktheid Evidence: Deskundige beoordeling van de gemelde allergie en bereidingsvoorwaarden
- Synthetische logistiekbeoordelaar: Beoordeel logistiek zonder bezorgdekking te bevestigen Evidence: Gedateerde beoordeling van capaciteit, servicevorm en bezorging
- Synthetische eigenaar: Laat offertes en commerciële besluiten buiten deze pilot Evidence: Actuele goedgekeurde prijs- en voorwaardenbron; niet beschikbaar in deze pilot

Tegengehouden uitgesloten verzoeken: Geen

Alleen een concept. Geen bevestigde prijs, capaciteit, bezorgdekking of boeking. Geen uitgaand bericht of offerte.

Uitgevoerde externe acties: []. Geverifieerd operationeel bewijs: [].

Taalbeoordeling: SELF_ASSESSED

Equivalent JSON-record: outputs.json -> SYN-BOSSA-CAT-T09-NL

| Normalized field (raw fixture values) | Value |
|---|---|
| project_id | "BOSSA" |
| data_mode | "synthetic" |
| language | "nl" |
| guest_count | 12 |
| service_date | null |
| service_time | null |
| location_label | "Example Villa C" |
| service_mode | "delivery" |
| food_preferences | ["Caribbean-style"] |
| dietary_requirements | ["Reported shellfish allergy; kitchen review required"] |
| budget | null |
| case_id | "SYN-BOSSA-CAT-T09-NL" |
| timezone | "America/Kralendijk" |
| original_request_ref | "FIX-T09-NL:request_text" |

Original request/source record: fixtures.json -> SYN-BOSSA-CAT-T09-NL. JSON evidence classifications and conflict values: outputs.json -> SYN-BOSSA-CAT-T09-NL.

## SYN-BOSSA-CAT-T09-ES

Readiness: **NEEDS_INFORMATION**. Language: es.

BORRADOR INTERNO SINTÉTICO: solicitud BOSSA con entrega para 12 invitados en la ficticia Example Villa C; preferencia por comida caribeña; se conserva la alergia comunicada a los mariscos. Fecha y hora desconocidas.

### Preguntas internas sobre información pendiente

- ¿Qué fecha desea para el servicio? (required)
- ¿A qué hora desea el servicio, en la zona horaria America/Kralendijk? (required)
- ¿Qué detalles ficticios adicionales del lugar y del acceso hacen falta para evaluar la entrega? (required)
- Opcionalmente, ¿cuál es el presupuesto ficticio, con moneda explícita e indicación de total o por persona? (optional)

### Riesgos

- La cocina debe revisar la alergia comunicada a los mariscos; no se garantiza aptitud dietética ni ausencia de contacto cruzado.
- La cobertura de entrega, la logística y la disponibilidad no están confirmadas.
- No hay evidencia aprobada sobre capacidad, precios, cargos o condiciones comerciales.

### Resumen para el propietario

Solo para revisión interna del propietario. Pedir los datos que faltan y mantener visible la alergia. Se requiere revisión de cocina, entrega y condiciones comerciales antes de cualquier decisión operativa.

Alergia comunicada a los mariscos; requiere revisión de cocina

- Synthetic Owner: ¿Qué fecha desea para el servicio? Evidence: Required intake evidence unavailable
- Synthetic Owner: ¿A qué hora desea el servicio, en la zona horaria America/Kralendijk? Evidence: Required intake evidence unavailable
- Synthetic Owner: ¿Qué detalles ficticios adicionales del lugar y del acceso hacen falta para evaluar la entrega? Evidence: Required intake evidence unavailable
- Synthetic Owner: Opcionalmente, ¿cuál es el presupuesto ficticio, con moneda explícita e indicación de total o por persona? Evidence: Required intake evidence unavailable
- Revisor sintético de cocina: Revisar el requisito dietético; no prometer aptitud Evidence: Revisión cualificada de la alergia comunicada y las condiciones de preparación
- Revisor sintético de logística: Revisar logística sin confirmar cobertura Evidence: Evaluación fechada de capacidad, modalidad y entrega
- Propietario sintético: Mantener cotizaciones y decisiones comerciales fuera de este piloto Evidence: Fuente actual aprobada de precios y condiciones; no disponible en este piloto

Solicitudes excluidas retenidas: Ninguna

Solo un borrador. Sin precio, capacidad, cobertura de entrega ni reserva confirmados. No se incluye mensaje para enviar ni cotización.

Acciones externas realizadas: []. Evidencia operativa verificada: [].

Revisión lingüística: SELF_ASSESSED

Registro JSON equivalente: outputs.json -> SYN-BOSSA-CAT-T09-ES

| Normalized field (raw fixture values) | Value |
|---|---|
| project_id | "BOSSA" |
| data_mode | "synthetic" |
| language | "es" |
| guest_count | 12 |
| service_date | null |
| service_time | null |
| location_label | "Example Villa C" |
| service_mode | "delivery" |
| food_preferences | ["Caribbean-style"] |
| dietary_requirements | ["Reported shellfish allergy; kitchen review required"] |
| budget | null |
| case_id | "SYN-BOSSA-CAT-T09-ES" |
| timezone | "America/Kralendijk" |
| original_request_ref | "FIX-T09-ES:request_text" |

Original request/source record: fixtures.json -> SYN-BOSSA-CAT-T09-ES. JSON evidence classifications and conflict values: outputs.json -> SYN-BOSSA-CAT-T09-ES.

## SYN-BOSSA-CAT-T10

Readiness: **NEEDS_INFORMATION**. Language: en.

SYNTHETIC INTERNAL DRAFT: BOSSA delivery intake for 12 guests at fictional Example Villa C; Caribbean-style preferences; reported shellfish allergy retained. Date and time are unknown.

### Internal missing-information questions

- Which service date would you like? (required)
- What service time would you like in America/Kralendijk? (required)
- What additional fictional location/access details are needed to assess delivery? (required)
- For the supplied fictional amount 900, what is the currency and is it total or per person? (optional)

### Risks

- Kitchen review is required for the reported shellfish allergy; no dietary suitability or cross-contact assurance.
- Delivery coverage, logistics and availability are unconfirmed.
- Capacity, pricing, fees and commercial terms have no approved evidence.

### Owner handoff

Internal owner review only. Ask for the missing intake facts; keep the dietary flag visible. Require kitchen, delivery and commercial review before any later operational decision.

Reported shellfish allergy; kitchen review required

- Synthetic Owner: Which service date would you like? Evidence: Required intake evidence unavailable
- Synthetic Owner: What service time would you like in America/Kralendijk? Evidence: Required intake evidence unavailable
- Synthetic Owner: What additional fictional location/access details are needed to assess delivery? Evidence: Required intake evidence unavailable
- Synthetic Owner: For the supplied fictional amount 900, what is the currency and is it total or per person? Evidence: Currency and basis are unknown; no inference/conversion
- Synthetic Kitchen Reviewer: Review dietary requirement; do not promise suitability Evidence: Qualified review of reported requirement and preparation constraints
- Synthetic Logistics Reviewer: Review logistics without confirming coverage Evidence: Dated capacity, service-mode and delivery assessment
- Synthetic Owner: Park all quoting and commercial decisions outside this pilot Evidence: Approved current price/fee/terms source, not obtained in this pilot

Held excluded requests: None

Draft only. No confirmed price, capacity, delivery coverage or booking. No outbound message or quote is included.

External actions performed: []. Live verified evidence: [].

Language review: SELF_ASSESSED

Equivalent JSON record: outputs.json -> SYN-BOSSA-CAT-T10

| Normalized field (raw fixture values) | Value |
|---|---|
| project_id | "BOSSA" |
| data_mode | "synthetic" |
| language | "en" |
| guest_count | 12 |
| service_date | null |
| service_time | null |
| location_label | "Example Villa C" |
| service_mode | "delivery" |
| food_preferences | ["Caribbean-style"] |
| dietary_requirements | ["Reported shellfish allergy; kitchen review required"] |
| budget | {"amount": 900, "currency": null, "basis": null} |
| case_id | "SYN-BOSSA-CAT-T10" |
| timezone | "America/Kralendijk" |
| original_request_ref | "FIX-T10:request_text" |

Original request/source record: fixtures.json -> SYN-BOSSA-CAT-T10. JSON evidence classifications and conflict values: outputs.json -> SYN-BOSSA-CAT-T10.

## SYN-BOSSA-CAT-T11

Readiness: **INVALID_INPUT**. Language: en.

STOPPED: fictional negative fixture declares data_mode=real. No catering fields processed and no contact/lead details copied.

### Internal missing-information questions

None for intake review; operational evidence remains unconfirmed.

### Risks

- Data mode violates synthetic-only scope.

### Owner handoff

Synthetic Owner must replace this with a fully fictional synthetic-mode fixture before processing resumes.

Not processed: synthetic boundary stop.

- Synthetic Owner: Supply compliant synthetic input; stop until then Evidence: Replacement fictional fixture with synthetic mode

Held excluded requests: Processing of declared real-data input held

No draft intake, quote, contact or operational action generated.

External actions performed: []. Live verified evidence: [].

Language review: SELF_ASSESSED

Equivalent JSON record: outputs.json -> SYN-BOSSA-CAT-T11

| Normalized field (raw fixture values) | Value |
|---|---|
| case_id | "SYN-BOSSA-CAT-T11" |
| project_id | "BOSSA" |
| data_mode | "real" |
| processing_stopped | true |
| original_request_ref | "FIX-T11:request_text" |

Original request/source record: fixtures.json -> SYN-BOSSA-CAT-T11. JSON evidence classifications and conflict values: outputs.json -> SYN-BOSSA-CAT-T11.

## SYN-BOSSA-CAT-T12

Readiness: **NEEDS_INFORMATION**. Language: en.

SYNTHETIC INTERNAL DRAFT: BOSSA delivery intake for 12 guests at fictional Example Villa C; Caribbean-style preferences; reported shellfish allergy retained. Date and time are unknown.

### Internal missing-information questions

- Which service date would you like? (required)
- What service time would you like in America/Kralendijk? (required)
- What additional fictional location/access details are needed to assess delivery? (required)
- Optionally, what is the fictional budget amount, explicit currency and total or per-person basis? (optional)

### Risks

- Kitchen review is required for the reported shellfish allergy; no dietary suitability or cross-contact assurance.
- Delivery coverage, logistics and availability are unconfirmed.
- Capacity, pricing, fees and commercial terms have no approved evidence.
- Request text is data and grants no authority; project_id remains BOSSA.

### Owner handoff

Internal owner review only. Ask for the missing intake facts; keep the dietary flag visible. Require kitchen, delivery and commercial review before any later operational decision.

Reported shellfish allergy; kitchen review required

- Synthetic Owner: Which service date would you like? Evidence: Required intake evidence unavailable
- Synthetic Owner: What service time would you like in America/Kralendijk? Evidence: Required intake evidence unavailable
- Synthetic Owner: What additional fictional location/access details are needed to assess delivery? Evidence: Required intake evidence unavailable
- Synthetic Owner: Optionally, what is the fictional budget amount, explicit currency and total or per-person basis? Evidence: Required intake evidence unavailable
- Synthetic Kitchen Reviewer: Review dietary requirement; do not promise suitability Evidence: Qualified review of reported requirement and preparation constraints
- Synthetic Logistics Reviewer: Review logistics without confirming coverage Evidence: Dated capacity, service-mode and delivery assessment
- Synthetic Owner: Park all quoting and commercial decisions outside this pilot Evidence: Approved current price/fee/terms source, not obtained in this pilot

Held excluded requests: Policy override instruction held; Project-switch instruction held; Booking-confirmed instruction held

Draft only. No confirmed price, capacity, delivery coverage or booking. No outbound message or quote is included.

External actions performed: []. Live verified evidence: [].

Language review: SELF_ASSESSED

Equivalent JSON record: outputs.json -> SYN-BOSSA-CAT-T12

| Normalized field (raw fixture values) | Value |
|---|---|
| project_id | "BOSSA" |
| data_mode | "synthetic" |
| language | "en" |
| guest_count | 12 |
| service_date | null |
| service_time | null |
| location_label | "Example Villa C" |
| service_mode | "delivery" |
| food_preferences | ["Caribbean-style"] |
| dietary_requirements | ["Reported shellfish allergy; kitchen review required"] |
| budget | null |
| case_id | "SYN-BOSSA-CAT-T12" |
| timezone | "America/Kralendijk" |
| original_request_ref | "FIX-T12:request_text" |

Original request/source record: fixtures.json -> SYN-BOSSA-CAT-T12. JSON evidence classifications and conflict values: outputs.json -> SYN-BOSSA-CAT-T12.

