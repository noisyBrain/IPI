'''
Escribí un programa que solicite el ingreso de 20 números enteros que se encuentren entre -10 y 10
e imprima la sumatoria de los valores negativos, la cantidad de valores iguales a cero y
el promedio de los valores positivos. Se deberá pedir el reingreso de un número si éste
estuviera fuera del rango dado.
'''

RANGE = range(-10, 11)

should_continue = []

positive_numbers = []
negative_numbers = []
zero_input_times = []

POSITIVE_AVERAGE = 0
NEGATIVE_AVERAGE = 0

FINAL_POSITIVE_AVERAGE = 0
FINAL_NEGATIVE_AVERAGE = 0

while len(should_continue) < 20:
    new_number = int(input('Ingresá un número entero del -10 al 10: '))

    if new_number not in RANGE:
        print('El número ingresado debe ser entre -10 y 10!')
        continue

    if new_number == 0:
        zero_input_times.append(new_number)
        should_continue.append(new_number)
        continue

    if new_number > 0:
        positive_numbers.append(new_number)
        should_continue.append(new_number)

    else:
        negative_numbers.append(new_number)
        should_continue.append(new_number)

if len(positive_numbers) > 0:
    for num in positive_numbers:
        POSITIVE_AVERAGE += num

    FINAL_POSITIVE_AVERAGE = POSITIVE_AVERAGE / len(positive_numbers)


if len(negative_numbers) > 0:
    for num in negative_numbers:
        NEGATIVE_AVERAGE += num

    FINAL_NEGATIVE_AVERAGE = NEGATIVE_AVERAGE / len(negative_numbers)

print(f'''
El promedio de los números positivos ingresados es: {FINAL_POSITIVE_AVERAGE}
El promedio de los números negativos es: {FINAL_NEGATIVE_AVERAGE}
La cantidad de veces que se ingresó el 0 es de: {len(zero_input_times)}
''')
