def add(a, b=0):
    """
    Adds two numbers.
    Default value of b is 0.
    """
    return a + b


def subtract(a, b):
    """
    Subtracts second number from first number.
    """
    return a - b


def multiply(a, b=1):
    """
    Multiplies two numbers.
    Default value of b is 1.
    """
    return a * b


def divide(a, b):
    """
    Divides first number by second number.
    Handles division by zero.
    """
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b


def get_numbers():
    """
    Takes two numbers from user and returns them.
    """
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))
    return x, y


def main():
    """
    Main function to control calculator flow.
    """
    print("\n--- Modular Calculator ---")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Choose an operation (1-4): ")

    a, b = get_numbers()

    if choice == "1":
        result = add(a, b)
    elif choice == "2":
        result = subtract(a, b)
    elif choice == "3":
        result = multiply(a, b)
    elif choice == "4":
        result = divide(a, b)
    else:
        print("Invalid choice!")
        return

    print(f"Result: {result}")


if __name__ == "__main__":
    main()
