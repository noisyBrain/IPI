'''
Escribí un programa que solicite al usuario el ingreso de un número 
mayor que 1 por teclado e informe si el número es primo o no.
Nota: los números primos son los que son divisible por si mismos
y por 1
'''

SHOULD_CONTINUE = True

while SHOULD_CONTINUE:
    odd_number = int(input('Ingresá un número mayor a 1: '))

    if odd_number == 1:
        print('Cerrando...')
        break

    IS_ODD = True
    for i in range(2, odd_number):
        if odd_number % i == 0:
            IS_ODD = False
            break

    if IS_ODD:
        print(f'{odd_number} es primo')

    else:
        print(f'{odd_number} no es primo')
