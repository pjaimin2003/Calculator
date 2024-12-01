def calculator():
    print("Welcome to the Simple Calculator!")
    print("Choose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    # Prompt the user for inputs
    try:
        operation = input("Enter the number corresponding to the operation (1/2/3/4): ")
        if operation not in ['1', '2', '3', '4']:
            raise ValueError("Invalid operation choice.")

        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        # Perform the calculation based on user choice
        if operation == '1':
            result = num1 + num2
            print(f"The result of addition is: {result}")
        elif operation == '2':
            result = num1 - num2
            print(f"The result of subtraction is: {result}")
        elif operation == '3':
            result = num1 * num2
            print(f"The result of multiplication is: {result}")
        elif operation == '4':
            if num2 == 0:
                raise ZeroDivisionError("Cannot divide by zero.")
            result = num1 / num2
            print(f"The result of division is: {result}")

    except ValueError as ve:
        print(f"Error: {ve}")
    except ZeroDivisionError as zde:
        print(f"Error: {zde}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    # Option to restart or exit
    again = input("Would you like to perform another calculation? (yes/no): ").strip().lower()
    if again == 'yes':
        calculator()
    else:
        print("Goodbye!")

# Run the calculator
calculator()
