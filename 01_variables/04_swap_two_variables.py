
# Project 4: Swap Two Variables
# Ask the user to enter two different words or colors.
# Store them in two variables.
# Swap the contents of the variables.
# Print both variables before and after swapping.

print("Welcome to the swap game")
first_word = input("Add your color here:\n")
second_word = input("Add your random meal here:\n")
print(f"You choose: \n 1.The first position: {first_word}\n 2.The second position: {second_word}\n... let's swap them...")
print("=======================================================")
third_world = first_word
first_word = second_word
second_word = third_world

print(f"After the swap we have: \n 1.The first position:{first_word}\n 2.The second position {second_word}\n... Did the swap worked?...")
print("=======================================================")