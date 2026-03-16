# Paper Report Pack

## Reporting Boundary

- Confirmed insight: reduced-config exploratory ablation on `computers` completed successfully.
- Exploratory only: component interpretation under GRU + hidden_dim=128.
- Not confirmed: any faithful default-transformer claim.

## Mechanism Table

| component | evidence | effect | interpretation | can_report? |
|---|---|---|---|---|
| both_paths | `ablation_reduced_computers_summary.json` `both_paths`: test `90.17 +- 0.39`, 0.81M params | reference point for reduced-config comparison | combined semantic + anonymous paths are strong, but this is still exploratory-only | yes, with reduced-config qualifier |
| semantic_only | summary `semantic_only`: test `90.10 +- 0.54`, 0.74M params | about `-0.07` vs both_paths with ~9% fewer params | semantic path alone is nearly sufficient under reduced config | yes, with reduced-config qualifier |
| anonymous_only | summary `anonymous_only`: test `90.19 +- 0.48`, 0.81M params | about `+0.01` vs both_paths within noise | anonymous structural path alone matches the combined path in this exploratory run | yes, with reduced-config qualifier |
| reduced_patterns | summary `reduced_patterns`: test `90.17 +- 0.61`, 0.81M params, fewer patterns | essentially flat test accuracy with lower pattern budget in this run | pattern count looks weakly sensitive on `computers` under reduced config; verify on faithful path before generalizing | yes, but frame as tentative |

## What Can Be Said In A Professor-Facing Report

### Confirmed insight

- The GPM mechanism is operational in sandbox form when the pattern encoder is switched to GRU.
- On `computers`, anonymous-path-only performance matches both-path performance within noise under reduced config.
- This makes anonymous structural signatures the most promising AML-transfer target because they preserve signal while avoiding the currently blocked transformer path.

### Exploratory-only insight

- Semantic-only is close to both-paths, so the semantic branch is not obviously dispensable or dominant.
- Lower pattern count does not collapse performance on `computers`, which suggests a smaller probe budget may be acceptable for AML prototyping.

### Not reportable as faithful claim

- Do not claim the default transformer mechanism has been reproduced.
- Do not compare reduced-config numbers directly to the paper's faithful benchmark table.

## AML Relevance Callout

The component most worth immediate AML attention is `anonymous path statistics`: it is structurally novel, transferable as features, and already looks competitive in the reduced-config ablation without needing the blocked transformer runtime.

## Evidence Paths

- Reduced ablation summary: `repro/results_db/ablation_reduced_computers_summary.json`
- Reduced ablation ticket: `review/tickets/TKT-803.md`
- Faithful blocker plan: `docs/FAITHFUL_REPRO_COMPLETION_PLAN.md`
