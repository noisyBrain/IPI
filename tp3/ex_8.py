'''
Implementá las funciones usuario(nombre) y contrasenia_por_defecto(dni). La primera función deberá recibir
como parámetro una cadena con el nombre completo de un usuario inscripto en el sistema Guaraní y retornar el
nombre de usuario para ingresar en la plataforma UNNOBA Virtual, que es el resultado de concatenar nombres y
apellidos sin espacios ni comas y en minúsculas. La segunda función deberá recibir un DNI (como número entero)
y retornar una cadena con los últimos 4 dígitos del DNI.
Nota: El formato del nombre en el sistema Guaraní es 'APELLIDO, NOMBRE' y usuario('GARCÍA, MARÍA VERÓNICA')
debería retornar 'mariaveronicagarcia'.
'''

from functions import user, default_password

username = input('Ingresá tu nombre completo: ')
dni = int(input('Ingresá tu número de DNI: '))

print(f'Nombre de usuario: {user(username)}')
print(f'Contraseña: {default_password(dni)}')

