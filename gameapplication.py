import time
import re
import IdentifyBaseWord as np
import wordlist as wl
import Commands
import random
import json
import loadgame

#gameState 0 means the game is not being played
gameState = 0
checkAuto = 0
checkBase = 0
getTotal = 0
puzzleStarted = 0
gaUserLetters = "empty"
gaReqLetter = "empty"
getList = list()

# loads game files from savegame.json and organizes them in a list.
def gameLoad():
    # open the json file and load its contents
    loadGame = list()
    with open('savegame.json', "r") as save:
        loaded = json.load(save)
    # for each element in a file, make it a separate entry in the list.
    for l in loaded:
        loadGame.append(l)
    
    # assign values based on the position of each element in the list.
    gaUserLetters = loadgame.loadUserLetters(loadGame[0])
    gaReqLetter = loadgame.loadRequiredLetter(loadGame[1])
    wl.userWordList = loadgame.loadGuessedWords(loadGame[2])
    getList = loadgame.loadWordBank(loadGame[3])
    getTotal = loadgame.loadTotalPoints(loadGame[4])
    
    #return everything in the end.
    return gaUserLetters, gaReqLetter, wl.userWordList, getList, int(getTotal)

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
    return shuffledLetters

def shuffleBase(userLetters):
    #SHUFFLE ALGO
    replaceString = userLetters.replace("[","").replace("]","")
    toList = list(replaceString)
    random.shuffle(toList)
    shuffledLetters = ''.join(toList)
    return shuffledLetters

def userGuess(userInput, userList):
    totalPoints = 0
    #search if what the user types exists within the list
    if gaReqLetter in userInput:
        if userInput in userList:
            #create set from user input
            toSet = set(userInput)
            #determine length of set to be later to check for 7 unique characters (if a pangram)
            length = len(userInput)
            #store into user word bank
            wl.userWordList.append(userInput)
            #print statements for testing
            print("Word found!")
            #    print(userInput)
            #    print(userList)
            #    print("user word list:")
            #    print(wl.userWordList)
            #remove the word from the word bank.
            userList.remove(userInput)
            #generates user points based on the length, if it's a pangram then add an additional 7 points.
            match length:
                case 4:
                    totalPoints += length
                case 5:
                    totalPoints += length
                case 6:
                    totalPoints += length
                case 7:
                    if(len(toSet) == 7):
                        totalPoints += (length + 7)
                    else:
                        totalPoints += length
                case 8:
                    if(len(toSet) == 7):
                        totalPoints += (length + 7)
                    else:
                        totalPoints += length
                case 9:
                    if(len(toSet) == 7):
                        totalPoints += (length + 7)
                    else:
                        totalPoints += length
                case 10:
                    if(len(toSet) == 7):
                        totalPoints += (length + 7)
                    else:
                        totalPoints += length
                case 11:
                    if(len(toSet) == 7):
                        totalPoints += (length + 7)
                    else:
                        totalPoints += length
                case 12:
                    if(len(toSet) == 7):
                        totalPoints += (length + 7)
                    else:
                        totalPoints += length
                case 13:
                    if(len(toSet) == 7):
                        totalPoints += (length + 7)
                    else:
                        totalPoints += length
                case 14:
                    if(len(toSet) == 7):
                        totalPoints += (length + 7)
                    else:
                        totalPoints += length
                case 15:
                    if(len(toSet) == 7):
                        totalPoints += (length + 7)
                    else:
                        totalPoints += length
        else:
            print("Sorry! Couldn't find that word.")
    else:
        print("Hey! you didn't use the required letter!")
    return totalPoints

print("Hello! Welcome to MediaTek's Spelling Bee!")
print("The goal of this game is to guess as many words as you can to accumulate points!")
playGame = input("Would you like to play our game? (yes/no): ")

while (playGame.lower() != 'yes') and (playGame.lower() != 'no'):
    print("Invalid input please enter yes or no!")
    playGame = input("Would you like to play our game? (yes/no): ")
    if(playGame == "yes" or playGame == "no"):
        break

if(playGame.lower() == "no"):
    print("Ok, goodbye!")
    time.sleep(2.5)
    exit()
if(playGame.lower() == "yes"):
    gameState = 1

while(gameState == 1):
    userInput = input("Please enter a guess or command: ")
    userInput.lower()
    hasNum = bool(re.search(r'\d', userInput))
    if (hasNum == True):
        userInput = input("No numbers/special characters besides \"!\" allowed! Please reenter your input: ")
        hasNum = bool(re.search(r'\d', userInput))
        while(hasNum != False):
            userInput = input("No numbers allowed! Please reenter your input: ")
            hasNum = bool(re.search(r'\d', userInput))

    
    #exit it put below all commands until their functions are implemented
    while(len(userInput) < 4) or (len(userInput) > 15):
        userInput = input("Input must be between 4 and 15 characters! Please reenter your input: ")

    #will rewrite this into pattern matching later, should've thought of this from the start but slipped my mind lol.
    #run the guess function
    if '!' not in userInput:
        if(puzzleStarted == 1):
            points = userGuess(userInput,getList)
            getTotal += points
        else:
            print("No word bank has been generated yet!")
    match userInput:
        case "!newpuzzle":
            #This if statement will check if a puzzle has been started
            #This is so after the user enters the puzzle command again after the first time, or if they loaded a puzzle
            #Prompt to ask them if they want to save the game
            if (puzzleStarted == 1):
                wantSave = input("Hey, you have a puzzle in progress! Do you want to save? (yes/no): ")
                if(wantSave.lower() == "yes"):
                    print("Alright! saving your game! ")
                    Commands.savePuzzle(gaUserLetters, gaReqLetter, wl.userWordList, getList, getTotal)
                    time.sleep(1)
                else:
                    print("Ok, lets generate a new puzzle! ")
            #Checks if the user wants to automatically generate the puzzle or not, regardless of their choice a puzzle is started.
            isAuto = input("Do you want the puzzle to be randomly generated?: ")
            isAuto.lower()
            puzzleStarted = 1
            isAuto = input("Do you want the puzzle to be randomly generated?: ")
            isAuto.lower()
            while (isAuto != 'yes') and (isAuto != 'no'):
               isAuto = input("Invalid input! Enter \"yes\" or \"no\": ")
            if(isAuto == 'yes'):
                gaUserLetters, gaReqLetter = np.autoGame()
                print("Your letters: " + gaUserLetters)
                print("Required letter: " + gaReqLetter)
                print("Words guessed: " + wl.userWordList)
                print("Total points: " + getTotal)
                #generate the unique word list.
                getList = wl.generateWordList(gaReqLetter,gaUserLetters)
                checkAuto = 1
                checkBase = 0
                wl.userWordList.clear()
            elif (isAuto == 'no'):
                gaUserLetters, gaReqLetter = np.baseGame()
                #if these values are empty that means their pangram doesn't exist, rerun function until a valid one is entered.
                while(gaUserLetters == "empty") and (gaReqLetter == "empty"):
                    gaUserLetters,gaReqLetter = np.baseGame()
                getList = wl.generateWordList(gaReqLetter,gaUserLetters)
                print("Your letters: " + gaUserLetters)
                print("Required letter: " + gaReqLetter)
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
                print("These are the letters after shuffling: " + gaUserLetters)
            if(checkBase == 1):
                gaUserLetters = shuffleBase(gaUserLetters)
                print("These are the letters after shuffling: " + gaUserLetters)
            if(isLoaded == 1):
                gaUserLetters = shuffleBase(gaUserLetters)
                print("These are the letters after shuffling: " + gaUserLetters)
        case "!savepuzzle":
            Commands.savePuzzle(gaUserLetters, gaReqLetter, wl.userWordList, getList, getTotal)
            print("Puzzle saved!")
        case "!loadpuzzle":
            gaUserLetter, gaReqLetter, wl.userWordList, getList, getTotal = gameLoad()
            puzzleStarted = 1
            print("Puzzle loaded!")
        case "!showstatus":
            Commands.showStatus()
        case "!help":
            Commands.help()
        case "!exit":
            Commands.exitCommand()
    


#!save command: prompt user to enter a name for the file
# create a json file with that name
# then store data into it.

#!load command: prompt user to enter a name for the file
#load data back into program

#store required letter
#store userLetters
#store user words guessed
#store word bank