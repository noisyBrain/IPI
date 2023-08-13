'''
Solicitar al usuario que ingrese el día de la semana y la cantidad de artículos
comprados por un cliente en una tienda. Finalmente, imprimir “accede al descuento”
si el día es lunes y el cliente compró más de 3 artículos. En
caso contrario, no imprimir nada.
'''


def qualifies_for_discount(week_day: str, amount_articles) -> bool:
    qualify_for_discount = week_day.upper() == 'LUNES' and amount_articles > 3

    return info_message(qualify_for_discount)


def info_message(qualify_for_discount: bool) -> str:
    if (qualify_for_discount):
        return 'Accede al descuento'
