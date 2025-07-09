# Calculate a user's final bill based on their order. Use the input() function to collect their preferences, sum the total cost of their order, and inform them of the amount due.

# Small pizza (S): $15
# Medium pizza (M): $20
# Large pizza (L): $25
# Pepperoni for small pizza (Y or N): +$2
# Pepperoni for medium or large pizza (Y or N): +$3
# Extra cheese for any size pizza (Y or N): +$1
# Example Interaction:
# Welcome to Python Pizza Deliveries!
# What size pizza do you want? S, M, or L: M
# Do you want pepperoni? Y or N: N
# Do you want extra cheese? Y or N: Y
# Your final bill is: $21.

print("Welcome to Py Pizza Deliveries!")

size = input("What size pizza do you want? S, M or L: ").upper()
bill = 0

if size == "S":
    bill = 15
elif size == "M":
    bill = 20
else:
    bill = 25

pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").upper()
if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

extra_cheese = input("Do you want extra cheese? Y or N: ").upper()
if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}.")