from unittest.mock import patch

from dir_ex_9.refactor_ex_9 import (
    total_numbers_to_process,
    number_to_process
)


@patch('builtins.input', side_effect=['5'])
def test_prompt_user_for_negative_number(mock_input):
    total_to_process = total_numbers_to_process()

    assert total_to_process == 5


@patch('builtins.input', side_effect=['3'])
def test_prompt_user_for_single_input(mock_input):
    single_input_to_process = number_to_process()

    assert single_input_to_process == 3
