---
name: sas-code-generator
description: Stage 4. Use to generate production-ready NumPy inference code matching the LP Emulator architecture.
---

# Code Generator (Stage 4)

This skill translates SAS code into the exact production NumPy inference pattern used by the LP Emulator architecture. It strictly enforces the 10 Author Pattern Rules.

## When to use this skill
- When asked to "run Stage 4" or "generate code"
- When a pattern has been mapped in Stage 2 and approved in Stage 3

## The 10 Author Pattern Rules
You MUST follow these rules, derived from `references/copilot_generation_rules.md`:
1. Feature engineering columns → keep exact same derived variable names.
2. Business formulas → keep exact same math.
3. Model coefficients → load from YAML/CSV, never hardcode.
4. Replace SAS DATA step loops → NumPy vector math / Python loop accumulation.
5. SAS BY group processing → single loan dict flowing through composed module chain.
6. SAS intermediate datasets → no persistence, pass in-memory.
7. SAS PROC EXPORT → single `pa_csv.CSVWriter` at the end.
8. SAS macro calls → `ComposedModule` chaining.
9. SAS variable names → Python dict keys with identical names.
10. SAS output columns → identical output schema.

## Process
1. Read the pattern from `policy_registry.yaml` and its `target_module_type`.
2. Review the corresponding template in the `templates/` directory:
   - `data_prep_template.py`
   - `panel_template.py`
   - `scoring_template.py`
   - `composed_module.py`
3. Generate 3 candidate implementations internally (Sequential Sampling).
4. Rank the candidates against the 10 Rules.
5. Output the winning candidate, wrapped in the `@checkpoint` decorator for validation.

## Next Step
Instruct the user to run the validation engine to diff the output against the SAS ground truth. If divergent rows > 0, instruct them to run `/run-repair`.
