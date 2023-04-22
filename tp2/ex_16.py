'''
Escribí un programa que solicite el ingreso de una cantidad indeterminada de números mayores que 1,
finalizando cuando se reciba un cero y mostrando la cantidad de números primos ingresados
'''

print('''
Ingresá números enteros mayores que 1 para tener un output de los números primos ingresados.
Ingresá 0 para salir del programa.
''')

SHOULD_CONTINUE = True
PRIME_NUMBERS = 0

while SHOULD_CONTINUE:
    int_number = int(input('Ingresá un número mayor que 0: '))

    if int_number == 0:
        print('Cerrando...')
        break

    IS_PRIME = True
    for num in range(2, int_number):
        if int_number % num == 0:
            IS_PRIME = False
            break

    if IS_PRIME:
        PRIME_NUMBERS += (int_number)

print(f'Esta es la cantidad de números primos que ingresaste: {PRIME_NUMBERS}')
