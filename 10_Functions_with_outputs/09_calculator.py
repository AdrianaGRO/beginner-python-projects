"""
Project Name: Calculator Program

Description:
Build a calculator program that can perform addition, subtraction, multiplication, and division. The program should use functions for each operation and store them in a dictionary, allowing the user to select the operation by entering a symbol ("+", "-", "*", "/"). The calculator should allow the user to continue calculations with the previous result or start a new calculation.

Demo:
You can see a demo of the calculator here: https://appbrewery.github.io/python-day10-demo/

Key Concepts:
- Storing functions as variable values (function references)
- Using a dictionary to map operation symbols to functions
- Looping to allow continuous calculations

Example (Storing Functions as Variables):
def add(n1, n2):
    return n1 + n2

my_favourite_calculation = add
my_favourite_calculation(3, 5)  # Will return 8

Task Instructions:
- Write four functions: add, subtract, multiply, and divide. Each should take two numbers and return the result.
- Store these functions in a dictionary with keys: "+", "-", "*", "/".
- Use the dictionary to perform calculations based on the user's chosen operator.
- Demonstrate multiplying 4 * 8 using the dictionary.
- Implement a loop to allow the user to continue calculations with the previous result or start over.
- Display a logo from art.py at the start of the program.

Functionality:
1. Ask the user to type the first number.
2. Ask the user to type a mathematical operator ("+", "-", "*", "/").
3. Ask the user to type the second number.
4. Work out the result based on the chosen operator.
5. Ask if the user wants to continue with the previous result or start a new calculation.
6. If yes, use the previous result as the first number and repeat. If no, start over.

Hints:
- You can store function references in a dictionary as values.
- Use a loop to allow continuous calculations.
- Use art.py for a logo.

TO DO List:
1. Write the add, subtract, multiply, and divide functions.
2. Store the functions in a dictionary with operation symbols as keys.
3. Use the dictionary to perform calculations (e.g., multiply 4 * 8).
4. Implement user input for numbers and operator selection.
5. Add a loop to allow continued calculations with the previous result.
6. Add the logo from art.py at the start of the program.
7. Test all operations and looping functionality with hard-coded values (no input or print in the solution file).
"""

from art import logo

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def division(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": division
}


def calculator():
    print(logo)
    should_accumulate = True
    first_number = float(input("Add your first number:\n"))

    while should_accumulate:
        math_operator = input("Please select the operator ('+', '-', '*', '/')\n")
        second_number = float(input("Add your second number:\n"))

        result = operations[math_operator](first_number,second_number)
        print(f"{first_number} {math_operator} {second_number} = {result}")

        previous_result = input(f"Do you want to work with the previous result {result}? type yes or no:\n").lower()

        if previous_result == "yes":
            first_number = result
        else:
            should_accumulate = False
            print("\n" * 20)
            calculator()


calculator()

