import random
from data_game import data
from art import logo, vs

option_a = {}
option_b = {}
score = 0

def clear_terminal():
    print("\n" * 20)

def generate_option():
    option = random.choice(data)
    return option

def check_answer(answer):
    followers_a = option_a["follower_count"]
    followers_b = option_b["follower_count"]
    if answer == "a":
        if followers_a > followers_b:
            return True
    else:
        if followers_b > followers_a:
            return True

    return False

def print_logo():
    clear_terminal()
    print(logo)

#Display the logo
print_logo()
#Initialize option A
option_a = generate_option()
#Display the option

while True:
    print(f"Compare A: {option_a['name']}, a {option_a['description']}, from {option_a['country']}")

    #Display the second logo
    print(vs)
    #Initialize option B
    option_b = generate_option()
    while option_a == option_b:
        option_b = generate_option()
    #Display option B
    print(f"Against B: {option_b['name']}, a {option_b['description']}, from {option_b['country']}")

    #Input from the user
    answer = input("Who has more followers? A or B?:\n").lower()
    print_logo()
    correct = check_answer(answer)
    if not correct:
        print(f"You were wrong! Your final score is: {score}")
        break
    else:
        score += 1
        print(f"You are right! Your current score is: {score}")
        option_a = option_b



