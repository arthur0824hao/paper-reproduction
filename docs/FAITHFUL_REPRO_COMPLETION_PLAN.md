# Faithful Reproduction Completion Plan

## Verdict

- Current status: not yet a faithful reproduction.
- Why: the default paper-facing transformer path crashes on all three `computers` seeds before epoch 1 completes, so there is no valid default-config metric to compare against the paper.
- What reduced config proves: the data pipeline, pattern cache, training loop, and non-transformer pattern encoder path all run end to end on this machine.
- What reduced config does not prove: paper-level transformer behavior, paper-matching accuracy, or full faithful reproduction.

## Decision Table

| item | current_state | blocker | completion_condition | next_action |
|---|---|---|---|---|
| default config on `computers` | 3/3 runs fail with `CUDA error: an illegal memory access was encountered` at `model/encoder.py:160` | local runtime mismatch on transformer attention path | one 3-seed default-config run finishes with terminal metrics and no illegal memory access | rerun exact default command on a parity runtime |
| environment parity | local box = RTX 2080 Ti 11GB, driver 570.124.06, nvcc 12.8, PyTorch cu121 | local driver/runtime stack differs from the working paper-style path | GPU/runtime stack matches PyTorch CUDA 12.1 expectation and transformer path is stable | use a >=24GB GPU with CUDA 12.1-compatible driver, or downgrade local driver stack |
| faithful claim threshold | currently unsupported | no valid default-config result | default config completes and lands in the expected paper band on the same dataset/split family | compare terminal accuracy against paper table and record delta |
| reduced config evidence | 4 reduced-config ablations completed successfully with GRU + hidden_dim=128 | not architecturally faithful to paper default | keep only as exploratory mechanism evidence | use these results for mechanism discussion, not faithful claim |
| short-term validation if no 24GB GPU | available | cannot validate transformer path locally today | at least one alternate parity path gives transformer success or a controlled CPU/smaller-scope sanity check rules out code bugs | prioritize remote >=24GB rerun; fallback to driver-aligned local rerun before any new ablation work |

## Exact Answers Required By Ticket

### Does this count as faithful reproduction?

No. The default config never reaches a completed training run, so there is no faithful reproduction result to report.

### Where is the default config blocked?

The blocker is the default transformer pattern encoder path on `computers` with `hidden_dim=256`, `num_patterns=16`, and `batch_size=256`. All three seeds fail at `model/encoder.py:160` during `_encode_pe(patterns.to(device))`.

### What does reduced-config success mean, and not mean?

It means the sandbox can load data, cache patterns, train GPM end to end, and support mechanism-oriented exploratory ablations through the GRU encoder path. It does not mean the default transformer path is validated, and it cannot be used to claim faithful paper reproduction.

### What hardware / driver / runtime is needed for a retry?

- Preferred: a >=24GB GPU with a CUDA 12.1-compatible driver/runtime stack.
- Acceptable local fallback: keep the current GPUs but align the driver/runtime stack with the PyTorch cu121 environment before rerunning the default transformer config.

### If there is no 24GB GPU soon, what is the next-best path?

1. Retry the exact default command on a CUDA-12.1-aligned local stack.
2. If local alignment is not possible, use a remote >=24GB machine for the default transformer run.
3. Until one of those happens, keep reporting reduced-config results strictly as exploratory-only evidence.

## Evidence Paths

- Default-config failures: `repro/results_db/computers_seed0.json`
- Default-config failures: `repro/results_db/computers_seed1.json`
- Default-config failures: `repro/results_db/computers_seed2.json`
- Failure summary: `repro/results_db/computers_summary.json`
- Exploratory reduced ablation summary: `repro/results_db/ablation_reduced_computers_summary.json`
