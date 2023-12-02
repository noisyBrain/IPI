'''
Escribí un programa con el cual se procesarán las notas de un final de la materia.
Para esto, se solicitará el ingreso del número de alumno y la nota recibida,
hasta que se ingrese un número de alumno igual a cero, en cuyo caso se deberá imprimir en pantalla
la leyenda 'Aprobados: ' y la cantidad de aprobados junto con la leyenda 'Desaprobados: '
y la cantidad de desaprobados. Se deberá tener en cuenta que se aprueba con una nota mayor a 4.
'''

def take_student_number() -> int:
    student = int(input('Ingresá el número de alumno: '))

    return student

def take_student_mark() -> int:
    mark = int(input('Ingresá la calificación del alumno: '))

    return mark

def classify_student_marks() -> tuple:
    approved = 0
    disapproved = 0
    student = take_student_number()

    while student > 0:
        mark = take_student_mark()

        if mark > 4: approved += 1
        else: disapproved += 1

        student = take_student_number()

    return (approved, disapproved)
