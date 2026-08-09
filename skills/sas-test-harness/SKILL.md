---
name: sas-test-harness
description: Stage 4c. Use to generate deterministic synthetic data and autonomously run pytest test suites.
---

# Test Harness Agent (Stage 4c)

This skill generates deterministic synthetic loan data matching the target schema and runs pytest autonomously to verify correctness before SAS diff validation.

## When to use this skill
- After the Code Reviewer (Stage 4b) outputs `APPROVED`
- When asked to "run tests"

## Process
1. Read `boundary_cases.yaml` to identify edge cases for the module.
2. Use `synthetic_data_factory.py` to generate deterministic synthetic loan dicts.
3. Write a pytest file in the `tests/` directory using `test_template.py`.
   - You MUST include unit tests, boundary tests, and regression tests.
4. Use the `execute_command` tool to run `pytest tests/ -v --tb=short`.
5. Analyze the test output:
   - If `ALL PASS`: output success and instruct user to run `/run-repair` (Stage 5 SAS diff validation).
   - If `FAILURES`: extract the failing test and traceback, output `NEEDS REVISION`, and instruct the Code Generator to fix it (max 3 retries).
