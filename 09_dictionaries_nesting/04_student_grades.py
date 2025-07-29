"""
Project: Student Grades
Description: Create a dictionary mapping student names to their grades. Implement a function to retrieve a student's grade.

# TODO-1: Create a dictionary with student names as keys and grades as values.
# TODO-2: Define a function that takes a student name (string) as an argument.
# TODO-3: In the function, look up the student in the dictionary.
# TODO-4: If the student exists, return a formatted string with their grade.
# TODO-5: If the student does not exist, return a message indicating it is not found.

Output Format:
The grade for John is A.

Sample Call:
get_grade("John")
# Expected: The grade for John is A.

Note: Use hard-coded values for testing, not input().
"""

student_grades = {
    "John": "A",
    "Alice": "B+",
    "Bob": "C",
    "Diana": "A-",
    "Ethan": "B"
}

def get_grade(student_name):
    if student_name in student_grades:
        return f"The grade for {student_name} is {student_grades[student_name]}."
    else:
        return "Student not found."

print(get_grade("Alice"))
print(get_grade("Adriana"))
print(get_grade("Bob"))