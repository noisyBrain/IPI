from unittest.mock import patch

from dir_ex_13.refactor_ex_12 import (
    take_user_input,
    is_valid_number,
    count_zeros,
    sum_negatives,
    average_positives
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

def test_should_return_total_of_zeros():
    user_inputs = [0, -4, 2, 10, -9, 5, 0, -3, 8, -6, 1, 4, -8, 3, -7, 6, -2, 9, -5, -10]
    total_zeros = count_zeros(user_inputs)
    
    assert total_zeros == 2

def test_should_sum_negative_values():
    user_inputs = [0, -4, 2, 10, -9, 5, 0, -3, 8, -6, 1, 4, -8, 3, -7, 6, -2, 9, -5, -10]
    negative_sum = sum_negatives(user_inputs)

    assert negative_sum == -54

def test_should_return_average_of_positive_numbers():
    user_inputs = [0, -4, 2, 10, -9, 5, 0, -3, 8, -6, 1, 4, -8, 3, -7, 6, -2, 9, -5, -10]
    average = average_positives(user_inputs)

    assert average == 5.33

def test_should_return_zero_when_no_positive_numbers():
    user_inputs = [0, -4, -9, 0, -3, -6, -8, -7, -2, -5, -10]
    average = average_positives(user_inputs)

    assert average == 0
