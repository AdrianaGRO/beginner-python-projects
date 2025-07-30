"""
Project Name: List Sum Calculator

Description:
Create a function called sum_list() that takes a list of numbers as an argument and returns the sum of all the numbers in the list.

Task Instructions:
- Define a function named sum_list().
- The function should accept one parameter: a list of numbers.
- Calculate and return the sum of all numbers in the list.

Output Format:
- The function should return a single number (the sum of the list elements).

Example:
- Sample function call: sum_list([1, 2, 3, 4, 5])
- Expected result: 15

Testing Note:
- Use hard-coded values for testing your function (e.g., sum_list([1, 2, 3, 4, 5])).
- Do NOT use input() or print() in your solution file.
"""

def sum_list(numbers):
    return sum(numbers)     

print(sum_list([1, 2, 3, 4, 5]))
print(sum_list([10, 20, 30]))
print(sum_list([-1, -2, -3, -4, -5]))
print(sum_list([0, 0, 0, 0]))
print(sum_list([])) 