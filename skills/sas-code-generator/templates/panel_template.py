# Stateful Accumulation Pattern (SAS RETAIN)
def build_d120_panel(loan_history: list) -> list:
    panel_history = []
    balance = 0.0 # RETAIN initialization
    for month_data in loan_history:
        current = month_data.copy()
        # Accumulation logic (Rule 2)
        balance = balance + current.get('transaction_amt', 0.0)
        current['running_balance'] = balance
        panel_history.append(current)
    return panel_history
