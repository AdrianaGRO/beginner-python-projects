"""
Sum of a List

Task:
Create a function called sum_list() that returns the sum of all numbers in a list.
- The function should take a list of numbers as an argument.
- Use a loop or the built-in sum() function to calculate the total.
- Output the result in the format:
  The sum of the list is X.
  (where X is the total sum)

Example:
If you call sum_list([1, 2, 3, 4]), the output should be:
The sum of the list is 10.

Note:
For testing, use hard-coded values instead of input().
"""

def sum_list(numbers):
    balance = 0
    for num in numbers:
        balance += num
    print(f"The sum of the list is {balance}")

sum_list([1,2,3,4])

