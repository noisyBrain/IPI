from unittest.mock import patch

from dir_ex_13.refactor_ex_12 import (
    take_user_input,
    is_valid_number
)

@patch('builtins.input', side_effect=['5'])
def test_should_take_user_input(mock_input):
    user_input = take_user_input()

    assert user_input == 5

def test_should_return_false_when_number_is_invalid():
    assert is_valid_number(-12) == False
    assert is_valid_number(20) == False

def test_should_return_true_when_number_is_valid():
    assert is_valid_number(-8) == True
    assert is_valid_number(5) == True
