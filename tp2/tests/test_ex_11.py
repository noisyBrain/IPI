from unittest.mock import patch

from dir_ex_11.refactor_ex_11bis import (
    take_student_number,
    take_student_mark,
    classify_student_marks
)

@patch('builtins.input', side_effect=['1'])
def test_should_take_student_number(mock_input):
    student = take_student_number()

    assert student == 1

@patch('builtins.input', side_effect=['10'])
def test_should_take_student_mark(mock_input):
    mark = take_student_mark()

    assert mark == 10

@patch('builtins.input', side_effect=[1, 10, 2, 4, 3, 7, 0])
def test_should_classify_student_marks(mock_input):
    (approved, disapproved) = classify_student_marks()

    assert approved == 2
    assert disapproved == 1
