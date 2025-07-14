# 3. Rock Paper Scissors - Classic game with random computer opponent
# Uses random.randint(0, 2) to generate computer's choice: 0=Rock, 1=Paper, 2=Scissors
# Compares user input vs computer's random choice using nested if/elif statements
# Includes ASCII art for visual representation of each choice

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
print("===Welcome to Rock, Paper, Scissors Game!===")
user_choice = int(input("What do you choose? Type '0' for rock, '1' for Paper, '2' for Scissor:\n"))
if user_choice == 0:
    print(rock)
elif user_choice == 1:
    print(paper)
elif user_choice == 2:
    print(scissors)
else:
    print("Incorrect submission, please type '0' for rock, '1' for Paper, '2' for Scissor")

computer_choice = random.randint(0,2)

if computer_choice == 0:
    print(rock)
elif computer_choice == 1:
    print(paper)
else:
    print(scissors)

print(f"You chose: {user_choice}, Computer chose: {computer_choice}")
print("===Game Result===")


if user_choice == 0 and computer_choice == 0:
    print("Draw!")
elif user_choice == 0 and computer_choice == 1:
    print("You lose!")
elif user_choice == 0 and computer_choice == 2:
    print("You win!")
elif user_choice == 1 and computer_choice == 0:
    print("You win!")
elif user_choice == 1 and computer_choice == 1:
    print("Draw!")
elif user_choice == 1 and computer_choice == 2:
    print("You lose!")
elif user_choice == 2 and computer_choice == 0:
    print("You lose!")
elif user_choice == 2 and computer_choice == 1:
    print("You win!")
elif user_choice == 2 and computer_choice == 2:
    print("Draw!")

else:
    print("It's an error! please check the code.")


