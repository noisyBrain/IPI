'''
Escribí un programa que solicite el ingreso del monto de cada venta realizada 
en una tienda durante la última semana. Luego, se deberá mostrar el monto total de las ventas. 
Si se lee un monto negativo, se debe informar el problema sin interrumpir el ingreso de los datos.
La lectura de la información finaliza al leer un monto igual a cero
'''

def take_user_input():
    sell = int(input("Ingresá el monto de venta [0 para salir]: "))
    return sell

def is_valid_input(number: int) -> bool:
    return number > 0

def total_sum():
    sell = take_user_input()
    total = 0

    while sell != 0:

        if (not is_valid_input(sell)):
            print("ingreso un valor negativo")
            sell = take_user_input()

            continue

        else: 
            total += sell
            sell = take_user_input()

    return total
