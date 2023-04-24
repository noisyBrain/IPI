from functions import *

POSITIVE_EVENS = 0
EVENS = 0

while EVENS < 8:
    input_number = int(input('Ingresá un número par: '))

    if is_even(input_number):
        EVENS += 1

    if input_number > 0:
        POSITIVE_EVENS += 1

if POSITIVE_EVENS == 8:
    print('Todos los números ingresados fueron positivos')
