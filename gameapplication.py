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

def gameLoad():
    loadGame = list()
    with open('savegame.json', "r") as save:
        loaded = json.load(save)
    for l in loaded:
        loadGame.append(l)
    
    gaUserLetters = loadgame.loadUserLetters(loadGame[0])
    gaReqLetter = loadgame.loadRequiredLetter(loadGame[1])
    wl.userWordList = loadgame.loadGuessedWords(loadGame[2])
    getList = loadgame.loadWordBank(loadGame[3])
    getTotal = loadgame.loadTotalPoints(loadGame[4])
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

def userGuess(userInput, userList):
    totalPoints = 0
    print(userList)
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
            print("found!")
            print(userInput)
            print(userList)
            print("user word list:")
            print(wl.userWordList)
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
            print("not found!")
            print(userInput)
            print(userList)
    else:
        print("hey you didn't use the required letter!")
    return totalPoints

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
        userInput = input("No numbers/special characters besides ! allowed please reenter a guess/command: ")
        hasNum = bool(re.search(r'\d', userInput))
        while(hasNum != False):
            userInput = input("No numbers allowed please reenter a guess/command: ")
            hasNum = bool(re.search(r'\d', userInput))

    
    #exit it put below all commands until their functions are implemented
    while(len(userInput) < 4) or (len(userInput) > 15):
        userInput = input("Input must be >= 4 and <= 15, please reenter a guess/command: ")

    #will rewrite this into pattern matching later, should've thought of this from the start but slipped my mind lol.
    #run the guess function
    if '!' not in userInput:
        if(puzzleStarted == 1):
            points = userGuess(userInput,getList)
            getTotal += points
            print(getTotal)
        else:
            print("No word bank has been generated yet!")
    match userInput:
        case "!newpuzzle":
            puzzleStarted = 1
            isAuto = input("Do you want the puzzle to be randomly generated?")
            isAuto.lower()
            while (isAuto != 'yes') and (isAuto != 'no'):
               isAuto = input("Invalid input please enter yes or no!: ")
            if(isAuto == 'yes'):
                gaUserLetters, gaReqLetter = np.autoGame()
                print("Game apps user letters: " + gaUserLetters)
                print("Game apps req letter: " + gaReqLetter)
                getList = wl.generateWordList(gaReqLetter,gaUserLetters)
                print(getList)
                checkAuto = 1
                checkBase = 0
            elif (isAuto == 'no'):
                gaUserLetters, gaReqLetter = np.baseGame()
                #if these values are empty that means their pangram doesn't exist, rerun function until a valid one is entered.
                while(gaUserLetters == "empty") and (gaReqLetter == "empty"):
                    gaUserLetters,gaReqLetter = np.baseGame()
                getList = wl.generateWordList(gaReqLetter,gaUserLetters)
                print(getList)
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
            Commands.savePuzzle(gaUserLetters, gaReqLetter, wl.userWordList, getList, getTotal)
        case "!loadpuzzle":
            gaUserLetter, gaReqLetter, wl.userWordList, getList, getTotal = gameLoad()
            puzzleStarted = 1
            print(gaUserLetters, gaReqLetter, wl.userWordList, getList, getTotal)
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