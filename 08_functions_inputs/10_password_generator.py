"""
Password Generator

Task:
Create a function called generate_password() that generates and prints a random password.
- The function should take the desired password length as an argument.
- Use letters, digits, and punctuation.
- Output the result in the format:
  Your generated password is: X
  (where X is the generated password)

Example:
If you call generate_password(10), the output should be:
Your generated password is: aB3!xYz@1Q

Note:
For testing, use hard-coded values instead of input().
"""
import random
import string

all_characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','0', '1', '2', '3', '4', '5', '6', '7', '8', '9','!', '#', '$', '%', '&', '(', ')', '*', '+']

def generate_password(length):
    password = ''
    for num_letter in range (length):
        password += random.choice(all_characters)
    print(f"Your generated password is {password}")

generate_password(50)


