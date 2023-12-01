'''
Escribí un programa que solicite el ingreso de una cadena de texto e informe:
a) La cantidad de palabras que posee la cadena.
b) La cantidad de caracteres que posee cada palabra.
c) La palabra más larga que contiene la cadena.
Nota: cada palabra estará separada por un espacio en blanco
(puede haber espacios al comienzo y al final de la
cadena).
'''

str_input = input('Ingresá un texto para analizar: ').strip()

WORDS_IN_INPUT = 0
WORD = ''
LONGEST_WORD = ''

while ' ' in str_input:
    WORD = WORD[:WORD.find(' ')]
    WORDS_IN_INPUT += 1

    print(f'Longitud de {WORD}: {len(WORD)}')

    if len(WORD) > len(LONGEST_WORD):
        LONGEST_WORD = WORD
    
    str_input = str_input[str_input.find(' '):]
