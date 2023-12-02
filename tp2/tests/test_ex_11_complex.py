'''
- tener una función que sea el "punto de entrada" del programa ✅
- tener una función que tome un alumno y su calificación ✅
- tener una función que valide si el alumno ya existe en la lista
- tener una función que valide el número de alumno ✅
- tener una función que valide la calificación ✅
- tener una función que imprima el resultado
'''

from unittest.mock import patch

from dir_ex_11.refactor_ex_11 import (
    bootstrap,
    is_valid_mark,
    is_valid_student,
    take_student_info,
)

@patch('builtins.input', side_effect=['1', '10'])
def test_should_take_student_information(mock_input):
    student_number, mark = take_student_info()

    assert student_number == 1
    assert mark == 10

def test_should_fail_for_invalid_student():
    invalid_student_number = -1
    is_valid = is_valid_student(invalid_student_number)

    assert not is_valid

def test_should_fail_for_invalid_mark():
    invalid_mark = -4
    is_valid = is_valid_mark(invalid_mark)

    assert not is_valid

# TODO: add validations
@patch('builtins.input', side_effect=['1', '10', '2', '8', '0', '3'])
def test_should_return_list_of_students_with_marks(mock_input):
    students_list = bootstrap()

    assert type(students_list) is list
