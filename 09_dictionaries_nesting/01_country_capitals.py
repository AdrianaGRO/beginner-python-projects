"""
Project: Country Capitals
Description: Create a dictionary mapping country names to their capitals. Implement a function that returns the capital for a given country name.

# TODO-1: Create a dictionary with country names as keys and capitals as values.
# TODO-2: Define a function that takes a country name (string) as an argument.
# TODO-3: In the function, look up the country in the dictionary.
# TODO-4: If the country exists, return a formatted string with its capital.
# TODO-5: If the country does not exist, return a message indicating it is not found.

Output Format:
The capital of France is Paris.

Sample Call:
get_capital("France")
# Expected: The capital of France is Paris.

Note: Use hard-coded values for testing, not input().
"""

top_15_country_capitals = {
    "China": "Beijing",
    "India": "New Delhi",
    "United States": "Washington, D.C.",
    "Indonesia": "Jakarta",
    "Pakistan": "Islamabad",
    "Nigeria": "Abuja",
    "Brazil": "Brasília",
    "Bangladesh": "Dhaka",
    "Russia": "Moscow",
    "Mexico": "Mexico City",
    "Ethiopia": "Addis Ababa",
    "Japan": "Tokyo",
    "Philippines": "Manila",
    "Egypt": "Cairo",
    "Vietnam": "Hanoi"
}


def get_capital(country_name):
    for capital in top_15_country_capitals:
        if country_name == capital:
            return f"Discover the capital of {country_name} it's {top_15_country_capitals[country_name]}."
    return f"Oops! We couldn't find the capital for {country_name}."

print(get_capital("Japan"))
print(get_capital("France"))
print(get_capital("Brazil"))
print(get_capital("India"))
print(get_capital("Germany"))
print(get_capital("Nigeria"))   