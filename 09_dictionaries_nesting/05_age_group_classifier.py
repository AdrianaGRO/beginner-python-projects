"""
Project: Age Group Classifier
Description: Create a dictionary mapping names to ages. Implement a function to classify each person into an age group (child, teen, adult, senior).

# TODO-1: Create a dictionary with names as keys and ages as values.
# TODO-2: Define a function that takes a name (string) as an argument.
# TODO-3: In the function, look up the name in the dictionary.
# TODO-4: If the name exists, classify the age into a group and return a formatted string.
# TODO-5: If the name does not exist, return a message indicating it is not found.

Output Format:
Alice is an adult.

Sample Call:
get_age_group("Alice")
# Expected: Alice is an adult.

Note: Use hard-coded values for testing, not input().
"""

# No code below this line

age_groups = {
    "Alice": 30,
    "Bob": 15,
    "Charlie": 8,
    "Diana": 65,
    "Ethan": 22             
}

def get_age_group(name):
    if name in age_groups:
        if age_groups[name] <= 18:
            return f"{name} is a child"
        elif age_groups[name] <= 55:
            return f"{name} is an adult"
        elif age_groups[name] >= 56:
            return f"{name} is elder"
        else:
            return f"Sorry! {name} was not found in our records!"

print(get_age_group("Maria"))
print(get_age_group("Diana"))
print(get_age_group("Ethan"))