import logging

# 1. Configure logging
logging.basicConfig(
    filename="error.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def divide_numbers(a, b):
    """
    Function to divide two numbers with exception handling.
    """
    try:
        result = a / b

    except ZeroDivisionError:
        logging.error("Division by zero attempted")
        print("Error: Cannot divide by zero")

    except TypeError:
        logging.error("Invalid data type used for division")
        print("Error: Please provide numeric values")

    else:
        print("Division Result:", result)

    finally:
        print("Division operation completed\n")


def read_file(filename):
    """
    Function to simulate file-related runtime error.
    """
    try:
        with open(filename, "r") as file:
            print(file.read())

    except FileNotFoundError:
        logging.error(f"File not found: {filename}")
        print("Error: File does not exist")

    finally:
        print("File read attempt finished\n")


# ==========================
# MAIN PROGRAM
# ==========================

print("Exception Handling & Logging Demo\n")

# Simulating runtime errors
divide_numbers(10, 0)          # ZeroDivisionError
divide_numbers(10, "a")        # TypeError
divide_numbers(10, 2)          # Successful case

read_file("data.txt")          # FileNotFoundError
