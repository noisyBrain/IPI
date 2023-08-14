from dir_ex_7.refactor_ex_7 import list_double_of_number


def test_should_return_a_list_of_numbers():
    input_number = 13
    is_list = list_double_of_number(input_number)

    assert type(is_list) == list


def test_last_number_of_list_should_be_double_of_the_inpuut():
    input_number = 23
    list_of_number = list_double_of_number(input_number)
    last_number_of_list = len(list_of_number) - 1

    assert list_of_number[last_number_of_list] == 46


def test_if_is_even_double_of_evens_should_be_called():
    input_number = 14
    list_of_evens = list_double_of_number(input_number)
    print(list_of_evens)

    assert list_of_evens == [14, 16, 18, 20, 22, 24, 26, 28]
