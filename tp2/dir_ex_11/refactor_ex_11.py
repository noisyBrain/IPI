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

def is_valid_student(student_number: int) -> bool:
    return student_number > 0

def is_valid_mark(mark: int) -> bool:
    return mark >= 1 and mark <= 10

def take_student_info():
    student_number = int(input('Ingresá el número del alumno: '))
    mark = int(input('Ingresá la calificación del alumno: '))

    return (student_number, mark)

def bootstrap() -> list:
    students_list: list = []
    (student_number, mark) = take_student_info()

    while student_number > 0:
        students_list.append({ 'student_number': student_number, 'mark': mark })

        (student_number, mark) = take_student_info()

    return students_list
