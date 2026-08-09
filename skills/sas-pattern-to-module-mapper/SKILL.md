---
name: sas-pattern-to-module-mapper
description: Stage 2. Use to discover SAS patterns and map them to production NumPy module types (data_prep, panel, scoring, composed).
---

# SAS Pattern to Module Mapper (Stage 2)

This skill analyzes SAS code blocks and maps them to the specific production NumPy inference patterns used in the LP Emulator architecture.

## When to use this skill
- When asked to "run Stage 2" or "discover patterns"
- When you need to classify SAS blocks into target production modules

## The 5 Production Target Modules
Every SAS block must map to one of these:
1. `data_prep_lss`: Stateless feature engineering (simple DATA steps).
2. `panel`: Loan-level stateful accumulation (DATA steps with RETAIN + BY groups).
3. `scoring`: Beta load + loop accumulation + score generation (PROC SQL or complex DATA steps).
4. `composed`: Module composition chain (SAS macros orchestrating multiple steps).
5. `lss_flow`: Single write at the end (PROC EXPORT or final dataset).

## Process
1. Read the `.sas` file and the `execution_trace.json` generated in Stage 1.
2. Build a Column Dependency Graph in memory to understand variable lineage.
3. Identify distinct SAS code blocks.
4. For each block, determine its `target_module_type` based on the 5 categories above.
5. Determine complexity:
   - **LOW**: Simple `data_prep_lss` or `lss_flow`.
   - **HIGH**: Stateful `panel` accumulations, `scoring` loops, or `composed` macros.
6. Write the results to `policy/policy_registry.yaml`.

## Output Requirements
The output MUST be a valid YAML file matching the schema shown in [proc_sql_to_scoring.yaml](examples/proc_sql_to_scoring.yaml). It must include the exact `sas_code_block` and the assigned `target_module_type`.

## Next Step
- If ANY pattern is flagged as **HIGH** complexity, instruct the user to run `/run-stage3` (Self-Consistency).
- If ALL patterns are **LOW/MEDIUM**, instruct the user to skip to `/run-stage4` (Code Generation).
