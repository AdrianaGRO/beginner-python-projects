# Guide the user through an extended text-based adventure game on Treasure Island to find the treasure. Use the input() function to collect their choices at each stage and determine the outcome based on their decisions. After choosing the yellow door, add three additional challenges before the user can win.

# First choice: At a crossroad, choose "left" or "right".
# Right: Fall into a hole. Game over.
# Left: Proceed to the lake.
# Other: Game over for invalid input.
# Second choice (if left): At a lake with an island, choose "swim" or "wait".
# Swim: Attacked by a shark. Game over.
# Wait: Reach the island safely.
# Other: Game over for invalid input.
# Third choice (if wait): At a house with three doors, choose "red", "yellow", or "blue".
# Red: Burned by fire. Game over.
# Blue: Eaten by beasts. Game over.
# Yellow: Enter the house and proceed.
# Other: Game over for invalid input.
# Fourth choice (if yellow): Inside the house, find a dusty chest with two keys, choose "gold" or "silver".
# Gold: Chest is booby-trapped with poison darts. Game over.
# Silver: Unlock the chest safely and proceed.
# Other: Game over for invalid input.
# Fifth choice (if silver): Find a hidden staircase leading down, choose "descend" or "stay".
# Stay: Floor collapses beneath you. Game over.
# Descend: Reach a secret chamber safely.
# Other: Game over for invalid input.
# Sixth choice (if descend): In the chamber, face three tunnels, choose "left", "middle", or "right".
# Left: Tunnel leads to a pit of snakes. Game over.
# Right: Tunnel collapses. Game over.
# Middle: Find the treasure and win.
# Other: Game over for invalid input.

# Example Interaction:
# Welcome to Treasure Island.
# Your mission is to find the treasure.
# You're at a crossroad. Where do you want to go?
# Type 'left' or 'right': left
# You've come to a lake. There is an island in the middle of the lake.
# Type 'wait' to wait for the boat. Type 'swim' to swim across: wait
# You arrive at the island unharmed. There is a house with 3 doors.
# One red, one yellow, one blue. Which color do you choose? yellow
# You enter the house and find a dusty chest with two keys.
# Type 'gold' or 'silver': silver
# You unlock the chest safely and find a hidden staircase.
# Type 'descend' or 'stay': descend
# You reach a secret chamber with three tunnels.
# Type 'left', 'middle', or 'right': middle
# YOU WIN!!! You found the treasure!

# Example Failure:
# Welcome to Treasure Island.
# Your mission is to find the treasure.
# You're at a crossroad. Where do you want to go?
# Type 'left' or 'right': left
# You've come to a lake. There is an island in the middle of the lake.
# Type 'wait' to wait for the boat. Type 'swim' to swim across: wait
# You arrive at the island unharmed. There is a house with 3 doors.
# One red, one yellow, one blue. Which color do you choose? yellow
# You enter the house and find a dusty chest with two keys.
# Type 'gold' or 'silver': gold
# The chest is booby-trapped with poison darts. GAME OVER!




print(r'''                     _.--.
                        _.-'_:-'||
                    _.-'_.-::::'||
               _.-:'_.-::::::'  ||
             .'`-.-:::::::'     ||
            /.'`;|:::::::'      ||_
           ||   ||::::::'     _.;._'-._
           ||   ||:::::'  _.-!oo @.!-._'-.
           \'.  ||:::::.-!()oo @!()@.-'_.|
            '.'-;|:.-'.&$@.& ()$%-'o.'\U||
              `>'-.!@%()@'@_%-'_.-o _.|'||
               ||-._'-.@.-'_.-' _.-o  |'||
               ||=[ '-._.-\U/.-'    o |'||
               || '-.]=|| |'|      o  |'||
               ||      || |'|        _| ';
               ||      || |'|    _.-'_.-'
               |'-._   || |'|_.-'_.-'
            jgs '-._'-.|| |' `_.-'
                    '-.||_/.-'
                    Treasure Island Adventure''')


print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
left_right = input("You\'re at a crossroad. Where do you want to go?\nType 'left' or 'right' ").lower()
if left_right == "right":
    print("Fall into a gole. GAME OVER!")
elif left_right == "left":
    swim_wait = input("You\'ve come to a lake. There is an island in the middle of the lake.\n"
                      "Type 'wait' to wait fot the boat. Type 'swim' to swim across. ").lower()
    if swim_wait == 'swim':
        print("Attacked by shark. GAME OVER!")
    elif swim_wait == 'wait':
        door = input("You arrive at the island unharmed. There is a house with 3 doors.\n"
                     "One red, one yellow, one blue. Which color do you choose? ").lower()
        if door == "red":
            print("Burned by fire. GAME OVER!")
        elif door == "blue":
            print("Eaten by beasts. GAME OVER!")
        elif door == "yellow":
            chest = input("You enter the house and find a dusty chest with two keys\n" \
            "choose 'gold' or 'silver': ").lower()
            if chest == "gold":
                print("Chest is booby-trapped with poison darts. GAME OVER!")
            elif chest == "silver":
               descend_stay = input("You find a hidden staircase leading down, choose 'descend' or 'stay': ").lower()
               if descend_stay == 'stay':
                   print("Floor collapses beneath you.GAME OVER!")
               elif descend_stay == 'descend':
                  tunnels = input("In the chamber, face three tunnels, choose 'left', 'middle', or 'right': ").lower()
                  if tunnels == "left":
                      print("Tunnel leads to a pit of snakes. GAME OVER!")
                  elif tunnels == "right":
                      print("Tunnel collapses. GAME OVER!")
                  elif tunnels == "middle":
                      print("YOU FOUND THE TREASURE, YOU WON!")
                      print(r'''                                               888            
                                               888            
                                               888            
 .d8888b .d88b. 88888b.  .d88b. 888d888 8888b. 888888.d8888b  
d88P"   d88""88b888 "88bd88P"88b888P"      "88b888   88K      
888     888  888888  888888  888888    .d888888888   "Y8888b. 
Y88b.   Y88..88P888  888Y88b 888888    888  888Y88b.      X88 
 "Y8888P "Y88P" 888  888 "Y88888888    "Y888888 "Y888 88888P' 
                             888                              
                        Y8b d88P                              
                         "Y88P"                               ''')
                  else:
                      print("You didn't follow the instructions, 'left', 'middle', or 'right'. GAME OVER!")

               else:
                   print("You didn't follow the instructions, descend or stay. GAME OVER!")

            else:
                print("You didn't follow the instructions, gold or silver key. GAME OVER!")
        else:
            print("You didn't follow the instructions, red door, yellow door, blue door! GAME OVER!")
    else:
        print("You didn't follow the instructions, swim or wait. GAME OVER!")
else:
    print(" You didn't follow the instructions, left or right. GAME OVER!")