# 4. Password Generator - Create random passwords with user specifications
# Uses loops, lists, and random selection to generate secure passwords
# Demonstrates user input processing, list manipulation, and randomization
# Two versions: Easy (sequential) and Hard (randomized positions)

# Project Instructions:
# The program will ask:
# - How many letters would you like in your password?
# - How many symbols would you like?
# - How many numbers would you like?
# 
# Easy Version: Generate password in sequence (letters, then symbols, then numbers)
# Example: 4 letters, 2 symbols, 3 numbers = "fgdx$*924"
#
# Hard Version: Randomize the positions of letters, symbols, and numbers
# Example: Same input could produce "x$d24g*f9"

# Character sets for password generation:
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# TODO: Implement your solution here
# Start with the Easy Version, then challenge yourself with the Hard Version!

import random   
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("🔐 Welcome to PyPassword Generator - Your Security Guardian! 🔐")
print("Creating ultra-secure passwords to protect your digital life!")

nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Easy Version: Generate password in sequence       

password = ''

for num_letter in range(nr_letters):
    password += random.choice(letters)

for num_number in range(nr_numbers):
    password += random.choice(numbers)

for num_symbols in range(nr_symbols):
    password += random.choice(symbols)

print(f"✅ Success! Your bulletproof password is ready! {password} - {len(password)} characters strong! 💪")

# Hard Version: Randomize the positions of letters, symbols, and numbers

mixed_password = []
for num_letter in range(nr_letters):
    mixed_password.append(random.choice(letters))

for num_number in range(nr_numbers):
    mixed_password.append(random.choice(numbers))

for num_symbols in range(nr_symbols):
    mixed_password.append(random.choice(symbols))
random.shuffle(mixed_password)
final_password = ''.join(mixed_password)

print(f"💪 Stay safe online with your new secure password! {final_password}")
