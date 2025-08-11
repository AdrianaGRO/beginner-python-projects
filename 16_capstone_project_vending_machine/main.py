
from data import INVENTORY, billnotes, coins
import inflect

#Global variables and constants

profit = 0
engine = inflect.engine()

#Functions and methods
def create_catalog():
    print("*********************************************")
    print("Welcome to Vending Machine")
    print("Refreshing choices are just a selection away.")
    print("*********************************************")
    print("Your available products:")


    for key, details in INVENTORY.items():
            if details['stock'] > 0:
                product = details['product']
                price = details['price']
                print(f"{key}. {product.title()} - {price:.2f} Lei")


def admin_menu():
    print("*********************************************")
    print("===========ADMIN MENU========================")
    print("*********************************************")
    pin_admin()
    choice_admin = input("Please select the choice to run it:\n"
                             "1. Report\n"
                             "2. Off \n"
                             "3. Back to the main menu\n").lower()
    while choice_admin not in ['report', '1', 'off', '2', 'main', '3']:
        print("Invalid option. Please try again.")
        choice_admin = input("Please select the choice to run it:\n"
                             "1. Report\n"
                             "2. Off \n"
                             "3. Back to the main menu\n").lower()
    if choice_admin == 'report' or choice_admin == '1':
        print_report()
    elif choice_admin == "off" or choice_admin == '2':
        return shutting_down()
    elif choice_admin == 'main' or choice_admin == '3':
        main()


def pin_admin():
    attempts = 0
    pin = '1234'
    while attempts < 3:
        ask_pin = input('Please enter the pin to access the admin menu:\n')
        attempts += 1
        if pin == ask_pin:
            print("Login successful")
            break
        else:
            print("Incorrect password, please try again")
    else:
        print("You tried 3 times, you are locked up.")
        main()
        return False


def shutting_down():
    print("Machine shutting down... ")
    return "off"


def print_report():
    print()
    print("===REPORT===")
    for key ,quantity in INVENTORY.items():
        product = quantity['product']
        stock = quantity['stock']
        if stock == 0 or stock == 1:
            print(f"{key}. {product}- stock: {stock} piece.")
        else:
            print(f"{key}. {product}- stock: {stock} pieces.")
    print(f"Money: {profit:.2f}")


def check_enough_stock(product):
    stock_product = INVENTORY[product]['stock']
    if stock_product > 0:
        return True

    print(f"Sorry we don't have stock for {stock_product}")
    return False

def check_machine_run_out_of_stock():
    # Check if the stock of all my projects is zero
    for product in INVENTORY.values():
        if product['stock'] != 0:
            return False

    print(f"We have no more product in stock. Shutting down...!")
    return True

def prepare_order(product):
    INVENTORY[product]['stock'] -= 1

    return True

def ask_for_money():
    cash = 0
    for bill in billnotes:
        while True:
            try:
                count_bills = int(input(f"How many notes {engine.plural(bill)}? "))
                if count_bills < 0:
                    print("Invalid input. Please enter a positive number.")
                    continue
                cash += count_bills * billnotes[bill]
                break
            except ValueError:
                print("Invalid input. Please enter a number.")

    return cash

def check_money(product, money):
    price = product['price']
    if money < price:
        print(f"Sorry that's not enough money. Money refunded.")
        return False

    return True


def process_money(product, money):
    price = product['price']

    global profit
    profit += price

    return money - price



#Main
def main():
    # create_catalog()
    while True:
        stock = None
        if check_machine_run_out_of_stock():
            break
        print()
        create_catalog()
        print("Please select your product by entering it's number.")
        user_choice = input(f"What you would like?: ")
        if user_choice == "admin":
            if admin_menu() == "off":
                break
        

        elif user_choice in INVENTORY:
            product = INVENTORY[user_choice]
            print(f"You choose the product: '{INVENTORY[user_choice]['product']}' - hang tight is on the way...")

            if check_enough_stock(user_choice):
                print("Please proceed with the payment for your product.")
                money = ask_for_money()
                if check_money(product, money):
                    change = process_money(product, money)
                    prepare_order(user_choice)

                    if change == 0:
                        print(f"No change, you introduced the same price!")

                    else:
                        print(f"Here is {change:.2f} lei in change.")
                    print(f"Here is your {INVENTORY[user_choice]['product']}. Enjoy!")

        else:
            print(f"Sorry, we don't have {user_choice}. Please choose from the menu")



main()