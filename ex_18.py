'''
Escribí un programa que solicite el ingreso de una cadena de caracteres e informe
qué vocales (mayúsculas y minúsculas indistintamente) aparecen en la cadena, sin repetir. 
Por ejemplo, para 'Programando' debería
informar: a, i, o.
'''

vowels = ["a", "e", "i", "o", "u"]

str_input = input('Ingresá el texto: ').strip()

spawned_vowels = []

for char in str_input:
    for vowel in vowels:
        if vowel == char and char not in spawned_vowels:
            spawned_vowels.append(char)

print(sorted(spawned_vowels))
