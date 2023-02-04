import time
import re
import IdentifyBaseWord as np
import wordlist as wl
import Commands

#gameState 0 means the game is not being played
gameState = 0


print("Hello welcome to MediaTek's Spelling bee!")
print("The goal of this game is to guess as many words as you can to accumulate points!")
playGame = input("Would you like to play our game? enter yes or no: ")

while (playGame != 'yes') and (playGame != 'no'):
    print("Invalid input please enter yes or no!")
    playGame = input("Would you like to play our game? enter yes or no\n")
    if(playGame == "yes" or playGame == "no"):
        break

if(playGame == "no"):
    print("Ok, goodbye!")
    time.sleep(2.5)
    exit()
if(playGame == "yes"):
    gameState = 1

while(gameState == 1):
    #print("Commands should always we started with !, an example would be !help")
    #print("All input without ! are considered guesses")
    userInput = input("Please enter a guess/command: ")
    userInput.lower()
    hasNum = bool(re.search(r'\d', userInput))
    if (hasNum == True):
        userInput = input("No numbers allowed please reenter a guess/command: ")
        hasNum = bool(re.search(r'\d', userInput))
        while(hasNum != False):
            userInput = input("No numbers allowed please reenter a guess/command: ")
            hasNum = bool(re.search(r'\d', userInput))
    
    #exit it put below all commands until their functions are implemented
    while(len(userInput) < 4):
        userInput = input("Input must be >= 4, please reenter a guess/command: ")



    #will rewrite this into pattern matching later, should've thought of this from the start but slipped my mind lol.
    #run the guess function
    if '!' not in userInput:
        print("Running the guess function")
    
    match userInput:
        case "!newpuzzle":
            isAuto = input("Do you want the puzzle to be randomly generated?")
            isAuto.lower()
            while (isAuto != 'yes') and (isAuto != 'no'):
               isAuto = input("Invalid input please enter yes or no!: ")
            if(isAuto == 'yes'):
                np.autoGame()
                print("User letters are: " + str(np.userLetters))
                print("Required letter is: *" + str(np.reqLetter))
                wl.generateWordList(np.reqLetter,np.userLetters)
            elif (isAuto == 'no'):
                np.baseGame() 
                print("User letters are: " + str(np.bguserLetters))
                print("Required letter is: *" + str(np.bgreqLetter))
                wl.generateWordList(np.bgreqLetter,np.bguserLetters)
        case "!showpuzzle":
            Commands.showPuzzle()
        case "!guess":
            Commands.guess()
        case "!showfoundwords":
            Commands.showFoundWords()
        case "!shuffle":
            Commands.shuffle()
        case "!savepuzzle":
            Commands.savePuzzle()
        case "!loadpuzzle":
            Commands.loadPuzzle()
        case "!showstatus":
            Commands.showStatus()
        case "!help":
            Commands.help()
        case "!exit":
            Commands.exitCommand()


    
    









