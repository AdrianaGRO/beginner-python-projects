# 9. Coffee Shop Order
# Create a program to calculate the cost of a coffee order.
# Set a fixed coffee price of $4.50.
# Ask the user how many coffees they want to order.
# Apply an 8% tax to the total cost.
# Calculate and display the final cost rounded to 2 decimal places.
# Print the data type of the number of coffees.

print("Coffee Shop Order")
coffee = 4.50
num_coffee = int(input("How many coffees you would want to order? "))
subtotal = coffee * num_coffee
tax = subtotal * 0.08
total_cost = subtotal + tax
print(f"Your total (including 8% tax): ${total_cost:.2f}")
print(f"Data type for the number of coffee is: {type(num_coffee)}")
