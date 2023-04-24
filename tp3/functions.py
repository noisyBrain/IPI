'''
almacenará todas las funciones usadas en los demás archivos
'''

# pylint: disable= missing-function-docstring
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
