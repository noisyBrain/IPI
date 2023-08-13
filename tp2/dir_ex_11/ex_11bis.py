'''
Escribí un programa con el cual se procesarán las notas de un final de la materia.
Para esto, se solicitará el ingreso del número de alumno y la nota recibida,
hasta que se ingrese un número de alumno igual a cero, en cuyo caso se deberá imprimir en pantalla
la leyenda 'Aprobados: ' y la cantidad de aprobados junto con la leyenda 'Desaprobados: '
y la cantidad de desaprobados. Se deberá tener en cuenta que se aprueba con una nota mayor a 4.
'''

APPROVED = 0
DISAPPROVED = 0

CONDITION = True

while CONDITION:
    student = int(input('Ingrese el número de alumno: '))
    calification = int(input('Ingrese su calificación: '))

    if student < 0:
        CONDITION = False

    if calification >= 4:
        APPROVED += 1
    else:
        DISAPPROVED += 1


print(f'''
cantidad de aprobados: {APPROVED};
cantidad de desaprobados: {DISAPPROVED}
''')
