# 3. Movie Ticket Price Calculator
# Build a program that calculates movie ticket prices.
# Ask the user for the standard ticket price and whether they are a student (yes/no).
# If yes, apply a 20% discount; otherwise, no discount.
# Calculate and display the final price rounded to 2 decimal places.
# Print the data type of the student status as a boolean.


print("Movie Ticket Price Calculator For Students")
#Ask for the standard ticket price
standard_price = float(input("What is the standard price of the ticket? $"))

#Ask if they are a student or not
student = input("Are you a student (yes/no)?\n").strip().lower()

is_student = student == ("yes")
#Print the boolean type of student status
print("Student status (as boolean) :", is_student)
print("Data type:", type(is_student))

#Calculate discount
price_full = round(standard_price, 2)
discount_price = round(standard_price - ((price_full * 20) /100), 2)

if student == "no":
    print(f"Your ticket price is ${standard_price:.2f}")
else:
    print(f"Your ticket price is ${discount_price:.2f}")

