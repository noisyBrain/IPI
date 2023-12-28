from unittest.mock import patch

from dir_ex_13.refactor_ex_12 import (
    take_user_input
)

@patch('builtins.input', side_effect=['5'])
def test_should_take_user_input(mock_input):
    user_input = take_user_input()

    assert user_input == 5
