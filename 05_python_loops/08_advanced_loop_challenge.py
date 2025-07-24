# 8. Advanced Loop Challenge - Multiple loop techniques combined
# Combines various loop concepts into more complex scenarios
# Demonstrates nested loops, complex logic, and real-world applications
# Choose one or more challenges based on your interest level

# Challenge :

# OPTION A: Multiplication Table Generator
# Create a multiplication table (1-12) using nested loops
# Display in a formatted grid showing products

# OPTION B: Pattern Printer
# Create various patterns using loops:
# - Triangle patterns with stars
# - Number pyramids
# - Diamond shapes


import random

print("Welcome to the Advanced Loop Challenge!")
print("Choose your challenge from the options below:")
print("A: Multiplication Table Generator")
print("B: Pattern Printer")
     

choice = input("Enter your choice (A or B): ").upper()

if choice == 'A':
    print("Generating a multiplication table (1-12)...")
   
    for num_x in range(1, 13):
        print(f"Row {num_x}", end="")
        for num_y in range(1 ,13):
            multiply = num_x * num_y
            print(f" {multiply:4}", end=" ")
        print()

if choice == 'B':
    print("Creating various patterns using loops...")

    # Triangle
    for row in range(1,6):
        for star in range(row):
            print('*', end="")
    print()

    # Number pyramid
    for row in range(1,6):
        spaces = (" " * (5 - row))  # Centering the numbers
        numbers = ""
        for num in range(1, (2* row)):
            numbers += str(num)
        print(spaces + numbers)

    #Diamond
    for row in range(1,6):
        if row <= 3:
            spaces = " " * (3 - row)
            stars = "*" * (2 * row - 1)
            print(spaces + stars)   
        else:
            mirror_row = 6 - row
            spaces = " " * (3 - mirror_row)
            stars = "*" * (2 * mirror_row - 1)
            print(spaces + stars)