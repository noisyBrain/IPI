'''
Escribí un programa que, dada una frase, imprima una a una las palabras que la contienen.
Se toma como precondición que cada palabra está separada por un espacio y que no existen
espacios al principio ni al final de la frase ingresada. Ejemplo: si la frase es
“aquí me pongo a cantar” se imprimirá:
aquí
me
pongo
a
cantar
'''

str_input = input('Ingresá una frase: ') + ' '
WORD = ' '

while ' ' in str_input:
    WORD = str_input[0:str_input.find(' ')]

    print(WORD)

    str_input = str_input[str_input.find(' ') + 1:]
