import sys
import IdentifyBaseWord as np
import wordlist as wl
import savegame
import loadgame



#run function that displays all the commands the user can type
def help():
    print('''

How To Play: The goal of our Spelling Bee game is to guess words given a choice of 7 letters, with 1 of them being required for all created words. Letters may be repeated but words must be 4 to 15 letters.
Each puzzle is based off of a pangram, a 7 to 15 letter word that contains 7 unique letters. You are free to use your own pangram to create a personalized puzzle!

Commands:
    !newpuzzle: Generates a new puzzle. You will be given the option to provide your own pangram for puzzle creation.
    !showpuzzle: Displays the current puzzle.
    !showfoundwords: Lists all of the correctly guessed words.
    !shuffle: Shuffles the given letters in a random arangement (except the required letter which stays in the center).
    !savepuzzle: Saves your puzzle to your local machine.
    !loadpuzzle: Allows the you to load a saved puzzle from files, type the file name of the saved puzzle with this command.
    !showstatus: Shows your current status.
    !help: You just typed this command. Congrats.
    !exit: Exits the game. You will be asked if you want to save your puzzle to not lose progress.
          ''')

#list of commands at the beginning of the program
def commandsStart():
    print('''

The goal of our Spelling Bee game is to guess words given a choice of 7 letters, with 1 of them being required for all created words. Letters may be repeated but words must be 4 to 15 letters.
Each puzzle is based off of a pangram, a 7 to 15 letter word that contains 7 unique letters. You are free to use your own pangram to create a personalized puzzle!

Try entering one of the following commands to start playing or exit the program:
    !newpuzzle: Generates a new puzzle. You will be given the option to provide your own pangram for puzzle creation.
    !loadpuzzle: Allows the you to load a saved puzzle from files, type the file name of the saved puzzle with this command.
    !help: Displays the list of commands currently accessible.
    !exit: Exits the game.
          ''')

#def newPuzzle():
    #exit()

def showPuzzle():
    print()

def showFoundWords():
    print(*wl.userWordList)

def guess():
    print()

def shuffle():
    print()

def savePuzzle(userLetters, requiredLetter, guessedWords, wordBank, totalPoints, inputFile):
    savegame.savegame(userLetters, requiredLetter, guessedWords, wordBank, totalPoints, inputFile)

def loadPuzzle():
    print()

def showStatus():
    print()

def exitCommand(userLetters, requiredLetter, guessedWords, wordBank, totalPoints):
    print("Whoa, slow down buddy! You're about to lose all of your epic progress, would you like to save your game first? yes/no")
    userInput = input()
    while(userInput != "yes") and (userInput != "no"):
        userInput = input("Please enter \"yes\" or \"no:\": ")
    if(userInput == "yes"):
        savePuzzle(userLetters, requiredLetter, guessedWords, wordBank, totalPoints)
        print("Puzzle saved! Goodbye!")
    elif(userInput == "no"):
        #Exit
        print("Okay! See you on the other side!")
        exit()
    sys.exit()