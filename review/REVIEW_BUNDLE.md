# GPM Reproduction & Transfer — Review Bundle

**Date**: 2026-03-16  
**Session**: sisyphus-ralph-004  
**Repo scope**: GPM sandbox only  
**Source repo**: `external/gpm_code/` at commit `2ed3ebf7df8d8401520e6ec3bdbd1c2b291b5784`

## GPM Round Contract

| layer | goal | canonical evidence | non-goal |
|---|---|---|---|
| reproduction | runnable default path or exact blocker localization | `repro/results_db/computers_summary.json` | not AML improvement |
| mechanism summary | component-level reportable insight with explicit caveats | `docs/PAPER_REPORT_PACK.md` | not faithful paper claim |
| transfer | AML-usable contract and ranking | `docs/AML_PROBE_SPEC.md` | not FraudDetect mainline execution |

## Professor Report Pack

| section | key point | evidence level | primary evidence |
|---|---|---|---|
| paper summary | GPM learns from explicit path/pattern representations rather than only message passing | paper-facing interpretation | `docs/PAPER_REPORT_PACK.md` |
| faithful boundary | faithful reproduction is still blocked on the default transformer runtime | evidence-backed boundary | `docs/FAITHFUL_REPRO_COMPLETION_PLAN.md` |
| reduced-config mechanism insight | anonymous-only matches both-paths within noise on `computers` | exploratory | `repro/results_db/ablation_reduced_computers_summary.json` |
| transfer takeaway | anonymous path statistics is the best immediate AML carry-back | evidence-informed proposal | `docs/AML_PROBE_SPEC.md` |
| caveat section | not a faithful transformer claim and not AML production validation | hard boundary | `docs/PAPER_REPORT_PACK.md` |

## Transfer Implementation Plan

| component | keep/drop/defer | AML form | required adapter | artifact target | success metric | first execution step |
|---|---|---|---|---|---|---|
| anonymous path statistics | keep | per-account structural features | directed AML graph adapter plus `node_id` mapping | `anon_path_features.csv`, `anon_path_features.pt`, `metadata_manifest.json` | >=80% coverage and >=3 low-correlation features | wire `probe_anon_path_stats_v1` |
| random-walk tokenizer | keep | reusable directed walk generator | direction-aware AML walk policy | tokenizer walk dump plus manifest | stable reproducible walk export on AML-shaped graph | adapt tokenizer input contract |
| pattern frequency statistics | defer | secondary feature family | reuse tokenizer/export path after first-step success | `pattern_freq_features.csv`, `pattern_freq_features.pt` | novelty gate must pass after anonymous-path baseline | run only after first-step success |
| pattern attention | drop | none in this round | would require model-side port and blocked mechanism confidence | none | not worth current round effort | do not implement |

## Faithful Reproduction Completion Plan

| item | current_state | blocker | completion_condition | next_action |
|---|---|---|---|---|
| faithful status | not faithful yet | default transformer path never completes | 3-seed default-config run completes and can be compared to paper | rerun exact default command on parity runtime |
| default config | 3/3 failed on `computers` | illegal memory access at `model/encoder.py:160` | one stable transformer run with terminal metrics | move to >=24GB CUDA-12.1-compatible machine or align local driver/runtime |
| reduced config | 4/4 exploratory ablations succeeded | not architecturally faithful | keep only as exploratory mechanism evidence | use for mechanism discussion, not faithful claims |
| short-term fallback | available | no local faithful runtime today | at least one parity rerun path scheduled and executable | prioritize remote >=24GB rerun; fallback to local CUDA alignment |

## Paper-Facing Mechanism Summary

| component | evidence | effect | interpretation | can_report? |
|---|---|---|---|---|
| semantic only | `90.10 +- 0.54` test, 0.74M params | about `-0.07` vs both paths | nearly sufficient alone under reduced config | yes, exploratory only |
| anonymous only | `90.19 +- 0.48` test, 0.81M params | about `+0.01` vs both paths | anonymous structural signal matches combined path within noise | yes, exploratory only |
| both paths | `90.17 +- 0.39` test, 0.81M params | reduced-config reference point | combined path remains the sandbox baseline | yes, exploratory only |
| reduced patterns | `90.17 +- 0.61` test with `num_patterns=4` | no visible collapse on `computers` | pattern budget looks flexible here, but faithful path still unverified | yes, exploratory only |

**Report boundary**: reduced-config insights are reportable only as exploratory mechanism evidence. No faithful transformer claim is currently valid.

## AML Probe Readiness

| probe | input graph contract | artifact format | success criterion | blocker | next_step |
|---|---|---|---|---|---|
| `probe_anon_path_stats_v1` | directed AML transaction graph keyed by `node_id`; edges need `src_node_id,dst_node_id,timestamp,amount,txn_type` | `anon_path_features.csv`, `anon_path_features.pt`, `metadata_manifest.json` | >=80% eligible-node walk coverage and >=3 features with corr < 0.7 vs existing bank | AML graph adapter not wired yet | implement adapter + run correlation gate |
| `probe_walk_stats_v1` | same graph surface, plus directed walk config | `walk_stats_features.csv`, `walk_stats_features.pt`, manifest | usable if walk statistics add low-correlation structural features | temporal walk policy not finalized | add directed/temporal walk mode |
| `probe_pattern_freq_v1` | same graph surface after tokenizer | `pattern_freq_features.csv`, `pattern_freq_features.pt`, manifest | continue only if novelty gate passes | may overlap existing degree features | run research gate before modeling |

## AML Transfer Priority Ranking

| rank | component | keep/drop/defer | effort | expected value | main risk | first target |
|---|---|---|---:|---:|---|---|
| 1 | anonymous path statistics | keep | 1 | 5 | sparse nodes may lack enough valid walks | `probe_anon_path_stats_v1` |
| 2 | random-walk tokenizer | keep | 2 | 4 | temporal-directed walk adaptation still needed | `probe_walk_stats_v1` |
| 3 | pattern frequency statistics | keep | 1 | 3 | feature overlap with current bank | `probe_pattern_freq_v1` after gate |
| 4 | pattern attention | defer | 5 | 3 | model change depends on blocked faithful transformer path | only after feature probes show value |

## Random Engineering Audit — Artifact Truth

| ticket_id | state_json | evidence_md | artifact_exists | bundle_claim | consistency_verdict |
|---|---|---|---|---|---|
| TKT-802 | `REVIEW_READY` | `review/tickets/TKT-802.md` | yes — `docs/FAITHFUL_REPRO_COMPLETION_PLAN.md`, `repro/results_db/computers_summary.json` | faithful plan is evidence-backed and not over-claimed | PASS |
| TKT-803 | `REVIEW_READY` | `review/tickets/TKT-803.md` | yes — `docs/PAPER_REPORT_PACK.md`, `repro/results_db/ablation_reduced_computers_summary.json` | paper-facing summary now matches current reduced-config artifact values | PASS |
| TKT-805 | `REVIEW_READY` | `review/tickets/TKT-805.md` | yes — `docs/AML_PROBE_SPEC.md` | AML probe spec is concrete enough for engineering hand-off | PASS |
| TKT-804 | `REVIEW_READY` | `review/tickets/TKT-804.md` | yes — ranking is embedded in bundle and ticket | ranking has hard keep/drop/defer decisions | PASS |
| TKT-699 | `REVIEW_READY` | `review/tickets/TKT-699.md` | yes — `docs/ENGINEERING_AUDIT.md` | audit still supports the runtime and hardware statements used here | PASS |

## Ticket Board Summary

| ticket_id | title | status |
|---|---|---|
| TKT-901 | Professor report pack finalization | REVIEW_READY |
| TKT-902 | Transfer implementation proposal freeze | REVIEW_READY |
| TKT-801 | GPM Round Contract Correction | REVIEW_READY |
| TKT-802 | Faithful Reproduction Completion Plan | REVIEW_READY |
| TKT-803 | Paper-Facing Mechanism Summary | REVIEW_READY |
| TKT-804 | AML Transfer Priority Ranking | REVIEW_READY |
| TKT-805 | AML Transfer Probe Spec | REVIEW_READY |
| TKT-899 | Random Engineering Audit — Artifact Truth | REVIEW_READY |
| TKT-000 | GPM Round Closeout | REVIEW_READY |

## Session Claim Map

| ticket_id | owner | session_id |
|---|---|---|
| TKT-901 | sisyphus | sisyphus-ralph-005 |
| TKT-902 | sisyphus | sisyphus-ralph-005 |
| TKT-802 | sisyphus | sisyphus-ralph-004 |
| TKT-803 | sisyphus | sisyphus-ralph-004 |
| TKT-804 | sisyphus | sisyphus-ralph-004 |
| TKT-805 | sisyphus | sisyphus-ralph-004 |
| TKT-899 | sisyphus | sisyphus-ralph-004 |
| TKT-000 | sisyphus | sisyphus-ralph-004 |

## Open / Stale Ticket Check

- `OPEN`: none
- `UNCLAIMED`: `TKT-903`, `TKT-904`, `TKT-000`
- `STALE_CLAIM`: none
- existing blocked evidence tickets: `TKT-602`, `TKT-603` remain blocked but are not open/stale

## Push Summary

- remote configured: yes — `origin -> https://github.com/arthur0824hao/paper-reproduction`
- push attempt status: success — `master` pushed and now tracks `origin/master`

## Worker Ticket Snapshots

- `TKT-901`: professor-facing pack is now presentation-ready with clear evidence-level boundaries.
- `TKT-902`: transfer path is frozen as a concrete feature-first implementation plan with explicit defer/drop calls.
- `TKT-802`: faithful completion plan converted blocker package into an executable decision table.
- `TKT-803`: professor-facing report pack now uses current reduced-config artifact values and explicit report boundaries.
- `TKT-804`: AML component ordering is hard-ranked with keep/defer decisions.
- `TKT-805`: first AML probe contract is concrete enough for adapter implementation.
- `TKT-899`: artifact-truth audit checks five tickets and reports no current inconsistencies.

## New Inbox Audit

- `### New` in `note/note_tasks.md`: empty
- unmapped fingerprints: none
- gate result: PASS

## Integrator Closeout

- Worker deliverables requested in `note/note_tasks.md` are now present.
- Bundle language is scoped to GPM sandbox only.
- No FraudDetect mainline execution claim is made.
- Final blocker remains explicit: faithful reproduction is still blocked on the default transformer runtime.

## Current Round Final State

- all_worker_tickets_ready = no
- all_push_done = yes
- final_board_clean = no
- new_inbox_gate_passed = yes
- repo_scope = GPM sandbox only

## Post-Round Note Bootstrap

| ticket_id | artifact | purpose | verdict |
|---|---|---|---|
| TKT-806 | `note/note_rules.md` | codify execution and evidence rules already in use | PASS |
| TKT-807 | `note/note_schema.md` | codify note, ticket, state, and bundle structure | PASS |

These protocol files are bootstrap guidance derived from current repo practice. They do not replace the active round contract in `note/note_tasks.md`.

## Self Review Dry Run

| ticket_id | review_target | result | boundary |
|---|---|---|---|
| TKT-808 | note protocol bootstrap artifacts | PASS | internal self-review, not independent review |

- `note/note_rules.md` and `note/note_schema.md` are consistent with the repository's observed ticket loop.
- `note/note_feedback.md` records the missing-bootstrap-file issue and the push-state drift that was already corrected.
