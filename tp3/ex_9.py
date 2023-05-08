'''
Escribí un programa que solicite el ingreso de nombre completo y número de documento de estudiantes de la
UNNOBA. La carga de datos finaliza cuando se encuentre 'Juan' o 'María' en el campo nombre (estos casos no se
deben procesar). Para todos los datos ingresados, se deberá informar el nombre de usuario para ingresar a la
plataforma UNNOBA Virtual junto con la contraseña generada por defecto. Utilizá las funciones del ejercicio
anterior.
'''

from functions import user, default_password

username = input('Ingresá tu nombre completo: ')
dni = int(input('Ingresá tu número de DNI: '))

while 'juan' not in username.lower() and 'maría' not in username.lower():
    print(f'Nombre de usuario: {user(username)}')
    print(f'Contraseña: {default_password(dni)}')

    username = input('Ingresá tu nombre completo: ')
    dni = int(input('Ingresá tu número de DNI: '))
