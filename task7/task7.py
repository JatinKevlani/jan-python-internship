import json

# 1. Store student details using dictionary
students = {
    101: {"name": "Jatin", "branch": "CE", "marks": 92},
    102: {"name": "Amit", "branch": "IT", "marks": 85},
    103: {"name": "Neha", "branch": "ME", "marks": 78}
}

print("Original Student Records:")
for roll, details in students.items():
    print(f"Roll No: {roll}, Details: {details}")


# 2. Access keys and values
print("\nAccessing Individual Student:")
print("Student 101 Name:", students[101]["name"])


# 3. Update entry
students[102]["marks"] = 88

# 4. Delete entry
del students[103]

print("\nUpdated Student Records:")
for roll, details in students.items():
    print(f"Roll No: {roll}, Details: {details}")


# 5. Convert dictionary to JSON and save to file
with open("students.json", "w") as file:
    json.dump(students, file, indent=4)

print("\nStudent records saved to students.json")


# 6. Read JSON back into Python
with open("students.json", "r") as file:
    loaded_data = json.load(file)

print("\nData Loaded From JSON File:")
for roll, details in loaded_data.items():
    print(f"Roll No: {roll}")
    for key, value in details.items():
        print(f"  {key}: {value}")
