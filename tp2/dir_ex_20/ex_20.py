'''
Escribí un programa que solicite al usuario el ingreso de strings de longitud 1 (un solo carácter),
uno por vez. La repetición finalizará cuando se ingrese un string que no tenga longitud 1, o cuando
el string ingresado corresponda al dígito numérico 0. Al finalizar, mostrar el string completo que
se formó con todos los caracteres ingresados y qué porcentaje de caracteres del total fueron la
letra “z” (minúscula).
'''
# pylint: disable= missing-function-docstring
# def is_string_number(string):
#     try:
#         number = int(string)
#         return is_zero(number)
#
#     except ValueError:
#         return False
#
# def is_zero(number):
#     if number == 0:
#         return True
#
#     return False
#
# OUTPUT = ''
# SHOULD_CONTINUE = True
#
# while SHOULD_CONTINUE:
#     str_input = input('Ingresá una letra: ')
#     should_not_continue = len(str_input) > 1 or is_string_number(str_input)
#
#     if should_not_continue:
#         break
#
#     OUTPUT += str_input
#
# Z_AVERAGE = (OUTPUT.count('z') / len(OUTPUT)) * 100
#
# print(OUTPUT)
# print(f'\nEl promedio ingresado de "z" es de: {Z_AVERAGE}%')

char_input = input('Ingresá un caracter: ')

OUTPUT = ''
Z_AVERAGE = 0
SHOULD_CONTINUE = len(char_input) == 1 and char_input != '0'

while SHOULD_CONTINUE:
    OUTPUT += char_input

    if char_input == 'z':
        Z_AVERAGE += 1

    char_input = input('Ingresá otro caracter: ')

Z_AVERAGE = (OUTPUT.count('z') / len(OUTPUT)) * 100

print(OUTPUT)
print(f'\nEl promedio ingresado de "z" es de: {Z_AVERAGE}%')
