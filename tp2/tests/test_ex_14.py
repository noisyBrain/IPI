from unittest.mock import patch
from dir_ex_14.refactor_ex_14 import (
    get_user_input,
    analyze_digit,
    count_digit_five
)

@patch('builtins.input', side_effect=['3'])
def test_should_return_a_number_from_input(mock_input):
    number = get_user_input()

    assert number == 3

def test_should_evaluate_number():
    result = analyze_digit(6, 126)

    assert result == "El dígito 6 del número 126 es par!"

def test_should_count_the_five_digit():
    total_of_fives = count_digit_five(5)

    assert total_of_fives == 1
