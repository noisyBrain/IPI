'''
Escribí un programa que solicite el ingreso de una cadena de texto e informe:
a) La cantidad de palabras que posee la cadena.
b) La cantidad de caracteres que posee cada palabra.
c) La palabra más larga que contiene la cadena.
Nota: cada palabra estará separada por un espacio en blanco 
(puede haber espacios al comienzo y al final de la
cadena).
'''

str_input = input('Ingresá un texto para analizar: ')
separated_words = str_input.split()
words_in_input = len(separated_words)

LONGEST_WORD = ''

print(f'La cadena "{str_input}" tiene {words_in_input} palabras\n')

for word in separated_words:
    if len(word) > len(LONGEST_WORD):
        LONGEST_WORD = word

    print(f'La palabra "{word}" tiene: {len(word)} letras\n')

print(f'La palabra más larga de "{str_input}" es "{LONGEST_WORD}"\n')
