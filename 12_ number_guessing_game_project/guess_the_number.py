import random
from art import logo_guess_the_number

attempts = 0
secret_number = 0

def chose_random_number():
    global secret_number
    secret_number = random.randrange(1, 101)
    print("I am thinking a number between 1 and 100.")
    print(f"Psst... the secret number is : {secret_number}")

# Print welcome message
print("Welcome to the Guess Number Game!")

# Ask difficulty
difficulty = input("Choose the difficulty level (easy or hard):\n").lower()

# Set number of attempts
if difficulty == "easy" or difficulty == "e":
    attempts = 10
else:
    attempts = 5

# Calculate magic number
chose_random_number()

while attempts > 0:
    print("can you guess the number? ")
    player_guess = int(input("Make your guess: "))

    if player_guess == secret_number:
        print("Congratulation you guessed the secret number! 🎯")
        break

    if player_guess < secret_number:
        print("Too low!")
    else:
        print("Too high!")

    attempts -= 1
    print(f"You have {attempts} attempts left to guess the secret number.")

    if attempts == 0:
        print("GAME OVER!")
        break

print("Bye!")





