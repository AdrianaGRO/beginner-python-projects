# 5. Shopping Cart Total - Calculate total cost using loops
# Uses loops to iterate through item prices and calculate running total
# Demonstrates accumulator pattern with addition and real-world application
# Shows how loops can process lists of prices for practical scenarios

# Project Instructions:
# Create a shopping cart system that calculates the total cost
# Use a list of item prices and loop through them to sum the total
# Add features like tax calculation, discount application, or item counting
# Display the final total with proper formatting

# Example item prices:
# prices = [2.50, 15.99, 8.75, 3.25, 12.00, 5.99]
# Expected output: "Total: $48.48"

# Bonus challenges:
# - Add item names with corresponding prices
# - Calculate tax (e.g., 8.5%)
# - Apply discounts for bulk purchases
# - Show individual items with running total

# TODO: Implement your solution here

print("Welcome to the Shopping Cart Total Calculator!")
print("Let's calculate your total cost with some awesome features! 🛒💰")
print("Analyzing your shopping basket with 10 premium items...")
print("Calculating savings and taxes for your purchase...")
print("Discount of 5% for bulk purchases if more than 5 items!")

prices = [25.00, 19.99, 75.00, 12.5, 5.55, 8.99, 15.00, 20.00, 30.00, 50.00]
total = 0

for price in prices:
    total += price
gross_price = 0
for price in prices:
    gross_price += price / 1.085

bulk_discount = 0
for price in range(0, len(prices)):
    if len(prices) > 5:
         bulk_discount += prices[price] * 0.05

print(f"Your total basket value is: $ {float(total)}")
print(f"The total amount of products without takes: $ {gross_price:.2f}")
print(f"The taxes for your basket ($8.5): $ {(total - gross_price):.2f}")
print(f"The total discount for your basket: $ {bulk_discount:.2f}")