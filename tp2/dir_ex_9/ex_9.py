'''
Modificar el programa anterior para que, si se ingresa un número negativo,
no se sume pero continúe con el proceso.
Finalmente, mostrar por separado la suma de los números positivos pares e
impares ingresados.
'''
amount_of_numbers = int(input('Qué cantidad de números vas a querer ingresar? '))

even_number_result = 0
odd_number_result = 0

while amount_of_numbers > 0:
    number = int(input('Ingresá los números: '))
    if number < 0:
        amount_of_numbers -= 1

    if number % 2 == 0:
        even_number_result += number

    else:
        odd_number_result += number

    amount_of_numbers -= 1


print(f'Even number result: {even_number_result}\nOdd number result: {odd_number_result}')
