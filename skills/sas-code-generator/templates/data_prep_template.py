# Stateless Feature Engineering Pattern
def make_loan_level_panel(loan_data: dict, cpi_dict: dict) -> dict:
    panel = loan_data.copy()
    # Derived variables (Rule 1)
    panel['age_d120_12'] = max(panel['age'] - 12, 0)
    # CPI lookup (Rule 2)
    panel['cpi_factor'] = cpi_dict.get(panel['orig_date'], 1.0)
    return panel
