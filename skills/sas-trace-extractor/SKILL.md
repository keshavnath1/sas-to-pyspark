---
name: sas-trace-extractor
description: Stage 1. Use to extract execution trace data from SAS scripts and logs into a structured JSON file.
---

# SAS Trace Extractor (Stage 1)

This skill extracts structural and execution metadata from `.sas` scripts and `.log` files to build the foundation for the migration pipeline.

## When to use this skill
- When starting a new migration
- When asked to "run Stage 1" or "extract trace"
- When you need to understand dataset lineage before mapping patterns

## Process
1. Use your `@workspace` capabilities to scan all `.sas` and `.log` files in the `data/` directory.
2. Extract the following from the `.sas` files:
   - `DATA` step input/output datasets
   - `RETAIN` variables and `BY` groups
   - `PROC SQL` tables and joins
   - `%macro` definitions and `%include` references
3. Extract the following from the `.log` files:
   - Row counts for all datasets
   - Execution runtimes
   - Warnings and errors
4. Output the extracted data as a structured JSON file directly to `stage1_extraction/output/execution_trace.json`.

## Expected Output Format
```json
{
  "scripts": {
    "filename.sas": {
      "macros_defined": [],
      "includes": [],
      "data_steps": [{"output": "WORK.A", "inputs": ["RAW.B"], "retain_vars": []}],
      "proc_sql": [{"output": "WORK.C", "joins": []}]
    }
  },
  "logs": {
    "filename.log": {
      "row_counts": {"WORK.A": 1000},
      "runtime_seconds": 45.2
    }
  }
}
```

## Next Step
Once the trace is saved, instruct the user to proceed to Stage 2 by running `/run-stage2`.
