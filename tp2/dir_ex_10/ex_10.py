'''
Calcular e imprimir la suma de los primeros 25 números de la sucesión de
Fibonacci. La sucesión comienza con los números 0 y 1 y, a partir de estos,
cada elemento es la suma de los dos números anteriores en la secuencia:
Ejemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55…
'''

previous = 0
two_previous = 0
current = 1

print(previous)
print(current)

i = 0
while i <= 25:
    next = current + previous
    print(next)

    two_previous = previous
    previous = current
    current = next

    i += 1
