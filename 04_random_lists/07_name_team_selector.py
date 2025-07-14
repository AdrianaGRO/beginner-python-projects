# 7. Name/Team Selector - Random selection from user-provided lists
# Uses random.sample() to pick multiple unique entries without replacement
# Processes user input by splitting strings and cleaning whitespace
# Perfect for selecting winners, teams, or random groups from a larger list

# Project Instructions:
# 1. Prompt the user to enter a comma-separated list of names or items
# 2. Split into a list, strip whitespace
# 3. Ask how many winners or teams to draw
# 4. Use random.sample() to pick unique entries and print them

import random

print("🎯 Welcome to the Random Team Builder!")
print("Perfect for creating fair teams, selecting winners, or picking random groups!")
names_input = input("Enter participant names separated by commas(e.g: John, Jane, Doe): \n").replace(" ", "")
participants = list(names_input.split(","))
formatted_names = list(map(str.capitalize, participants))
teams_size = int(input("How many people should be in the selected team?\n"))
if teams_size <= 0:
    print("⚠️ Team size must be at least 1 person!")
elif teams_size <= len(formatted_names) != 0:
    selected_team = random.sample(formatted_names, teams_size)
    print(f"🏆 Your randomly selected team members are: {', '.join(selected_team)}")
else:
    print(f"❌ Not enough participants! You have {len(formatted_names)} people, but need {teams_size}.")

print("🎉 Thank you for using the Random Team Builder!")