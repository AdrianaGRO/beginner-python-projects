# 6. Leap Year Validator
# Ask the user to input a year (integer). Determine if it's a leap year using these rules:
# LEAP YEAR RULES (in order of priority):
# 1. If divisible by 400 → leap year (e.g., 2000, 1600)
# 2. elif divisible by 100 → NOT leap year (e.g., 1900, 1800)
# 3. elif divisible by 4 → leap year (e.g., 2024, 2020)
# 4. else → NOT leap year (e.g., 2023, 2021)
# Print the result and include a global variable like calendar = "Gregorian" in the message Year Validator


print("Welcome to Leap Year Validator!")
year = int(input("Enter the year: "))
calendar = "Gregorian"
# Check leap year rules in order of priority:
# Rule 1: Every 400 years is always a leap year
# Rule 2: Every 100 years (except 400) is NOT a leap year  
# Rule 3: Every 4 years is a leap year
# Rule 4: All other years are NOT leap years
if year % 400 == 0:
    print(f"{year} is a leap year in the {calendar} calendar.")
elif year % 100 == 0:
    print(f"{year} is not a leap year in the {calendar} calendar.")
elif year % 4 == 0:
    print(f"{year} is a leap year in the {calendar} calendar.")
else:
    print(f"{year} is not a leap year in the {calendar} calendar.")