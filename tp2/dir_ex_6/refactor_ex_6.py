'''
Solicitar el ingreso de un número entero e imprimir los números correlativos
desde el ingresado hasta el doble del mismo. Por ejemplo, si se ingresa un 6,
se deberá mostrar: 6, 7, 8, 9, 10, 11, 12.
'''


def correlative_numbers(input_number: int) -> list:
    result = store_relative_numbers(input_number)

    return result


def store_relative_numbers(number: int) -> list:
    double = double_of_number(number)
    numbers = []

    for num in range(number, double + 1):
        numbers.append(num)

    return numbers


def double_of_number(number: int):
    return number * 2
