"""
Palindrome Checker

Task:
Create a function called is_palindrome() that checks if a word or phrase is a palindrome.
- The function should take a string as an argument.
- Ignore case and non-alphanumeric characters.
- Output the result in the format:
  'X' is a palindrome.
  or
  'X' is not a palindrome.
  (where X is the input string)

Example:
If you call is_palindrome("Racecar"), the output should be:
'Racecar' is a palindrome.

Note:
For testing, use hard-coded values instead of input().
"""
def is_palindrome(word):
    cleaned = ''. join(char.lower() for char in word if char.isalnum())
    
    if cleaned == cleaned[::-1]:
        print(f"'{word}' is a palindrome.")
    else:
        print(f"'{word}' is not a palindrome.")

is_palindrome("Racecar")
is_palindrome("Hello")
is_palindrome("A man, a plan, a canal: Panama")
is_palindrome("No 'x' in Nixon")
is_palindrome("Was it a car or a cat I saw?")
is_palindrome("12321")
is_palindrome("12345")
is_palindrome("Able was I ere I saw Elba")
is_palindrome("Madam, in Eden, I'm Adam")