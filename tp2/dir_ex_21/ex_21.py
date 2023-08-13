'''
Escribí un programa que solicite al usuario el título de su libro preferido. 
Imprimir luego 'Tu libro preferido es: [nombre del libro ingresado]' donde el nombre del
libro debe mostrarse con la primera letra en mayúscula y el resto en minúscula,
independientemente de cómo lo haya ingresado el usuario. Esto es, si el usuario ingresó 
“el SEÑOR DE LOS ANILLOS” se debería mostrar: “Tu libro preferido es: El señor de los anillos”.
Nota: no usar capitalize(). Se debe construir el algoritmo que convierta el string al formato
pedido.
'''

favourite_book = input('Ingresá tu libro favorito: ')
NORMALIZED_BOOK_NAME = ''

for char in favourite_book:
    if favourite_book.find(char) == 0:
        NORMALIZED_BOOK_NAME += char.upper()

    else:
        NORMALIZED_BOOK_NAME += char.lower()

print(f'Tu libro favorito es: {NORMALIZED_BOOK_NAME}')


# Easy way...
# favourite_book = input('Ingresá tu libro favorito: ').lower()
# favourite_book = favourite_book[0].upper() + favourite_book[1:0]
# print(favourite_book)
