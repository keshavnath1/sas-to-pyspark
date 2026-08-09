---
name: sas-validation-repair
description: Stage 5. Use to generate minimal code patches based on validation diff reports.
---

# Validation Repair Agent (Stage 5)

This skill acts as an Evaluator-Optimizer. It reads diff reports showing mismatches between the generated Python code and the SAS ground truth, and generates minimal patches to fix the bugs.

## When to use this skill
- When asked to "run repair" or "fix divergent rows"
- When the validation engine reports `divergent_rows > 0`

## Process
1. Read `stage5_validation/output/diff_report.json` and the failing Python file.
2. Analyze the diff:
   - Are there null handling mismatches?
   - Are there floating point precision differences?
   - Did a stateful variable fail to reset at a group boundary?
3. Generate a minimal patch using the structure in `templates/repair_patch_template.py`.
4. Explain exactly *why* the code failed and *how* the patch fixes it.

## Next Step
Instruct the user to apply the patch and re-run the validation engine until divergent rows reach 0.
