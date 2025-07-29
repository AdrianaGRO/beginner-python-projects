"""
Project: Grading Program
Description: Create a dictionary mapping student names to their scores. Implement a function to assign a letter grade based on the score.

# TODO-1: Create a dictionary with student names as keys and scores as values.
# TODO-2: Define a function that takes a student name (string) as an argument.
# TODO-3: In the function, look up the student in the dictionary.
# TODO-4: If the student exists, assign a letter grade based on the score and return a formatted string.
# TODO-5: If the student does not exist, return a message indicating it is not found.

Output Format:
John's grade is A.

Sample Call:
get_letter_grade("John")
# Expected: John's grade is A.

Note: Use hard-coded values for testing, not input().
"""

student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}


student_grades = {}

for student in student_scores:
    score = student_scores[student]
    if score >=91:
        student_grades[student] = "Outstanding"
    elif score >= 81:
        student_grades[student] = "Exceeds Expectations"
    elif score >=71:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"

print(student_grades["Harry"])