---
agent: 'agent'
description: 'Run Stage 4b: Code review against 10 Golden Rules with Mermaid markdown report'
tools: ['vscode/readFile', 'vscode/writeFile']
---
Execute the instructions in `.github/skills/sas-code-reviewer/SKILL.md`.
Read the generated Python file, evaluate it against `review_checklist.md`, and write a review report to `docs/reviews/review_<module_name>.md`.
The report MUST include:
1. A violations table.
2. A Mermaid flowchart of the module composition chain.
3. A Mermaid flowchart of variable lineage (SAS to Python dict keys).
Output APPROVED or NEEDS REVISION.
