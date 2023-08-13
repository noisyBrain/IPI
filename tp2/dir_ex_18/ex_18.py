'''
Escribí un programa que solicite el ingreso de una cadena de caracteres e informe
qué vocales (mayúsculas y minúsculas indistintamente) aparecen en la cadena, sin repetir. 
Por ejemplo, para 'Programando' debería
informar: a, o.
'''

str_input = input('Ingresá un texto: ').strip().lower()

VOWELS = 'aeiou'
VOWELS_APPEARED = ''

for letter in str_input:
    if letter in VOWELS and letter not in VOWELS_APPEARED:
        VOWELS_APPEARED += letter

print(f'Vocales en {str_input}: {VOWELS_APPEARED}')
