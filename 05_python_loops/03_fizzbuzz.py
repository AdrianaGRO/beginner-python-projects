# 3. FizzBuzz - Classic programming challenge with loops and conditionals
# Print numbers 1-100 with special rules for multiples of 3 and 5
# Demonstrates modulo operator, nested conditionals, and loop iteration
# One of the most famous programming interview questions

# Project Instructions:
# Your program should print each number from 1 to 100 in turn and include number 100.
# But when the number is divisible by 3 then instead of printing the number it should print "Fizz".
# When the number is divisible by 5, then instead of printing the number it should print "Buzz".
# And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"

# Expected output example:
# 1
# 2
# Fizz
# 4
# Buzz
# Fizz
# 7
# 8
# Fizz
# Buzz
# 11
# Fizz
# 13
# 14
# FizzBuzz
# ...etc

print("Welcome to the FizzBuzz Challenge!")
print("This program will print numbers from 1 to 100 with special rules for multiples of 3 and 5.")

for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)

print("FizzBuzz Challenge completed!")