def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x / y

while True:
    print("Options: '+', '-', '*', '/'.")
    print("Or")
    print("Enter 'exit' to end the program")

    user_choice = input(": ")

    if user_choice == "exit":
        break

    if user_choice in ("+", "-", "*", "/"):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter valid numbers.")
            continue  # Restart the loop

        if user_choice == "+":
            print("Result:", add(num1, num2))
        elif user_choice == "-":
            print("Result:", subtract(num1, num2))
        elif user_choice == "*":
            print("Result:", multiply(num1, num2))
        elif user_choice == "/":
            print("Result:", divide(num1, num2))
    else:
        print("Invalid input. Please enter a valid operation ('+', '-', '*', '/', or 'exit').")
