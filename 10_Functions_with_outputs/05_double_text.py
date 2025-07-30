"""
Project Name: String Doubler Function

Description:
Create a function called double_text() that takes a single string argument and returns the string repeated twice (concatenated).

Task Instructions:
- Define a function named double_text().
- The function should accept one parameter: text (a string).
- Return the string with its contents repeated twice (e.g., 'hello' becomes 'hellohello').

Output Format:
- The function should return a single string (the doubled text).

Example:
- Sample function call: double_text('hello')
- Expected result: 'hellohello'

Testing Note:
- Use hard-coded values for testing your function (e.g., double_text('hello')).
- Do NOT use input() or print() in your solution file.
"""

def double_text(text):
    return text * 2
print(double_text('hello'))
print(double_text('Python'))
print(double_text('Adriana'))
print(double_text('12345'))
print(double_text('!@#$%')) 