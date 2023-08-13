'''
Escribí un programa que, dada una frase, la muestre completamente en mayúsculas,
únicamente si hay al menos 2 letras mayúsculas en los primeros 4 caracteres de la frase.
Precondición: los primeros 4 caracteres serán siempre letras.
'''

str_input = input('Ingresá un texto: ')

MAYUS_LETTERS = ''

for char in str_input[0:4]:
    if char == char.upper():
        MAYUS_LETTERS += char

if len(MAYUS_LETTERS) >= 2:
    str_input = str_input.upper()

print(str_input)
