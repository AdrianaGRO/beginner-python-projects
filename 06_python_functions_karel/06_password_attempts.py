# 🔐 Password Attempts Project
# Give user 3 attempts to enter correct password

def password_attempts():
    attempts = 0
    password = "?AdrianaPython04"
    while attempts < 3:
        ask = (input("Enter your password:\n"))
        attempts += 1
        if password == ask:
            print("Login successful!")
            break
        else:
            print("Incorrect password, please try again!")

    else:
        print("Allow up to 3 tries, lock out after failed attempts")
        print("Locked out!")

password_attempts()
