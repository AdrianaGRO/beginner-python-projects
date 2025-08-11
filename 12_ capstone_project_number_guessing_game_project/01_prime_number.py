"""
Project Name: Prime Number Checker

Description:
This project requires you to write a function that determines whether a given number is a prime number. A prime number is a number greater than 1 that is only divisible by 1 and itself. The function should return True if the number is prime, and False otherwise.

Task Instructions:
- Implement a function named is_prime().
- The function should take a single integer argument (number).
- The function should check if the number is a prime number.
- Return True if the number is prime, otherwise return False.

Output Format:
- The function should return a boolean value: True if the number is prime, False otherwise.

Example:
Input: 73
Output: True

Input: 75
Output: False

Sample Function Call and Expected Result:
>>> is_prime(73)
True
>>> is_prime(75)
False

Note:
- Do not use input() for user input. Use hard-coded values for testing your function.
- No code should be present in this file—only the specifications as comments.
"""

def is_prime(num):
    if num <=1:
        print(False)
    if num >= 1:
        for i in range(2, num):
            if num % i ==0:
                print(False)
                return False
        else:
             print(True)


is_prime(73)
is_prime(75)
is_prime(1)
is_prime(2)
is_prime(3)
is_prime(4)
is_prime(5) 
is_prime(6)
is_prime(7)
is_prime(8)
is_prime(9)