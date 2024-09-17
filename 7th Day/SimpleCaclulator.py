import art


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculator():
    """
    Will take 2 input and will choose the operation for simple calculator
    :return: will display result base on desired operation
    """
    print(art.logo)

    result_choice = True
    num1 = float(input("What is the first number?: "))
    while result_choice:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What is the next number?: "))

        num1 = operations[operation_symbol](num1, num2)

        choice = input(f"Type 'y' to continue calculating with {num1}, or type 'n' to start a new calculation: ")
        if choice.lower() == "n":
            result_choice = False
            print("\n" * 20)
            calculator()


calculator()
