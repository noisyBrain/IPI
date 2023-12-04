from unittest.mock import patch

from dir_ex_12.refactor_ex_12 import (
    is_valid_input,
    take_user_input,
    total_sum
)

@patch('builtins.input', side_effect=['12'])
def test_should_return_user_input(mock_input):
    sells = take_user_input()

    assert sells == 12

@patch('builtins.input', side_effect=['-4'])
def test_should_return_false_when_is_invalid_input(mock_input):
    sells = take_user_input()

    is_valid = is_valid_input(sells)

    assert is_valid == False

@patch('builtins.input', side_effect=['3'])
def test_should_return_true_when_is_valid_input(mock_input):
    sells = take_user_input()

    is_valid = is_valid_input(sells)

    assert is_valid == True

@patch('builtins.input', side_effect=['3', '4', '-10', '-3', '10', '0'])
def test_should_return_total_sum_of_sells(mock_input):
    total = total_sum()

    assert total == 17
