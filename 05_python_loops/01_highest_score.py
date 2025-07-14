# 1. Highest Score - Find the maximum score using loops and conditionals
# Uses for loops to iterate through a list of exam scores
# Demonstrates accumulator pattern with conditional logic to track maximum value
# Shows how loops can replace built-in functions like max() for learning purposes

# Project Instructions:
# Given a list of exam scores, find and print the highest score
# Use for loops and conditionals (no built-in max() function)
# Example: scores = [8, 65, 89, 86, 55, 91, 64, 89] should output 91

print("Welcome to the Highest Score Finder!")
print("This program will find the highest score from a list of student scores.")
student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]

highest_score = student_scores[0]
for score in student_scores:
    if score > highest_score:
        highest_score = score

print(f"The highest score is: {highest_score}")
print(f"Congratulations to the student who scored {highest_score} points!")