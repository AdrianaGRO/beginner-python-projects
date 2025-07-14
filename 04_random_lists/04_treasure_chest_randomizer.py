# 4. Treasure Chest Randomizer - Multiple random selections with inventory tracking
# Uses random.choice() repeatedly to simulate opening multiple treasure chests
# Demonstrates how randomness can create varied outcomes from the same list

# Project Instructions:
# 1. Create a list of possible chest contents (e.g., "gold", "potion", "trap", "gem")
# 2. Ask the user how many chests they want to open
# 3. For each chest, use random.choice() to reveal its content


# Your code goes here:
import random

print("====Welcome to Treasure hunt chest===")
possible_items = [
    # Treasure chests
    "gold", "silver", "copper", "platinum", "jewels", "coins", "treasure", "riches",

    # Consumables
    "potion", "elixir", "scroll", "food", "medicine", "brew", "tonic", "antidote",

    # Hazards
    "trap", "poison", "curse", "mimic", "explosion", "spikes", "gas", "alarm",

    # Valuables
    "gem", "ruby", "diamond", "emerald", "crystal", "pearl", "artifact", "relic",

    # Creatures
    "spider", "snake", "bat", "rat", "scorpion", "bee", "worm", "moth",

    # Weapons/Equipment
    "sword", "shield", "armor", "bow", "dagger", "staff", "ring", "amulet",

    # Magic items
    "wand", "orb", "tome", "rune", "charm", "talisman", "crystal_ball", "enchanted_item",

    # Supplies
    "key", "map", "rope", "torch", "bandage", "lockpick", "compass", "lantern"
]
user_num_chests = int(input("How many chests do you want to open? (1,2 or 3): \n"))

if user_num_chests == 1:
    chest_1 = random.choice(possible_items)
    print(f"You opened one chest, you discovered: {chest_1}.")
elif user_num_chests == 2:
    chest_1 = random.choice(possible_items)
    chest_2 = random.choice(possible_items)
    print(f"You opened two chests, you discovered: {chest_1} and {chest_2}")
elif user_num_chests == 3:
    chest_1 = random.choice(possible_items)
    chest_2 = random.choice(possible_items)
    chest_3 = random.choice(possible_items)
    print(f"You opened three chests, you discovered: {chest_1}, {chest_2} and {chest_3}")
else:
    print("⚠️Please choose the number of chest accordingly with the rules of the game!")

print(f"🎲✨You opened {user_num_chests} chest(s) to play in this game.")
print("🎉Congratulations! You have completed the Treasure Chest Randomizer game!")