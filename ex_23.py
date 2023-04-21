'''
Escribí un programa que, dada una frase, la muestre completamente en mayúsculas,
únicamente si hay al menos 2 letras mayúsculas en los primeros 4 caracteres de la frase.
Precondición: los primeros 4 caracteres serán siempre letras.
'''

str_input = input('Ingresá un texto: ')

ALPHABET = 'ABCDEFGJIJKLMÑOPQRSTUVWQYZ'
MAYUS_LETTERS = ''

for index, input_char in enumerate(str_input):
    accepted_range = 0 <= index <= 4

    if accepted_range and input_char in ALPHABET :
        MAYUS_LETTERS += input_char


if len(MAYUS_LETTERS) >=2:
    str_input = str_input.upper()

print(str_input)
