# ⏱️ Countdown Timer Project
# Count down from a given number to zero

def countdown_timer(seconds):
    while seconds > 0:
        print(f"{seconds}...")
        seconds -= 1
    print("Blast off!")

# Test the countdown timer
countdown_timer(5)
