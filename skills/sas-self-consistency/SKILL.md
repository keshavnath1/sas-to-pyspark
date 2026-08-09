---
name: sas-self-consistency
description: Stage 3. Use to classify ambiguous HIGH complexity SAS patterns via a 5-run majority vote.
---

# Self-Consistency Classifier (Stage 3)

This skill resolves ambiguity for HIGH complexity patterns (like complex RETAIN loops) by running 5 independent internal classifications and tallying a majority vote before committing to a PySpark/NumPy approach.

## When to use this skill
- When asked to "run Stage 3" or "classify pattern"
- When `policy_registry.yaml` contains patterns flagged as HIGH complexity

## Process
1. Read `policy/policy_registry.yaml`.
2. For each HIGH complexity pattern, extract the `sas_code_block`.
3. Run 5 independent internal evaluations to determine the exact PySpark/NumPy implementation strategy (e.g., `stateful_mapPartitions` vs `window_function_lag`).
4. Tally the votes.
5. Apply the decision rule:
   - **4/5 or 5/5 majority:** Output `ACCEPT` and the winning pattern.
   - **3/5 or lower:** Output `ESCALATE TO MCTS`.
6. Save the result as a JSON file.

## Output Requirements
Output MUST match the structure shown in [sc_result_accept.json](examples/sc_result_accept.json).

## Next Step
- If the decision is `ACCEPT`, instruct the user to run `/run-stage4` (Code Generation).
- If the decision is `ESCALATE TO MCTS`, instruct the user to run `/run-mcts` (MCTS Fallback).
