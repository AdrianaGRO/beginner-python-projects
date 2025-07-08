# 1. Grocery Budget Tracker
# Create a program that tracks your grocery budget.
# Ask the user for their total budget, the cost of items they want to buy, and a discount percentage (for example, 10 for 10%).
# Calculate the discount amount, final cost after discount, and remaining budget.
# Display the final cost and remaining budget rounded to 2 decimal places.
# Also, print the data type of the discount amount.

print("========================")
print("Grocery budget tracker!")
print("========================")

budget = float(input("What is your budget?\nRON "))
cost = float(input("What is the total cost of your groceries?\nRON "))
discount_percentage = float(input("What is the discount percentage applied to the basket? (for example 10 for 10 %)\n% "))

discount_amount = (cost * discount_percentage) / 100
final_cost = round(cost - discount_amount , 2)
remaining_budget = round(budget - final_cost , 2)

print("*************************************************")
print(f"After applying {discount_percentage}% to your total cost of the basket, you need to pay at the cash register "
      f"the value: {final_cost:.2f} RON, your budget after this acquisition is: {remaining_budget:.2f} RON.")

print(type(discount_amount))