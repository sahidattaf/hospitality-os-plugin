# AGENTS.md — Hospitality OS Plugin

This file is the project-specific governance standard for the Hospitality OS plugin, following the Sahid AI Ecosystem AGENTS.md standard. It governs how Claude Code, Codex, and any other agent must operate in this repository.

**Repository:** `https://github.com/sahidattaf/hospitality-os-plugin` (default branch `main`), cloned locally at `C:\Users\sahid\plugins\hospitality-os-plugin`. Current plugin version: `0.4.0`.

## 1. Mission

Build Hospitality OS as a professional, reusable AI operations plugin and agent system for restaurants, hotels, hospitality teams, demos, delivery, sales, intelligence, and operational execution.

The system must remain:

- Installable
- Testable
- Documented
- Versioned
- Compatible with its declared plugin architecture
- Safe for client and production use
- Reusable across hospitality businesses

## 2. Source-of-Truth Files

Inspect actual repository files before editing. Read in this order:

1. `AGENTS.md` (this file)
2. `CLAUDE.md`
3. `README.md`
4. `.codex-plugin/plugin.json` (plugin manifest, currently v0.4.0)
5. `.agents/plugins/marketplace.json` (repo-local marketplace metadata)
6. `skills/` — one `SKILL.md` per workflow (30 skills as of v0.4.0; see Section 3)
7. `prompts/hospitality-os-prompts.md` and `prompts/video-production-agent.md`
8. `examples/` (including `examples/video-production/`)
9. `tests/` (`tests/README.md`, `tests/yaml.py`, `tests/video-production-agent-validation.md`)
10. Validation scripts referenced in `tests/README.md` and `README.md` (external, under `C:\Users\sahid\.codex\skills\.system\plugin-creator\scripts\`)
11. Release and version documentation — **gap: no `CHANGELOG.md` or release notes exist yet**; version history is currently only tracked informally via the "v0.1/v0.2/v0.3/v0.4 additions" sections of `README.md`.
12. Hospitality OS context in `sahid-ai-clone-pack`: `sahid-ai-clone-pack/projects/hospitality-os-plugin.md`

Do not invent files that do not exist. If a listed file or folder is missing, continue using the real repository structure, document the gap, and do not create replacement architecture unless the task explicitly calls for it.

## 3. Product Priorities

Work in this order. Anything outside this list is backlog/post-MVP unless explicitly approved.

1. Plugin validity and installation reliability
2. Agent and skill registration
3. Sales Operator — `skills/sales-operator/SKILL.md` (exists)
4. Demo Producer — `skills/demo-producer/SKILL.md` (exists)
5. Delivery Manager — `skills/delivery-manager/SKILL.md` (exists)
6. Controller — **gap: no `skills/controller/` directory exists**. Treat as backlog/post-MVP until a SKILL.md, prompt entry, example, and test are created together.
7. Market Intelligence — `skills/market-intelligence/SKILL.md` (exists)
8. Weekly AI Brief — `skills/weekly-ai-brief/SKILL.md` (exists)
9. Decision Log — `skills/decision-log/SKILL.md` (exists)
10. SOP Builder — `skills/sop-builder/SKILL.md` (exists)
11. Review Generator — `skills/review-generator/SKILL.md` (exists)
12. Menu Engineer — `skills/menu-engineer/SKILL.md` (exists)
13. Revenue Optimizer — `skills/revenue-optimizer/SKILL.md` (exists)
14. AI Concierge — `skills/ai-concierge/SKILL.md` (exists)
15. Video Production Agent — `skills/video-production-agent/SKILL.md` (exists, v0.4 addition, with `references/`, `templates/`, `schemas/video-job.schema.json`)
16. Documentation, examples, and tests

### Additional skills already shipped (beyond the priority list above)

These exist in the repo and must be preserved/maintained even though they weren't named in the priority list:

- **v0.2 outreach/finance/ops**: `restaurant-outreach-agent`, `hotel-outreach-agent`, `catering-sales-agent`, `event-booking-agent`, `investor-deck-agent`, `social-media-agent`, `menu-costing-agent`, `inventory-agent`, `staff-training-agent`, `customer-recovery-agent`
- **v0.3 BOSSA Asado i Mar specialization layer**: `bossa-fire-chef-agent`, `bossa-fire-box-agent`, `bossa-tourist-experience-agent`, `bossa-whatsapp-sales-agent`, `bossa-owner-dashboard-agent`, `bossa-kpi-agent`, `bossa-inventory-forecast-agent`, `bossa-reservation-agent`

## 4. Repository Rules

- Preserve the plugin schema and declared folder structure (`.codex-plugin/plugin.json`, `.agents/plugins/marketplace.json`, `skills/`, `prompts/`, `examples/`, `tests/`).
- Do not invent integrations, agents, routes, APIs, tools, credentials, or deployment results. This plugin has **no application code, APIs, or runtime integrations today** — it is a Markdown-based skill pack plus one JSON schema (`skills/video-production-agent/schemas/video-job.schema.json`).
- Do not commit secrets, tokens, passwords, API keys, customer data, or private Notion URLs.
- Do not push directly to `main`.
- Work on a scoped feature branch.
- Inspect before editing. Reuse existing repository patterns — every `skills/*/SKILL.md` follows the same template (frontmatter `name`/`description`, then Purpose, When to use, Inputs needed, Step-by-step workflow, Output format, BOSSA Asado i Mar example, Test prompt). The Video Production Agent additionally has a "Do not use" section and supporting `references/`, `templates/`, `schemas/` directories — follow that extended pattern for any future production/operational agents with similar risk profiles.
- Keep changes scoped, reviewable, reversible, and documented.
- TypeScript strict mode / `any` / Zod rules: **not applicable today** — there is no TypeScript or runtime code in this repo. Apply these rules if/when code is introduced.
- Do not register an agent/skill without its required supporting files (SKILL.md, prompt entry, example, test coverage).
- Keep agent/skill names, aliases, routing, capabilities, and version metadata synchronized between `.codex-plugin/plugin.json`, `skills/`, `prompts/`, and `examples/`.
- Validate YAML/Markdown frontmatter, JSON manifests (`.codex-plugin/plugin.json`, `.agents/plugins/marketplace.json`, `skills/video-production-agent/schemas/video-job.schema.json`), and registry entries.
- Avoid hidden dependencies. Do not add runtime integrations without documentation and environment configuration.
- Treat `examples/` as executable/testable demonstrations (inputs + expected outputs), not decorative text.
- Add validation coverage for every new agent or skill (see Testing Rules).
- Update release notes and version metadata (`.codex-plugin/plugin.json` `version` field, and the "vX additions" section of `README.md`) when behavior changes — **gap: no standalone `CHANGELOG.md` exists yet; consider creating one when the next versioned change is made**.
- Never weaken validation only to make a broken plugin pass.

## 5. Deployment Rules

For Hospitality OS, "deployment" means plugin release readiness, not application hosting:

- Repository validation
- Plugin packaging
- Installation testing
- Version consistency checks (`.codex-plugin/plugin.json` version vs. `README.md` version sections)
- GitHub release readiness
- Optional application deployment only where explicitly configured — **not applicable today; this plugin has no app to deploy**

Do not assume Vercel, Supabase, or another cloud platform is required for the plugin itself.

Before release:

- Run the plugin validator (see Testing Rules)
- Confirm `.codex-plugin/plugin.json` and `.agents/plugins/marketplace.json` are valid JSON and reference real paths
- Confirm every skill referenced exists under `skills/`
- Confirm skill `name`/IDs are unique
- Confirm version numbers are synchronized (`.codex-plugin/plugin.json` and `README.md`)
- Confirm installation steps in `README.md` work
- Confirm examples and tests pass / are followed
- Confirm no secrets are committed
- Confirm release documentation is updated (once it exists)

Do not publish or tag a release when required checks fail.

## 6. Testing Rules

Inspect the repository first, then run the commands that actually exist. There is **no `pnpm`/Node/Python project config** (no `package.json`, `pyproject.toml`, etc.) in `hospitality-os-plugin` itself, so most of the generic command list below does **not apply**. The commands that actually exist for this repo:

```powershell
# Plugin validator (external script, referenced by README.md and tests/README.md)
C:\Users\sahid\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe C:\Users\sahid\.codex\skills\.system\plugin-creator\scripts\validate_plugin.py C:\Users\sahid\OneDrive\Documents\hospitality-os-plugin
```

Expected result: `Plugin validation passed`.

> **Gap:** the validator command as written in `README.md`/`tests/README.md` points at `C:\Users\sahid\OneDrive\Documents\hospitality-os-plugin`, a path different from where this repo's working clone lives (`C:\Users\sahid\plugins\hospitality-os-plugin`). Confirm the correct path before relying on this command, and update both docs if the canonical location changes.

`tests/yaml.py` exists as a lightweight YAML/frontmatter check — inspect it before assuming what it validates; do not assume it covers everything.

`tests/video-production-agent-validation.md` documents the manual validation steps for the v0.4 Video Production Agent — follow it when changing that skill or its `references/`, `templates/`, or `schemas/`.

`pnpm lint` / `pnpm typecheck` / `pnpm test` / `pnpm build` / `python -m pytest` — **not applicable** (no such tooling configured in this repo). Do not claim these passed.

Also validate, where relevant to a change:

- Manifest references (`.codex-plugin/plugin.json` and `.agents/plugins/marketplace.json` paths resolve to real files)
- Missing files referenced by README/SKILL.md
- Duplicate skill names/IDs across `skills/*/SKILL.md`
- Broken prompt paths (`prompts/hospitality-os-prompts.md`, `prompts/video-production-agent.md`)
- Skill metadata (frontmatter `name`/`description` present and consistent)
- Example coverage (each skill has at least one `examples/*.md` or, for video production, `examples/video-production/*.md`)
- Test coverage (`tests/`)
- Version consistency (`.codex-plugin/plugin.json` `version` vs. `README.md`)
- Markdown formatting
- YAML/JSON validity (including `skills/video-production-agent/schemas/video-job.schema.json`)

Manual smoke test for any skill change: run that skill's "Test prompt" — including v0.2 outreach/finance/ops agents, v0.3 BOSSA agents, and the v0.4 Video Production Agent — and confirm the response matches its "Output format," and that the BOSSA Asado i Mar example stays grounded in the facts provided.

Do not claim a check passed unless it was actually run successfully. If a command or dependency is unavailable, report it honestly, explain the missing requirement, and do not invent a successful result.

## 7. Notion Integration Rules

Use Notion for:

- Agent registry
- Release planning
- Client delivery tracking
- Demo pipeline
- Installation checklist
- Decision log
- Roadmap
- Operational documentation index
- Client implementation plans
- Training notes
- Support and maintenance tracking

The GitHub repository (`sahidattaf/hospitality-os-plugin`) remains the source of truth for:

- Plugin files
- Manifests
- Prompts
- Skills
- Examples
- Tests
- Validation scripts
- Versioned releases

Do not duplicate live plugin definitions in Notion. Never commit Notion API tokens, private integration secrets, sensitive workspace URLs, or client-confidential information. Document which system owns each dataset as integrations are added — **gap: no Notion integration currently exists in this repo**.

## 8. Claude Code and Codex Operating Instructions

At the beginning of every task:

1. Read `AGENTS.md` (this file).
2. Inspect the repository tree (`C:\Users\sahid\plugins\hospitality-os-plugin`).
3. Read relevant source-of-truth files (Section 2).
4. Check the current Git branch and working tree (`git status`, `git branch --show-current`) — confirm you are in `C:\Users\sahid\plugins\hospitality-os-plugin`, which is a standalone clone of `sahidattaf/hospitality-os-plugin`, not the user's home-directory git repo.
5. Identify the affected agent, skill, manifest, or workflow.
6. State the intended scope before editing.
7. Avoid editing until current behavior is understood.

During execution:

- Inspect before editing.
- Reuse existing patterns (the shared `SKILL.md` template).
- Keep edits scoped.
- Update all related registration and metadata files together (`.codex-plugin/plugin.json`, `.agents/plugins/marketplace.json`, `skills/`, `prompts/`, `examples/`, `tests/`).
- Add tests/examples and documentation with the feature.
- Do not fabricate integrations or results.
- Preserve existing working behavior unless explicitly changing it.
- Stop and report if an action would expose secrets, damage production systems, or operate on the wrong repository.

Before completion:

1. Run available validators (Section 6).
2. Run available tests/checks.
3. Run lint/typecheck/build only if applicable (currently not applicable — report as such).
4. Inspect the final diff.
5. Confirm no secrets were added.
6. List changed files.
7. Report passed, failed, and unavailable checks.
8. Explain release and deployment impact.
9. Explain Notion impact.
10. Explain rollback steps.
11. Record major decisions in the decision log (`skills/decision-log/` workflow output, or `sahid-ai-clone-pack/projects/hospitality-os-plugin.md`).

## 9. Supabase Governance

Supabase is optional for the core plugin. **Gap: Supabase is not currently used anywhere in this repository** — do not assume it is required.

If Supabase is introduced in the future:

- Use organization and client isolation.
- Use Row Level Security.
- Keep service-role credentials server-side.
- Never expose service-role keys in browser code or plugin files.
- Validate all API input server-side.
- Use immutable migrations after deployment.
- Add audit logging for sensitive actions.
- Test migrations outside production first.
- Do not run destructive production SQL without explicit approval.
- Document rollback considerations.
- Minimize personal and client-confidential data.
- Define retention and deletion behavior.

## 10. GitHub Workflow Standards

Branch naming:

```text
feat/<short-description>
fix/<short-description>
docs/<short-description>
chore/<short-description>
refactor/<short-description>
test/<short-description>
```

Conventional commits:

```text
feat: add hospitality agent
fix: correct plugin manifest path
docs: add project AGENTS governance
test: validate agent registration
chore: update release metadata
```

Every pull request must include:

- Objective
- Product impact
- Summary of changes
- Changed files
- Validation results
- Test results
- Version impact
- Manifest impact
- Installation impact
- Deployment impact
- Environment-variable impact
- Supabase impact
- Notion impact
- Security considerations
- Human-review requirements
- Rollback notes

Do not merge when required checks fail. Use squash merge unless repository policy specifies otherwise.

## 11. Ecosystem-Standard Relationship

This repository follows the Sahid AI Ecosystem structure:

```text
Master governance:
sahid-ai-clone-pack/AGENTS.md   <-- gap: does not exist yet (only sahid-ai-clone-pack/agents/ directory and CLAUDE.md exist today)

Project governance:
hospitality-os-plugin/AGENTS.md  <-- this file

Project context and memory:
sahid-ai-clone-pack/projects/hospitality-os-plugin.md  <-- exists

Reusable workflows and governance:
sahid-ai-clone-pack/workflows/   <-- exists
sahid-ai-clone-pack/docs/        <-- exists
sahid-ai-clone-pack/memory/      <-- exists

Operational plugin code:
hospitality-os-plugin (this repo, https://github.com/sahidattaf/hospitality-os-plugin)

Executive tracking:
Notion Command Center  <-- gap: no integration configured

Transactional data:
Supabase or another approved database only when required  <-- gap: not used
```

Hospitality OS-specific rules in this file override the master (`sahid-ai-clone-pack/AGENTS.md`) when they are more restrictive — once that master file exists. Until then, this file is the authoritative governance document for this repository.

## 12. Completion Checklist

Before completing work in this repository:

- [ ] Correct repository confirmed (`sahidattaf/hospitality-os-plugin`, clone at `C:\Users\sahid\plugins\hospitality-os-plugin`)
- [ ] Correct branch confirmed (feature branch, not `main`)
- [ ] Repository structure inspected
- [ ] Source-of-truth files reviewed (Section 2)
- [ ] Plugin schema preserved (`.codex-plugin/plugin.json`, `.agents/plugins/marketplace.json`, `skills/`, `prompts/`, `examples/`, `tests/`)
- [ ] Skill metadata synchronized across manifest, skills, prompts, examples
- [ ] No secrets added
- [ ] Validators completed or explained (Section 6)
- [ ] Tests completed or explained
- [ ] Lint/typecheck/build completed or explained (or marked not applicable)
- [ ] Version impact documented (`.codex-plugin/plugin.json`, `README.md`)
- [ ] Manifest impact documented
- [ ] Supabase impact documented (or marked not applicable)
- [ ] Notion impact documented (or marked not applicable)
- [ ] Changed files listed
- [ ] Release impact explained
- [ ] Rollback steps explained
