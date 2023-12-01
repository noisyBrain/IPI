'''
Modificar el programa anterior para que, si se ingresa un número negativo,
no se sume pero continúe con el proceso.
Finalmente, mostrar por separado la suma de los números positivos pares e
impares ingresados.
'''


def total_numbers_to_process():
    amount_of_numbers = int(input('Qué cantidad de números vas a querer ingresar? '))
    return amount_of_numbers


def number_to_process():
    number_to_process = int(input('Ingresá el número a procesar: '))
    return number_to_process


def sum_inputs():
    total_inputs = total_numbers_to_process()
    total_sum = 0

    for i in range(total_inputs):
        number = number_to_process()
        total_sum += number

    return total_sum
