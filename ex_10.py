'''
Calcular e imprimir la suma de los primeros 25 números de la sucesión de Fibonacci.
La sucesión comienza con los números 0 y 1 y, a partir de estos, cada elemento es
la suma de los dos números anteriores en la secuencia:
Ejemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55…
'''

MAX_FIBO = 25
current_fibo = [0, 1]


for i in range(MAX_FIBO + 1):
    if i == 0:
        print(current_fibo[i])

    if i == 1:
        print(current_fibo[i])

    if i > 1:
        new_fibo = current_fibo[i - 1] + current_fibo[i - 2]
        current_fibo.append(new_fibo)
        print(current_fibo[len(current_fibo) - 1])
