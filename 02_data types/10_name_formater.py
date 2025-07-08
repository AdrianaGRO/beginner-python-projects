# 10. Name Formatter
# Write a program to format a user's full name.
# Prompt the user for their first and last names.
# Combine them into a full name with the first letter of each capitalized.
# Display the formatted full name.
# Print the data type of the full name.

print("Welcome to Name Formatter!")

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
full_name = first_name.capitalize() + ' ' + last_name.capitalize()
print(f"Your formatted name is: {full_name}")
print(f" Data type for full_name is: {type(full_name)}")