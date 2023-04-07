'''
Escribí un programa que solicite el ingreso del monto de cada venta realizada 
en una tienda durante la última semana. Luego, se deberá mostrar el monto total de las ventas. 
Si se lee un monto negativo, se debe informar el problema sin interrumpir el ingreso de los datos.
La lectura de la información finaliza al leer un monto igual a cero
'''
SHOULD_CONTINUE = True
SELLS = 0

while SHOULD_CONTINUE:
    new_incoming = int(input('Ingresá un monto: '))

    if new_incoming == 0:
        SHOULD_CONTINUE = False
        print(f'Lo que ganaste esta semana fue: {SELLS}')
        break

    if new_incoming < 0:
        print('El monto ingresado no puede ser negativo!')
        continue

    SELLS += new_incoming
