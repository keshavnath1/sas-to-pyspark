def create_synthetic_loan(overrides: dict = None) -> dict:
    """Generates a deterministic loan dict matching the LP Emulator schema."""
    base_loan = {
        "account_id": "TEST_001",
        "age": 12,
        "transaction_amt": 5000.0,
        "orig_date": "2020-01",
        "intercept": 1,
        "eltv_disp50": 0.0,
        "amort_oltv": 0.80
    }
    if overrides:
        base_loan.update(overrides)
    return base_loan
