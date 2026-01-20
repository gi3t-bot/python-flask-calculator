import os

# ------------------------------------------------
# File path handling (IMPORTANT)
# ------------------------------------------------
BASE_DIR = os.path.dirname(__file__)
HISTORY_FILE = os.path.join(BASE_DIR, "history.txt")


# ------------------------------------------------
# History related functions
# ------------------------------------------------
def show_history():
    try:
        with open(HISTORY_FILE, "r") as file:
            data = file.read()

        if not data.strip():
            print("No history found!!!")
        else:
            print(data)

    except FileNotFoundError:
        print("No history found!!!")


def clear_history():
    with open(HISTORY_FILE, "w"):
        pass
    print("All history cleared.")


def saving_history(equation, result):
    with open(HISTORY_FILE, "a") as file:
        file.write(f"{equation} = {result}\n")


# ------------------------------------------------
# Core calculation logic
# ------------------------------------------------
def calculate(expression):
    """
    Performs calculation on expressions like:
    5+6 , 10-3 , 4*8 , 9/3
    """

    expression = expression.replace(" ", "")

    for op in ["+", "-", "*", "/"]:
        if op in expression:
            try:
                number1, number2 = expression.split(op)
                number1 = float(number1)
                number2 = float(number2)
            except ValueError:
                raise ValueError("Invalid numbers")

            if op == "+":
                return number1 + number2

            elif op == "-":
                return number1 - number2

            elif op == "*":
                return number1 * number2

            elif op == "/":
                if number2 == 0:
                    raise ZeroDivisionError
                return number1 / number2

    raise ValueError("Invalid expression. Use + - * / only.")


# ------------------------------------------------
# Flask-facing function
# ------------------------------------------------
def evaluate_and_save(expression):
    result = calculate(expression)
    saving_history(expression, result)
    return result


# ------------------------------------------------
# CLI helper functions
# ------------------------------------------------
def show_help():
    print("""
Commands:
  history         View calculation history
  clear           Clear saved history
  help            Show help
  exit            Exit program

Examples:
  5 + 6
  10 * 3
  8 / 2
""")


def main():
    print("Welcome to my Simple Calculator....")

    while True:
        user_input = input(
            "Enter calculation or command (history, clear, help, exit): "
        ).strip()

        if user_input == "exit":
            print("Exit Successful.")
            break

        elif user_input == "history":
            show_history()

        elif user_input == "clear":
            clear_history()

        elif user_input == "help":
            show_help()

        else:
            try:
                result = evaluate_and_save(user_input)
                print(f"Result = {result}")

            except ZeroDivisionError:
                print("Cannot divide by zero")

            except ValueError as e:
                print(e)


# ------------------------------------------------
# Entry point
# ------------------------------------------------
if __name__ == "__main__":
    main()
