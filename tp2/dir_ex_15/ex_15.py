'''
Escribí un programa que solicite al usuario el ingreso de un número 
mayor que 1 por teclado e informe si el número es primo o no.
Nota: los números primos son los que son divisible por si mismos
y por 1
'''

SHOULD_CONTINUE = True

while SHOULD_CONTINUE:
    input_number = int(input('Ingresá un número mayor a 1: '))

    if input_number == 1:
        print('Cerrando...')
        break

    IS_PRIME = True
    for i in range(2, input_number):
        if input_number % i == 0:
            IS_PRIME = False
            break

    if IS_PRIME:
        print(f'{input_number} es primo')

    else:
        print(f'{input_number} no es primo')
