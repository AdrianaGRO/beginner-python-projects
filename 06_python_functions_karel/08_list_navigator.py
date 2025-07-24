# 🧭 List Navigator Project
# Allow user to navigate through a list with commands

def list_navigator():
    fruits = ["apples", "pears", "peaches", "bananas", "cherries"]
    current_index = 0
    while True:
        print(f"Current item is: {fruits[current_index]}")
        print(f"Position: {current_index + 1} of {len(fruits)}")
        user_command = input("Enter your command(next/previous/quit):\n").lower()
        if user_command == "next":
            if current_index < len(fruits) - 1:
                current_index += 1
            else:
                print(f"Already at the last item")
        elif user_command == "previous":
            if current_index > 0:
                current_index -= 1
            else:
                print(f"Already at the first item")
        elif user_command == "quit":
            print("Goodbye!")
            break
        else:
            print("Invalid command. Use: next, previous or quit")

list_navigator()
