# 6. Name Length Processor - Analyze name lengths using loops
# Uses loops to process a list of names and find statistics
# Demonstrates string length analysis and comparison logic
# Shows how to find minimum, maximum, and average values through iteration

# Project Instructions:
# Process a list of names to find length statistics
# Use loops to calculate:
# - Longest name (maximum length)
# - Shortest name (minimum length) 
# - Average name length
# - Total character count

# Example names list:
# names = ["Adriana", "Bob", "Christopher", "Diana", "Ed", "Francesca", "George"]

# Expected analysis:
# - Longest: "Christopher" (11 characters)
# - Shortest: "Ed" (2 characters)
# - Average: X.X characters
# - Total characters: XX

# Bonus challenges:
# - Show all names with their lengths
# - Find names that are longer/shorter than average
# - Count names by length categories (short, medium, long)

# TODO: Implement your solution here

print("Welcome to the Name Length Processor!")
print("This program will analyze a list of names to find length statistics.")
names = ["Adriana", "Bob", "Christopher", "Diana", "Ed", "Francesca", "George"]

longest = names[0]

for name in names:
    print(f" Your name {name} has {len(name)} characters.")
    if len(name) > len(longest):
        longest = name

shortest = names[0]
for name in names:
    if len(name) < len(shortest):
        shortest = name

total_characters = 0
for name in names:
    total_characters += len(name)
average = total_characters / len(names)


print(f"🏆 Champion: '{longest}' wins with {len(longest)} characters!")
print(f"🥇 Shortest: '{shortest}' keeps it concise with just {len(shortest)} characters!")
print(f"Average name length: {average:.2f}")
print(f"Total character analysis: {total_characters}")
print("Thank you for using the Name Length Processor! Have a great day! 😊")