"""
Project: Employee Performance
Description: Create a dictionary mapping employee names to their performance scores. Implement a function to retrieve an employee's score.

# TODO-1: Create a dictionary with employee names as keys and performance scores as values.
# TODO-2: Define a function that takes an employee name (string) as an argument.
# TODO-3: In the function, look up the employee in the dictionary.
# TODO-4: If the employee exists, return a formatted string with their score.
# TODO-5: If the employee does not exist, return a message indicating it is not found.

Output Format:
The performance score for Alice is 92.

Sample Call:
get_performance("Alice")
# Expected: The performance score for Alice is 92.

Note: Use hard-coded values for testing, not input().
"""
top_15_employee_performance = {
    "Alice": 92,
    "Bob": 85,
    "Charlie": 78,
    "David": 88,                                                                                                                                        
    "Eve": 95,
    "Frank": 80,
    "Grace": 90,
    "Hannah": 82,
    "Ian": 76,      
    "Jack": 89,
    "Kathy": 91,
    "Liam": 84,
    "Mia": 87,
    "Noah": 93,
    "Olivia": 79,
}

def performance(name):
        if name in top_15_employee_performance:
            return f"The score for employee {name} is {top_15_employee_performance[name]}."
        else:
            return f"The employee {name} was not found in database."

print(performance("Ian"))