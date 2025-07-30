"""
Project Name: Name Formatter Function

Description:
This project requires you to create a function called format_name() that takes two string arguments: f_name and l_name. The function should return the full name in Title Case (i.e., each name starts with a capital letter and the rest are lowercase), using the title() method.

Task Instructions:
- Define a function named format_name().
- The function should accept two parameters: f_name and l_name.
- Use the title() function to convert both parameters to Title Case.
- Return the formatted full name as a single string, with a space between the first and last names.

Output Format:
- The function should return a string in the format: 'First Last' (both names in Title Case).

Example:
- Sample function call: format_name('ada', 'lovelace')
- Expected result: 'Ada Lovelace'

Testing Note:
- Use hard-coded values for testing your function (e.g., format_name('ada', 'lovelace')).
- Do NOT use input() or print() in your solution file.
"""

def format_name(f_name, l_name):
    return f_name.title() + " " + l_name.title()

print(format_name("adriana","gropan"))