from MVC.model import wordlist as wl
from MVC.model import savegame as savegame

#run function that displays all the commands the user can type
def help():
    print('''

How To Play: 
- The objective of the game is to guess words based of 7 letters, 1 of them being required in every word.
- The letters can be repeated, but all words are required to be between 4 and 15 letters long. 
- Each puzzle is based on a pangram, which is a word containing 7 unique letters and can be 7 to 15 letters long.

Commands:
    newpuzzle: Generates a new puzzle. You can even provide your own pangram for puzzle creation!
    showpuzzle: Displays the current puzzle.
    showfoundwords: Lists all of the correctly guessed words.
    shuffleletters: Shuffles the given letters in a random arangement (except the required letter in the center).
    savepuzzle: Saves your puzzle to your local machine.
    loadpuzzle: Allows the you to load a saved puzzle from files, type the file name of the saved puzzle with this command.
    showstatus: Shows your current status.
    showhints: Shows hints for your current game.
    giveup: 'Give up' on the puzzle and submit your score and provided username to the high scores board.
    showhighscore: Displays the top ten local high scores for a given puzzle (if there are any existing scores).
    gamehelp: You just typed this command. Congrats.
    gameexit: Exits the game. You will be asked if you want to save your puzzle before exiting.
          ''')

#list of commands at the beginning of the program
def commandsStart():
    print('''

- The objective of the game is to guess words based of 7 letters, 1 of them being required in every word.
- The letters can be repeated, but all words are required to be between 4 and 15 letters long. 
- Each puzzle is based on a pangram, which is a word containing 7 unique letters and can be 7 to 15 letters long.

To get started, you can type:
    newpuzzle: To generate a new puzzle. You can even provide your own pangram for puzzle creation!
    loadpuzzle: To load a saved puzzle from a file. You will need to enter the file name of the saved puzzle.
    gamehelp: To see the list of all the commands.
    gameexit: To exit the program.
          ''')

def showFoundWords():
    print(*wl.userWordList)

def savePuzzle(userLetters, requiredLetter, guessedWords, wordBank, totalPoints, maxPoints, inputFile):
    savegame.savegame(userLetters, requiredLetter, guessedWords, wordBank, totalPoints, maxPoints, inputFile)

#for saving an encrypted game, same as above but just passing in the encrypted word bank.
def saveSecretPuzzle(userLetters,requiredLetter,guessedWords,encryptedBank,totalPoints,maxPoints, author, inputFile):
    savegame.saveencryptedgame(userLetters, requiredLetter, guessedWords, encryptedBank, totalPoints, maxPoints, author, inputFile)