# Simulate an ATM withdrawal. 
# Ask the user for their account balance (float) and withdrawal amount (float).
# If the withdrawal amount exceeds the balance, print “Insufficient funds” and keep the balance unchanged.
# elif the withdrawal amount is zero or negative, print “Invalid amount.”
# else, subtract the amount from balance and print the new balance.
# Use nested conditions and print the data type of the final balance.

print(r'''                                  
__        __   _                            _          ____        
\ \      / /__| | ___ ___  _ __ ___   ___  | |_ ___   |  _ \ _   _ 
 \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \ | __/ _ \  | |_) | | | |
  \ V  V /  __/ | (_| (_) | | | | | |  __/ | || (_) | |  __/| |_| |
   \_/\_/_\___|_|\___\___/|_| |_| |_|\___|  \__\___/  |_|    \__, |
   / \|_   _|  \/  |                                         |___/ 
  / _ \ | | | |\/| |                                               
 / ___ \| | | |  | |                                               
/_/   \_\_| |_|  |_| ''')

balance = float(input("Enter your account balance:$ "))
withdrawal_amount = float(input("Enter withdrawal amount:$ "))



if withdrawal_amount > balance:
    print("Insufficient funds in your account!")
elif withdrawal_amount <= 0:
    print("Invalid amount! Please enter a positive amount greater than zero.")
else:
    new_balance = balance - withdrawal_amount
    print(f"Transaction successful!\nYour new balance is {new_balance:.2f}")
    print(f"Data type for new balance is {type(new_balance)}")


