# 5. Simple Interest Calculator
# Create a program to calculate simple interest.
# Ask the user for the principal amount, annual interest rate (as a percentage), and time in years.
# Use the formula: interest = (principal * rate * time) / 100.
# Display the interest rounded to 2 decimal places.
# Print the data type of the principal.

print("Welcome to the Simple Interest Calculator")
principal_amount = float(input("What is your principal amount? $ "))
interest_rate_percentage = float(input("What is your interest rate percent? % "))
years = float(input("What are the years that you want to cover the debt?"))

interest = round((principal_amount * interest_rate_percentage * years) / 100, 2)
print(f"The interest will be: ${interest:.2f}")
print(f"Data type for the principal amount is: {type(principal_amount)}")