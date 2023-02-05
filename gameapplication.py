import time
import re
import IdentifyBaseWord as np
import wordlist as wl
import Commands
import random

#gameState 0 means the game is not being played
gameState = 0
checkAuto = 0
checkBase = 0
gaUserLetters = None
gaReqLetter = None

def shuffleAuto(userLetters):
    #SHUFFLE ALGO
    #replace the brackets within the user letters string
    replaceString = userLetters.replace("[","").replace("]","")
    #convert it to a list
    toList = list(replaceString)
    #use shuffle with the list to change the positions of the letters.
    random.shuffle(toList)
    #afterwards convert list to a string.
    shuffledLetters = ''.join(toList)
    print(shuffledLetters)
    return shuffledLetters



def shuffleBase(userLetters):
    #SHUFFLE ALGO
    replaceString = userLetters.replace("[","").replace("]","")
    toList = list(replaceString)
    random.shuffle(toList)
    shuffledLetters = ''.join(toList)
    print(shuffledLetters)
    return shuffledLetters


print("Hello welcome to MediaTek's Spelling bee!")
print("The goal of this game is to guess as many words as you can to accumulate points!")
playGame = input("Would you like to play our game? enter yes or no: ")

while (playGame.lower() != 'yes') and (playGame.lower() != 'no'):
    print("Invalid input please enter yes or no!")
    playGame = input("Would you like to play our game? enter yes or no\n")
    if(playGame == "yes" or playGame == "no"):
        break

if(playGame.lower() == "no"):
    print("Ok, goodbye!")
    time.sleep(2.5)
    exit()
if(playGame.lower() == "yes"):
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
                gaUserLetters, gaReqLetter = np.autoGame()
                print("Game apps user letters: " + gaUserLetters)
                print("Game apps req letter: " + gaReqLetter)
                #print("User letters are: " + str(np.userLetters))
                #print("Required letter is: *" + str(np.reqLetter))
                wl.generateWordList(gaReqLetter,gaUserLetters)
                #gaUserLetters = str(np.userLetters)
                #gaReqLetter = str(np.reqLetter)
                checkAuto = 1
                checkBase = 0
            elif (isAuto == 'no'):
                gaUserLetters, gaReqLetter = np.baseGame() 
                #print("User letters are: " + str(np.bguserLetters))
                #print("Required letter is: *" + str(np.bgreqLetter))
                wl.generateWordList(gaReqLetter,gaUserLetters)
                #gaUserLetters = str(np.bguserLetters)
                #gaReqLetter = str(np.bgreqLetter)
                print("Game apps user letters: " + gaUserLetters)
                print("Game apps req letter: " + gaReqLetter)
                checkAuto = 0
                checkBase = 1
        case "!showpuzzle":
            Commands.showPuzzle()
        case "!guess":
            Commands.guess()
        case "!showfoundwords":
            Commands.showFoundWords()
        case "!shuffle":
            if(checkAuto == 1):
                gaUserLetters = shuffleAuto(gaUserLetters)
                print("After SHUFFLING these are the letters!: " + gaUserLetters)
            if(checkBase == 1):
                gaUserLetters = shuffleBase(gaUserLetters)
                print("After SHUFFLING these are the letters!: " + gaUserLetters)
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


    









