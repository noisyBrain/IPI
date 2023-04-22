'''
Escribí un programa que solicite el ingreso de 20 números enteros que se encuentren entre -10 y 10
e imprima la sumatoria de los valores negativos, la cantidad de valores iguales a cero y
el promedio de los valores positivos. Se deberá pedir el reingreso de un número si éste
estuviera fuera del rango dado.
'''

POSITIVE_VALUES = 0
POSITIVE_COUNTER = 0
NEGATIVE_VALUES = 0
ZERO_COUNTER = 0

TOTAL_NUMBERS = 0

while TOTAL_NUMBERS < 20:

    input_number = int(input('Ingresá 20 números enteros entre -10 y 10 (de a uno a la vez): '))

    if input_number not in range(-10, 11):
        print('Rango de número inválido! Intentá de vuelta...')
        continue

    if input_number == 0:
        ZERO_COUNTER += 1

    elif input_number < 1:
        NEGATIVE_VALUES += input_number

    else:
        POSITIVE_COUNTER += 1
        POSITIVE_VALUES += input_number


    TOTAL_NUMBERS += 1

print(f'''
La suma de los valores negativos es: {NEGATIVE_VALUES}.
El promedio de los valores positivos es: {POSITIVE_VALUES / POSITIVE_COUNTER}.
La cantidad de valores iguales a 0 es: {ZERO_COUNTER}.
''')
