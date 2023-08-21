from unittest.mock import patch

from dir_ex_8.refactor_ex_8 import (
    sum_inputs,
    prompt_total_numbers_to_process,
    prompt_number_to_process
)


@patch('builtins.input', side_effect=['5'])
def test_prompt_user_for_total_numbers_to_process(mock_input):
    total_count = prompt_total_numbers_to_process()

    assert total_count == 5


@patch('builtins.input', side_effect=['3'])
def test_prompt_user_for_single_number_to_process(mock_input):
    number_to_process = prompt_number_to_process()

    assert number_to_process == 3


# pylint: disable=line-too-long
@patch('dir_ex_8.refactor_ex_8.prompt_total_numbers_to_process', side_effect=[3])
@patch('dir_ex_8.refactor_ex_8.prompt_number_to_process', side_effect=[3, 4, 5])
def test_should_return_sum_of_inputs(mock_prompt_total_numbers_to_process, mock_prompt_number_to_process):
    number_to_process = sum_inputs()

    assert number_to_process == 12
