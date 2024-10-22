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
            break
    # BLACKLIST
        else:
            print("Incorrect credentials! Try again")
            signin()
            break
        
def footprint():
    print("Type one of the following to view:")
    view = input("information, calculator")
    for select in footprint:
        if view == "information":
            print("-" * 30)
            print("Information")
            print("-" * 30)

def menu():
    print("You are now using the Cobra Climate program.")
    global cobraMenu
    print("-" * 30)
    print("Type one of the following to view:")
    cobraMenu = input("footprint")
    for menu in cobraMenu:
        if cobraMenu == "footprint":
            print("-" * 30)
            print("Footprint")
            print("-" * 30)
            footprint()
            break
        else:
            print(cobraMenu, "is not an option. Try again")
            menu()
            break

signin()
