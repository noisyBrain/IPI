'''
Escribí un programa que solicite el ingreso de números enteros positivos.
Se deberán analizar los dígitos que componen a cada número ingresado informando:
    a) La cantidad de dígitos pares e impares que posee cada número ingresado.
    b) Cuántas veces apareció en total el dígito 5 en todos los números procesados.
La lectura de números finaliza al leer el valor -1
'''

SHOULD_CONTINUE = True
COUNT_FIVE = 0

while SHOULD_CONTINUE:
    int_number = int(input('Ingresá un número entero o -1 para cerrar: '))
    aux_to_analize = int_number

    if aux_to_analize == -1:
        print('Cerrando...')
        break

    while aux_to_analize > 0:

        analize_number = aux_to_analize % 10

        if analize_number % 2 == 0:
            print(f'el dígito {analize_number} del número {int_number} es par')

        else:
            print(f'el dígito {analize_number} del número {int_number} es impar')

        if analize_number == 5:
            COUNT_FIVE += 1

        aux_to_analize = aux_to_analize // 10

    print(f'\nEl número 5 apareció {COUNT_FIVE} veces\n')
    COUNT_FIVE = 0



