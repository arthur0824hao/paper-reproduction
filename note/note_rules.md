# Note Rules

## Purpose

This file captures the working rules that are already being followed in this repository when `note/note_tasks.md` and `review/REQUEST_BUNDLE.md` define the active round.

## Core Rules

1. `note/note_tasks.md` remains the user-side task log and must be treated as read-only.
2. `review/REQUEST_BUNDLE.md` is the review-agent inbox and round execution contract when present.
3. Scope defaults to GPM sandbox only unless a newer round note explicitly says otherwise.
4. Only one active claimed ticket is allowed at a time.
5. Re-read `### New` from `note/note_tasks.md` and the active request bundle before claim, before close, and before session exit.
6. If the active request bundle has no `### New` section, treat it as empty rather than inventing one.
7. Every worker ticket close must update:
   - `review/tickets/TKT-xxx.md`
   - `review/tickets/state/TKT-xxx.json`
   - `review/REVIEW_BUNDLE.md`
8. A worker ticket is not considered done until evidence paths and close-criteria checks are written down.
9. If a ticket cannot be completed, it must be moved to an evidence-bearing blocked state instead of being silently abandoned.
10. If `OPEN`, `UNCLAIMED`, or `STALE_CLAIM` tickets remain and there is no active claim, claim the next ticket from the active request bundle.
11. Only the round integrator ticket may perform final closeout.
12. Do not claim FraudDetect mainline execution, production AML results, or mainline repo progress from sandbox-only work.

## Evidence Rules

- Claims in bundle, ticket markdown, state JSON, and concrete artifacts must agree.
- Ticket definitions should be read from `review/REQUEST_BUNDLE.md` when that file is the active inbox.
- Exploratory reduced-config results must be labeled exploratory.
- Faithful reproduction claims require the default path to complete on a parity runtime.
- Transfer ideas must be written as probes, contracts, or hypotheses unless real AML execution evidence exists.

## Review Rules

- `REVIEW_READY` means deliverables exist, close criteria are checked, and evidence paths are explicit.
- `BLOCKED_WITH_EVIDENCE` means the blocker and current evidence are both written in state JSON.
- Final board clean means no `OPEN`, `UNCLAIMED`, or `STALE_CLAIM` remain for the target round.

## Commit and Push Rules

- Prefer one coherent commit per ticket close when commit is requested.
- Never claim push success unless the branch actually reached the configured remote.
- If remote state changes after closeout, sync the integrator metadata before handoff.
