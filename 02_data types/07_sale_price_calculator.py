# 7. Sale Price Calculator
# Build a program to calculate the sale price of an item.
# Ask the user for the original price and discount percentage.
# Calculate the sale price after applying the discount.
# Then, add an additional 5% coupon savings to the total savings (original price minus sale price).
# Display the sale price and total savings rounded to 2 decimal places.
# Print the data type of the savings.

print("Welcome to Sale Price Calculator")

price = float(input("Enter the original price of the product: $ "))
discount_percent = float(input("Enter the discount percentage: "))

sale_price = price - (price * discount_percent / 100)
print(f"Sale price after discount: ${sale_price:.2f}")

coupon_savings = (price * 5) / 100
total_savings = (price - sale_price) + coupon_savings
print(f"Total savings after applying coupon: ${total_savings:.2f}")
print(f"The data type for the savings is: {type(total_savings)}")