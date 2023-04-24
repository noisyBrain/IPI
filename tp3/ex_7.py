'''
Implementá la función maximo(num_1, num_2) que calcule y retorne el máximo entre 
num_1 y num_2, ambos positivos.
Luego, usá esa función para implementar un programa que solicite la lectura de 5
números e informe el máximo número leído
'''

from functions import max_number

input_number = int(input('Ingresá un número entero: '))

SHOULD_CONTINUE = 1
MAX_NUMBER = 0

while SHOULD_CONTINUE < 5:
    second_input_number = int(input('Ingresá otro número entero: '))

    if SHOULD_CONTINUE <= 1:
        MAX_NUMBER = max_number(input_number, second_input_number)

    else:
        MAX_NUMBER = max_number(MAX_NUMBER, second_input_number)

    SHOULD_CONTINUE += 1

print(f'El máximo número ingresado fue: {MAX_NUMBER}')
