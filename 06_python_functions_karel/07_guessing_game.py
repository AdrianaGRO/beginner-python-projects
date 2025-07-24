# 🎯 Guessing Game Helper Project
# Count attempts in a simple guessing game

import random

def guessing_number():
    attempts = 0
    guess_the_number = random.randint(0,100)
    print(guess_the_number)
    while True:
        user_guess = int(input("Try to guess the number: \n"))
        attempts += 1
        if guess_the_number == user_guess:
            print(f"Congratulation! You guessed the number: {guess_the_number} - in  {attempts} attempts")
            break
        elif attempts > 10:
            print("Game over! You had 10 attempts to guess the number.")
            break
        else:
            print(f"{attempts}/10 You have another try!")

guessing_number()
