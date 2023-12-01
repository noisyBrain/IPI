'''
Escribí un programa que solicite ingresar una cantidad de números enteros a procesar.
Luego, permitir al usuario ir ingresando uno a uno la cantidad pedida de números.
Una vez finalizado el ingreso, se deberá mostrar la suma total de los números ingresados.
'''

amount_of_numbers = int(input('Qué cantidad de números vas a querer ingresar?\n'))
result = 0

while amount_of_numbers > 0:
    numbers = int(input('Ingresá los números: '))
    result += numbers
    amount_of_numbers -= 1


print(result)
