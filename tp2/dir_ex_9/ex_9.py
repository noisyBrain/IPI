'''
Modificar el programa anterior para que, si se ingresa un número negativo, 
no se sume pero continúe con el proceso. 
Finalmente, mostrar por separado la suma de los números positivos pares e impares ingresados.
'''
amount_of_numbers = int(input('Qué cantidad de números vas a querer ingresar? '))

EVEN_NUMBER_RESULT = 0
ODD_NUMBER_RESULT = 0

while amount_of_numbers > 0:
    number = int(input('Ingresá los números: '))
    if number < 0:
        amount_of_numbers -= 1

    if number % 2 == 0:
        EVEN_NUMBER_RESULT += number

    else:
        ODD_NUMBER_RESULT += number

    amount_of_numbers -= 1


print(f'Even number result: {EVEN_NUMBER_RESULT}\nOdd number result: {ODD_NUMBER_RESULT}')
