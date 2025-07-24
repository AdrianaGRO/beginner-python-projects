# 🔄 Menu System Project
# Create a menu that keeps running until user chooses to exit

menu_on = True
while menu_on:
    choice = int(input("Select one option type 1 / 2 / 3 / 4 > for the menu:\n"
                     "1. Get news\n"
                     "2. Get feeds\n"
                     "3. Get shorts\n"
                     "4. Exit\n"))

    if choice == 4:
        print("You got out from the menu!")
        break

    else:
        print("This is one of the options")
