'''
Escribí un programa que solicite el ingreso de 20 números enteros que se encuentren entre -10 y 10
e imprima la sumatoria de los valores negativos, la cantidad de valores iguales a cero y
el promedio de los valores positivos. Se deberá pedir el reingreso de un número si éste
estuviera fuera del rango dado.
'''

def take_user_input():
    user_input = int(input('Ingresá un valor entre -10 y 10: '))

    return user_input

def is_valid_number(num: int) -> bool:
    return num < 10 and num > -10

def sum_zeros(numbers: list) -> int:
    total_zeros = 0

    for number in numbers:
        if number == 0:
            total_zeros += 1

    return total_zeros
