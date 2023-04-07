'''
Solicitar el ingreso de un número entero e imprimir los números correlativos
desde el ingresado hasta el doble del mismo. Por ejemplo, si se ingresa un 6,
se deberá mostrar: 6, 7, 8, 9, 10, 11, 12.
'''
int_number = int(input('Ingresá un número entero: '))

double = int_number * 2

for num in range(int_number, double + 1):
    print(num)
