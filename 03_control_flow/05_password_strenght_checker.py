# 5. Password Strength Checker
# Create a program that checks password strength. Prompt the user to enter a password string.
# If the length is less than 8, print “Too short.”
# elif it contains no digits or no uppercase letters, print “Add numbers and capitals.”
# else, print “Strong password.”
# Use and/or to combine checks. Show a global variable like min_length = 8 in your output.

print("Welcome to Password Strength Checker")
password = input("Enter your password: ")
min_length = 8

if len(password) < min_length:
    print("Your password is too short")
    print(f"Your password requires {min_length} characters!")

elif password.islower() or password.isalpha():
    print("Add numbers and capitals")

else:
    print("Strong password")
    