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
