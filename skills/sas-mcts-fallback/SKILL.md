---
name: sas-mcts-fallback
description: MCTS Fallback. Use to resolve highly ambiguous patterns that failed Self-Consistency voting.
---

# MCTS Fallback Loop

This skill executes a 4-step Monte Carlo Tree Search to resolve patterns that split the vote in Stage 3.

## When to use this skill
- When asked to "run MCTS" or "escalate"
- When Stage 3 outputs `ESCALATE TO MCTS`

## Process
Execute the following 4 steps sequentially:

1. **Selection:** Pick the most promising unexplored PySpark/NumPy approach for the SAS block.
2. **Expansion:** Write a candidate implementation.
3. **Simulation:** Mentally simulate running the candidate against the SAS ground truth. Predict if it will produce divergent rows.
4. **Backpropagation:**
   - If simulation predicts failure: score path LOW, backtrack to Step 1.
   - If simulation predicts success: output the final implementation.

## Next Step
Once a viable path is found, output the final code and instruct the user to proceed to validation.
