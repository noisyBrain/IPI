'''
Escribí un programa que solicite el ingreso de una cadena de caracteres e informe
qué vocales (mayúsculas y minúsculas indistintamente) aparecen en la cadena, sin repetir. 
Por ejemplo, para 'Programando' debería
informar: a, i, o.
'''

str_input = input('Ingresá un texto: ').strip()

VOWELS = 'aeiou'
VOWELS_APPEARED = ''

for letter in str_input:
    normalized_letter = letter.lower()

    if normalized_letter in VOWELS and normalized_letter not in VOWELS_APPEARED:
        VOWELS_APPEARED += normalized_letter

VOWELS_APPEARED = ''.join(sorted(VOWELS_APPEARED))

print(f'Vocales en {str_input}: {VOWELS_APPEARED}')
