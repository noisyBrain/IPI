'''
Escribí un programa que solicite el ingreso del monto de cada venta realizada 
en una tienda durante la última semana. Luego, se deberá mostrar el monto total de las ventas. 
Si se lee un monto negativo, se debe informar el problema sin interrumpir el ingreso de los datos.
La lectura de la información finaliza al leer un monto igual a cero
'''
SHOULD_CONTINUE = True
SELLS = 0

suma_monto = 0
monto = int(input("ingrese el monto de venta, ingrese 0 para finalizar"))

while monto != 0:

    if monto < 0:
        print("ingreso un valor negativo")
        monto = int(input("ingrese el monto de venta, ingrese 0 para finalizar"))
        continue

    elif monto > 0: 
        suma_monto += monto
        monto = int(input("ingrese el monto de venta, ingrese 0 para finalizar"))

print(suma_monto)