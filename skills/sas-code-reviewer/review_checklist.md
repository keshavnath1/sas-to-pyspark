# Code Review Checklist (The 10 Golden Rules)

| Rule | Description | What to check |
|---|---|---|
| 1 | Feature engineering | Are derived variable names exactly the same as SAS? |
| 2 | Business formulas | Is the math identical? No rounding or approximation? |
| 3 | Model coefficients | Are betas loaded from config, not hardcoded? |
| 4 | Execution engine | Is it NumPy/Python loops? NO Spark DataFrames allowed. |
| 5 | Loan-level flow | Does the function accept a single `loan_dict`? |
| 6 | No persistence | Are there any `df.write` or `to_csv` calls? (Should be NONE) |
| 7 | Single write | Is `pa_csv.CSVWriter` only used at the top-level orchestrator? |
| 8 | Module composition | Are macros translated to `ComposedModule` chains? |
| 9 | Variable names | Do Python dict keys match SAS variable names exactly? |
| 10 | Output schema | Do the output dict keys match the SAS output columns? |
