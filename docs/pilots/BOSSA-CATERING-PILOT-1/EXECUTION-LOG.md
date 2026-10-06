# Local synthetic execution record

Final run, 2026-10-05, America/Kralendijk. Working directory: `C:\Users\sahid\OneDrive\Documents\SAIOS-SKILLS-ACCEPTANCE-LAB`.

```powershell
& 'C:\Users\sahid\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' -B '.\BOSSA-CATERING-PILOT-1\run-synthetic-pilot.py'
```

Observed output:

```json
{"executions": 15, "numbered_tests": 12, "counts": {"PASS": 14, "FAIL": 0, "BLOCKED": 1}, "package_hash_differences": 0, "acceptance": "BLOCKED: PAP human language review pending"}
```

Observed process exit code: 0. Exit 0 means local serialization/invariants completed without a critical failure; it does **not** mean pilot acceptance PASS. The required PAP language-review check remains blocked and the owner decision remains pending.

Method: exact fictional inputs and manually authored instruction-guided outputs are stored separately. The local wrapper serialized these records and checked readiness, null preservation, counts/conflicts, source references, nonexecution and isolation. It is not the installed skill's implementation, an installed API invocation or an independent evaluator. Manual results remain self-assessed.

After inspecting generated outputs, the local output wrapper was refined to include normalized-field tables, translated handoff roles, explicit missing budget-currency/basis evidence, a minimal real-mode negative fixture, and Dutch wording preserving both crustaceans and molluscs rather than narrowing shellfish. Final artifacts were regenerated in the same ordered 15-run sequence. Source/plugin/spec files were not edited.

Actual tool actions: local file/policy reads and hash reads through exec_command; local artifact authoring through apply_patch; local Python evidence-wrapper execution through exec_command; file inventory verification. No web or network call, external connector, message, quote, deposit, booking, purchase, live record, provider activation, configuration/package/source edit, commit/push/merge or deployment.

Source and installed packages remain 62 files each, all matching the Gate 6A raw-byte inventory. Artifact hashes are in ARTIFACT-SHA256.csv. The supplied specification is retained unchanged; its expected SHA256 is recorded in CONTRACT-REVIEW.md and test-evidence.json.
