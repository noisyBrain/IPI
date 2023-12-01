'''
Escribí un programa que solicite ingresar una cantidad de números enteros a procesar. 
Luego, permitir al usuario ir ingresando uno a uno la cantidad pedida de números.
Una vez finalizado el ingreso, se deberá mostrar la suma total de los números ingresados.
'''


def prompt_total_numbers_to_process() -> int:
    total_numbers = int(input('Qué cantidad de números desea ingresar?\n'))
    return total_numbers


def prompt_number_to_process():
    number_to_process = int(input('Ingresá un número: '))

    return number_to_process


def sum_inputs() -> int:
    total_to_process = prompt_total_numbers_to_process()
    total_sum = 0

    for input_number in range(total_to_process):
        number_to_process = prompt_number_to_process()
        total_sum += number_to_process

    return total_sum
