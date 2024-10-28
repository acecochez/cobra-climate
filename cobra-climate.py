# COBRA CLIMATE
# Sign in 
def signin():
    
    global uname
    global passw
    
    # ENTER USERNAME
    print("+", "-" * 30, "+")
    print(("|" + " " * 30 + "|\n") * 1, end="")
    uname = input("| Enter your username: ")
    print(("|" + " " * 30 + "|\n") * 1, end="")
    print("+", "-" * 30, "+")
    
    # ENTER PASSWORD
    print(("|" + " " * 30 + "|\n") * 1, end="")
    passw = input("| Enter your password: ")
    print(("|" + " " * 30 + "|\n") * 1, end="")
    print("+", "-" * 30, "+")

    # WHITELIST (valid user)
    for credentials in uname and passw:
        if uname == "acochez" and passw == "1234":
            print("Welcome, " + uname)
            print("+", "-" * 30, "+")         
            print("You are now using the Cobra Climate program.")
            print("~ Typos can cause loss of progress, consider copy & pasting options. ~")
            menu()
            break
        
    # BLACKLIST
        else:
            print("Incorrect credentials! Try again")
            signin()
            break
        
# SOLUTIONS
def solution():
    
    # SELECT
    for solution in cobraMenu:
        if cobraMenu == "solutions":
            global sol
            sol = input('Type:\nPLACEHOLDER;\nback;\n')
            
        # BACK
        if sol == "back":
            print("Leaving the solutions page...")
            menu()
            break
        
        # FALSE OPTION
        else:
            print(sol, "is not an option! Try again.")
            solution()
            break
        
# FOOTPRINT
def footprint():
    
    # SELECT
    for footprint in cobraMenu:
        if cobraMenu == "footprint":
            global fp
            fp = input('Type:\nPLACEHOLDER;\nback;\n')
            
        # BACK
        if fp == "back":
            print("Leaving the footprint page...")
            menu()
            break

        # FALSE OPTION
        else:
            print(fp, "is not an option! Try again.")
            solution()
            break

# TUTORIAL
def tutorial():
    
    # SELECT
    for tutorial in cobraMenu:
        if cobraMenu == "tutorial":
            global tut
            tut = input('Type:\nfullTut;\nsearchTut;\nback;\n')
            
        # BACK
        if tut == "back":
            print("Leaving the tutorial page...")
            menu()
            break
        
        # FALSE OPTION
        else:
            print(tut, "is not an option! Try again.")
            tutorial()
            break
        
# ESTIMATOR
def estimate():
    for estimator in calc:
        print("-" * 30)
        print("Welcome to the emission estimator")
        print("-" * 30)
        
        # SELECT
        print("Device used (type one):")
        estdevice = input("\npc;\nmobile;\nback;")
        
        # PC ESTIMATOR
        if estdevice == "pc":
            estfp = int(500)
            print("PC/Laptop")
            # HOURS
            print("\nHours spent:")
            esttime = input("Hrs: ")
            try:
                pcest = estfp * int(esttime)
                print("The estimated footprint of spending", esttime,\
                      "hours on a", estdevice, "is", pcest, "g CO2e")
                print("-" * 30)
                estimate()
                break
            
            # INVALID INPUT
            except:
                print("Invalid input! Try again.")
                estimate()
                break
        
        # MOBILE ESTIMATOR
        if estdevice == "mobile":
            estfp = int(300)
            print("Mobile device")
            # HOURS
            print("\nHours spent:")
            esttime = input("Hrs: ")
            try:
                mbest = estfp * int(esttime)
                print("The estimated footprint of spending", esttime,\
                      "hours on a", estdevice, "device is", mbest, "g CO2e")
                print("-" * 30)
                estimate()
                break
                
            # INVALID INPUT
            except:
                print("Invalid input! Try again.")
                estimate()
                break
        
        # BACK
        if estdevice == "back":
            print("Leaving the Emission Estimator page...")
            print("-" * 30)
            calcPage()
            break
        
        # FALSE OPTION
        else:
            print(estdevice, "is not an option! Try again.")
            print("-" * 30)
            estimate()
            break
    
# INFORMATION
def information():
    for info in cobraMenu:

        # SELECT
        if cobraMenu == "info":
            global inf
            inf = input('Type:\ndocuments;\nback;\n')
            
            # DOCUMENTATION
            if inf == "documents":
                print("\nDocumentation")
                docs = input("Type to view:\ndata;\ncalcs;\nback;\n")

                # DATA DOCUMENTATION
                if docs == "data":
                    print("\nWhich data would you like to view?")
                    # DATA DICTIONARY
                    datadict = {"estimates" : "Avg CO2e/hr device use (mobile): 300g \
                                \nAvg CO2e/hr device use (PC): 500g",
                                "mobileData" : "CO2/hr phone call: 80g \
                                \nCO2/hr messaging: 20g \
                                \nCO2/hr instagram: 90g \
                                \nCO2/hr tiktok: 180g \
                                \nCO2/hr other social media: 110g",
                                "pcData" : "CO2/hr watching videos: 55g \
                                \nCO2/hr online work: 330g \
                                \nCO2/hr gaming: 500g"
                                }
                    
                    # SELECT DATA
                    data = input("Type to view:\nestimates;\nmobileData;\npcData;\nall;\nback;\n")

                    # ESTIMATES DATA DOCS
                    if data == "estimates":
                        print("-" * 30)
                        print(datadict['estimates'])
                        print("-" * 30)
                        information()
                        break

                    # MOBILE DATA DOCS
                    if data == "mobileData":
                        print("-" * 30)
                        print(datadict['mobileData'])
                        print("-" * 30)
                        information()
                        break

                    # PC DATA DOCS
                    if data == "pcData":
                        print("-" * 30)
                        print(datadict['pcData'])
                        print("-" * 30)
                        information()
                        break

                    # BACK
                    if data == "back":
                        print("Returning to information home page...")
                        information()
                        break

                    # ALL DATA DOCS
                    if data == "all":
                        print("-" * 30)
                        print("Estimates\n")
                        print(datadict['estimates'])
                        print("-" * 30)
                        print("Mobile Device data\n")
                        print(datadict['mobileData'])
                        print("-" * 30)
                        print("PC/Laptop data\n")
                        print(datadict['pcData'])
                        print("-" * 30)
                        information()
                        break

                    # FALSE OPTION
                    else:
                        print(data, "is not an option! Try again.")
                        information()
                        break

                # CALCULATIONS
                if docs == "calcs":
                    # CALCULATIONS DICTIONARY
                    calcdict = {"calculator": "(based on device) ACTION FOOTPRINT * HOURS SPENT = TOTAL FOOTPRINT",
                                "estimator": "AVG DEVICE FOOTPRINT * HOURS SPENT = TOTAL FOOTPRINT"
                                }
                    # SELECT CALCULATIONS
                    calcs = input("Type to view:\ncalculator;\nestimator;\nall;\nback;\n")

                    # CARBONCALC CALCULATIONS
                    if calcs == "calculator":
                        print("-" * 30)
                        print(calcdict['calculator'])
                        print("-" * 30)
                        information()
                        break
                    
                    # ESTIMATOR CALCULATIONS
                    if calcs == "estimator":
                        print("-" * 30)
                        print(calcdict['estimator'])
                        print("-" * 30)
                        information()
                        break

                    # BACK
                    if calcs == "back":
                        print("Leaving the calcs documentation...")
                        information()
                        break

                    # VIEW ALL CALCULATIONS
                    if calcs == "all":
                        print("-" * 30)
                        print("The calculators formulas\n")
                        print(calcdict['calculator'])
                        print("-" * 30)
                        print("The estimators formulas\n")
                        print(calcdict['estimator'])
                        print("-" * 30)
                        information()
                        break

                    # FALSE OPTION
                    else:
                        print(calcs, "is not an option! Try again.")
                        information()
                        break

                # BACK
                if docs == "back":
                    print("Returning to Information page...")
                    information()
                    break
        # BACK
        if inf == "back":
            print("Leaving the information page...")
            menu()
            break

# SELECT CALCULATOR
def calcPage():
    for carbonCalc in cobraMenu:

        # CALCULATOR SELECTOR
        if cobraMenu == "carbonCalc":
            global calc
            print("Cobra Climate's Carbon Calculator!")
            calc = input('\nType one:\ncalculate;\nestimate;\nback;\n')

        # USE ESTIMATOR
        if calc == "estimate":
            estimate()
            break

        # USE CARBON CALCULATOR
        if calc == "calculate":
            calculator()
            break

        # BACK
        if calc == "back":
            print("Leaving the carbonCalc page...")
            menu()
            break

        # FALSE OPTION
        else:
            print(calc, "is not an option. Try again.")
            menu()
            break

# CARBON CALCULATOR
def calculator():
    for calculator in calc:
        print("-" * 30)
        print("You are now using the Carbon Calculator")
        print("-" * 30)

        # SELECT DEVICE
        print("\nDevice used:")
        device = input("Type one of the following\npc;\nmobile;\n")

        # PC DEVICE CALCULATOR
        if device == "pc":
            print("-" * 30)
            print("PC/Laptop")
            
            # ACTION
            print("\nAction (type one):")
            action = input("videos;\nwork;\ngaming;\n")
            
            # VIDEOS
            if action == "videos":
                use = int(55)
                # HOURS
                print("\nHours spent:")
                time = input("Hrs: ")
                try:
                    global pcvid
                    pcvid = use * int(time)
                    print("The footprint of spending", time, "hours watching", action,\
                          "using a", device, "is", pcvid, "g CO2e.")
                    print("-" * 30)

                    # STORE FOOTPRINT
                        # script wants the writing to be a string
                    
                    print("Would you like to store this footprint?")
                    sconf = input("Type: yes; no;\n")
                    if sconf == "yes":
                        stpcvid = str((pcvid))
                        store = open("footprint.txt", "w")
                        store.write(stpcvid)
                        store.close()
                        open1 = open("footprint.txt", "r")
                        print(open1.store())
                        
                        calcPage()
                        break
                    # INVALID INPUT
                except:
                    print("Invalid input! Try again.")
                    calcPage()
                    break

            # FALSE OPTION
            else:
                print("Sorry,", action, "is not an option. Try again.")
                calcPage()
                break
            
            # WORK
            if action == "work":
                use = int(330)
                # HOURS
                print("\nHours spent:")
                time = input("Hrs: ")
                try:
                    pcwork = use * int(time)
                    print("The footprint of spending", time, "hours doing", action,\
                          "using a", device, "is", pcwork, "g CO2e.")
                    print("-" * 30)
                    calcPage()
                    break
                
                # INVALID INPUT
                except:
                    print("Invalid input! Try again.")
                    calcPage()
                    break

            # FALSE OPTION
            else:
                print("Sorry,", action, "is not an option. Try again.")
                calcPage()
                break
            
            # GAMING
            if action == "gaming":
                use = int(500)
                # HOURS
                print("\nHours spent:")
                time = input("Hrs: ")
                try:
                    pcgame = use * int(time)
                    print("The footprint of spending", time, "hours", action,\
                          "using a", device, "is", pcgame, "g CO2e.")
                    print("-" * 30)
                    calcPage()
                    break
                
                # INVALID INPUT
                except:
                    print("Invalid input! Try again.")
                    calcPage()
                    break

            # FALSE OPTION
            else:
                print("Sorry,", action, "is not an option. Try again.")
                calcPage()
                break

        # MOBILE DEVICE CALCULATOR
        if device == "mobile":
            print("-" * 30)
            print("Phone/Tablet")

            # ACTION
            print("\nAction (type one):")
            action = input("calling;\ntexting;\nsocialMedia;\n")
            
            # CALLING
            if action == "calling":
                use = int(80)
                # HOURS
                print("\nHours spent:")
                time = input("Hrs: ")
                try:
                    mbcall = use * int(time)
                    print("The footprint of spending", time, "hours", action,\
                          "using a", device, "is", mbcall, "g CO2e.")
                    print("-" * 30)
                    calcPage()
                    break

                # INVALID INPUT
                except:
                    print("Invalid input! Try again.")
                    calcPage()
                    break
            
            # TEXTING
            if action == "texting":
                use = int(20)
                # HOURS
                print("\nHours spent:")
                time = input("Hrs: ")
                try:
                    mbtext = use * int(time)
                    print("The footprint of spending", time, "hours", action,\
                          "using a", device, "is", mbtext, "g CO2e.")
                    print("-" * 30)
                    calcPage()
                    break

                # INVALID INPUT
                except:
                    print("Invalid input! Try again.")
                    calcPage()
                    break
            
            # SOCIAL MEDIA
            if action == "socialMedia":

                # SELECT SOCIAL MEDIA APP
                print("\nWhich Social Media?")
                media = input("Type one:\ninstagram;\ntiktok;\nother;\n")

                # INSTAGRAM
                if media == "instagram":
                    use = int(90)
                    # HOURS
                    print("\nHours spent:")
                    time = input("Hrs: ")
                    try:
                        mbtext = use * int(time)
                        print("The footprint of spending", time, "hours on", media,\
                              "using a", device, "is", mbtext, "g CO2e.")
                        print("-" * 30)
                        calcPage()
                        break
                        
                    # INVALID INPUT
                    except:
                        print("Invalid input! Try again.")
                        calcPage()
                        break
                
                # TIKTOK
                if media == "tiktok":
                    use = int(180)
                    # HOURS
                    print("\nHours spent:")
                    time = input("Hrs: ")
                    try:
                        mbtext = use * int(time)
                        print("The footprint of spending", time, "hours on", media,\
                              "using a", device, "is", mbtext, "g CO2e.")
                        print("-" * 30)
                        calcPage()
                        break

                    # INVALID INPUT
                    except:
                        print("Invalid input! Try again.")
                        calcPage()
                        break

                # OTHER
                if media == "other":
                    use = int(110)
                    # HOURS
                    print("\nHours spent:")
                    time = input("Hrs: ")
                    try:
                        mbtext = use * int(time)
                        print("The footprint of spending", time, "hours on", media,\
                              "using a", device, "is", mbtext, "g CO2e.")
                        print("-" * 30)
                        calcPage()
                        break

                    # INVALID INPUT
                    except:
                        print("Invalid input! Try again.")
                        calcPage()
                        break
                
                # FALSE OPTION
                else:
                    print("Sorry,", action, "is not an option. Try again.")
                    calcPage()
                    break

        # FALSE OPTION
        else:
            print(device, "is not an option. Try again.")
            calcPage()
            break
            
# MENU
def menu():
    global cobraMenu
    print("-" * 30)

    # SELECT
    print("Type one of the following to view:\n")
    cobraMenu = input("tutorial;\ninfo;\ncarbonCalc\nfootprint;\nsolutions;\nsignout;\n")
    
    for select in cobraMenu:
        
        # SELECT TUTORIAL
        if cobraMenu == "tutorial":
            print("-" * 30)
            print("Tutorial")
            print("-" * 30)
            tutorial()
            break
        
        # SELECT INFORMATION
        if cobraMenu == "info":
            print("-" * 30)
            print("Information Interface")
            print("-" * 30)
            information()
            break
        
        # SELECT CALCULATOR
        if cobraMenu == "carbonCalc":
            print("-" * 30)
            print("Carbon Calculator")
            print("-" * 30)
            calcPage()
            break
        
        # SELECT ESTIMATOR
        if cobraMenu == "emissionEst":
            print("-" * 30)
            print("Emission Estimator")
            print("-" * 30)
            estimate()
            break
        
        # SELECT FOOTPRINT
        if cobraMenu == "footprint":
            print("-" * 30)
            print("Footprint Focus")
            print("-" * 30)
            footprint()
            break
        
        # SELECT SOLUTIONS
        if cobraMenu == "solutions":
            print("-" * 30)
            print("Simple Solutions")
            print("-" * 30)
            solution()
            break
        
        # SIGN OUT
        if cobraMenu == "signout":
            print("-" * 30)
            print("Signing out of", uname + "...")
            signin()
            break

        # FALSE OPTION
        else:
            print(cobraMenu, "is not an option. Try again")
            menu()
            break

# LAUNCH PROGRAM
signin()
