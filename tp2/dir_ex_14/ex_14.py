'''
Escribí un programa que solicite el ingreso de números enteros positivos.
Se deberán analizar los dígitos que componen a cada número ingresado informando:
    a) La cantidad de dígitos pares e impares que posee cada número ingresado.
    b) Cuántas veces apareció en total el dígito 5 en todos los números procesados.
La lectura de números finaliza al leer el valor -1
'''

count_five = 0
input_number = int(input('Ingresá un número entero o -1 para cerrar: '))

while input_number != -1:

    aux = input_number

    while aux > 0:

        analize_number = aux % 10

        if analize_number % 2 == 0:
            print(f'el dígito {analize_number} del número {input_number} es par')

        else:
            print(f'el dígito {analize_number} del número {input_number} es impar')

        if analize_number == 5:
            count_five += 1

        aux = aux // 10

    print(f'\nEl número 5 apareció {count_five} veces\n')
    count_five = 0

    input_number = int(input('Ingresá un número entero o -1 para cerrar: '))
