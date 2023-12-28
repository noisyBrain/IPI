from unittest.mock import patch

from dir_ex_13.refactor_ex_12 import (
    take_user_input,
    is_valid_number,
    sum_zeros
)

@patch('builtins.input', side_effect=['7', '-4', '2', '10', '-9', '5', '0', '-3', '8', '-6', '1', '4', '-8', '3', '-7', '6', '-2', '9', '-5', '-10'])
def test_should_take_user_input(mock_input):
    user_input = take_user_input()

    assert type(user_input) is list
    assert len(user_input) == 20
    assert user_input[0] == 7

def test_should_return_false_when_number_is_invalid():
    assert is_valid_number(-12) == False
    assert is_valid_number(20) == False

def test_should_return_true_when_number_is_valid():
    assert is_valid_number(-8) == True
    assert is_valid_number(5) == True

def test_should_return_sum_of_zeros():
    user_inputs = [0, -4, 2, 10, -9, 5, 0, -3, 8, -6, 1, 4, -8, 3, -7, 6, -2, 9, -5, -10]
    total_zeros = sum_zeros(user_inputs)
    
    assert total_zeros == 2
