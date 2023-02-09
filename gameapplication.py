import time
import re
import IdentifyBaseWord as np
import wordlist as wl
import Commands
import random
import json
import loadgame


#gameState 0 means the game is not being played
#variable will keep the game going basically.
gameState = 0

#I don't fully remember why I chose to do it this way.
#if the user chose to automatically generate a puzzle
checkAuto = 0

#if the user chose to give a word to the puzzle
checkBase = 0

#Tracks total number of points the user has earned through correct guesses
getTotal = 0

#used to store if a puzzle has been started or not.
puzzleStarted = 0

#set the variables to empty to solve some really weird TypeError with None, not sure if this was the best way to do this.
gaUserLetters = "empty"
gaReqLetter = "empty"
getList = list()
showRank = ""
puzzleTotal = 0

#tracks if a puzzle was loaded or not.
isLoaded = 0

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


#function for rank, currently assigns ranks based on static point values but will be updated to work based on percentages of total points from userunique (word bank for a puzzle)
def gameRank(puzzleRank):
    #variable to store ranks
    puzzleRank = ""
    #for a game in progress, matches point values to ranks
    #redo so that we take words from userunique, get point values (can yoink code above ^) for total value, use that value to do like getTotal < value * .10 (ten percent?) etc... 
    if (getTotal < 10):
        puzzleRank = "Beginner"
    elif (getTotal >= 10) and (getTotal < 30):
        puzzleRank = "Novice"
    elif (getTotal >= 30) and (getTotal < 65):
        puzzleRank = "Advanced"
    elif (getTotal >= 65) and (getTotal < 150):    
        puzzleRank = "Expert"
    else:    
        puzzleRank = "Master"
    #messages for when a user reaches a new rank
    return puzzleRank
    
print("Hello! Welcome to MediaTek's Spelling bee!")
print("The goal of this game is to guess as many words as you can to accumulate points!")
playGame = input("Would you like to play our game? (yes/no): ")

#While loop will check whether or not the user wants to play our game.
while (playGame.lower() != 'yes') and (playGame.lower() != 'no'):
    print("Invalid input please enter yes or no!")
    playGame = input("Would you like to play our game? (yes/no): ")
    if(playGame == "yes" or playGame == "no"):
        break
#If no, then exit the program.
if(playGame.lower() == "no"):
    print("Ok, goodbye!")
    time.sleep(2.5)
    exit()
#If yes then the game begins!
if(playGame.lower() == "yes"):
    gameState = 1

#big while loop for our game.
while(gameState == 1):
    userInput = input("Please enter a guess or command: ")
    userInput.lower()
    #searches the user input for any digits, would like to get this working for special characters but it wasn't.
    #if it has a number we don't want to take the input, ask again!
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

    #checks whether or not the users input is a command or not by checking for !.
    #run the guess function
    if '!' not in userInput:
        if(puzzleStarted == 1):
            points = userGuess(userInput,getList)
            getTotal += points
        else:
            print("No word bank has been generated yet!")
    #pattern matching to match the users input to the available commands
    #I should find a way to add some type of fall through case possibly case _: since a base case doesn't exist for pattern matching in python?
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

            #Checks the users choice.
            while (isAuto != 'yes') and (isAuto != 'no'):
               isAuto = input("Invalid input! Enter \"yes\" or \"no\": ")
            if(isAuto == 'yes'):
                #generate the user letters and required letters
                gaUserLetters, gaReqLetter = np.autoGame()
                print("Your letters: " + gaUserLetters)
                print("Required letter: " + gaReqLetter)
                print("Words guessed: " + str(wl.userWordList))
                print("Total points: " + str(getTotal))
                #generate the unique word list.
                getList = wl.generateWordList(gaReqLetter,gaUserLetters)
                checkAuto = 1
                checkBase = 0
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
            #clear the users guessed word list if they generate a new puzzle.
            wl.userWordList.clear()
            #set the total to 0
            getTotal = 0
            #set isLoaded to false
            isLoaded = 0
        case "!showpuzzle":
            print("Your letters: " + gaUserLetters)
            print("Required letter: " + gaReqLetter)
            print("Words guessed: " + str(wl.userWordList))
            print("Total points: " + str(getTotal))
        case "!showfoundwords":
            Commands.showFoundWords()
        case "!shuffle":
            #I HAVE NO IDEA WHY I MADE 2 SHUFFLE FUNCTIONS BUT I DID.
            #SHUFFLES THE LETTERS BASED ON THEIR CHOICE. 
            if(checkAuto == 1):
                gaUserLetters = shuffleAuto(gaUserLetters)
                print("Thwomp! Shuffled!")
                print("These are the letters after shuffling: " + gaUserLetters)
            if(checkBase == 1):
                gaUserLetters = shuffleBase(gaUserLetters)
                print("Thwomp! Shuffled!")
                print("These are the letters after shuffling: " + gaUserLetters)
            if(isLoaded == 1):
                gaUserLetters = shuffleBase(gaUserLetters)
                print("Thwomp! Shuffled!")
                print("These are the letters after shuffling: " + gaUserLetters)
        case "!savepuzzle":
            Commands.savePuzzle(gaUserLetters, gaReqLetter, wl.userWordList, getList, getTotal)
            print("Puzzle saved!")
        case "!loadpuzzle":
            #load the data from the save json file
            gaUserLetters, gaReqLetter, wl.userWordList, getList, getTotal = gameLoad()
            #set that a puzzle is started.
            puzzleStarted = 1
            isLoaded = 1
            checkBase = 0
            checkAuto = 0
            print("Puzzle loaded!")
        case "!showstatus":
            if (puzzleStarted == 0):
                print("Can't show a status for a puzzle that isn't in progress!")
            else:
                showRank = gameRank(showRank)
                print(showRank)
        case "!help":
            Commands.help()
        case "!exit":
            Commands.exitCommand(gaUserLetters, gaReqLetter, wl.userWordList, getList, getTotal)
    


#!save command: prompt user to enter a name for the file
# create a json file with that name
# then store data into it.

#!load command: prompt user to enter a name for the file
#load data back into program

#store required letter
#store userLetters
#store user words guessed
#store word bank