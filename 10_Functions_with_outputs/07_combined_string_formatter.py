"""
Project Name: Combined String Formatter

Description:
Create two functions: double_text() and to_title_case(). Use them together to process a string by first doubling it and then converting it to Title Case. The final function should return the processed string.

Task Instructions:
- Define a function named double_text() that takes a string and returns it repeated twice.
- Define a function named to_title_case() that takes a string and returns it in Title Case.
- Demonstrate how to use these functions together by passing the output of double_text() into to_title_case().
- Return the final processed string.

Output Format:
- The function should return a single string (the doubled and title-cased text).

Example:
- Sample function call: to_title_case(double_text('hello'))
- Expected result: 'Hellohello'

Testing Note:
- Use hard-coded values for testing your function (e.g., to_title_case(double_text('hello'))).
- Do NOT use input() or print() in your solution file.
"""
def double_text(text):
     return text * 2

def to_title_case(text):
     return text.title()

print(double_text(to_title_case(" hello  world")))
