# COBRA CLIMATE
# Sign in 
def signin():
    global uname
    global passw
    # Enter username
    print("+", "-" * 30, "+")
    print(("|" + " " * 30 + "|\n") * 1, end="")
    uname = input("| Enter your username: ")
    print(("|" + " " * 30 + "|\n") * 1, end="")
    print("+", "-" * 30, "+")
    # Enter password
    print(("|" + " " * 30 + "|\n") * 1, end="")
    passw = input("| Enter your password: ")
    print(("|" + " " * 30 + "|\n") * 1, end="")
    print("+", "-" * 30, "+")

    for credentials in uname and passw:
    # WHITELIST
        if uname == "acochez" and passw == "1234":
            print("Welcome, " + uname)
            print("+", "-" * 30, "+")
            menu()
    # BLACKLIST
        else:
            print("Incorrect credentials! Try again")
            signin()
            break

def menu():
    print("You are now on the Cobra Climate app.")
    global cobraMenu
    cobraMenu = input("")

signin()
