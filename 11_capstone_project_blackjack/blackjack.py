import random
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_cards = []
computer_cards = []
player_score = 0
computer_score = 0

def askQuestion(question):
    response = input(question + " (y/n): ").lower()

    if response == 'y' or response == 'yes':
        return True

    return False

def game_logo():
    print(logo)

def initialize_game():
    global player_cards
    player_cards = []

    global computer_cards
    computer_cards = []

    global player_score
    player_score = 0

    global computer_score
    computer_score = 0

def computer_hand():
    first_card = random.choice(cards)
    computer_cards.append(first_card)
    second_card = random.choice(cards)
    computer_cards.append(second_card)

    update_computer_score(first_card, second_card)

def update_computer_score(first_card, second_card):
    global computer_score
    computer_score = first_card + second_card

def player_hand():
    player_card = random.choice(cards)
    player_cards.append(player_card)

    update_player_score(player_card)

def update_player_score(player_card):
    global player_score
    player_score += player_card

def user_exceeds_21():
    if player_score > 21:
        return player_score > 21

def not_exceeds_21():
    user_wants_another_card = input("Do you want another card? ")

def print_state():
    print("")
    print("Computer's first card: " + str(computer_cards[0]))

    print("Your cards: " + str(player_cards))
    print("You current score: " + str(player_score))
    print("")

def results():
    if player_score > computer_score:
        print("You won! 🏆\n")
        print("")
    elif player_score == computer_score:
        print("It's a tie/draw!\n "
              "Continue playing...")
        print("")
    else:
        print("You lost! 😞")
        print("")

def print_state_endgame():
    print("")
    print("Computer's cards: " + str(computer_cards))
    print("Computer's score: "  + str(computer_score))
    print("******************************************")
    print("Your cards: " + str(player_cards))
    print("You current score: " + str(player_score))
    print("")


def main():
    while True:
        user_wants_to_play = askQuestion("Would you like to play blackjack?")
        if not user_wants_to_play:
            break

        initialize_game()
        game_logo()

        computer_hand()

        player_hand()
        player_hand()
        print_state()

        
        while True:
            if user_exceeds_21():
                print(f"Busted! your cards are {player_cards} and your score is: {player_score}")
                print("\n" * 3)
                break
            user_wants_another_card = askQuestion("Do you want another card?\n")
            if not user_wants_another_card:
                break
            player_hand()
            print_state()

        if not user_exceeds_21():
                print_state_endgame()
                results()


    print("Bye!")

main()






