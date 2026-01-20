def calculate_grade(marks):
    """
    This function takes marks as input and returns grade and message.
    """

    # Handle invalid marks
    if marks < 0 or marks > 100:
        return "Invalid", "Marks should be between 0 and 100."

    # Grade logic
    if marks >= 90 and marks <= 100:
        return "A+", "Excellent performance!"
    
    elif marks >= 80:
        return "A", "Very good job!"
    
    elif marks >= 70:
        return "B", "Good performance."
    
    elif marks >= 60:
        return "C", "Average performance."
    
    elif marks >= 40:
        return "D", "You passed, but improvement needed."
    
    else:
        return "F", "Failed. Better luck next time."


def main():
    try:
        marks = float(input("Enter your marks (0-100): "))

        grade, message = calculate_grade(marks)

        print("\n--- Result ---")
        print(f"Marks : {marks}")
        print(f"Grade : {grade}")
        print(f"Message : {message}")

    except ValueError:
        print("Invalid input! Please enter numeric values only.")


if __name__ == "__main__":
    main()
