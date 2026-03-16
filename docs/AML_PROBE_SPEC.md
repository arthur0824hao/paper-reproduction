# AML Probe Spec

## Probe Choice

- First probe: `probe_anon_path_stats_v1`
- Target component: anonymous path statistics
- Why first: lowest integration effort, structurally novel signal, and strongest reduced-config transfer hint.

## Input Graph Contract

| field | contract |
|---|---|
| graph surface | directed account-to-account transaction graph |
| node key | `node_id` = AML account identifier used by feature bank joins |
| edge source | `src_node_id` |
| edge target | `dst_node_id` |
| required edge fields | `timestamp`, `amount`, `txn_type` |
| optional edge fields | `channel`, `country`, `currency`, `risk_flag` |

## Feature Contract

- Walk basis: directed random walks that preserve edge direction; temporal ordering is preferred if available.
- Primary output fields: `cycle_participation`, `chain_length_mean`, `revisit_hist_0..K`, `walk_valid_mask`.
- Optional companion fields: `fan_out_score`, `pattern_count`, `pattern_entropy` if the tokenizer pass is already available.

## Artifact Contract

| artifact format | shape / schema | consumer |
|---|---|---|
| `anon_path_features.csv` | `node_id, cycle_participation, chain_length_mean, revisit_hist_0..K, walk_valid_mask` | merge into AML feature bank |
| `anon_path_features.pt` | tensor `[N, D]` aligned to sorted `node_id` manifest | tensor-side probe / model-side reuse |
| `metadata_manifest.json` | tokenizer config, graph stats, feature dims, generation timestamp | audit and reproducibility |

## Success Criterion

| criterion | threshold |
|---|---|
| graph contract validity | 100% of rows resolve to valid `node_id` keys |
| feature coverage | >= 80% of eligible accounts receive at least one valid walk |
| novelty gate | at least 3 generated features have max correlation < 0.7 vs existing AML feature bank |
| probe usefulness | downstream probe is worth continuing if any accepted feature family clears the novelty gate |

## Engineering Hand-Off

1. Build AML graph adapter that emits sorted `node_id` mapping.
2. Run tokenizer on the directed graph surface.
3. Export `.csv`, `.pt`, and `metadata_manifest.json` together.
4. Run correlation gate before any mainline or modeling claim.

## Evidence Links

- Reduced-config mechanism evidence: `docs/PAPER_REPORT_PACK.md`
- Existing transfer implementation base: `transfer/pattern_tokenizer/tokenizer.py`
- Existing feature extractor base: `transfer/feature_extraction/extract_features.py`
