# Simple Calculator in Python

# Function to perform arithmetic operations
def calculator():
    try:
        # Take user input for numbers
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        # Show available operations
        print("\nChoose operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)\n")

        # Take user choice
        choice = input("Enter choice (1/2/3/4): ")

        # Perform operation based on choice
        if choice == '1':
            print(f"Result: {num1} + {num2} = {num1 + num2}")
        elif choice == '2':
            print(f"Result: {num1} - {num2} = {num1 - num2}")
        elif choice == '3':
            print(f"Result: {num1} * {num2} = {num1 * num2}")
        elif choice == '4':
            try:
                print(f"Result: {num1} / {num2} = {num1 / num2}")
            except ZeroDivisionError:
                print("Error: Division by zero is not allowed.")
        else:
            print("Invalid choice! Please select 1, 2, 3, or 4.")

    except ValueError:
        # Handles non-numeric input
        print("Error: Please enter valid numbers.")

# Run the calculator
calculator()
