# 🧮 Calculator with History Project
#
# Project Requirements:
#
# 1. Create a calculator that supports addition, subtraction, multiplication, and division.
# 2. The calculator should keep a history of all calculations performed during the session.
# 3. Allow the user to view the calculation history at any time.
# 4. Provide an option to clear the history.
# 5. The user should be able to quit the program from a menu.
# 6. Use functions to organize the code for each operation and for displaying/clearing history.
# 7. Use a while loop to keep the program running until the user chooses to quit.
# 8. Handle invalid input gracefully (e.g., non-numeric input, division by zero).
#
# Example menu options:
#   add, subtract, multiply, divide, history, clear, quit
#

#Basic functions

def add(a,b):
    return a + b
def subtract(a,b):
    return a - b
def multiply(a,b):
    return a * b
def divide(a,b):
    return a/ b if b != 0 else "Error: Division by zero"
def exponentiate(a, b):
    return a ** b

# Memory Storage
memory = None

def store_memory(value):
    global memory
    memory = value
    print("Stored in memory")

def recall_memory():
    return memory if memory is not None else "No value in memory"

def clear_memory():
    global memory
    memory = None
    print ("Memory cleared")

history = []
def calculator():

    while True:
        print("\nSimple calculator")
        print("Select operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Exponential (^)")
        print("6. Recall Memory (M)")
        print("7. Clear Memory (MC)")
        print("8. Exit (X)")
        print("9. View History (H)")
        print("10. Clear History (CH)")

        choice = input("Enter choice: ").strip().lower()
        if choice in  ['x', '8']:
            print("Exiting the calculator. Goodbye!")
            break
        elif choice in ['m', '6']:
            print("Memory: ", recall_memory())
            continue
        elif choice in ['mc', '7']:
            clear_memory()
        elif choice in ['h', '9']:
            print("History:")
            for entry in history:
                print(" - ", entry)
            continue
        elif choice in ['ch', '10']:
            history.clear()
            print("History cleared.")
            continue
        if choice not in ['1', '2', '3', '4', '5', '+', '-', '*', '/', '^']:
            print("Invalid input. Try again.")
            continue
        try:
            number_1 = float(input("Add your first number: "))
            number_2 = float(input("Add your second number: "))
        except:
            print("Invalid number. Please enter numeric values")
            continue

        if choice in ["1", "+"]:
            result = add (number_1, number_2)
            history.append(f"{number_1} + {number_2} = {result}")
        elif choice in ['2', '-']:
            result = subtract(number_1,number_2)
            history.append(f"{number_1} - {number_2} = {result}")   
        elif choice in ['3', '*']:
            result = multiply(number_1,number_2)
            history.append(f"{number_1} * {number_2} = {result}")
        elif choice in ['4', '/']:
            result = divide(number_1,number_2)
            history.append(f"{number_1} / {number_2} = {result}")   
        elif choice in ['5', '^']:
            result = exponentiate(number_1,number_2)
            history.append(f"{number_1} ^ {number_2} = {result}")
        else:
            print(f"Result {result}")

        store_option = input("Store result in memory? (y/n): ").strip().lower()
        if store_option == 'y':
            store_memory(result)

if __name__=='__main__':
    calculator()

