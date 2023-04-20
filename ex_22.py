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

str_input = input('Ingresá una frase: ').strip().split()

for word in str_input:
    print(word)
