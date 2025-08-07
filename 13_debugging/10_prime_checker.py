# 10_Debugging Prime Number Checker
# - Read the code in exercise.py
# - Spot the problems 🐞.
# - Modify the code to fix the program so it works as expected.
# A prime number is only divisible by 1 and itself.

# def is_prime(n):
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#         else:
#             return True
#     return True

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True



print(is_prime(4))  # False
print(is_prime(5))  # True
print(is_prime(1))  # False
print(is_prime(2))  # True
print(is_prime(3))  # True