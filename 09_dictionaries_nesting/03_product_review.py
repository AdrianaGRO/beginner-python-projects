"""
Project: Product Review
Description: Create a dictionary mapping product names to their review ratings. Implement a function to retrieve a product's review rating.

# TODO-1: Create a dictionary with product names as keys and review ratings as values.
# TODO-2: Define a function that takes a product name (string) as an argument.
# TODO-3: In the function, look up the product in the dictionary.
# TODO-4: If the product exists, return a formatted string with its review rating.
# TODO-5: If the product does not exist, return a message indicating it is not found.

Output Format:
The review rating for Widget is 4.5 stars.

Sample Call:
get_review("Widget")
# Expected: The review rating for Widget is 4.5 stars.

Note: Use hard-coded values for testing, not input().
"""

products = {
    "Widget": 4.5,
    "Gadget": 3.8,
    "Doodad": 4.0,
    "Thingamajig": 4.2,
    "Contraption": 3.5
}

def get_review(product_name):
    if product_name in products:
        return f"The review rating for {product_name} is {products[product_name]} stars."
    else:
        return f"Sorry, we don't have any review for the product {product_name}."

print(get_review("TV"))