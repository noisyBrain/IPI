from dir_ex_6.refactor_ex_6 import correlative_numbers, double_of_number, store_relative_numbers


def test_double_of_number_should_return_double_of_input():
    input_number = 10
    result = double_of_number(input_number)

    assert result == 20


def test_store_relative_numbers_should_return_a_list_of_numbers():
    input_number = 10
    result = store_relative_numbers(input_number)

    assert type(result) == list


def test_store_relative_numbers_should_return_a_list_of_numbers_with_double_of_input():
    input_number = 3
    result = store_relative_numbers(input_number)
    last_number_list = len(result) - 1

    assert result[last_number_list] == 6


def test_correlative_numbers_should_return_a_list_with_correlative_numbers_of_input():
    input_number = 6
    expected_result = [6, 7, 8, 9, 10, 11, 12]

    result = correlative_numbers(input_number)

    assert result == expected_result
