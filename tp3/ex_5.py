from functions import show_digits_sum
# El problema con esta función es que no está retornado nada.

# Haciéndolo de la forma anterior, me arrojaría un "None".
# Si quisiera imprimir por pantalla el resultado, solamente debería
# invocar a la función directamente porque ya se encarga de imprimir por
# pantalla el resultado.

input_number = int(input('Ingresá un número entero: '))

show_digits_sum(input_number)
