"""
Project Name: Title Case Converter Function

Description:
Create a function called to_title_case() that takes a single string argument and returns the string in Title Case (first letter of each word capitalized).

Task Instructions:
- Define a function named to_title_case().
- The function should accept one parameter: text (a string).
- Return the string converted to Title Case using the title() method.

Output Format:
- The function should return a single string (the title-cased text).

Example:
- Sample function call: to_title_case('hello world')
- Expected result: 'Hello World'

Testing Note:
- Use hard-coded values for testing your function (e.g., to_title_case('hello world')).
- Do NOT use input() or print() in your solution file.
"""

def to_title_case(text):
    return text.title()     

print(to_title_case('hello world'))