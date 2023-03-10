import sys
#import MVC.model.IdentifyBaseWord as np
from MVC.model import IdentifyBaseWord as np
#import MVC.model.wordlist as wl
from MVC.model import wordlist as wl
from MVC.model import savegame as savegame
from MVC.model import loadgame as loadgame



#run function that displays all the commands the user can type
def help():
    print('''

How To Play: 
- The objective of the game is to guess words based of 7 letters, 1 of them being required in every word.
- The letters can be repeated, but all words are required to be between 4 and 15 letters long. 
- Each puzzle is based on a pangram, which is a word containing 7 unique letters and can be 7 to 15 letters long.

Commands:
    !newpuzzle: Generates a new puzzle. You can even provide your own pangram for puzzle creation!
    !showpuzzle: Displays the current puzzle.
    !showfoundwords: Lists all of the correctly guessed words.
    !shuffle: Shuffles the given letters in a random arangement (except the required letter in the center).
    !savepuzzle: Saves your puzzle to your local machine.
    !loadpuzzle: Allows the you to load a saved puzzle from files, type the file name of the saved puzzle with this command.
    !showstatus: Shows your current status.
    !help: You just typed this command. Congrats.
    !exit: Exits the game. You will be asked if you want to save your puzzle before exiting.
          ''')

#list of commands at the beginning of the program
def commandsStart():
    print('''

- The objective of the game is to guess words based of 7 letters, 1 of them being required in every word.
- The letters can be repeated, but all words are required to be between 4 and 15 letters long. 
- Each puzzle is based on a pangram, which is a word containing 7 unique letters and can be 7 to 15 letters long.

To get started, you can type:
    !newpuzzle: To generate a new puzzle. You can even provide your own pangram for puzzle creation!
    !loadpuzzle: To load a saved puzzle from a file. You will need to enter the file name of the saved puzzle.
    !help: To see the list of all the commands.
    !exit: To exit the program.
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

def savePuzzle(userLetters, requiredLetter, guessedWords, wordBank, totalPoints, maxPoints, inputFile):
    savegame.savegame(userLetters, requiredLetter, guessedWords, wordBank, totalPoints, maxPoints, inputFile)

def loadPuzzle():
    print()

def showStatus():
    print()