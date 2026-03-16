你現在進入 **GPM sandbox round v3**。  
這個 workspace 是 **完全獨立的新資料夾**，不是 FraudDetect 主線 repo。  
本 round 的 scope **只限 GPM sandbox**。

# Round contract

- round_goal = 所有向教授報告的前置數據與工作
- mainline_hypothesis = GPM 有可用於 FraudDetect 的部分，並提出具體方案，並簡單驗證
- non_goals = none
- reportable_target = none
- support_scope = 允許的支援性工程
- stop_condition = none

# Global invariants

1. 一次只 claim 一張 ticket
2. `Phase3/note/note_tasks.md` 對你永遠是 readonly
3. claim 前 / ticket close 前 / session exit 前都要 reread `### New`
4. 每張 worker ticket close 前必須：
   - 更新 `review/tickets/TKT-xxx.md`
   - 更新 `review/tickets/state/TKT-xxx.json`
   - 更新 `review/REVIEW_BUNDLE.md`
   - commit
   - push
5. 若仍有 `OPEN / UNCLAIMED / STALE_CLAIM`，且你沒有 active ticket，就必須再 claim 一張
6. 只有 `TKT-000` 可以做 final closeout
7. 本 round 不得生成 FraudDetect mainline ticket，也不得聲稱主線已推進
8. 本 round 不要求 faithful reproduction 補完；faithful blocker 只能當報告邊界，不得拖住本 round

---

# Bootstrap

固定做：

- `using-superpowers`
- `skill-system-router`
- `skill-system-memory`
- `skill-system-workflow`
- `skill-system-behavior`

讀：

- `Phase3/note/note_rules.md`
- `Phase3/note/note_schema.md`
- `Phase3/note/note_tasks.md`
- `Phase3/note/note_feedback.md`
- `review/REVIEW_BUNDLE.md`

然後：

- search memory
- `git status --short --branch`
- 生成 /確認 `session_id`

---

# Scope contract

本 round = **GPM sandbox only**

允許：
- GPM paper-facing report
- GPM → AML transfer plan
- 一個最小 simple validation
- sandbox artifact / state / bundle audit

禁止：
- 直接宣稱 faithful paper reproduction 完成
- 直接宣稱 FraudDetect mainline 已推進
- 直接修改 FraudDetect 主 repo pipeline
- 生成 FraudDetect ML-xxx 類正式主線票
- 把 GPM sandbox 的工具 / spec 假裝成 AML production evidence

---

# Ticket board (this round)

## TKT-901 — Professor report pack finalization
Priority: P0
Type: analysis
Owner: unclaimed

### Goal
把目前已有 evidence 整成可直接拿去跟教授報告的完整材料。

### Required output
建立：
- `docs/PAPER_REPORT_PACK.md`

並在 `review/REVIEW_BUNDLE.md` 新增：

## Professor Report Pack

至少包含：

### A. Paper one-paragraph summary
- GPM 核心方法一句話版
- 它與 message passing GNN 的差異

### B. Faithful reproduction boundary
- 現在能說什麼
- 不能說什麼
- faithful blocker 是什麼

### C. Reduced-config mechanism insight
- semantic only
- anonymous only
- both paths
- reduced patterns
- 哪個 component 對 AML 最值得關注

### D. Transfer takeaway
- 現在最值得搬回 AML 的 2~3 個元件
- 為什麼

### E. Caveat section
- reduced-config exploratory only
- not faithful transformer claim
- not AML production validation

### Close criteria
- 報告包可直接拿去講 paper
- evidence level 分級清楚
- ticket md + state + bundle 已更新

---

## TKT-902 — Transfer implementation proposal freeze
Priority: P0
Type: analysis
Owner: unclaimed

### Goal
把 GPM → FraudDetect 的導入方案正式凍結成具體 implementation plan。

### Required output
建立：
- `docs/TRANSFER_IMPLEMENTATION_PLAN.md`

並在 bundle 新增：

## Transfer Implementation Plan
| component | keep/drop/defer | AML form | required adapter | artifact target | success metric | first execution step |
|---|---|---|---|---|---|---|

至少覆蓋：
- random-walk tokenizer
- anonymous path statistics
- pattern frequency statistics
- pattern attention

必須明確回答：
- 第一個先做什麼
- 第二個如果第一個成功再做什麼
- 哪些明確 defer
- 哪些不值得現在做

### Close criteria
- 不是 ranking 而已，而是 implementation plan
- keep / defer / drop 都有明確理由
- ticket md + state + bundle 已更新

---

## TKT-903 — Simple validation of one transfer component
Priority: P0
Type: transfer
Owner: unclaimed

### Goal
對最優先的 GPM component 做一個**最小、可執行、可解釋的簡單驗證**。

### Important rule
不要假設 AML 真資料一定已準備好。  
你必須先檢查可用資料條件，然後選擇**最高可行等級**的 validation：

#### Tier 1
AML-compatible real graph slice
#### Tier 2
FraudDetect-compatible exported graph / adapter dry-run
#### Tier 3
Feature novelty / correlation gate only

你必須選擇當前可行的最高 tier，並明確說明為什麼。

### Required output
在 bundle 新增：

## Simple Transfer Validation
| chosen_component | validation_tier | input_data | artifact | metric_or_gate | result | verdict |
|---|---|---|---|---|---|---|

並補：

### Validation Rationale
- 為什麼選這個 component
- 為什麼選這個 tier
- 這個驗證支持了什麼、不支持什麼

### Close criteria
- 至少有一個真正執行過的 validation artifact
- 不是只有 spec / script
- verdict 明確：
  - positive signal
  - negative signal
  - inconclusive

---

## TKT-904 — Random engineering audit — sandbox truth consistency
Priority: P1
Type: audit
Owner: unclaimed

### Goal
抽查 GPM sandbox 的 artifact / state / bundle 是否一致，防止自我欺騙。

### Required output
在 bundle 新增：

## Random Engineering Audit — Sandbox Truth Consistency
| ticket_id | state_json | evidence_md | primary_artifact | bundle_claim | consistency_verdict |
|---|---|---|---|---|---|

至少抽查 5 張：
- TKT-802
- TKT-803
- TKT-804
- TKT-805
- TKT-901 / 902 / 903 其中至少一張本輪新票

### Close criteria
- 至少 5 張抽查完成
- 若有不一致，明確寫出
- ticket md + state + bundle 已更新

---

## TKT-000 — GPM round closeout
Priority: P0
Type: integrator
Owner: unclaimed
Depends on: all worker tickets

### Role
不是唯一 bundle writer。
只做：
- board sweep
- bundle consistency audit
- `### New` final gate
- 確認本 round 沒混入 FraudDetect mainline execution claim
- final push
- final closeout summary

### Close rule
不得 close 若：
- 有 worker ticket 沒更新 bundle
- 有 `OPEN / UNCLAIMED / STALE_CLAIM`
- 有 `new_item_unmapped_fingerprints`
- 有 evidence 與 state 不一致
- round summary 混入 FraudDetect mainline claim

### Required output
在 bundle 新增或更新：

## Ticket Board Summary
## Session Claim Map
## Open / Stale Ticket Check
## Push Summary
## Worker Ticket Snapshots
## New Inbox Audit
## Integrator Closeout
## Current Round Final State

其中 `Current Round Final State` 至少要有：
- all_worker_tickets_ready = yes/no
- all_push_done = yes/no
- final_board_clean = yes/no
- new_inbox_gate_passed = yes/no
- repo_scope = GPM sandbox only

---

# REVIEW_BUNDLE required sections for this round

下一版 `review/REVIEW_BUNDLE.md` 至少要新增或更新：

## GPM Round Contract
## Professor Report Pack
## Transfer Implementation Plan
## Simple Transfer Validation
## Random Engineering Audit — Sandbox Truth Consistency
## Current Round Final State

---

# Ticket execution protocol

1. 掃描 `review/tickets/state/*.json`
2. 找 `OPEN / UNCLAIMED`
3. claim exactly one ticket
4. 實作
5. 更新 ticket md
6. 更新 state json
7. 更新 `review/REVIEW_BUNDLE.md`
8. commit
9. push
10. 檢查 board
11. reread `### New`
12. 若還有 open/stale 且自己沒有 active ticket，繼續 claim

---

# Final response format

只回：

1. `session_id`
2. `claimed_ticket`
3. `repo_scope = GPM sandbox`
4. `current_status`
5. `files_touched`
6. `tests_run`
7. `artifact_paths`
8. `commit_sha`
9. `push_status`
10. `open_or_stale_ticket_check`
11. `next_claimed_ticket_or_integrator_decision`