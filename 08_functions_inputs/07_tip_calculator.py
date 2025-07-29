"""
Tip Calculator

Task:
Create a function called calculate_tip() that calculates and prints the tip and total bill.
- The function should take the bill amount and tip percentage as arguments.
- Use math and f-Strings to calculate the tip and total.
- Output the result in the format:
  For a bill of $X, a Y% tip is $Z. Total: $W
  (where X is the bill amount, Y is the tip percent, Z is the tip, and W is the total, all formatted to two decimals.)

Example:
If you call calculate_tip(50, 15), the output should be:
For a bill of $50, a 15% tip is $7.50. Total: $57.50

Note:
For testing, use hard-coded values instead of input().
"""


def calculate_tip(bill_amount, percentage_tip):
    tip = bill_amount * (percentage_tip/100)
    total_bill = bill_amount + tip
    print(f"For a bill of ${bill_amount}, a {percentage_tip}% tip is ${tip:.2f}. Total: ${total_bill:.2f}")

calculate_tip(50,15)
