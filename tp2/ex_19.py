'''
Escribí un programa que permita al usuario ingresar una frase y luego un carácter 
(string de longitud 1) y luego muestre la frase ingresada, pero con todas las ocurrencias
del carácter indicado por el usuario reemplazadas por “*”. 
Nota: no utilizar replace().
'''

str_input = input('Ingresá un texto: ').strip()
char_to_replace = input('Ingresá el caracter que querés reemplazar: ')

REPLACED = ''

for CHAR in str_input:
    if CHAR == char_to_replace:
        CHAR = "*"

    REPLACED += CHAR

print(REPLACED)
