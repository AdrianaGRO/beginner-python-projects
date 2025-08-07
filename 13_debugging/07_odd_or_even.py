# 07 Debugging Odd or Even
# - Read the code in exercise.py
# - Spot the problems 🐞.
# - Modify the code to fix the program. Fix the code so that it works and passes the tests when you submit.
# You can debug functionality from IDE   

# def odd_or_even(number):
#     if number % 2 = 0:
#         return "This is an even number."
#     else:
#         return "This is an odd number."


def odd_or_even(number):
    if number % 2 == 0:
        return "This is an even number."
    else:
        return "This is an odd number."

print(odd_or_even(10))
print(odd_or_even(11))
print(odd_or_even(0))
print(odd_or_even(-1))
print(odd_or_even(-2))
print(odd_or_even(1000000))
print(odd_or_even(-1000000))