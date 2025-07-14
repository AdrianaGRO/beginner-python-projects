# 5. Random Password Generator - Creates secure passwords using random character selection
# Uses random.choice() to pick characters from different lists (lowercase, uppercase, digits, symbols)
# Combines multiple character types to create a strong, randomized password
# Each character position is randomly selected from available character sets

# Project Instructions:
# 1. Prepare lists of characters: lowercase letters, uppercase letters, digits, and symbols
# 2. Ask the user for desired password length
# 3. For each character position, pick randomly from one of the lists
# 4. Combine into a string and display the generated password

import random


lowercase_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
uppercase_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

print("Welcome to the Random Password Generator!")
pass_length = int(input("Choose your password strength - enter length (maximum 15 characters): \n"))
all_characters = lowercase_letters + uppercase_letters + symbols + digits
password = ''

if pass_length >= 1:
    password += random.choice(all_characters)
if pass_length >= 2:
    password += random.choice(all_characters)
if pass_length >= 3:
    password += random.choice(all_characters)
if pass_length >= 4:
    password += random.choice(all_characters)
if pass_length >= 5:
        password += random.choice(all_characters)
if pass_length >= 6:
    password += random.choice(all_characters)
if pass_length >= 7:
    password += random.choice(all_characters)
if pass_length >= 8:
    password += random.choice(all_characters)
if pass_length >= 9:
    password += random.choice(all_characters)
if pass_length >= 10:
    password += random.choice(all_characters)
if pass_length >= 11:
    password += random.choice(all_characters)
if pass_length >= 12:
    password += random.choice(all_characters)
if pass_length >= 13:
    password += random.choice(all_characters)
if pass_length >= 14:
    password += random.choice(all_characters)
if pass_length == 15:
    password += random.choice(all_characters)


print(f"Success! Here is your random generated password: '{password}' - {len(password)} characters strong!.")

print("🎉 Thank you for choosing the Random Password Generator! Stay secure and have a great day!")