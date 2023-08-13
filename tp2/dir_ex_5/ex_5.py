'''
Solicitar al usuario que ingrese el día de la semana y la cantidad de artículos
comprados por un cliente en una tienda. Finalmente, imprimir “accede al descuento”
si el día es lunes y el cliente compró más de 3 artículos. En
caso contrario, no imprimir nada.
'''

week_day = input('Ingresá el día de la semana: ')
amount_articles = int(input('Ingresá los articulos comprados: '))

AMOUNT_FOR_DISCOUNT = 3
DAY_OFF = 'LUNES'
access_to_discount = amount_articles > AMOUNT_FOR_DISCOUNT and week_day.upper() == DAY_OFF

if access_to_discount:
    print('Accede al descuento!')
