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

words_in_input = 0
word = ''
longest_word = ''

while ' ' in str_input:
    word = word[:word.find(' ')]
    words_in_input += 1

    print(f'Longitud de {word}: {len(word)}')

    if len(word) > len(longest_word):
        longest_word = word

    str_input = str_input[str_input.find(' '):]
