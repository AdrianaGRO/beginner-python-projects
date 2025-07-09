# 8. Number Guessing Hint Game
# Compare a user’s guess to a secret number.
# If exact, celebrate;
# if within 2, say “Very close”;
# if too high/low, guide accordingly.
# Combine relational checks and show the type of the guess.
import random

print("Welcome to Number Guessing Hint Game")
secret_number = random.randint(1, 101)
print(secret_number)
guess = int(input("Guess the secret number: "))

if guess == secret_number:
    print(f"Congratulations! you guessed the secret number {secret_number}")
elif abs(guess - secret_number) <=2:
    print( "You are very close!")
elif guess < secret_number:
    print(f"Your guess {guess} is too low! Try again.")
else:
    print(f"Your guess {guess} is too high! Try again.")
