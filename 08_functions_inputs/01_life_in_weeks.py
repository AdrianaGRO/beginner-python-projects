"""
Life in Weeks

Inspired by Tim Urban’s “Your Life in Weeks,” this project helps you visualize how much time you have left if you live to 90 years old.

Task:
Create a function called life_in_weeks() that calculates and prints how many weeks you have left until age 90.
- The function should take your current age as an argument.
- It should use math and f-Strings to calculate: (90 - age) * 52
- Output the result in the format:
  You have x weeks left.
  (where x is the calculated number, and don’t forget the full stop!)

Example:
If you call life_in_weeks(56), the output should be:
You have 1768 weeks left.

Note:
For testing, use hard-coded values instead of input().
"""
# Your code here
def life_in_weeks(age):
    weeks_left = (90 - age) * 52
    print(f"You have {weeks_left} weeks left from this life if you are lucky enough to live to 90.")

life_in_weeks(40)
