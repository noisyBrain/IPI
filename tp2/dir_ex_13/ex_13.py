'''
Escribí un programa que solicite el ingreso de 20 números enteros que se encuentren entre -10 y 10
e imprima la sumatoria de los valores negativos, la cantidad de valores iguales a cero y
el promedio de los valores positivos. Se deberá pedir el reingreso de un número si éste
estuviera fuera del rango dado.
'''

positive_values = 0
positive_counter = 0
negative_values = 0
zero_counter = 0

total_numbers = 0

while total_numbers < 20:

    input_number = int(input('Ingresá 20 números enteros entre -10 y 10 (de a uno a la vez): '))

    if input_number not in range(-10, 11):
        print('Rango de número inválido! Intentá de vuelta...')
        continue

    if input_number == 0:
        zero_counter += 1

    elif input_number < 1:
        negative_values += input_number

    else:
        positive_counter += 1
        positive_values += input_number

    total_numbers += 1

print(f'''
La suma de los valores negativos es: {negative_values}.
El promedio de los valores positivos es: {positive_values / positive_counter}.
La cantidad de valores iguales a 0 es: {zero_counter}.
''')
