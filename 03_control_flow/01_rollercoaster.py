
# Calculate a user's rollercoaster ticket bill based on their input. Use the input() function to collect their height, age, and photo preference, then determine and display the final bill.

# Height requirement: Must be at least 120 cm to ride.
# Ticket prices:
# Child (under 12 years): $5
# Youth (12 to 18 years): $7
# Adult (over 18 years, except 45–55 years): $12
# Midlife (45 to 55 years): $0 (free)
# Photo option (Y or N): +$3

# Example Interaction:
# Welcome to the rollercoaster!
# What is your height in cm? 130
# You can ride the rollercoaster!
# What is your age? 15
# Youth tickets are $7.
# Do you want a photo taken? Y or N: Y
# Your final bill is $10.

# If height < 120 cm:
# Welcome to the rollercoaster!
# What is your height in cm? 110
# Sorry, you have to grow taller before you can ride.

print("Welcome to Bucharest rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    elif age >= 45 and age <= 55:
        bill += 0
        print("Your ticket is for free!")

    else:
        bill = 12
        print("Adult tickets are $12.")

    wants_photo = input("Do you want a photo taken? Y or N. ").upper()
    if wants_photo == "Y":
        bill += 3

    print(f"Your final bill is ${bill}")

else:
    print("Sorry, you have to grow taller before you can ride.")