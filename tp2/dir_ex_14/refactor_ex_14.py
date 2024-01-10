def get_user_input() -> int:
    number = int(input('Ingresá un número entero o -1 para cerrar: '))

    return number

def analyze_digit(digit: int, original_number) -> str:
    if digit % 2 == 0:
        return f"El dígito {digit} del número {original_number} es par!"

    return f"El número {digit} del número {original_number} es impar!"

def count_digit_five(digit: int) -> int:
    if digit == 5:
        return 1

    return 0

def main():
    user_input = get_user_input()
    counter = 0

    while user_input != -1:
        aux = user_input

        while aux > 0:
            digit = user_input % 10
            print(analyze_digit(digit, user_input))
            counter += count_digit_five(digit)

        aux = aux // 10

    print(f"El número 5 apareció {counter} veces\n")

if __name__ == "__main__":
    main()
