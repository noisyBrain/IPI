'''
Solicitar el ingreso de un número entero. Si es número ingresado es impar, 
se deberán imprimir los números correlativos desde el ingresado hasta el doble del mismo. 
Si el número ingresado es par, se deberán mostrar los números pares desde el ingresado 
hasta el doble del ingresado. Por ejemplo, si se ingresa un 8, se mostrará 8,
10, 12, 14, 16. Si se ingresa un 5, se mostrarán 5, 6, 7, 8, 9, 10.
'''


def list_double_of_number(input_number: int) -> str:
    result = check_if_is_even(input_number)

    return result


def check_if_is_even(input_number: int) -> str:
    if input_number % 2 == 0:
        return double_of_evens(input_number)

    return correlative_odd_numbers(input_number)


def double_of_evens(number: int) -> list:
    return store_correlative_even_numbers(number)


def store_correlative_even_numbers(number: int) -> list:
    double = number * 2
    numbers = []

    for i in range(number, double + 1, 2):
        numbers.append(i)

    return numbers


def correlative_odd_numbers(number: int) -> list:
    return store_correlative_odd_numbers(number)


def store_correlative_odd_numbers(odd_number: int) -> list:
    double = odd_number * 2
    numbers = []

    for i in range(odd_number, double + 1):
        numbers.append(i)

    return numbers
