# Problem 3: Function Returns Wrong Value
def multiply(a, b):
    result = a + b
    return result

print(multiply(3, 4))
# Task: This is supposed to multiply, not add. Fix it so it returns the correct result.

def multiply(a, b):
    result = a *b
    return result
   
   
print(multiply(3,4))