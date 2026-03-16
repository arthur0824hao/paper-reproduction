# Note Schema

## 1. Round Note Schema

`note/note_tasks.md` should use the following logical sections:

| section | required | purpose |
|---|---|---|
| `# Prompt` | yes | top-level round prompt container |
| `## User` | yes | user-owned request area |
| `### New` | yes | new inbox items to be re-read during execution |
| `### Request` | yes | active request area |
| `### Asking Question` | yes | blocking questions that require user confirmation |
| `## Review Agent Inbox` | yes | machine-readable round instructions |
| `# Global invariants` | yes | non-negotiable execution rules |
| `# Bootstrap` | yes | files/tools to load before claiming tickets |
| `# Scope contract` | yes | allowed and forbidden work |
| `# Ticket board` | yes | ticket definitions for the round |
| `# REVIEW_BUNDLE required sections for this round` | yes | required bundle outputs |
| `# Ticket execution protocol` | yes | claim/execute/close loop |
| `# Final response format` | yes | response contract |

## 1A. Request Bundle Schema

`review/REQUEST_BUNDLE.md` is the preferred review-agent inbox when the round is split out of `note/note_tasks.md`.

| section | required | purpose |
|---|---|---|
| round intro paragraph | yes | declares sandbox / scope / round identity |
| `# Round contract` | yes | high-level objective and boundaries |
| `# Global invariants` | yes | non-negotiable execution rules |
| `# Bootstrap` | yes | files/tools to load before claiming tickets |
| `# Scope contract` | yes | allowed and forbidden work |
| `# Ticket board (this round)` | yes | ticket definitions for the round |
| `# REVIEW_BUNDLE required sections for this round` | yes | round aggregation requirements |
| `# Ticket execution protocol` | yes | claim/execute/close loop |
| `# Final response format` | yes | response contract |

Optional sections:

| section | purpose |
|---|---|
| `### New` | new inbox items that must be re-read during execution |
| supporting notes | special round constraints or rationale |

## 2. Ticket Markdown Schema

Each `review/tickets/TKT-xxx.md` should contain:

| field/section | required | notes |
|---|---|---|
| title line | yes | `# TKT-xxx — Title` |
| priority | yes | `P0`, `P1`, etc. |
| type | yes | reproduction / analysis / transfer / audit / integrator / governance |
| status | yes | keep aligned with state JSON |
| owner or claimed/closed metadata | preferred | use whichever style already exists for the ticket family |
| `## Goal` | yes | one clear objective |
| deliverable/evidence/results section | yes | must name artifact paths or bundle anchors |
| `## Close Criteria Check` | yes | explicit checklist |

## 3. Ticket State JSON Schema

Minimum required fields for `review/tickets/state/TKT-xxx.json`:

```json
{
  "ticket_id": "TKT-xxx",
  "title": "...",
  "type": "...",
  "priority": "P0|P1|P2",
  "status": "OPEN|CLAIMED|IN_PROGRESS|REVIEW_READY|BLOCKED_WITH_EVIDENCE|CLOSED",
  "round": "..."
}
```

Recommended fields:

| field | purpose |
|---|---|
| `owner` | current ticket owner |
| `owner_session_id` | execution session trace |
| `claimed_at` / `closed_at` / `updated_at` | lifecycle timestamps |
| `artifacts` | concrete evidence paths |
| `bundle_section` | matching bundle section anchor |
| `close_criteria_met` | final boolean gate |
| `commit_sha` | commit associated with close |
| `push_status` | remote synchronization status |
| `blocker` | structured blocker detail when blocked |
| `gate_results` | integrator-only closeout checks |

## 4. Review Bundle Schema

`review/REVIEW_BUNDLE.md` should be the round-level aggregation layer.

Required behavior:

1. Include every round-mandated section from the active round contract, typically `review/REQUEST_BUNDLE.md` or `note/note_tasks.md`.
2. Keep ticket claims synchronized with artifact truth.
3. Make scope boundaries explicit.
4. Separate faithful claims, exploratory claims, and transfer hypotheses.
5. Record board-clean and push state in the final state block.

Recommended section pattern:

| section kind | examples |
|---|---|
| contract | round contract, scope |
| worker outputs | plan, summary, probe, ranking, audit |
| board status | ticket summary, claim map, open/stale check |
| final gate | push summary, inbox audit, integrator closeout, final state |

## 5. Status Semantics

| status | meaning |
|---|---|
| `OPEN` | known work item not yet claimed |
| `CLAIMED` | owner assigned but work not yet evidenced |
| `IN_PROGRESS` | active work underway |
| `REVIEW_READY` | deliverables and evidence are ready for review |
| `BLOCKED_WITH_EVIDENCE` | blocked, but blocker and current evidence are recorded |
| `CLOSED` | reviewed and fully resolved |

## 6. Consistency Gate

Before handoff, the following must agree:

- active request bundle ticket definition
- ticket markdown status
- state JSON status
- bundle summary language
- actual artifact existence
- push claim versus real git remote state
