# 2. Banker Roulette - Random person selector from a list
# Uses random.choice() to pick one random element from a list of friends
# Creates a list of names, then randomly selects who pays the bill
# Each person has equal probability of being chosen

import random

print("Welcome to Banker Roulette")
friends = ["Marina", "Antonio", "Sergiu", "Bogdan", "Oana", "Antonia", "Madalina"]

bill_payment = random.choice(friends)

print(f"The person that will take care of the bill is: {bill_payment}")