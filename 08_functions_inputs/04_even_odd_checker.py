"""
Even or Odd Checker

Task:
Create a function called is_even_or_odd() that checks if a number is even or odd.
- The function should take a single integer as an argument.
- Use the modulo operator (%) to check divisibility by 2.
- Output the result in the format:
  X is even.
  or
  X is odd.
  (where X is the input number)

Example:
If you call is_even_or_odd(7), the output should be:
7 is odd.

Note:
For testing, use hard-coded values instead of input().
"""

def is_even_or_odd(number):
    if number % 2 == 0:
        print(f"{number} is even.")
    else:
        print(f"{number} is odd.")


# Test cases
is_even_or_odd(5)
is_even_or_odd(10)
is_even_or_odd(-3)
is_even_or_odd(0)
