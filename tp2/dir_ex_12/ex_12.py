'''
Escribí un programa que solicite el ingreso del monto de cada venta realizada 
en una tienda durante la última semana. Luego, se deberá mostrar el monto total de las ventas. 
Si se lee un monto negativo, se debe informar el problema sin interrumpir el ingreso de los datos.
La lectura de la información finaliza al leer un monto igual a cero
'''

total_sum = 0
monto = int(input("ingrese el monto de venta, ingrese 0 para finalizar: "))

while monto != 0:

    if monto < 0:
        print("ingreso un valor negativo")
        monto = int(input("ingrese el monto de venta, ingrese 0 para finalizar: "))
        continue

    else: 
        total_sum += monto
        monto = int(input("ingrese el monto de venta, ingrese 0 para finalizar: "))

print(f"\nLa suma total de las ventas es de: {total_sum}")
