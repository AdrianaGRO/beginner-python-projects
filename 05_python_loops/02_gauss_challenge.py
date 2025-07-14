# 2. The Gauss Challenge - Sum of numbers from 1 to 100
# Calculate the total sum of all numbers between 1 and 100 (inclusive)
# Uses for loops and range() to demonstrate accumulator pattern with addition
# Named after Carl Friedrich Gauss who famously solved this as a child

# Project Instructions:
# Work out the total of the numbers between 1 and 100, inclusive of both 1 and 100
# Use loops to add each number from 1 to 100
# The expected result should be 5050

print("Welcome to the Gauss Challenge!")
print("This program will calculate the total sum of all numbers between 1 and 100, inclusive.") 
print("Gauss as a child famously solved this by realizing the sum of the first and last numbers is equal to the sum of the second and second-to-last numbers, and so on.")
sum = 0
for num in range(1, 101):
    sum += num

print(f"The total sum of all numbers between 1 and 100 is: {sum}")
