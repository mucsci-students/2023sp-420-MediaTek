import sys
import IdentifyBaseWord as np
import wordlist as wl
import savegame
import loadgame



#run function that displays all the commands the user can type
def help():
    print('''
!newpuzzle: Generates a new puzzle. If you are generating a puzzle from a chosen pangram, enter said pangram along with the command.
!showpuzzle: Displays the current puzzle.
!showfoundwords: Lists all of the correctly guessed words.
!guess: Type this command with a word you would like to guess.
!shuffle: Shuffles the given letters in a random arangement (except the required letter which stays in the center).
!savepuzzle: Saves your puzzle to your local machine.
!loadpuzzle: Allows the you to load a saved puzzle from files, type the file name of the saved puzzle with this command.
!showstatus: Shows your current status.
!help: You just typed this command. Congrats.
!exit: Exits the game. You will be asked if you're sure OR want to save your game.
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

def savePuzzle(userLetters, requiredLetter, guessedWords, wordBank, totalPoints):
    savegame.savegame(userLetters, requiredLetter, guessedWords, wordBank, totalPoints)

def loadPuzzle():
    print()

def showStatus():
    print()

def exitCommand():
    print("Whoa, slow down buddy! You're about to lose all of your epic progress, would you like to save your game first? yes/no")
    userInput = input()
    while(userInput != "yes") and (userInput != "no"):
        userInput = input("Please enter a yes OR no: ")
    if(userInput == "yes"):
        #save command
        print("saved")
    elif(userInput == "no"):
        #Exit
        exit()
    sys.exit()