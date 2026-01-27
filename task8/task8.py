import csv

# ==========================
# TXT FILE HANDLING
# ==========================

try:
    # 1. Create and write to a text file
    with open("users.txt", "w") as file:
        file.write("Name: Jatin\n")
        file.write("Role: Python Intern\n")
        file.write("Location: Ahmedabad\n")

    # 2. Read text file contents
    print("Reading users.txt:")
    with open("users.txt", "r") as file:
        print(file.read())

    # 3. Append data to text file
    with open("users.txt", "a") as file:
        file.write("Status: Active\n")

except IOError as e:
    print("File error occurred:", e)


# ==========================
# CSV FILE HANDLING
# ==========================

try:
    # 4. Create CSV file and write multiple rows
    with open("students.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Roll No", "Name", "Marks"])
        writer.writerow([101, "Jatin", 92])
        writer.writerow([102, "Amit", 88])
        writer.writerow([103, "Neha", 79])

    # 5. Read CSV file
    print("\nReading students.csv:")
    with open("students.csv", "r") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            print(row)

except Exception as e:
    print("CSV error occurred:", e)
