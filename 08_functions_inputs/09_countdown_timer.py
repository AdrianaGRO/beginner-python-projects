"""
Countdown Timer

Task:
Create a function called countdown() that prints numbers counting down to zero.
- The function should take the number of seconds as an argument.
- Output each number on a new line, ending with "Time's up!"

Example:
If you call countdown(5), the output should be:
5
4
3
2
1
0
Time's up!

Note:
For testing, use hard-coded values instead of input().
"""
def countdown(seconds):
    for i in range(seconds, -1, -1):
        second = i
        if second == 0:
            second = "Time's up!"
        else:
            second = str(second)
        print(second)
countdown(seconds=5)