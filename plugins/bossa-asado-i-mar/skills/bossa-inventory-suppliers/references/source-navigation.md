# Source navigation and freshness

Initial provenance: owner-attached BOSSA_ChatGPT_Project_Source_Pack.md (2026-08-16), BOSSA_PROJECT_SOURCE_INDEX.md (2026-08-22), P0-R1_SURVEY_CHECKLIST.pdf, BOSSA_Menu_Costing_Control_2026.xlsx and Boosa Owner Dashboard.zip inspected 2026-10-14. These are snapshots. Their historic statuses are not newly verified live records.

## Canonical sources
- Owner Dashboard: resolve the current authorized page by this title in the connected workspace.
- Phase 0 Control Center: resolve the current authorized page by this title in the connected workspace.
- Licensing & Permit Register: resolve the current authorized page by this title in the connected workspace.
- Rebuild & Contractor Register: resolve the current authorized page by this title in the connected workspace.
- Document Register: resolve the current authorized page by this title in the connected workspace.
- Supplier Setup Register: resolve the current authorized page by this title in the connected workspace.
- Recipe Ingredient Lines: resolve the current authorized page by this title in the connected workspace.
- Menu Assembly Map: resolve the current authorized page by this title in the connected workspace.
- Menu Items — Master: resolve the current authorized database by its exact title; verify the accessible live database before querying/updating. Keep older menu databases as legacy until reconciled.
- Existing OneDrive root: resolve the owner-approved BOSSA operations folder in the authorized evidence system. Preserve this root; do not create a duplicate.
- Survey evidence: 02_Construction & Rebuild/P0-R1_Current-Condition-Survey/{01_Photos,02_Measurements,03_Current-Layout-Sketch,04_Survey-Report}.
- Recipe evidence: 05_Recipes & Costing Evidence/{01_Bread Tests,02_Fire Box Component Tests,03_Fire Box Assembly Tests,04_Approved Recipes}.
- Costing authority: BOSSA_Menu_Costing_Control_2026.xlsx under 03 -BOSSA Menu Costing. Inspected SHA-256: 4833cd02377b79776eecaeb98d2ed360f56f1bc1b96c5281ac6aed918dd1988a. Hash matches supplied index; this does not establish current prices or completed recipes.
- Workbook tabs: Ingredients, Recipe Components, Recipe Ingredient Lines, Menu Assembly, Direct Purchase, Menu Summary, Costing Dashboard, Instructions, Lists. Preserve architecture for scoped edits. BOSSA_Menu_Costing_2026.xlsx is a separate legacy/future template.
- Public code: sahidattaf/BOSSA-ASADO-I-MAR.
- Internal code: sahidattaf/bossa-ai-os.
- Legacy reference: sahidattaf/BossaGPT-AI-Operations-Hub; do not promote it without owner instruction.

## Snapshot conflicts and unknowns
- Menu text export lists a different address from the source pack. Retrieve current approved address before use.
- Menu text export uses a legacy currency label; index and master snapshot use XCG. Do not translate legacy amounts into newly approved offers. Retrieve item-level current price and status.
- Dashboard snapshot includes demo/service-day rows while explicitly marking Phase 0 / NOT YET OPEN. Never count those rows as proof of opening or real operating results.
- Survey completion, permitted use, prior horeca license, alcohol scope, exact license category and inspection evidence need current verification.

## Notion record discipline
Inspect accessible page/database title, schema and record IDs before mutations. Preserve native property types and relations. Use existing records rather than duplicates. For approved changes read back the changed properties. For blocked access provide a draft containing: title, domain, status, owner, source link/version, evidence label, dependency, next action, decision/gate, timestamp (America/Kralendijk). Do not claim an unexecuted write.
