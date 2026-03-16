# Transfer Implementation Plan

## Freeze Decision

This plan freezes the GPM-to-AML transfer path into a two-step feature-first implementation sequence. The objective is to carry back the lowest-risk structural signal first, validate novelty before deeper integration, and avoid spending effort on model-side components that still depend on the blocked faithful transformer path.

## Implementation Table

| component | keep/drop/defer | AML form | required adapter | artifact target | success metric | first execution step |
|---|---|---|---|---|---|---|
| anonymous path statistics | keep | per-account structural feature block | directed AML graph adapter with `node_id` mapping and walk export | `anon_path_features.csv`, `anon_path_features.pt`, `metadata_manifest.json` | >=80% eligible-node walk coverage and >=3 features with corr < 0.7 vs existing bank | wire graph adapter and export `probe_anon_path_stats_v1` |
| random-walk tokenizer | keep | reusable directed walk generator for downstream probes | direction-aware and eventually temporal walk policy | tokenizer walk dump plus manifest feeding feature extractors | stable walk generation on AML-shaped graph slice with reproducible config | adapt tokenizer input contract to AML edge fields |
| pattern frequency statistics | defer | secondary feature family on top of tokenizer output | reuse tokenizer output and feature export path | `pattern_freq_features.csv`, `pattern_freq_features.pt` | only continue if novelty gate passes after anonymous path features are checked | run after tokenizer + anonymous-path baseline is established |
| pattern attention | drop | none for current freeze | would require model-side training/inference port, not just feature export | no artifact target in this round | not worth current effort until feature probes show clear value and transformer path risk falls | do not implement in this round |

## Ordered Execution Plan

### First step

1. Implement and validate `anonymous path statistics` on the AML-compatible graph surface.
2. Use the existing tokenizer and feature extraction base to emit feature artifacts plus metadata.
3. Run the novelty/correlation gate before any model-side experiment.

### Second step if the first succeeds

1. Stabilize the `random-walk tokenizer` as a reusable AML adapter layer.
2. Add `pattern frequency statistics` as the next feature family only if the first step shows non-redundant structural signal.

## Explicit Defer / Drop Calls

- Defer `pattern frequency statistics` until the first feature family proves it adds value; this avoids stacking speculative features before the adapter path is validated.
- Drop `pattern attention` for the current freeze because it is a high-effort model port, has no immediate feature-export path, and depends on confidence in a mechanism family that is still blocked on the faithful transformer runtime.

## Why This Freeze

- It keeps the plan feature-first, which matches the strongest currently evidenced transfer signal.
- It minimizes coupling to the blocked faithful reproduction path.
- It yields concrete artifacts that can be audited independently of any claim about AML production impact.

## Evidence Links

- Professor-facing report: `docs/PAPER_REPORT_PACK.md`
- Faithful boundary: `docs/FAITHFUL_REPRO_COMPLETION_PLAN.md`
- AML probe contract: `docs/AML_PROBE_SPEC.md`
- Tokenizer base: `transfer/pattern_tokenizer/tokenizer.py`
- Feature extractor base: `transfer/feature_extraction/extract_features.py`
