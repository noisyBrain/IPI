'''
Escribí un programa que solicite el ingreso de números enteros, finalizando 
luego de leer un número para el cual la suma de sus dígitos sea menor que 10 
o mayor que 50. Informar la cantidad de números impares leídos.
Utilizá las funciones es_par(numero) y suma_digitos(numero) implementadas anteriormente.
'''

from functions import is_even, sum_digits

SHOULD_CONTINUE = True
ODD_NUMBERS = 0

while SHOULD_CONTINUE:
    input_number = int(input('Ingresá un número entero: '))

    check_number = sum_digits(input_number)

    should_not_continue = check_number > 50 or check_number < 10
    if should_not_continue:
        break

    if not is_even(input_number):
        ODD_NUMBERS += 1

print(f'La cantidad total de números impares ingresados es de: {ODD_NUMBERS}')
