'''
Escribí un programa que solicite el ingreso de 20 números enteros que se encuentren entre -10 y 10
e imprima la sumatoria de los valores negativos, la cantidad de valores iguales a cero y
el promedio de los valores positivos. Se deberá pedir el reingreso de un número si éste
estuviera fuera del rango dado.
'''

def take_user_input() -> list:
    max_input = 20
    user_input = []

    for _ in range(max_input):
        number = int(input('Ingresá un valor entre -10 y 10: '))
        user_input.append(number)

    return user_input

def is_valid_number(num: int) -> bool:
    return num < 10 and num > -10

def count_zeros(numbers: list) -> int:
    total_zeros = 0

    for number in numbers:
        if number == 0:
            total_zeros += 1

    return total_zeros

def sum_negatives(numbers: list) -> int:
    total_sum = 0

    for num in numbers:
        if num < 0:
            total_sum += num

    return total_sum
