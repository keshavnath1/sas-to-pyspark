import pytest
from synthetic_data_factory import create_synthetic_loan
# from module_under_test import function_under_test

def test_normal_case():
    loan = create_synthetic_loan()
    # result = function_under_test(loan)
    # assert result['expected_key'] == expected_value

def test_boundary_first_month():
    loan = create_synthetic_loan({"age": 0})
    # result = function_under_test(loan)
    # assert result['balance'] == 0.0  # RETAIN reset check
