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
            print("You are now using the Cobra Climate program.")
            # print('~Type "close" at any time to exit the program.~')
            # print("~Typos can cause loss of progress, consider copy & pasting options.~")
            menu()
            break
    # BLACKLIST
        else:
            print("Incorrect credentials! Try again")
            signin()
            break
        
# Solutions view
def solution():
    # Tutorial
    for solution in cobraMenu:
        if cobraMenu == "solutions":
            print("-" * 30)
            global sol
            sol = input('Type: add, back ')
        if sol == "back":
            print("Leaving the solutions page...")
            menu()
            break
        
# Footprint view
def footprint():
    # Tutorial
    for footprint in cobraMenu:
        if cobraMenu == "footprint":
            print("-" * 30)
            global fp
            fp = input('Type: add, back ')
        if fp == "back":
            print("Leaving the footprint page...")
            menu()
            break

# Tutorial view
def tutorial():
    # Tutorial
    for tutorial in cobraMenu:
        if cobraMenu == "tutorial":
            print("-" * 30)
            global tut
            tut = input('Type: add, back ')
        if tut == "back":
            print("Leaving the tutorial page...")
            menu()
            break
        
# Estimate view
def estimate():
    # Emission Estimate
    for estimator in calc:
        print("-" * 30)
        print("Welcome to the emission estimator")
        print("-" * 30)
        print("Device used (type one):")
        estdevice = input("pc; mobile; ")
            if estdevice == "pc":
                estfp = 
                print("PC/Laptop")
                print("\nHours spent:")
                esttime = input("Hrs: ")
                break
            if estdevice == "mobile":
                print("Mobile device")
                print("\nHours spent:")
                esttime = input("Hrs:")
                
                break
    
# Information view
def information():
    # Information page
    for info in cobraMenu:
        if cobraMenu == "info":
            print("-" * 30)
            global inf
            inf = input('Type: add, back ')
        if inf == "back":
            print("Leaving the information page...")
            menu()
            break

# Calculator page view
def calcPage():
    # Calculator PAGE
    for carbonCalc in cobraMenu:
        if cobraMenu == "carbonCalc":
            global calc
            print("Cobra Climate's Carbon Calculator!")
            calc = input('\nType one: calculate; estimate; back; ')
        if calc == "estimate":
            estimate()
            break
        if calc == "back":
            print("Leaving the carbonCalc page...")
            menu()
            break
        if calc == "calculate":
            calculator()
            break
        else:
            print(calc, "is not an option. Try again.")
            calculator()
            break

# Calculators
def calculator():
    for calculator in calc:
        print("-" * 30)
        print("You are now using the Carbon Calculator")
        print("-" * 30)
        print("\nDevice used:")
        device = input("Type one of the following\npc;\nmobile;\n")

        # PC DEVICE CALCULATOR
        if device == "pc":
            print("-" * 30)
            print("PC/Laptop")
            print("\nAction (type one):")
            action = input("videos;\nwork;\ngaming;\n")
            # VIDEOS
            if action == "videos":
                use = int(55)
                print("\nHours spent:")
                time = input("Hrs: ")
                pcvid = use * int(time)
                print("The footprint of spending", time, "hours watching", action, "using a", device, "is", pcvid, "g CO2e.")
                print("-" * 30)
                calcPage()
                # Add store/don't
                break
            # WORK
            if action == "work":
                use = int(330)
                print("\nHours spent:")
                time = input("Hrs: ")
                pcwork = use * int(time)
                print("The footprint of spending", time, "hours doing", action, "using a", device, "is", pcwork, "g CO2e.")
                print("-" * 30)
                calcPage()
                break
            # GAMING
            if action == "gaming":
                use = int(400)
                print("\nHours spent:")
                time = input("Hrs: ")
                pcgame = use * int(time)
                print("The footprint of spending", time, "hours", action, "using a", device, "is", pcgame, "g CO2e.")
                print("-" * 30)
                calcPage()
                break
            else:
                print("Sorry,", action, "is not an option. Try again.")
                calculator()
                break

        # MOBILE DEVICE CALCULATOR
        if device == "mobile":
            print("-" * 30)
            print("Phone/Tablet")
            print("\nAction (type one):")
            action = input("calling;\ntexting;\nsocialMedia;\n")
            # CALLING
            if action == "calling":
                use = int(80)
                print("\nHours spent:")
                time = input("Hrs: ")
                mbcall = use * int(time)
                print("The footprint of spending", time, "hours", action, "using a", device, "is", mbcall, "g CO2e.")
                print("-" * 30)
                calcPage()
                # Add store/don't
                break
            # TEXTING
            if action == "texting":
                use = int(1)
                print("\nHours spent:")
                time = input("Hrs: ")
                mbtext = use * int(time)
                print("The footprint of spending", time, "hours", action, "using a", device, "is", mbtext, "g CO2e.")
                print("-" * 30)
                calcPage()
                break
            # SOCIAL MEDIA
            if action == "socialMedia":
                print("\nWhich Social Media?")
                media = input("Type one:\ninstagram;\ntiktok;\nother;\n")
                if media == "instagram":
                    use = int(90)
                    print("\nHours spent:")
                    time = input("Hrs: ")
                    mbtext = use * int(time)
                    print("The footprint of spending", time, "hours on", media, "using a", device, "is", mbtext, "g CO2e.")
                    print("-" * 30)
                    calcPage()
                    break
                if media == "tiktok":
                    use = int(180)
                    print("\nHours spent:")
                    time = input("Hrs: ")
                    mbtext = use * int(time)
                    print("The footprint of spending", time, "hours on", media, "using a", device, "is", mbtext, "g CO2e.")
                    print("-" * 30)
                    calcPage()
                    break
                if media == "other":
                    use = int(110)
                    print("\nHours spent:")
                    time = input("Hrs: ")
                    mbtext = use * int(time)
                    print("The footprint of spending", time, "hours on", media, "using a", device, "is", mbtext, "g CO2e.")
                    print("-" * 30)
                    calcPage()
                    break
                else:
                    print("Sorry,", action, "is not an option. Try again.")
                    calculator()
                    break
                break
                
        else:
            print(device, "is not an option. Try again.")
            calculator()
            break
            
# MENU
def menu():
    global cobraMenu
    print("-" * 30)
    print("Type one of the following to view:\n")
    cobraMenu = input("tutorial;\ninfo;\ncarbonCalc\nfootprint;\nsolutions;\nsignout;\n")
    
    for select in cobraMenu:
        # Select tutorial
        if cobraMenu == "tutorial":
            print("-" * 30)
            print("Tutorial")
            print("-" * 30)
            tutorial()
            break
        # Select information
        if cobraMenu == "info":
            print("-" * 30)
            print("Information Interface")
            print("-" * 30)
            information()
            break
        # Select calculator
        if cobraMenu == "carbonCalc":
            print("-" * 30)
            print("Carbon Calculator")
            print("-" * 30)
            calcPage()
            break
        # Select estimator
        if cobraMenu == "emissionEst":
            print("-" * 30)
            print("Emission Estimator")
            print("-" * 30)
            estimate()
            break
        # Select footprint
        if cobraMenu == "footprint":
            print("-" * 30)
            print("Footprint Focus")
            print("-" * 30)
            footprint()
            break
        # Select solutions
        if cobraMenu == "solutions":
            print("-" * 30)
            print("Simple Solutions")
            print("-" * 30)
            solution()
            break
        # Sign out
        if cobraMenu == "signout":
            print("-" * 30)
            print("Signing out of", uname + "...")
            signin()
            break
        else:
            print(cobraMenu, "is not an option. Try again")
            menu()
            break

signin()
