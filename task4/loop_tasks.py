import time

# 1. FOR LOOP: Print numbers from 1 to 100
print("1. Numbers from 1 to 100:")
for i in range(1, 101):
    print(i, end=" ")
print("\n")


# 2. WHILE LOOP: Countdown timer
print("2. Countdown Timer:")
count = 5
while count > 0:
    print(count)
    time.sleep(1)  # Simulates real countdown
    count -= 1
print("Countdown finished!\n")


# 3. BREAK and CONTINUE example
print("3. Break & Continue Example:")
for i in range(1, 11):
    if i == 5:
        continue  # Skip number 5
    if i == 8:
        break     # Stop loop at 8
    print(i)
print()


# 4. Iterate over string characters
print("4. Iterating Over String:")
name = "Python"
for char in name:
    print(char)
print()


# 5. Multiplication table
print("5. Multiplication Table of 5:")
num = 5
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
print()


# 6. RANGE with steps
print("6. Even Numbers from 2 to 20:")
for i in range(2, 21, 2):
    print(i, end=" ")
print("\n")


# 7. Loop with conditions (real-world logic)
print("7. Student Pass/Fail Check:")
marks_list = [95, 82, 40, 33, 67]

for marks in marks_list:
    if marks >= 40:
        print(f"Marks: {marks} → PASS")
    else:
        print(f"Marks: {marks} → FAIL")
print()


# 8. Real-World Example: Login Attempts
print("8. Login Attempts Simulation:")
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    password = input("Enter password: ")
    if password == "admin123":
        print("Login Successful!")
        break
    else:
        print("Incorrect password")
        attempts += 1
else:
    print("Account Locked!")
