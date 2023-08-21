from dir_ex_7.refactor_ex_7 import user_output, double_of, is_even, double_odds, double_evens


def test_should_return_a_list_of_numbers():
    input_number = 13

    evens_list = double_evens(input_number)
    odds_list = double_odds(input_number)
    result = user_output(input_number)

    assert type(evens_list) == list
    assert type(odds_list) == list
    assert type(result) == list


def test_last_number_of_list_should_be_double_of_the_inpuut():
    input_number = 23

    result_list = user_output(input_number)
    result_last_number = len(result_list) - 1

    assert result_list[result_last_number] == 46


def test_is_even_should_return_boolean():
    input_number = 4

    result = is_even(input_number)

    assert type(result) == bool


def test_is_even_should_return_false():
    input_number = 4

    result = is_even(input_number)

    assert result is True


def test_double_of_should_retur_tuple():
    input_number = 16

    result = double_of(input_number)

    assert type(result) == tuple


def test_double_of_should_retur_double_of_number_and_empty_list():
    input_number = 16

    double, numbers = double_of(input_number)

    assert type(double) == int
    assert double == 32
    assert type(numbers) == list
    assert len(numbers) == 0
