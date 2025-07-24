# ➕ Number Accumulator Project
# Keep adding numbers until user enters 0

def number_accumulator():
    sum_num = 0
    while True:
        number = int(input("What number do you have in mind?\n"))
        sum_num += number
        print(f"The sum of numbers is: {sum_num}")
        if number == 0:
            print(f"you choose a number that make you loose.")
            break

number_accumulator()
