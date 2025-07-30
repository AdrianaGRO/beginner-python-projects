"""
Project Name: Maximum of Three Numbers

Description:
Create a function called max_of_three() that takes three numerical arguments and returns the largest of the three numbers.

Task Instructions:
- Define a function named max_of_three().
- The function should accept three parameters: num1, num2, and num3.
- Determine and return the largest of the three numbers.

Output Format:
- The function should return a single number (the maximum of the three inputs).

Example:
- Sample function call: max_of_three(5, 12, 7)
- Expected result: 12

Testing Note:
- Use hard-coded values for testing your function (e.g., max_of_three(5, 12, 7)).
- Do NOT use input() or print() in your solution file.
"""


def max_of_three(num1, num2, num3):
    return max(num1, num2, num3)    

print(max_of_three(5, 12, 7))
print(max_of_three(10, 20, 30))
print(max_of_three(-5, -12, -7))
print(max_of_three(0, 0, 0))    