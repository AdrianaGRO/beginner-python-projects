import random

from hangman_words import word_list

lives = 6

from hangman_art import logo
print(logo)
print("Welcome to Hangman!")
print("Guess the word by entering one letter at a time.")
print("You have 6 lives. Good luck!")
print()

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []

while not game_over:
    print(f"****************************{lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

    if guess in correct_letters:
        print(f"You already guessed {guess}")
        continue
    display = ""
    found = False
    for letter in chosen_word:
        if letter == guess:
            display += letter
            found = True
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    if found:
        correct_letters.append(guess)
    print("Word to guess: " + display)

    if not found:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        if lives == 0:
            game_over = True
            print(f"IT WAS '{chosen_word}'! YOU LOSE")
            print(f"***********************YOU LOSE**********************")

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    from hangman_art import stages
    print(stages[lives])
