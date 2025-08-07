# 09_Debugging Palindrome Checker
# - Read the code in exercise.py
# - Spot the problems 🐞.
# - Modify the code to fix the program so it works as expected.
# A palindrome is a word that reads the same forwards and backwards.
# Example: 'level' is a palindrome, 'hello' is not.

# def is_palindrome(word):
#     if word == word.reverse():
#         return True
#     else:
#         return False


def is_palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False

print(is_palindrome("level"))  # True
print(is_palindrome("hello"))  # False
print(is_palindrome("racecar"))  # True
print(is_palindrome("python"))  # False