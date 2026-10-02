# Changelog

## 0.5.1 — Local candidate, unreleased

Implemented under `HOSPITALITY-PLUGIN-MARKETPLACE-2` from main commit `3667a4209b832a5bfe888f4430c2efe7f6fcd3c2`.

- Add the portable plugin-root manifest and keep the native Codex manifest consistent.
- Retain plugin `hospitality-os-plugin`, marketplace `hospitality-os`, and the existing 12 skills.
- Set marketplace display label to GPT Innovation by Attaf and use the 29-character subtitle Hospitality planning & drafts.
- Bundle light and dark composer icons and logos as SVG assets.
- Replace retired video-agent handoffs with current skill links and identify the unsupported multi-channel social-calendar scope.
- Replace the fixed v0.5.0 validator assertion with SemVer and cross-manifest agreement; add listing, artwork, routing, and skills-only package checks.
- Add 17 package regression tests and a reusable full video-schema fixture check to the existing CI workflow.
- Document installation routes and correct the historical v0.5 review status.

This candidate has not been pushed, merged, installed, imported into a workspace, published, or connected to live systems by this gate. No Notion pages or operational records were changed. The MIT license-file decision and installed acceptance remain open.

## 0.5.0 — Merged September 7, 2026

[PR #3](https://github.com/sahidattaf/hospitality-os-plugin/pull/3), commit `3667a4209b832a5bfe888f4430c2efe7f6fcd3c2`, consolidated 30 v0.4 agents into 12 focused skills. It introduced shared owner gates, evidence and privacy policies, controlled examples, video authorization controls, synthetic fixtures, and local/CI validation. The merge is a repository event and does not by itself establish installation or a pilot result.
