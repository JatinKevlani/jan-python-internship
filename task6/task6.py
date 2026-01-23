# ===============================
# LIST, TUPLE & SET DEMONSTRATION
# ===============================

# 1. LIST: Store student names
students = ["Jatin", "Amit", "Neha", "Priya", "Amit"]

print("Original Student List:")
print(students)


# 2. Add, Remove, Sort elements in list
students.append("Rohit")
students.remove("Neha")
students.sort()

print("\nUpdated Student List:")
for student in students:
    print(f"- {student}")


# 3. TUPLE: Fixed data (Immutable)
college_info = ("Government Polytechnic", "Computer Engineering", 2025)

print("\nCollege Info (Tuple):")
print(f"College: {college_info[0]}")
print(f"Branch: {college_info[1]}")
print(f"Passing Year: {college_info[2]}")

# Uncommenting below line will cause error (tuple is immutable)
# college_info[0] = "XYZ College"


# 4. Convert List to Set to remove duplicates
unique_students = set(students)

print("\nUnique Students (Set):")
print(unique_students)


# 5. SET OPERATIONS
set_a = {"Python", "Java", "C"}
set_b = {"Python", "C++", "JavaScript"}

print("\nSet Operations:")
print("Union:", set_a | set_b)
print("Intersection:", set_a & set_b)
print("Difference (A - B):", set_a - set_b)


# 6. Iterating over Set
print("\nIterating Over Skills Set:")
for skill in set_a:
    print(skill)


# 7. Mutable vs Immutable Comparison
print("\nMutable vs Immutable:")
print("List can be modified")
students[0] = "Kunal"
print("Modified List:", students)

print("Tuple cannot be modified")
print("Tuple:", college_info)
