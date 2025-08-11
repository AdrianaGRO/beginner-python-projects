from data import MENU, resources, coins

import inflect

# Global variables and constants
my_menu = None
profit = 0
engine = inflect.engine()

# Functions and methods
def create_menu():
    global my_menu
    my_menu = "/".join(MENU.keys())

def print_report():
    for res in resources:
        print(f"{res.title()}: {resources[res]}")
    print(f'Money: {profit:.2f}')

def check_enough_ingredients(recipe):
    for ing in recipe["ingredients"]:
        quantity_left = resources[ing]
        quantity_needed = recipe["ingredients"][ing]
        if quantity_needed > quantity_left:
            print(f"Sorry there is not enough {ing}.")
            return False

    return True

def prepare_order(recipe):
    for ing in recipe["ingredients"]:
        quantity_needed = recipe["ingredients"][ing]
        resources[ing] -= quantity_needed

    return True

def ask_for_money():
    cash = 0
    for coin in coins:
        cash += int(input(f"How many {engine.plural(coin)}? ")) * coins[coin]

    return cash

def check_money(recipe, money):
    price = recipe["cost"]

    if money < price:
        print(f"Sorry that's not enough money. Money refunded.")
        return False

    return True

def process_money(recipe, money):
    price = recipe["cost"]

    global profit
    profit += price

    return money - price

# main
def main():
    create_menu()
    while True:
        recipe = None
        user_choice = input(f"What would you like? ({my_menu}): ").lower()
        if user_choice == 'off':
            print("Turning off the machine.")
            break
        # Process report
        elif user_choice == 'report':
            print_report()

        elif user_choice in MENU:
            recipe = MENU[user_choice]

            # Continue processing the order
            if check_enough_ingredients(recipe):
                money = ask_for_money()
                if check_money(recipe, money):
                    change = process_money(recipe, money)
                    prepare_order(recipe)

                    if change == 0:
                        print(f"No change, you introduced the exact price!")
                    else:
                        print(f"Here is ${change:.2f} dollars in change.")
                    print(f"Here is your {user_choice}. Enjoy!")
        else:
            print(f"Sorry, we don't have {user_choice}. Please choose from the menu.")

main()