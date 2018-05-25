#Bottom Golf v 1.0 last update 5/24/18
#FULL VERSION FINISHED
#Added a multiplayer option for two people to play on one screen

#1-2 players, login/out, 2 clubs, 360 directions, barriers, hole, obsicle
#Tested with both players and functions properly
#Going to add an "online mode" and a computer mode, which will both be CPU's, look diferent
#All information is properly displayed
#No Audio currently added
#Sometimes the login will give you three attempts on diferent tries of opening the game

################################### MIC. ##########################################

global attempts
import tkinter as tk
from tkinter import ttk
import os
import time
import random
import time #The time stuff just lets me add a time stamp on the ledger part.
ts = time.gmtime()
time_formatted=(time.strftime("%Y-%m-%d %H:%M:%S", ts))

############################## FUNCTIONALITY ##########################################

class Position: #Position system.
    def __init__(self, initx, inity, initD):
        self.x = initx #x and y positions.
        self.y = inity
        self.D = initD

    def getx(self): #Returns x position of the ball.
        return self.x

    def gety(self): #Returns y position of the ball.
        return self.y

    def getD(self): #Returns direction of the ball.
        return self.D

    def __str__(self): #Returns the ball's details in string form.
        return ("Full stats (x,y,direction: " +str(self.x)+ "," +str(self.y)+ "," +str(self.D)+"°")

    def distanceFromOrigin(self): #Determines the length from the x position to the y position.
        return ((self.x **2) + (self.y ** 2)) ** .5

Ball_W = Position(0,0,0)
randlength = random.randrange(8,16)
scoretype = 0

################################ MENUS  (1) ##########################################

def menu(): #A simple hub allowing the user to do anything without admin privliges.
    global attempts
    attempts = 3
    print ('''
   ____     U  ___ u _____    _____   U  ___ u  __  __         ____    U  ___ u   _       _____  
U | __")u    \/"_ \/|_ " _|  |_ " _|   \/"_ \/U|' \/ '|u    U /"___|u   \/"_ \/  |"|     |" ___| 
 \|  _ \/    | | | |  | |      | |     | | | |\| |\/| |/    \| |  _ /   | | | |U | | u  U| |_  u 
  | |_) |.-,_| |_| | /| |\    /| |\.-,_| |_| | | |  | |      | |_| |.-,_| |_| | \| |/__ \|  _|/  
  |____/  \_)-\___/ u |_|U   u |_|U \_)-\___/  |_|  |_|       \____| \_)-\___/   |_____| |_|     
 _|| \\\_       \\\   _// \\\_  _// \\\_     \\\   <<,-,,-.        _)(|_       \\\     //  \\\  )(\\\,-  
(__) (__)     (__) (__) (__)(__) (__)   (__)   (./  \.)      (__)__)     (__)   (_")("_)(__)(_/  

_.-=*"*=-._.-=*"*=-._
|1-Login
|2-Create Profile
|3-Administration
|4-Quit
"*=-._.-=*"*=-._.-=*"''')
    opt1 = input ("|")
    if opt1 == "1":
        os.system('cls')
        login()
    if opt1 == "2":
        os.system('cls')
        create()
    if opt1 == "3":
        os.system('cls')
        aduse = input ("You will never guess my super secret administation username!|")
        adpass = input ("Or the administation password!|")
        if aduse == "admin" and adpass == "1111": #hardcoded username and password
            os.system('cls')
            time.sleep(.5)
            print(".")
            time.sleep(1)
            print(".")
            time.sleep(1)
            print(".")
            time.sleep(3)
            os.system('cls')
            print("Gosh dang it...")
            time.sleep(1)
            admin()
        else:
            print ("Incorrect username or password")
            print ("")
            menu()
    if opt1 == "4":
        quit()
    else: #Redirects user back to this menu if they mess up.
        print("Input unknown, please try again!")
        print ("")
        menu()

def admin():
    os.system('cls')
    print ('''
   ____     U  ___ u _____    _____   U  ___ u  __  __         ____    U  ___ u   _       _____  
U | __")u    \/"_ \/|_ " _|  |_ " _|   \/"_ \/U|' \/ '|u    U /"___|u   \/"_ \/  |"|     |" ___| 
 \|  _ \/    | | | |  | |      | |     | | | |\| |\/| |/    \| |  _ /   | | | |U | | u  U| |_  u 
  | |_) |.-,_| |_| | /| |\    /| |\.-,_| |_| | | |  | |      | |_| |.-,_| |_| | \| |/__ \|  _|/  
  |____/  \_)-\___/ u |_|U   u |_|U \_)-\___/  |_|  |_|       \____| \_)-\___/   |_____| |_|     
 _|| \\\_       \\\   _// \\\_  _// \\\_     \\\   <<,-,,-.        _)(|_       \\\     //  \\\  )(\\\,-  
(__) (__)     (__) (__) (__)(__) (__)   (__)   (./  \.)      (__)__)     (__)   (_")("_)(__)(_/  

₳Đ₥ł₦ ₱Ø₩ɆⱤ!
_.-=*"*=-._.-=*"*=-._
|1-Delete User
|2-Change User
|3-Main Menu
"*=-._.-=*"*=-._.-=*"''')
    opt2 = input ("|")
    if opt2 == "1":
        os.system('cls')
        delete()
    if opt2 == "2":
        os.system('cls')
        change()
    if opt2 == "3":
        os.system('cls')
        menu()
    else: #Redirects user back to this menu if they mess up.
        print("Input unknown, please try again!")
        print ("")
        admin()

def create(): #Allows only an admin to create usernames and passwords.
        newuser = input ("Make your username unique.|")
        newpass = input ("Make a password.|")
        os.system('cls')
        caprand = random.randrange(1,3)
        print ("Type the letters you see. (Make sure to include spaces and capital letters)") #Just a fun captcha bit I added.
        print ("___________________________________________________________________________")
        if caprand == 1:
            print ("|͇ Λ ͇| |͇ ͇͇| ͇ ͇\̿ ͇ ͇\̿  |̶̿' |͇̿ ͇̿| |̶̿' |̶̿' | |̿ \͇|") #"Wuss poppin" in a wierd font I looked up.
            print ("___________________________________________________________________________")
            print ("")
            notarobo = input ("|")
        if caprand == 2:
            print ("ȻȺⱣŦȻĦȺ") #"CAPTCHA" in a wierd font I looked up.
            print ("___________________________________________________________________________")
            print ("")
            notarobo = input ("|")
        userwords = open("logins.txt", "r") #\/-- Checks file to see if the user name that the user entered is already taken.
        nucheck = userwords.readline()
        while nucheck:
            usepass = nucheck.split()
            if newuser == usepass[0]: 
                print ("That username is already taken!")
                print ("")
                create()
            elif newuser == "unique": 
                print ("Do you think that's funny?")
                print ("")
                create()
            nucheck = userwords.readline() #Assures that the program checks more than one line.
        else:
            upcreator = open("logins.txt", "a")
            upcreator.write("" +str(newuser)+ " " +str(newpass))#Keeps a record of their account.
            upcreator.write("\n") #This is so that the .txt file does not just have one big line of entrys.
            upcreator.close()
            print ("")
            menu()

def delete(): #Allows only an admin to delete usernames and passwords.
    deluser = input ("Enter the username that you would like to delete.|")
    delpass = input ("Enter the password that you would like to delete.|")
    os.system('cls')
    deluserwords = open("logins.txt", "r") #\/-- Checks file to see if the user name that the user entered is already taken.
    templist = []
    for line in deluserwords:
        delusepass = line.split()
        if deluser != delusepass[0]: #Makes sure that both the username and password are in the same line.
            if delpass != delusepass[1]:
                templist.append(line)
    newfile = open('logins.txt','w')
    for x in templist:
        newfile.write(x) #Writes the usernames and passwords line by line to the file.
    print (templist)
    deluserwords.close()
    newfile.close()
    admin()

def change(): #Allows only an admin to delete usernames and passwords.
    chauser = input ("Enter the username that you would like to change.|")
    chapass = input ("Enter what you want to change the password to.|")
    os.system('cls')
    chauserwords = open("logins.txt", "r") #\/-- Checks file to see if the user name that the user entered is already taken.
    ok = 0
    templist = []
    for line in chauserwords:
        chausepass = line.split()
        if chauser != chausepass[0]: #Makes sure that both the username and password are in the same line.
            if chapass != chausepass[1]:
                templist.append(line)
        else:
            if chauser == chausepass[0]: #Only needs the username then, step by step, rewrites the line.
                templist.append(chauser)
                templist.append(" ")
                templist.append(chapass)
                print ("Success! The specified user's password has been changed!")
                ok = 1 #This assures that if the user is there, it doesn't say user not found.
    if ok == 0: #If this variable is not changed the whole loop, it prooves the user is not found and sais so.
        print ("User not foud try again...")
        print ("")
        change()
    newfile = open('logins.txt','w')
    for x in templist:
        newfile.write(x) #Writes the usernames and passwords line by line to the file.
    chauserwords.close()
    newfile.close()
    admin()

def login():
    global attempts, username, password, ifsuccess
    global usepass #If I don't have this, it will say that "usepass" was used before, so I used global and it worked!
    if attempts == 0: #I put this up here because if it was lower, it would error before it got the chance to check.
            print ("You have exceeded your login attempts!")
            print ("Now go away!") #Just to be nice.
            ifsuccess = ("Unsuccessful")
            quit()
    print ('''
   ____     U  ___ u _____    _____   U  ___ u  __  __         ____    U  ___ u   _       _____  
U | __")u    \/"_ \/|_ " _|  |_ " _|   \/"_ \/U|' \/ '|u    U /"___|u   \/"_ \/  |"|     |" ___| 
 \|  _ \/    | | | |  | |      | |     | | | |\| |\/| |/    \| |  _ /   | | | |U | | u  U| |_  u 
  | |_) |.-,_| |_| | /| |\    /| |\.-,_| |_| | | |  | |      | |_| |.-,_| |_| | \| |/__ \|  _|/  
  |____/  \_)-\___/ u |_|U   u |_|U \_)-\___/  |_|  |_|       \____| \_)-\___/   |_____| |_|     
 _|| \\\_       \\\   _// \\\_  _// \\\_     \\\   <<,-,,-.        _)(|_       \\\     //  \\\  )(\\\,-  
(__) (__)     (__) (__) (__)(__) (__)   (__)   (./  \.)      (__)__)     (__)   (_")("_)(__)(_/  

''')
    username = input ("What is your Username?|") #\/-- Asks for bother username
    password = input ("What is your Password?|") #and password at the same time.
    userwords = open("logins.txt", "r")
    uwcheck = userwords.readline()
    while uwcheck and attempts > 0:
        usepass = uwcheck.split()
        if username == usepass[0]: #\/-- Makes sure that the username and password 
            if password == usepass[1]: #have to be correct (and in oreder).
                print ("Logging in")
                time.sleep(1)
                print (".")
                time.sleep(1)
                print (".")
                time.sleep(1)
                print (".")
                time.sleep(1)
                os.system('cls')
                ifsuccess = ("Successful")
                ledger()
                loginmenu()
        uwcheck = userwords.readline()
    if username != usepass[0]: #Makes sure that you can only try to log in three times before it quits.
        if password != usepass[1]:
            attempts = attempts - 1
    os.system('cls')
    print ("Incorrect, you have", attempts, "attempts left!")
    ifsuccess = ("Unsuccessful")
    ledger()
    userwords.close() #Assures you can run this program as many times as needed.
    print ("")
    login()

def ledger():
    global username, password, ifsuccess
    ledcheck = open("logged_in.txt", "a")
    ledcheck.write("" +str(username)+ " " +str(password)+ " " +str(ifsuccess)+ " " +str(time_formatted)+ "") #Shows what was tryed, when, and if it was successful, with spacing inbetween.
    ledcheck.write("\n") #This is so that the .txt file does not just have one big line of entrys.
    ledcheck.close()

################################ MENUS (2) ##########################################
    
def loginmenu():
    print ('''
   ____     U  ___ u _____    _____   U  ___ u  __  __         ____    U  ___ u   _       _____  
U | __")u    \/"_ \/|_ " _|  |_ " _|   \/"_ \/U|' \/ '|u    U /"___|u   \/"_ \/  |"|     |" ___| 
 \|  _ \/    | | | |  | |      | |     | | | |\| |\/| |/    \| |  _ /   | | | |U | | u  U| |_  u 
  | |_) |.-,_| |_| | /| |\    /| |\.-,_| |_| | | |  | |      | |_| |.-,_| |_| | \| |/__ \|  _|/  
  |____/  \_)-\___/ u |_|U   u |_|U \_)-\___/  |_|  |_|       \____| \_)-\___/   |_____| |_|     
 _|| \\\_       \\\   _// \\\_  _// \\\_     \\\   <<,-,,-.        _)(|_       \\\     //  \\\  )(\\\,-  
(__) (__)     (__) (__) (__)(__) (__)   (__)   (./  \.)      (__)__)     (__)   (_")("_)(__)(_/  

_.-=*"*=-._.-=*"*=-._
|1-[PLAY]
|2-[HOW TO PLAY]
|3-[LOG OUT]
|4-[QUIT]
"*=-._.-=*"*=-._.-=*"''')
    opt2 = input ("|")
    if opt2 == "1":
        os.system('cls')
        playopt()
    elif opt2 == "2":
        os.system('cls')
        htp()
    elif opt2 == "3":
        os.system('cls')
        menu()
    elif opt2 == "4":
        quit()
    else: #Redirects user back to this menu if they mess up.
        print("Input unknown, please try again!")
        print ("")
        loginmenu()

def playopt(): #This is for deciding weather to keep giving the inputs to one person, or take turns.
    global playtype
    print ('''_.-=*"*=-._.-=*"*=-._
|1-[SINGLE PLAYER]
|2-[MULTIPLAYER]
|3-[BACK]
"*=-._.-=*"*=-._.-=*"''')
    opt3 = input ("|")
    if opt3 == "1":
        os.system('cls')
        playtype = "single"
        gen_hole()
    elif opt3 == "2":
        os.system('cls')
        playtype = "2"
        gen_hole()
    elif opt3 == "3":
        os.system('cls')
        loginmenu()
    else: #Redirects user back to this menu if they mess up.
        print("Input unknown, please try again!")
        print ("")
        playopt()

############################ STARTING A GAME ########################################

def gen_hole(): #This creates the course to be played along with player stats and generally the entire setting of the game.
    global Ball_W1, Ball_W2, randlength, randwidth, scoretype1, scoretype2, holey, holex, club, scoredict, wind, rock, rockx, rocky, playtype
    Ball_W1 = Position(0,0,0) #Resets the P1 ball's position.
    Ball_W2 = Position(0,0,0) #Resets the P2 ball's position.
    club = "driver"
    randlength = random.randrange(70,101) #Generates a randomly sized course v.
    randwidth = random.randrange(40,61)
    scoretype1 = 0 #Resets the number of shots taken.
    scoretype2 = 0
    scoredict = "none"
    holey = randlength - 5
    holex = random.randrange(-15,16) #Makes a hole
    rockx = random.randrange(0,101)
    rocky = random.randrange(-60,61) #Makes an obstical.
    rock = Position(rockx,rocky,0)
    if rockx == 0 and rocky == 0 or rockx >= ((randwidth / 2) + 1) or rockx <= ((randwidth / -2) - 1) or rocky >= (randlength + 1) or rocky <= 0:
        gen_hole()
    if playtype == "single": #This is what "playopt()" was for.
        play1()
    elif playtype == "2":
        two_player_rand = random.randrange(1,3)
        if two_player_rand == 1:
            play1()
        elif two_player_rand == 2:
            play2()
        else:
            print ("Uh oh, something went wrong! Resetting game...")
            gen_hole()
    else:
        print ("Uh oh, something went wrong! Resetting game...")
        gen_hole()

################################## PLAYER 1 ##########################################
    
def play1(): #This tells the player everything they need about the course, where they are, and asks them what to do as far as hitting the ball.
    global NewClub, NewDirection, NewDistance, Ball_W1, randlength, randwidth, scoretype1, scoredict, club, holey, holex, wind, rock, rockx, rocky, player, username
    player = 1
    wind = 0
    print ("The first stage is " +str(randlength)+ " inches long and is " +str(randwidth)+ " inches wide.") #V Tells the user all the stats they need to make their next shot.
    print ("The hole's y position is " +str(holey)+ ", and it's x position is " +str(holex)+ ".")
    print ("There is a rock at x = " +str(rockx)+ ", and y = " +str(rocky)+ ".")
    print ("")
    print ("It's [" +str(username)+ "]'s turn for a swing!") #V Displays everything required about the hole and player.
    print ("You have currently taken " +str(scoretype1)+ " shot(s).")
    print ("Your current position is (" +str(Ball_W1.getx())+ ","+str(Ball_W1.gety())+ ") ((x,y))")
    print ("You are currently aiming " +str(Ball_W1.getD())+ "°.")
    
    try: #V Asks for all contributing factors for hitting the ball
        NewClub = int(input ("Which club would you like to use? (1 = putter, 2 = driver)|"))
        NewDirection = int(input ("What direction will you be aiming? (in degrees and between -180° and 180°)|"))
        NewDistance = int(input ("How hard will you hit the ball? (in a number from 0 - 10)|"))
    except (ValueError): #Assures the inputs are numbers.
        print ("All entrys must be numbers!")
        NewDirection = 0
        NewDistance = 0
        NewClub = 2
        play1()
            
    OWMYBRAIN1()

def OWMYBRAIN1(): #This function mostly consists of math and such that I didn't like looking at, so I put it in another function.
    global NewClub, NewDirection, NewDistance, Ball_W1, randlength, randwidth, scoretype1, scoredict, club, holey, holex, wind, rock, rockx, rocky, playtype, username
    if NewDirection >= -180 and NewDirection <= 180 and NewDistance >= 0 and NewDistance <= 10 and NewClub == 1 or NewClub == 2 or NewClub == 200 or NewDirection == 200 or NewDistance == 200:
        if NewClub == 1: #gives the club inputs string names.
            club = "putter"
        elif NewClub == 2:
            club = "driver"
        elif NewClub == 200: #This defines the quit option inbedded in the hotkey "200".
            print ("Quitting game...")
            time.sleep(2)
            quit()
        if NewDistance == 200:
            print ("Quitting game...")
            time.sleep(2)
            quit()
        if NewDirection == 200:
            print ("Quitting game...")
            time.sleep(2)
            quit()
        if club == "driver": #Defining how far a driver club hits.
            DupDistance = NewDistance * 10
        else:
            DupDistance = NewDistance
        scoretype1 = scoretype1 + 1
        AddDistancey = Ball_W1.gety()
        AddDistancex = Ball_W1.getx()

        if NewDirection == 0: #Facing straight
            NewDistance = 0
            for x in range(DupDistance): #Adds one to the distance the ball travels the number of the value based on the user's power input.
                NewDistance = (NewDistance + 1) - NewDistance
                AddDistancey = AddDistancey + NewDistance
                AddDistancex = AddDistancex + int(wind / 10)
                if AddDistancey == holey and AddDistancex == holex: #This (and all parts of code like it) check if the ball has hit the hole.
                    if scoretype1 == 1: #This defines what type of score the user got based on their number of shots.
                        scoredict = "[HOLE-IN-ONE!]"
                    elif scoretype1 == 2:
                        scoredict = "BIRDIE!"
                    elif scoretype1 == 3:
                        scoredict = "Par!"
                    elif scoretype1 == 4:
                        scoredict = "Bogey"
                    elif scoretype1 == 5:
                        scoredict = "double bogey"
                    elif scoretype1 >= 6:
                        scoredict = "nIcE tRy..." 
                    else:
                        print ("Uh oh, something went wrong! Resetting game...")
                        gen_hole()
                    fplay1()
        if NewDirection <= 89 and NewDirection >= 1: #Facing upper right
            NewDistance = 0
            for x in range(DupDistance): #Adds one to the distance the ball travels the number of the value based on the user's power input.
                NewDistance = (NewDistance + 1) - NewDistance
                AddDistancey = AddDistancey + (float(NewDistance) / 2)
                AddDistancex = AddDistancex + ((NewDistance / 2)+ int(wind / 10))
                if AddDistancey == holey and AddDistancex == holex: #This (and all parts of code like it) check if the ball has hit the hole.
                    if scoretype1 == 1: #This defines what type of score the user got based on their number of shots.
                        scoredict = "[HOLE-IN-ONE!]"
                    elif scoretype1 == 2:
                        scoredict = "BIRDIE!"
                    elif scoretype1 == 3:
                        scoredict = "Par!"
                    elif scoretype1 == 4:
                        scoredict = "Bogey"
                    elif scoretype1 == 5:
                        scoredict = "double bogey"
                    elif scoretype1 >= 6:
                        scoredict = "nIcE tRy..." 
                    else:
                        print ("Uh oh, something went wrong! Resetting game...")
                        gen_hole()
                    fplay1()
        if NewDirection == 90: #Facing right
            NewDistance = 0
            for x in range(DupDistance): #Adds one to the distance the ball travels the number of the value based on the user's power input.
                NewDistance = (NewDistance + 1) - NewDistance
                AddDistancex = AddDistancex + (NewDistance + int(wind / 10))
                if AddDistancey == holey and AddDistancex == holex: #This (and all parts of code like it) check if the ball has hit the hole.
                    if scoretype1 == 1: #This defines what type of score the user got based on their number of shots.
                        scoredict = "[HOLE-IN-ONE!]"
                    elif scoretype1 == 2:
                        scoredict = "BIRDIE!"
                    elif scoretype1 == 3:
                        scoredict = "Par!"
                    elif scoretype1 == 4:
                        scoredict = "Bogey"
                    elif scoretype1 == 5:
                        scoredict = "double bogey"
                    elif scoretype1 >= 6:
                        scoredict = "nIcE tRy..." 
                    else:
                        print ("Uh oh, something went wrong! Resetting game...")
                        gen_hole()
                    fplay1()
        if NewDirection <= 179 and NewDirection >= 91: #Facing bottom right
            NewDistance = 0
            for x in range(DupDistance): #Adds one to the distance the ball travels the number of the value based on the user's power input.
                NewDistance = (NewDistance + 1) - NewDistance
                AddDistancey = AddDistancey + (NewDistance / -2)
                AddDistancex = AddDistancex + ((NewDistance / 2)+ int(wind / 10))
                if AddDistancey == holey and AddDistancex == holex: #This (and all parts of code like it) check if the ball has hit the hole.
                    if scoretype1 == 1: #This defines what type of score the user got based on their number of shots.
                        scoredict = "[HOLE-IN-ONE!]"
                    elif scoretype1 == 2:
                        scoredict = "BIRDIE!"
                    elif scoretype1 == 3:
                        scoredict = "Par!"
                    elif scoretype1 == 4:
                        scoredict = "Bogey"
                    elif scoretype1 == 5:
                        scoredict = "double bogey"
                    elif scoretype1 >= 6:
                        scoredict = "nIcE tRy..." 
                    else:
                        print ("Uh oh, something went wrong! Resetting game...")
                        gen_hole()
                    fplay1()
        if NewDirection == 180 or NewDirection == -180: #Facing straight down
            NewDistance = 0
            for x in range(DupDistance): #Adds one to the distance the ball travels the number of the value based on the user's power input.
                NewDistance = (NewDistance + 1) - NewDistance
                AddDistancey = AddDistancey + (NewDistance / -1)
                AddDistancex = AddDistancex + int(wind / 10)
                if AddDistancey == holey and AddDistancex == holex: #This (and all parts of code like it) check if the ball has hit the hole.
                    if scoretype1 == 1: #This defines what type of score the user got based on their number of shots.
                        scoredict = "[HOLE-IN-ONE!]"
                    elif scoretype1 == 2:
                        scoredict = "BIRDIE!"
                    elif scoretype1 == 3:
                        scoredict = "Par!"
                    elif scoretype1 == 4:
                        scoredict = "Bogey"
                    elif scoretype1 == 5:
                        scoredict = "double bogey"
                    elif scoretype1 >= 6:
                        scoredict = "nIcE tRy..." 
                    else:
                        print ("Uh oh, something went wrong! Resetting game...")
                        gen_hole()
                    fplay1()
        if NewDirection <= -179 and NewDirection >= -91: #Facing bottom left
            NewDistance = 0
            for x in range(DupDistance): #Adds one to the distance the ball travels the number of the value based on the user's power input.
                NewDistance = (NewDistance + 1) - NewDistance
                AddDistancey = AddDistancey + (NewDistance / -2)
                AddDistancex = AddDistancex + ((NewDistance / -2)+ int(wind / 10))
                if AddDistancey == holey and AddDistancex == holex: #This (and all parts of code like it) check if the ball has hit the hole.
                    if scoretype1 == 1: #This defines what type of score the user got based on their number of shots.
                        scoredict = "[HOLE-IN-ONE!]"
                    elif scoretype1 == 2:
                        scoredict = "BIRDIE!"
                    elif scoretype1 == 3:
                        scoredict = "Par!"
                    elif scoretype1 == 4:
                        scoredict = "Bogey"
                    elif scoretype1 == 5:
                        scoredict = "double bogey"
                    elif scoretype1 >= 6:
                        scoredict = "nIcE tRy..." 
                    else:
                        print ("Uh oh, something went wrong! Resetting game...")
                        gen_hole()
                    fplay1()
        if NewDirection == -90: #Facing left
            NewDistance = 0
            for x in range(DupDistance): #Adds one to the distance the ball travels the number of the value based on the user's power input.
                NewDistance = (NewDistance + 1) - NewDistance
                AddDistancex = AddDistancex + ((NewDistance / -1) + int(wind / 10))
                if AddDistancey == holey and AddDistancex == holex: #This (and all parts of code like it) check if the ball has hit the hole.
                    if scoretype1 == 1: #This defines what type of score the user got based on their number of shots.
                        scoredict = "[HOLE-IN-ONE!]"
                    elif scoretype1 == 2:
                        scoredict = "BIRDIE!"
                    elif scoretype1 == 3:
                        scoredict = "Par!"
                    elif scoretype1 == 4:
                        scoredict = "Bogey"
                    elif scoretype1 == 5:
                        scoredict = "double bogey"
                    elif scoretype1 >= 6:
                        scoredict = "nIcE tRy..." 
                    else:
                        print ("Uh oh, something went wrong! Resetting game...")
                        gen_hole()
                    fplay1()
        if NewDirection <= -89 and NewDirection >= -1: #Facing upper left
            NewDistance = 0
            for x in range(DupDistance): #Adds one to the distance the ball travels the number of the value based on the user's power input.
                NewDistance = (NewDistance + 1) - NewDistance
                AddDistancey = AddDistancey + (NewDistance / 2)
                AddDistancex = AddDistancex + ((NewDistance / -2)+ int(wind / 10))
                if AddDistancey == holey and AddDistancex == holex: #This (and all parts of code like it) check if the ball has hit the hole.
                    if scoretype1 == 1: #This defines what type of score the user got based on their number of shots.
                        scoredict = "[HOLE-IN-ONE!]"
                    elif scoretype1 == 2:
                        scoredict = "BIRDIE!"
                    elif scoretype1 == 3:
                        scoredict = "Par!"
                    elif scoretype1 == 4:
                        scoredict = "Bogey"
                    elif scoretype1 == 5:
                        scoredict = "double bogey"
                    elif scoretype1 >= 6:
                        scoredict = "nIcE tRy..." 
                    else:
                        print ("Uh oh, something went wrong! Resetting game...")
                        gen_hole()
                    fplay1()

        if AddDistancex == rockx and AddDistancey == rocky: #This (and all parts of code like it) check if the ball has hit a rock.
            AddDistancey = AddDistancey - 10
        if AddDistancex >= ((randwidth / 2) + 1): #V This complicated batch tests to see if the player has overshot, and exited the course.
            if AddDistancey >= (randlength + 1) or AddDistancey <= 0:
                os.system('cls')
                print ("You over shot, placing user back to previous location...")
                print ("")
                play2()
        elif AddDistancex <= ((randwidth / -2) - 1):
            if AddDistancey >= (randlength + 1) or AddDistancey <= 0:
                os.system('cls')
                print ("You over shot, placing user back to previous location...")
                print ("")
                play2()
        else:
            Ball_W1 = Position(AddDistancex,AddDistancey,NewDirection)
        if AddDistancey == holey and AddDistancex == holex: #This (and all parts of code like it) check if the ball has hit the hole.
            if scoretype1 == 1: #This defines what type of score the user got based on their number of shots.
                scoredict = "[HOLE-IN-ONE!]"
            elif scoretype1 == 2:
                scoredict = "BIRDIE!"
            elif scoretype1 == 3:
                scoredict = "Par!"
            elif scoretype1 == 4:
                scoredict = "Bogey"
            elif scoretype1 == 5:
                scoredict = "double bogey"
            elif scoretype1 >= 6:
                scoredict = "nIcE tRy..." 
            else:
                print ("Something went wrong! Resetting game...")
                gen_hole()
            fplay1()
        else:
            os.system('cls')
            if playtype == "single": #This is also what "playopt()" was for.
                play1()
            elif playtype == "2":
                play2()
    else:
        os.system('cls')
        print ("Club must be a number between 1 and 2!")
        print ("Degree of angle must be a number between -180 and 180!")
        print ("Measure of power must be a number between 0 and 10!")
        play1()

def fplay1(): #This activates when the game ends, it displays what the winning players score was, and sends them back to the loginmenu.
    os.system('cls')
    print (scoredict)
    time.sleep(3)
    os.system('cls')
    loginmenu()

################################## PLAYER 2 ##########################################
    
def play2(): #All the basic programming for player 2 remains the same as player one, only variable names have changed.
    global NewClub, NewDirection, NewDistance, Ball_W2, randlength, randwidth, scoretype2, scoredict, club, holey, holex, wind, rock, rockx, rocky, player
    player = 2
    username2 = "Player 2" #I will delete this and global username for the final project.
    wind = 0
    print ("The first stage is " +str(randlength)+ " inches long and is " +str(randwidth)+ " inches wide.") #V Tells the user all the stats they need to make their next shot.
    print ("The hole's y position is " +str(holey)+ ", and it's x position is " +str(holex)+ ".")
    print ("There is a rock at x = " +str(rockx)+ ", and y = " +str(rocky)+ ".")
    print ("")
    print ("It's [" +str(username2)+ "]'s turn for a swing!") #V Displays everything required about the hole and player.
    print ("You have currently taken " +str(scoretype2)+ " shot(s).")
    print ("Your current position is (" +str(Ball_W2.getx())+ ","+str(Ball_W2 .gety())+ ") ((x,y))")
    print ("You are currently aiming " +str(Ball_W2.getD())+ "°.")
    
    try: #V Asks for all contributing factors for hitting the ball
        NewClub = int(input ("Which club would you like to use? (1 = putter, 2 = driver)|"))
        NewDirection = int(input ("What direction will you be aiming? (in degrees and between -180° and 180°)|"))
        NewDistance = int(input ("How hard will you hit the ball? (in a number from 0 - 10)|"))
    except (ValueError): #Assures the inputs are numbers.
        print ("All entrys must be numbers!")
        NewDirection = 0
        NewDistance = 0
        NewClub = 2
        play2()
    OWMYBRAIN2()

def OWMYBRAIN2(): #This function mostly consists of math and such that I didn't like looking at, so I put it in another function.
    global NewClub, NewDirection, NewDistance, Ball_W2, randlength, randwidth, scoretype2, scoredict, club, holey, holex, wind, rock, rockx, rocky
    if NewDirection >= -180 and NewDirection <= 180 and NewDistance >= 0 and NewDistance <= 10 and NewClub == 1 or NewClub == 2 or NewClub == 200 or NewDirection == 200 or NewDistance == 200:
        if NewClub == 1: #gives the club inputs string names.
            club = "putter"
        elif NewClub == 2:
            club = "driver"
        elif NewClub == 200: #This defines the quit option inbedded in the hotkey "200".
            print ("Quitting game...")
            time.sleep(2)
            quit()
        if NewDistance == 200:
            print ("Quitting game...")
            time.sleep(2)
            quit()
        if NewDirection == 200:
            print ("Quitting game...")
            time.sleep(2)
            quit()
        if club == "driver": #Defining how far a driver club hits.
            DupDistance = NewDistance * 10
        else:
            DupDistance = NewDistance
        scoretype2 = scoretype2 + 1
        AddDistancey = Ball_W2.gety()
        AddDistancex = Ball_W2.getx()

        if NewDirection == 0: #Facing straight
            NewDistance = 0
            for x in range(DupDistance): #Adds one to the distance the ball travels the number of the value based on the user's power input.
                NewDistance = (NewDistance + 1) - NewDistance
                AddDistancey = AddDistancey + NewDistance
                AddDistancex = AddDistancex + int(wind / 10)
                if AddDistancey == holey and AddDistancex == holex: #This (and all parts of code like it) check if the ball has hit the hole.
                    if scoretype1 == 1: #This defines what type of score the user got based on their number of shots.
                        scoredict = "[HOLE-IN-ONE!]"
                    elif scoretype1 == 2:
                        scoredict = "BIRDIE!"
                    elif scoretype1 == 3:
                        scoredict = "Par!"
                    elif scoretype1 == 4:
                        scoredict = "Bogey"
                    elif scoretype1 == 5:
                        scoredict = "double bogey"
                    elif scoretype1 >= 6:
                        scoredict = "nIcE tRy..." 
                    else:
                        print ("Uh oh, something went wrong! Resetting game...")
                        gen_hole()
                    fplay2()
        if NewDirection <= 89 and NewDirection >= 1: #Facing upper right
            NewDistance = 0
            for x in range(DupDistance): #Adds one to the distance the ball travels the number of the value based on the user's power input.
                NewDistance = (NewDistance + 1) - NewDistance
                AddDistancey = AddDistancey + (float(NewDistance) / 2)
                AddDistancex = AddDistancex + ((NewDistance / 2)+ int(wind / 10))
                if AddDistancey == holey and AddDistancex == holex: #This (and all parts of code like it) check if the ball has hit the hole.
                    if scoretype1 == 1: #This defines what type of score the user got based on their number of shots.
                        scoredict = "[HOLE-IN-ONE!]"
                    elif scoretype1 == 2:
                        scoredict = "BIRDIE!"
                    elif scoretype1 == 3:
                        scoredict = "Par!"
                    elif scoretype1 == 4:
                        scoredict = "Bogey"
                    elif scoretype1 == 5:
                        scoredict = "double bogey"
                    elif scoretype1 >= 6:
                        scoredict = "nIcE tRy..." 
                    else:
                        print ("Uh oh, something went wrong! Resetting game...")
                        gen_hole()
                    fplay2()
        if NewDirection == 90: #Facing right
            NewDistance = 0
            for x in range(DupDistance): #Adds one to the distance the ball travels the number of the value based on the user's power input.
                NewDistance = (NewDistance + 1) - NewDistance
                AddDistancex = AddDistancex + (NewDistance + int(wind / 10))
                if AddDistancey == holey and AddDistancex == holex: #This (and all parts of code like it) check if the ball has hit the hole.
                    if scoretype1 == 1: #This defines what type of score the user got based on their number of shots.
                        scoredict = "[HOLE-IN-ONE!]"
                    elif scoretype1 == 2:
                        scoredict = "BIRDIE!"
                    elif scoretype1 == 3:
                        scoredict = "Par!"
                    elif scoretype1 == 4:
                        scoredict = "Bogey"
                    elif scoretype1 == 5:
                        scoredict = "double bogey"
                    elif scoretype1 >= 6:
                        scoredict = "nIcE tRy..." 
                    else:
                        print ("Uh oh, something went wrong! Resetting game...")
                        gen_hole()
                    fplay2()
        if NewDirection <= 179 and NewDirection >= 91: #Facing bottom right
            NewDistance = 0
            for x in range(DupDistance): #Adds one to the distance the ball travels the number of the value based on the user's power input.
                NewDistance = (NewDistance + 1) - NewDistance
                AddDistancey = AddDistancey + (NewDistance / -2)
                AddDistancex = AddDistancex + ((NewDistance / 2)+ int(wind / 10))
                if AddDistancey == holey and AddDistancex == holex: #This (and all parts of code like it) check if the ball has hit the hole.
                    if scoretype1 == 1: #This defines what type of score the user got based on their number of shots.
                        scoredict = "[HOLE-IN-ONE!]"
                    elif scoretype1 == 2:
                        scoredict = "BIRDIE!"
                    elif scoretype1 == 3:
                        scoredict = "Par!"
                    elif scoretype1 == 4:
                        scoredict = "Bogey"
                    elif scoretype1 == 5:
                        scoredict = "double bogey"
                    elif scoretype1 >= 6:
                        scoredict = "nIcE tRy..." 
                    else:
                        print ("Uh oh, something went wrong! Resetting game...")
                        gen_hole()
                    fplay2()
        if NewDirection == 180 or NewDirection == -180: #Facing straight down
            NewDistance = 0
            for x in range(DupDistance): #Adds one to the distance the ball travels the number of the value based on the user's power input.
                NewDistance = (NewDistance + 1) - NewDistance
                AddDistancey = AddDistancey + (NewDistance / -1)
                AddDistancex = AddDistancex + int(wind / 10)
                if AddDistancey == holey and AddDistancex == holex: #This (and all parts of code like it) check if the ball has hit the hole.
                    if scoretype1 == 1: #This defines what type of score the user got based on their number of shots.
                        scoredict = "[HOLE-IN-ONE!]"
                    elif scoretype1 == 2:
                        scoredict = "BIRDIE!"
                    elif scoretype1 == 3:
                        scoredict = "Par!"
                    elif scoretype1 == 4:
                        scoredict = "Bogey"
                    elif scoretype1 == 5:
                        scoredict = "double bogey"
                    elif scoretype1 >= 6:
                        scoredict = "nIcE tRy..." 
                    else:
                        print ("Uh oh, something went wrong! Resetting game...")
                        gen_hole()
                    fplay2()
        if NewDirection <= -179 and NewDirection >= -91: #Facing bottom left
            NewDistance = 0
            for x in range(DupDistance): #Adds one to the distance the ball travels the number of the value based on the user's power input.
                NewDistance = (NewDistance + 1) - NewDistance
                AddDistancey = AddDistancey + (NewDistance / -2)
                AddDistancex = AddDistancex + ((NewDistance / -2)+ int(wind / 10))
                if AddDistancey == holey and AddDistancex == holex: #This (and all parts of code like it) check if the ball has hit the hole.
                    if scoretype1 == 1: #This defines what type of score the user got based on their number of shots.
                        scoredict = "[HOLE-IN-ONE!]"
                    elif scoretype1 == 2:
                        scoredict = "BIRDIE!"
                    elif scoretype1 == 3:
                        scoredict = "Par!"
                    elif scoretype1 == 4:
                        scoredict = "Bogey"
                    elif scoretype1 == 5:
                        scoredict = "double bogey"
                    elif scoretype1 >= 6:
                        scoredict = "nIcE tRy..." 
                    else:
                        print ("Uh oh, something went wrong! Resetting game...")
                        gen_hole()
                    fplay2()
        if NewDirection == -90: #Facing left
            NewDistance = 0
            for x in range(DupDistance): #Adds one to the distance the ball travels the number of the value based on the user's power input.
                NewDistance = (NewDistance + 1) - NewDistance
                AddDistancex = AddDistancex + ((NewDistance / -1) + int(wind / 10))
                if AddDistancey == holey and AddDistancex == holex: #This (and all parts of code like it) check if the ball has hit the hole.
                    if scoretype1 == 1: #This defines what type of score the user got based on their number of shots.
                        scoredict = "[HOLE-IN-ONE!]"
                    elif scoretype1 == 2:
                        scoredict = "BIRDIE!"
                    elif scoretype1 == 3:
                        scoredict = "Par!"
                    elif scoretype1 == 4:
                        scoredict = "Bogey"
                    elif scoretype1 == 5:
                        scoredict = "double bogey"
                    elif scoretype1 >= 6:
                        scoredict = "nIcE tRy..." 
                    else:
                        print ("Uh oh, something went wrong! Resetting game...")
                        gen_hole()
                    fplay2()
        if NewDirection <= -89 and NewDirection >= -1: #Facing upper left
            NewDistance = 0
            for x in range(DupDistance): #Adds one to the distance the ball travels the number of the value based on the user's power input.
                NewDistance = (NewDistance + 1) - NewDistance
                AddDistancey = AddDistancey + (NewDistance / 2)
                AddDistancex = AddDistancex + ((NewDistance / -2)+ int(wind / 10))
                if AddDistancey == holey and AddDistancex == holex: #This (and all parts of code like it) check if the ball has hit the hole.
                    if scoretype1 == 1: #This defines what type of score the user got based on their number of shots.
                        scoredict = "[HOLE-IN-ONE!]"
                    elif scoretype1 == 2:
                        scoredict = "BIRDIE!"
                    elif scoretype1 == 3:
                        scoredict = "Par!"
                    elif scoretype1 == 4:
                        scoredict = "Bogey"
                    elif scoretype1 == 5:
                        scoredict = "double bogey"
                    elif scoretype1 >= 6:
                        scoredict = "nIcE tRy..." 
                    else:
                        print ("Uh oh, something went wrong! Resetting game...")
                        gen_hole()
                    fplay2()

        if AddDistancex == rockx and AddDistancey == rocky: #This (and all parts of code like it) check if the ball has hit a rock.
            AddDistancey = AddDistancey - 10
        if AddDistancex >= ((randwidth / 2) + 1): #V This complicated batch tests to see if the player has overshot, and exited the course.
            if AddDistancey >= (randlength + 1) or AddDistancey <= 0:
                os.system('cls')
                print ("You over shot, placing user back to previous location...")
                print ("")
                play1()
        elif AddDistancex <= ((randwidth / -2) - 1):
            if AddDistancey >= (randlength + 1) or AddDistancey <= 0:
                os.system('cls')
                print ("You over shot, placing user back to previous location...")
                print ("") 
                play1()
        else:
            Ball_W2 = Position(AddDistancex,AddDistancey,NewDirection)
        if AddDistancey == holey and AddDistancex == holex: #This (and all parts of code like it) check if the ball has hit the hole.
            if scoretype2 == 1: #This defines what type of score the user got based on their number of shots.
                scoredict = "[HOLE-IN-ONE!]"
            elif scoretype2 == 2:
                scoredict = "BIRDIE!"
            elif scoretype2 == 3:
                scoredict = "Par!"
            elif scoretype2 == 4:
                scoredict = "Bogey"
            elif scoretype2 == 5:
                scoredict = "double bogey"
            elif scoretype2 >= 6:
                scoredict = "nIcE tRy..." 
            else:
                print ("Something went wrong! Resetting game...")
                gen_hole()
            fplay2()
        else:
            os.system('cls')
            play1()
    else:
        os.system('cls')
        print ("Club must be a number between 1 and 2!")
        print ("Degree of angle must be a number between -180 and 180!")
        print ("Measure of power must be a number between 0 and 10!")
        play2()

def fplay2(): #This activates when the game ends, it displays what the winning players score was, and sends them back to the loginmenu.
    os.system('cls')
    print (scoredict)
    time.sleep(3)
    os.system('cls')
    loginmenu()

############################## HOW TO PLAY ##########################################

def htp(): #Explains the game and how to play it. ---v
    print ("First, choose your club, these will determine length of shots.")
    print ("Putter = shorter range")
    print ("Driver = longer range")
    print ('''The putter's range goes as follows:
1 - 10 = themselves in inches''')
    print('''The driver's range goes as follows:
1 - 10 = themselves times 2 in inches''')
    print ("")
    print ("Chose a degree angle to aim.")
    print ("Follow the chart below for help with degrees:")
    print (''' _________________
|++\+++++0°++++/++|
|+++\++++|++++/+++|
|++++\+++|+++/++++|
|+++++\++|++/+++++|
|++++++\+|+/++++++|
|_______\|/_______|
|-90°+++/|\++++90°|
|++++++/+|+\++++++|
|+++++/++|++\+++++|
|++++/+++|+++\++++|
|+++/++++|++++\+++|
|++/+++++|+++++\++|
|_/___-/+180°___\_|''')
    print ("")
    print ("When hitting, you have to choose how hard to hit the ball.")
    print ("When asked how hard to hit the ball, type a number from 1 - 10.")
    print ("The amount in inches the ball moves will depend on what club you have selected.")
    print ("")
    print ("Hotkeys:")
    print ("200: allows you to quit anytime")
    input ("")
    os.system('cls')
    loginmenu()

print ('''READ BEFORE PLAYING!:
DO NOT PLAY IN IDLE!
I HIGHLY suggest that you read the how to play option after logging in before playing, it will explain alot.
This is the kind of game you may need play a few times before you fully understand... I understand it can be confusing at first.''')
input ("Type anything to continue.") 
menu()
