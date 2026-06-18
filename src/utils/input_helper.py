def read_text(message: str) -> str:
    # Lê um texto digitado pelo usuário e remove espaços desnecessários.
    value = input(message).strip()

    while value == "":
        print("This field cannot be empty.")
        value = input(message).strip()

    return value


def read_int(message: str) -> int:
    # Lê um número inteiro com validação para evitar erro no programa.
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("Please enter a valid integer number.")