'''
Escribí un programa con el cual se procesarán las notas de un final de la materia.
Para esto, se solicitará el ingreso del número de alumno y la nota recibida,
hasta que se ingrese un número de alumno igual a cero, en cuyo caso se deberá imprimir en pantalla
la leyenda 'Aprobados: ' y la cantidad de aprobados junto con la leyenda 'Desaprobados: '
y la cantidad de desaprobados. Se deberá tener en cuenta que se aprueba con una nota mayor a 4.
'''

approved = 0
disapproved = 0

student = int(input('Ingrese el número de alumno: '))

while student > 0:
    calification = int(input('Ingrese su calificación: '))

    if calification >= 4:
        approved += 1
    else:
        disapproved += 1

    student = int(input('Ingrese el número de otro alumno: '))


print(f'''
cantidad de aprobados: {approved};
cantidad de desaprobados: {disapproved}
''')
