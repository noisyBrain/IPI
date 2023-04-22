'''
Escribí un programa que permita encriptar un texto dado por el usuario y lo imprima.
Para ello se utilizará un método muy antiguo, llamado “la cifra de césar”, 
que consiste en correr cada letra una determinada cantidad de lugares.
Por ejemplo, si corremos las letras 2 lugares, la palabra “hola” se transforma en “jqnc”.
Si el abecedario termina antes de poder correr la cantidad de lugares necesarios, 
se vuelve a comenzar desde la letra “a”.
Así, la palabra “extra” corrida 3 lugares se convierte en “hawud”.
La cantidad de lugares que se correrán las letras será dada por el usuario.
Pista: para sortear el obstáculo de que se “termine” el abecedario al intentar correr una letra,
podemos usar el siguiente cálculo matemático: (índice de la letra a correr+corrimiento)%27
(si utilizamos el alfabeto español de 27 letras). Si alguno de los caracteres en la frase
no es una letra, se la debe dejar como está, sin encriptar.
'''

str_to_encrypt = input('Ingresá un texto para que sea encriptado: ')
encrypt_level = int(input('Cuál es el número de lugares que se deberá correr el texto?\n'))

ALPHABET = 'abcdefghijklmnñopqrstuvwxyz'
ENCRYPTED_TEXT = ''

for letter in str_to_encrypt:

    LETTER_IN_ALPHABET = ALPHABET.find(letter)
    normalized_letter_in_alphabet = (LETTER_IN_ALPHABET+encrypt_level) % 27

    ENCRYPTED_TEXT += ALPHABET[normalized_letter_in_alphabet]

print(ENCRYPTED_TEXT)
