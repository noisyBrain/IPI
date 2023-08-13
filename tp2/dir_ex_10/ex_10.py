'''
Calcular e imprimir la suma de los primeros 25 números de la sucesión de Fibonacci.
La sucesión comienza con los números 0 y 1 y, a partir de estos, cada elemento es
la suma de los dos números anteriores en la secuencia:
Ejemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55…
'''

PREVIOUS = 0
TWO_PREVIOUS = 0
CURRENT = 1

print(PREVIOUS)
print(CURRENT)

i = 0
while i <= 25:
    NEXT = CURRENT + PREVIOUS
    print(NEXT)

    TWO_PREVIOUS = PREVIOUS
    PREVIOUS = CURRENT
    CURRENT = NEXT

    i += 1
