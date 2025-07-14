# 1. Random Heads or Tails - Coin flip simulator
# Uses random.randint(0, 1) to generate either 0 or 1
# 0 = Tails, 1 = Heads
# This simulates flipping a real coin with 50/50 probability

import random   

print("Welcome to Coin Flip")

computer_choose = random.randint(0, 1)
print(computer_choose)
if computer_choose == 0:
    print("Tail")
else:
    print("Head")
