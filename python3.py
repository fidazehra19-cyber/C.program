 calculator():
    """Perform a basic arithmetic operation on two numbers."""
    first_number = int(input("Enter first number: "))
    second_number = int(input("Enter second number: "))
    operator = input("Choose an operator (+, -, *, /, //, %): ")

    if operator == "+":
        print(f"Addition: {first_number + second_number}")
    elif operator == "-":
        print(f"Subtraction: {first_number - second_number}")
    elif operator == "*":
        print(f"Multiplication: {first_number * second_number}")
    elif operator == "/":
        print(f"Division: {first_number / second_number}")
    elif operator == "//":
        print(f"Floor division: {first_number // second_number}")
    elif operator == "%":
        print(f"Modulo: {first_number % second_number}")
    else:
        print("Invalid operator. Try one of: +, -, *, /, //, %")

