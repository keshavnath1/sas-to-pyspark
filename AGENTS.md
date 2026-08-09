# Agent Build & Test Instructions

This file provides autonomous agents (like GitHub Copilot Agent Mode) with the commands needed to build, test, and validate the migration pipeline.

## Validation Engine
The validation engine compares the generated Python output against the SAS ground truth.

**To run validation:**
```bash
python3 stage5_validation/core/checkpoint_logger.py --config stage5_validation/core/validation_config.yaml
```

**To check diff results:**
```bash
cat stage5_validation/output/diff_report.json
```

## Python Environment
- Use `python3` for all scripts.
- No external dependencies are required beyond `numpy` and `pandas`.

## Directory Structure
- `data/` - Source SAS scripts and logs.
- `policy/` - The `policy_registry.yaml` mapping file.
- `.github/skills/` - The 6 agent skills.
- `.github/prompts/` - The slash command definitions.
