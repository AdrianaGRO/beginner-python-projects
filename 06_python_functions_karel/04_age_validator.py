# ✅ Input Validator Project
# Keep asking for input until valid data is entered

def age_validator():
    while True:
        age = int(input("What is your age?\n"))
        if age <=150:
            print("Is a success!")
            break
        else:
            print("I am sorry, your input is invalid, try again.")

age_validator()
