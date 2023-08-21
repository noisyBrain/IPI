'''
Solicitar el ingreso de un número entero. Si es número ingresado es impar, 
se deberán imprimir los números correlativos desde el ingresado hasta el doble del mismo. 
Si el número ingresado es par, se deberán mostrar los números pares desde el ingresado 
hasta el doble del ingresado. Por ejemplo, si se ingresa un 8, se mostrará 8,
10, 12, 14, 16. Si se ingresa un 5, se mostrarán 5, 6, 7, 8, 9, 10.
'''

user_input = int(input("Ingresá un número distinto de 0: "))


def user_prompt(input_number: int):
    if is_even(input_number):
        return double_evens(input_number)
    else:
        return double_odds(input_number)


def is_even(input_number: int) -> str:
    if input_number % 2 == 0:
        return True


def double_of(number: int) -> tuple:
    double = number * 2
    numbers = []

    return (double, numbers)


def double_evens(even_number: int) -> list:
    double, numbers = double_of(even_number)

    for i in range(even_number, double + 1, 2):
        numbers.append(i)

    return numbers


def double_odds(odd_number: int) -> list:
    double, numbers = double_of(odd_number)

    for i in range(odd_number, double + 1):
        numbers.append(i)

    return numbers


print(user_prompt(user_input))
