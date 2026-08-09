---
agent: 'agent'
description: 'Run Stage 4c: Generate pytest suite with synthetic data and run tests autonomously'
tools: ['vscode/readFile', 'vscode/writeFile', 'vscode/runCommand']
---
Execute the instructions in `.github/skills/sas-test-harness/SKILL.md`.
1. Read `boundary_cases.yaml` and generate synthetic loan dicts.
2. Write a pytest file in `tests/test_<module_name>.py`.
3. Run `pytest tests/ -v --tb=short` and analyze results.
Output ALL PASS or NEEDS REVISION with the failing test details.
