# Getting started

Hospitality OS supplies 12 skills, shared instructions, examples, and schemas. It includes no MCP server, connected app, reservation backend, POS, WhatsApp adapter, or bundled account credentials.

## Candidate and identities

| Item | Value |
| --- | --- |
| Repository | `sahidattaf/hospitality-os-plugin` |
| Marketplace identity | `hospitality-os` |
| Marketplace display label | GPT Innovation by Attaf |
| Plugin identity | `hospitality-os-plugin` |
| Installation key | `hospitality-os-plugin@hospitality-os` |
| Plugin root | `plugins/hospitality-os-plugin/` |
| Current remote package, verified 2026-10-12 | `0.5.1` on `main` at `5942d49c9d57b36f297815d693440f5b5a97087c` |
| Historical audited main version | `0.5.0` at `3667a4209b832a5bfe888f4430c2efe7f6fcd3c2` |

The instructions below are an installation and refresh runbook. Remote `main` now contains `0.5.1`; verify the actual installed and loaded package separately. Historically, `HOSPITALITY-PLUGIN-MARKETPLACE-2` authorized source edits and local validation only, and no installation command was run under that gate. The 12 October source review does not itself establish local installation acceptance.

## Codex CLI

After the candidate is accepted, made available on the chosen remote ref, and installation is authorized, check the installed CLI first:

```bash
codex --version
codex plugin marketplace --help
```

Add the GitHub catalog and inspect it:

```bash
codex plugin marketplace add sahidattaf/hospitality-os-plugin --ref main
codex plugin marketplace list
codex
```

In the Codex session, open `/plugins`, select the `hospitality-os` marketplace, and install `hospitality-os-plugin`. Confirm the displayed package version and installation key. `--ref main` retrieves the current remote main, which was verified to contain `0.5.1` on 12 October 2026. Confirm the ref and package version again at installation time; use an explicitly accepted branch, tag, or commit ref for reproducible testing when supported by the installed CLI.

For a separately authorized local candidate test, run this from the directory containing the checkout:

```bash
codex plugin marketplace add ./hospitality-os-plugin
```

After an accepted remote update, refresh the named catalog:

```bash
codex plugin marketplace upgrade hospitality-os
```

Verify the catalog and installed plugin version again, complete any plugin update offered by the surface, and start a new thread. A catalog refresh alone is not evidence that a thread has loaded the new skill contents.

Codex desktop and CLI support plugins. The Codex IDE extension does not currently support plugins; running Codex CLI in a VS Code terminal uses the CLI route. Account plan, workspace role, and surface controls still determine what is available.

## Managed ChatGPT workspace

A workspace administrator can use the GitHub-backed marketplace import and sync route after confirming access and the accepted ref. Use the repository URL, with the Path field empty because `.agents/plugins/marketplace.json` is at the repository marketplace root. Set distribution and member-access controls deliberately; repository privacy and plugin workspace availability are separate settings. Automatic sync is daily by default and is configurable.

Importing or syncing this catalog is not public-directory publication. This gate did not inspect or change account-level install or admin controls.

## First synthetic acceptance session

Record surface, CLI/app version, source ref, commit, manifest version, and loaded skill names. Confirm the exact 12-skill baseline and render both light and dark listing assets in the supported surface. Use synthetic facts for the [behavior matrix](../plugins/hospitality-os-plugin/tests/behavioral-test-matrix.md) and [video cases](../plugins/hospitality-os-plugin/tests/video-production-agent-validation.md).

Check that unsupported integrations stay at draft or supplied-evidence handling, missing facts are flagged, current routing destinations exist, and no external action occurs without its authorized scope. BOSSA and Sea Horizon live acceptance need their own scope and authoritative business evidence.

## Later distribution

This repository currently has public source visibility; a private workspace catalog does not make that source private. A private-marketplace product requires a separately authorized private source and workspace import arrangement. Confirm the intended MIT license file and copyright before distribution.

Public-directory submission is a separate package, account, and review process. Under the current skills-only submission route, MCP cannot be added later to an already submitted skills-only plugin; prepare a separately reviewed integration-bearing identity if live tools are planned. Optional connectors named in the shared policies require their own availability, authentication, and action authorization.

## Specification references

Checked against the official documentation during the October 2026 audit; recheck before installation or submission:

- [OpenAI plugin packaging](https://developers.openai.com/plugins/build/plugins)
- [OpenAI submission metadata and assets](https://developers.openai.com/plugins/deploy/submission)
- [Supported plugin surfaces and CLI routes](https://learn.chatgpt.com/docs/plugins)
- [Workspace plugin management](https://learn.chatgpt.com/docs/enterprise/plugin-management)
