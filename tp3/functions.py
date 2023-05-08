def is_even(number):
    return number % 2 == 0

def sum_digits(number):
    aux = number
    sum_of_digits = 0

    while aux > 0:
        rest = aux % 10
        sum_of_digits += rest

        aux = aux // 10

    return sum_of_digits

def show_digits_sum(number):
    aux = number
    sum_of_digits = 0

    while aux > 0:
        rest = aux % 10
        sum_of_digits += rest

        aux = aux // 10

    print(sum_of_digits)

def max_number(number1, number2):
    if number1 > number2:
        return number1

    return number2

def user(name):
    username = ''

    for letter in name.lower():
        if letter == " " or letter == ",":
            continue
        else:
            username += letter

    return username

def default_password(dni):
    return dni % 10000
