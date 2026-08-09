---
name: sas-code-reviewer
description: Stage 4b. Use to review generated Python code against the 10 Golden Rules and generate a Markdown audit report with Mermaid diagrams.
---

# Code Review Agent (Stage 4b)

This skill acts as a pre-test review gate. It ensures the generated code matches the production LP Emulator NumPy architecture before any tests are run.

## When to use this skill
- Immediately after Stage 4 code generation
- When asked to "run review"

## Process
1. Read the generated Python file.
2. Read `review_checklist.md` (the 10 Golden Rules).
3. Evaluate the code against every rule.
4. Generate the `review_report_<module>.md` file in the `docs/reviews/` directory.
   - You MUST include a Mermaid flowchart showing the module composition chain.
   - You MUST include a Mermaid flowchart showing variable lineage (SAS to Python dict keys).
5. If any rule is violated, output `NEEDS REVISION` and instruct the Code Generator to fix it (max 2 retries).
6. If all rules pass, output `APPROVED` and instruct the user to run `/run-tests`.
