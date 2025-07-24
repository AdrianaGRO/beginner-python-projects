# 🐍 Function Creator
# Today you will create essential utility functions to master Python function fundamentals!

# Instructions:
# Write a program that creates a collection of utility functions.
# The goal is to understand function definition, parameters, return values, and code organization.

# Your program should include these functions:

# 1. greet_user(name) - Creates a personalized greeting message
# Example Output: greet_user("Alice") → "Hello, Alice! Welcome to Python programming!"

# 2. calculate_average(numbers) - Calculates the average of a list of numbers  
# Example Output: calculate_average([10, 20, 30, 40]) → 25.0

# 3. find_maximum(data) - Finds the maximum value in a list of numbers
# Example Output: find_maximum([5, 2, 9, 1, 7]) → 9

# 4. count_vowels(text) - Counts the number of vowels in a given text
# Example Output: count_vowels("Hello World") → 3

# 5. convert_temperature(celsius) - Converts temperature from Celsius to Fahrenheit
# Example Output: convert_temperature(25) → 77.0

# 6. is_even(number) - Checks if a number is even
# Example Output: is_even(8) → True, is_even(7) → False

# 7. reverse_string(text) - Returns a reversed version of the input string
# Example Output: reverse_string("hello") → "olleh"

# 8. calculate_factorial(n) - Calculates the factorial of a number using a function
# Example Output: calculate_factorial(5) → 120

# BONUS CHALLENGE:
# Create a main() function that demonstrates all your functions by calling them with sample data!

# 💡 Hints:
# - Use def keyword to define functions
# - Use return statement to send back results
# - Test each function as you write it
# - Remember that functions should be reusable
# - Add comments to explain your logic

print("🎯 Let's create some amazing functions!")

# 1. greet_user(name) - Creates a personalized greeting message
# Example Output: greet_user("Alice") → "Hello, Alice! Welcome to Python programming!"


def greet_user(name):
    print(f"Hello {name}!\nWelcome to Python programming!")
greet_user("Ariana")


#  2. calculate_average(numbers) - Calculates the average of a list of numbers
# # Example Output: calculate_average([10, 20, 30, 40]) → 25.0


def calculate_average(numbers):
    result = sum(numbers)/len(numbers)
    print(f"The average of the list numbers is: {result}")

calculate_average([10, 20, 30, 40])

# 3. find_maximum(data) - Finds the maximum value in a list of numbers
# Example Output: find_maximum([5, 2, 9, 1, 7]) → 9

def find_maximum(data):
    result = max(data)
    print(f"The maximum value from the data is {result}")

find_maximum([5, 2, 9, 1, 7])

# 4. count_vowels(text) - Counts the number of vowels in a given text
# Example Output: count_vowels("Hello World") → 3

def count_vowels(text):
    vowels = ("a", "e", "i", "o", "u", 'A', 'E', 'I', 'O', 'U')
    num_vowels = 0
    for char in text:
        if char in vowels:
            num_vowels += 1
    print(f"The number of vowels in text is: {num_vowels} vowels")
    return num_vowels

count_vowels("Hello World")

# 5. convert_temperature(celsius) - Converts temperature from Celsius to Fahrenheit
# Example Output: convert_temperature(25) → 77.0

def convert_temperature(celsius):
    fahrenheit = round((celsius * 9/5) + 32, 1)
    print(f"The temperature in Fahrenheit is {fahrenheit}")
    return fahrenheit
convert_temperature(25)

# 6. is_even(number) - Checks if a number is even
# Example Output: is_even(8) → True, is_even(7) → False

def is_even(number):
    if number % 2 == 0:
        print(f"The number {number} is even? → True")
    else:
        print(f"The number {number} is even? → False")

is_even(8)

# 7. reverse_string(text) - Returns a reversed version of the input string
# Example Output: reverse_string("hello") → "olleh"

def reverse_string(text):
    result = text[::-1]
    print(f"The text is reversed: {result}")
    return result


# 8. calculate_factorial(n) - Calculates the factorial of a number using a function
# Example Output: calculate_factorial(5) → 120

def calculate_factorial(n):
    factorial = 1
    for num in range(1 , n+1):
        factorial *= num
    print(f"The factorial of {n} is {factorial}")
    return factorial
calculate_factorial(5)

# BONUS CHALLENGE:
# Create a main() function that demonstrates all your functions by calling them with sample data!

# 💡 Hints:
# - Use def keyword to define functions
# - Use return statement to send back results
# - Test each function as you write it
# - Remember that functions should be reusable
# - Add comments to explain your logic

def main():
    print("===========================")
    print("Demonstrating all functions")
    print("============================")
    greet_user("Adriana")
    calculate_average([20,55,25,14,58,45,56,655,25,12])
    find_maximum(([21,12,12.2,22,36,99,125]))
    count_vowels("In my mind, in my head, this is where we all came from")
    convert_temperature(35)
    is_even(99)
    reverse_string("adriana")
    calculate_factorial(20)
main()