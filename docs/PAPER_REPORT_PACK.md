# Paper Report Pack

## A. Paper One-Paragraph Summary

GPM treats graph learning as a pattern modeling problem rather than pure neighborhood message passing: it samples path-like graph patterns, encodes semantic and anonymous structural views of those patterns, and aggregates them into node-level predictions. Compared with a standard message-passing GNN, the distinctive move is that GPM explicitly builds reusable pattern tokens and statistics, so the model can reason over recurring structural motifs instead of only repeatedly mixing local neighbor features layer by layer.

## B. Faithful Reproduction Boundary

### What we can say now

- The sandbox reproduces the end-to-end data pipeline, pattern cache, training loop, and reduced-config GRU encoder path.
- Reduced-config ablations on `computers` completed and support mechanism-oriented discussion.

### What we cannot say now

- We cannot claim faithful reproduction of the paper's default transformer path.
- We cannot claim paper-level benchmark parity or compare current reduced-config numbers as if they were the faithful result.

### Faithful blocker

- All three default-config `computers` runs fail before epoch 1 with `CUDA error: an illegal memory access was encountered` at `model/encoder.py:160`.
- Current evidence points to a CUDA 12.8 driver versus PyTorch cu121 runtime mismatch on the transformer attention path.

## C. Reduced-Config Mechanism Insight

| component | evidence | effect | interpretation | evidence_level |
|---|---|---|---|---|
| both paths | `90.17 +- 0.39` test, 0.81M params | reduced-config reference point | combined semantic + anonymous paths remain the sandbox baseline | exploratory |
| semantic only | `90.10 +- 0.54` test, 0.74M params | about `-0.07` vs both paths | semantic path alone is nearly sufficient under reduced config | exploratory |
| anonymous only | `90.19 +- 0.48` test, 0.81M params | about `+0.01` vs both paths | anonymous structural signal matches combined path within noise | exploratory |
| reduced patterns | `90.17 +- 0.61` test, 0.81M params with `num_patterns=4` | no visible collapse on `computers` | pattern budget may be compressible for probing, but this is not a faithful claim | exploratory |

### Most AML-worthy component

- `anonymous path statistics` is the strongest immediate AML candidate because it preserves signal in the reduced-config ablation, is naturally exportable as features, and does not depend on the blocked transformer runtime.

## D. Transfer Takeaway

- First carry back `anonymous path statistics`: lowest integration effort, clearest structural novelty, and strongest current signal.
- Second carry back `random-walk tokenizer`: it is the enabling layer for path-derived features and a practical bridge to directed AML transaction graphs.
- Consider `pattern frequency statistics` only after a novelty gate confirms they add information beyond the existing AML feature bank.

## E. Caveat Section

- Reduced-config results are exploratory only.
- This is not a faithful transformer claim.
- This is not AML production validation.

## Evidence Level Guide

| claim type | current level | usable for professor report? |
|---|---|---|
| reduced-config mechanism comparison | evidence-backed exploratory result | yes |
| faithful default-transformer reproduction | blocked / unverified | no |
| AML transfer implementation direction | evidence-informed proposal | yes, as proposal |
| AML production impact | untested | no |

## Evidence Paths

- Reduced ablation summary: `repro/results_db/ablation_reduced_computers_summary.json`
- Reduced ablation ticket: `review/tickets/TKT-803.md`
- Faithful blocker plan: `docs/FAITHFUL_REPRO_COMPLETION_PLAN.md`
- Transfer probe contract: `docs/AML_PROBE_SPEC.md`
