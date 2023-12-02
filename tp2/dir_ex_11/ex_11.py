'''
Escribí un programa con el cual se procesarán las notas de un final de la materia.
Para esto, se solicitará el ingreso del número de alumno y la nota recibida,
hasta que se ingrese un número de alumno igual a cero, en cuyo caso se deberá imprimir en pantalla
la leyenda 'Aprobados: ' y la cantidad de aprobados junto con la leyenda 'Desaprobados: '
y la cantidad de desaprobados. Se deberá tener en cuenta que se aprueba con una nota mayor a 4.
'''

print('''
Bienvenidos a la base de datos de la unnoba!

Ingresá el número de alumno y luego su nota
Ingresá 0 para ver el listado de aprobados y desaprobados
''')

students: list = []
should_continue = True

while should_continue:
    student_number = int(input('Ingresá el número del alumno: '))

    iterable = (i for i, obj in enumerate(students) if obj.get('student_number') == student_number)
    not_found = next(iterable, None)

    if student_number == 0:
        should_continue = False
        break

    if not_found is None:
        calification = int(input('Ingresá su calificación: '))
        students.append({'student_number': student_number, 'calification': calification})

    else:
        print('Este usuario ya tiene calificación')


approved = []
disapproved = []

for student in students:
    if student.get('calification') >= 4:
        approved.append(student)

    else:
        disapproved.append(student)

print(f'''
    Acá está la lista de aprobados y desaprobados:
    Aprobados: {approved}
    Desaprobados: {disapproved}
''')
