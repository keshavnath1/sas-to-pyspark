# SAS to PySpark Migration — Prompt Engineering Pipeline (v15)

This project converts legacy SAS code into the production **LP Emulator NumPy Inference Architecture** using a structured 8-step pipeline powered by GitHub Copilot Agent Skills.

---

## Before You Start — One-Time Setup (Do This First)

These three steps seed the pipeline with your team's actual production patterns. Without them, the Code Generator skill will use generic templates instead of your real author conventions.

### Step 1 — Generate `author_patterns.md`

Open your production LP Emulator codebase in VS Code. Open GitHub Copilot Chat in Agent Mode and paste **Prompt 1** from `pasted_content_12.txt`:

```
You are acting as a Principal Software Architect and Reverse Engineering Expert.
Analyze the entire workspace and identify the coding patterns...
```

Save the output as:
```
.github/skills/sas-code-generator/references/author_patterns.md
```

### Step 2 — Generate `performance_improvement_analysis.md`

In the same Copilot Agent session, paste **Prompt 3** from `pasted_content_12.txt`:

```
Analyze all files in this workspace.
Identify every performance improvement introduced by the author...
```

Save the output as:
```
.github/skills/sas-code-generator/references/performance_improvement_analysis.md
```

### Step 3 — Generate `copilot_generation_rules.md`

Paste **Prompt 2** from `pasted_content_12.txt`:

```
Using the previously generated architecture analysis:
Create a document named: copilot_generation_rules.md...
```

Save the output as:
```
.github/skills/sas-code-generator/references/copilot_generation_rules.md
```

### Step 4 — Extract the 4 Production Templates

Copy the following functions from your actual production `.py` files into the template stubs in `.github/skills/sas-code-generator/templates/`:

| Template file | Copy from production |
|---|---|
| `data_prep_template.py` | `make_loan_level_panel()` from `data_prep_lss.py` |
| `panel_template.py` | `build_*_panel()` from `d120_panel.py` or `severity_panel.py` |
| `scoring_template.py` | `score_data_linear()` from `severity_scoring.py` or `d120_scoring.py` |
| `composed_module.py` | `ComposedModule` class from `util.py` or `core.py` |

After these 4 steps, the `references/` folder should contain 3 files and the `templates/` folder should contain 4 files. The pipeline is now fully seeded.

---

## The 8-Step Pipeline

Run these slash commands in order inside GitHub Copilot Chat (Agent Mode):

### `/run-stage1` — Extract Execution Trace
Scans all `.sas` and `.log` files in `data/` and generates `stage1_extraction/output/execution_trace.json`.

**You provide:** Nothing. Copilot reads the workspace.
**You get:** `execution_trace.json` with all DATA steps, RETAIN vars, PROC SQL joins, row counts, and runtimes.

---

### `/run-stage2` — Map SAS Patterns to Module Types
Reads the trace and SAS files, builds a column dependency graph, and classifies every SAS block into one of 5 production module types.

**You provide:** Nothing. Copilot reads `execution_trace.json` and the `.sas` files.
**You get:** `policy/policy_registry.yaml` — each pattern tagged with `target_module_type` and `complexity`.

**Decision after this step:**
- If ALL patterns are LOW or MEDIUM → skip to `/run-stage4`
- If ANY pattern is HIGH → proceed to `/run-stage3`

---

### `/run-stage3` — Self-Consistency Classifier *(HIGH complexity only)*
Runs 5 independent internal evaluations for each HIGH complexity pattern and tallies a majority vote.

**You provide:** `policy/policy_registry.yaml` (already in workspace).
**You get:** A JSON tally with `ACCEPT` or `ESCALATE TO MCTS` per pattern.

**Decision after this step:**
- `ACCEPT` (4/5 or 5/5 vote) → proceed to `/run-stage4`
- `ESCALATE TO MCTS` (split vote) → proceed to `/run-mcts`

---

### `/run-mcts` — MCTS Fallback *(escalated patterns only)*
Runs a 4-step Monte Carlo Tree Search (Selection → Expansion → Simulation → Backpropagation) to resolve patterns that split the Self-Consistency vote.

**You provide:** Nothing extra. Copilot reads the registry.
**You get:** A final PySpark/NumPy method for the escalated pattern.

---

### `/run-stage4` — Generate Code
Generates production-ready NumPy inference code using the 10 Golden Rules and your production templates.

**You provide:** Nothing extra. Copilot reads the registry and templates.
**You get:** A Python module in `output/` matching the LP Emulator architecture, wrapped in `@checkpoint`.

---

### `/run-review` — Code Review + Mermaid Report
Reviews the generated code against all 10 Golden Rules and generates a Markdown audit report with Mermaid diagrams.

**You provide:** Nothing extra. Copilot reads the generated file.
**You get:** `docs/reviews/review_<module>.md` containing:
- A violations table (rule, line, issue, fix)
- A Module Composition Chain diagram
- A Variable Lineage diagram

**Decision after this step:**
- `APPROVED` → proceed to `/run-tests`
- `NEEDS REVISION` → Copilot sends violations back to `/run-stage4` automatically (max 2 retries)

---

### `/run-tests` — Synthetic Data + Pytest
Generates deterministic synthetic loan dicts, writes a pytest suite, and runs it autonomously.

**You provide:** Nothing extra. Copilot reads `boundary_cases.yaml` and the generated module.
**You get:** Pytest results — `ALL PASS` or `NEEDS REVISION` with the failing test and traceback.

**Decision after this step:**
- `ALL PASS` → proceed to `/run-repair`
- `NEEDS REVISION` → Copilot sends the failing test back to `/run-stage4` automatically (max 3 retries)

---

### `/run-repair` — SAS Diff Validation + Patch
Runs the validation engine to diff the generated output against the SAS ground truth. Generates a minimal patch if divergent rows are found.

**You provide:** Nothing extra. Copilot reads `diff_report.json`.
**You get:** A patch file and explanation. Loops until divergent rows reach 0.

---

## Self-Healing Loop Summary

| Gate | Max Retries | What happens on failure |
|---|---|---|
| Code Review (`/run-review`) | 2 | Violations sent back to `/run-stage4` |
| Test Harness (`/run-tests`) | 3 | Failing test + traceback sent back to `/run-stage4` |
| Validation Repair (`/run-repair`) | Until 0 divergent rows | Patch generated and re-run |

---

## The 10 Golden Rules

Every piece of generated code is checked against these rules at the review gate:

| Rule | Description |
|---|---|
| 1 | Feature engineering variable names are identical to SAS |
| 2 | Business formulas are mathematically identical to SAS |
| 3 | Model coefficients are loaded from YAML/CSV — never hardcoded |
| 4 | SAS DATA step loops are replaced with NumPy vector math |
| 5 | SAS BY group processing becomes a single loan dict through a composed chain |
| 6 | No intermediate persistence — all data passed in-memory |
| 7 | `pa_csv.CSVWriter` is used only once at the top-level orchestrator |
| 8 | SAS macros are translated to `ComposedModule` chains |
| 9 | Python dict keys match SAS variable names exactly |
| 10 | Output dict keys match SAS output column names exactly |

---

## Project Structure

```
.github/
  copilot-instructions.md          ← Orchestrator: 10 rules + routing logic
  agents.md                        ← Build/test/run commands for autonomous agents
  skills/
    sas-trace-extractor/           ← Stage 1
    sas-pattern-to-module-mapper/  ← Stage 2
    sas-self-consistency/          ← Stage 3
    sas-code-generator/            ← Stage 4
      templates/                   ← 4 production code templates (you fill these)
      references/                  ← 3 author pattern docs (you generate these)
    sas-code-reviewer/             ← Stage 4b: review + Mermaid report
    sas-test-harness/              ← Stage 4c: synthetic data + pytest
    sas-mcts-fallback/             ← MCTS fallback
    sas-validation-repair/         ← Stage 5
  prompts/
    run-stage1.prompt.md
    run-stage2.prompt.md
    run-stage3.prompt.md
    run-stage4.prompt.md
    run-review.prompt.md
    run-tests.prompt.md
    run-mcts.prompt.md
    run-repair.prompt.md
data/
  sas_scripts/                     ← Put your .sas files here
  sas_logs/                        ← Put your .log files here
policy/
  policy_registry.yaml             ← Generated by Stage 2
docs/
  reviews/                         ← Review reports generated by /run-review
tests/                             ← Pytest files generated by /run-tests
stage1_extraction/output/          ← execution_trace.json
stage5_validation/                 ← Validation engine + diff reports
```
