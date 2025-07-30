"""
Project Name: Palindrome Checker Function

Description:
Create a function called is_palindrome() that takes a single string argument and determines if it is a palindrome (the same forwards and backwards, case-insensitive). The function should return True if the input is a palindrome, and False otherwise.

Task Instructions:
- Define a function named is_palindrome().
- The function should accept one parameter: a string.
- Ignore case when checking for palindromes.
- Return True if the string is a palindrome, otherwise return False.

Output Format:
- The function should return a boolean value: True or False.

Example:
- Sample function call: is_palindrome('Racecar')
- Expected result: True

Testing Note:
- Use hard-coded values for testing your function (e.g., is_palindrome('Racecar')).
- Do NOT use input() or print() in your solution file.
"""
def is_palindrome(word):
    normalized_word = word.lower()
    return normalized_word == normalized_word[::-1]

print(is_palindrome("civic"))
print(is_palindrome("Adriana"))
print(is_palindrome("Racecar"))
print(is_palindrome("A man a plan a canal Panama"))

# text normalization
def normalize_text(text):
    return ''.join(char.lower() for char in text if char.isalnum())                             

print(is_palindrome(normalize_text("A man a plan a canal Panama")))
