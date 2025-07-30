"""
Project Name: Leap Year Checker

Description:
Write a function called is_leap_year() that determines whether a given year is a leap year. A leap year has 366 days, with an extra day in February. The function should return True if the year is a leap year, and False otherwise, following the leap year rules:
- Every year that is divisible by 4 is a leap year,
- Except every year that is evenly divisible by 100 is not a leap year,
- Unless the year is also divisible by 400, then it is a leap year.

Task Instructions:
- Define a function named is_leap_year().
- The function should accept one parameter: year (an integer).
- Apply the leap year rules to determine if the year is a leap year.
- Return True if the year is a leap year, otherwise return False.

Output Format:
- The function should return a boolean value: True or False.

Example:
- Sample function call: is_leap_year(2400)
- Expected result: True

- Sample function call: is_leap_year(1989)
- Expected result: False

Testing Note:
- Use hard-coded values for testing your function (e.g., is_leap_year(2400)).
- Do NOT use input() or print() in your solution file.

TO DO:
1. Define a function named is_leap_year that takes one argument (year).
2. Check if the year is divisible by 4. If not, return False.
3. If the year is divisible by 4, check if it is divisible by 100. If not, return True.
4. If the year is divisible by 100, check if it is also divisible by 400. If yes, return True; otherwise, return False.
5. Test your function with hard-coded values (e.g., is_leap_year(2400), is_leap_year(1989)).
"""

def is_leap_year(year):
    if year % 4 == 0 and year % 100 != 0:
        return True
    elif year % 400 == 0:
            return True
    else:
            return False


print(is_leap_year(2400))
print(is_leap_year(1989))   
print(is_leap_year(2000))
print(is_leap_year(2020))
print(is_leap_year(2021))
print(is_leap_year(1900))
print(is_leap_year(1600))
print(is_leap_year(2024))
print(is_leap_year(2023))           