'''
Solicitar el ingreso de un número entero. Si es número ingresado es impar, 
se deberán imprimir los números correlativos desde el ingresado hasta el doble del mismo. 
Si el número ingresado es par, se deberán mostrar los números pares desde el ingresado 
hasta el doble del ingresado. Por ejemplo, si se ingresa un 8, se mostrará 8,
10, 12, 14, 16. Si se ingresa un 5, se mostrarán 5, 6, 7, 8, 9, 10.
'''

int_number = int(input('Ingresá un número entero: '))

even_number = int_number % 2 == 0
double = int_number * 2

if even_number:
    for number in range(int_number, double + 1, 2):
        print(number)
else:
    for number in range(int_number, double + 1):
        print(number)
