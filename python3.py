 calculator():
    """Perform a basic arithmetic operation on two numbers."""
    first_number = int(input("Enter first number: "))
    second_number = int(input("Enter second number: "))
    operator = input("Choose an operator (+, -, *, /, //, %): ")

    if operator == "+":
        print("Addition: {first_number + second_number}")
    elif operator == "-":
        print("Subtraction: {first_number - second_number}")
    elif operator == "*":
        print("Multiplication: {first_number * second_number}")
    elif operator == "/":
        print("Division: {first_number / second_number}")
    elif operator == "//":
        print("Floor division: {first_number // second_number}")
    elif operator == "%":
        print("Modulo: {first_number % second_number}")
    else:
        print("Invalid operator. Try one of: +, -, *, /, //, %")

