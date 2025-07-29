"""
Maximum of Three Numbers

Task:
Create a function called max_of_three() that returns the largest of three numbers.
- The function should take three numbers as arguments.
- Use conditional statements to compare the numbers.
- Output the result in the format:
  The largest number is X.
  (where X is the largest of the three)

Example:
If you call max_of_three(3, 7, 5), the output should be:
The largest number is 7.

Note:
For testing, use hard-coded values instead of input().
"""

def max_of_three(a, b, c):
    the_maximum_number = max(a, b, c)
    print(f"The largest number is: {the_maximum_number}")

max_of_three(10, 5, 3)