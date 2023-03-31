import time
import re
from MVC.controller import Controller as ctrl
from MVC.model import Commands as Commands
import random
import json
from MVC.model import loadgame as loadgame
import sys
import os
import textwrap
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter as wrdcmp


#create controller object
'''
controller = ctrl.controller()
print("Hello! Welcome to MediaTek's Spelling bee!")
print("The goal of this game is to guess as many words as you can to accumulate points!")
controller.ensureYesOrNo()'''
class view:
    #set instance to None at first
    instance = None
    #upon the view class being called, a new single instance of it will be created.
    def __new__(self):
        if self.instance is None:
              self.instance = super().__new__(self)
        return self.instance
    #while loop for the CLI.
    def __init__(self):
        self.controller = ctrl.controller()
        #variable to store user letters into a list for displaying a honeycomb.
        self.displayLetters = []
        self.check = False
        self.b4commands = ["newpuzzle","loadpuzzle","gamehelp","gameexit"]
        self.commands = ["newpuzzle","showpuzzle","showfoundwords","shuffleletters","savepuzzle","loadpuzzle","showstatus","showhints","gamehelp","gameexit"]

    def grid(self):
        x = self.controller.gridHint()

        # Formats Matrix
        cell_width = 2
        fmt = '{:>' + str(cell_width) + '}'
        for i in range(0, x.shape[0]):
            for j in range(0, x.shape[1]):
                if x[i,j] is not None:
                    x[i,j] = fmt.format(x[i,j])
        # Prints Matrix
        print("Grid Hint:")
        print(x)
        print("\n")
        
    def hintCount (self):
        count = self.controller.firstTwo()
        print("Two Word List:")
        print(count)
        print("\n")

    def totHint(self):
        x,y = self.controller.totalHint()
        # Prints
        print(f"WORDS:{self.controller.getTotalWords()} POINTS:{self.controller.controllerGetPuzzleTotal()} PANGRAMS:{x} ({y} Perfect)")
    
    def hint(self):
        hints = [self.grid(),self.hintCount(),self.totHint()]
        hint = random.choice(hints)
        
    def showHoneyComb(self):

            self.controller.controllerToHoneyComblist()
            self.displayLetters = self.controller.controllerGetHoneyCombList()
            print('''  
                        %s
                    %s       %s
                        %s
                    %s       %s
                        %s      
            ''' % (self.displayLetters[0], self.displayLetters[1],self.displayLetters[2], self.controller.controllerGetReqLetter(), self.displayLetters[3],self.displayLetters[4],self.displayLetters[5]))
    def newPuzzle(self):
        if(self.controller.controllerGetPuzzleState() == 1):
            wantSave = input("Hey do you want to save the game? (yes/no): ")
            if (wantSave.lower() == "yes"):
                inputFile = input("Please choose a name for the file: ")
                print("Saving your game!")
                self.controller.controllerSaveGame(inputFile)
            else:
                print("Ok, lets generate a new puzzle! ")
        self.controller.controllerNewGame()
        isAuto = input("Do you want it to be automatically generated? (yes/no): ")
        while isAuto.lower() != "yes" and isAuto.lower() != "no":
            isAuto = input("Do you want it to be automatically generated? (yes/no): ")
    
        if (isAuto.lower() == "yes"):
            self.controller.controllerRunAutoGame()
            print("User letters: " + self.controller.controllerGetLetters())
            print("Required letter: " + self.controller.controllerGetReqLetter())
            self.showHoneyComb()
            self.controller.controllerUpdatePuzzleState1()
        elif isAuto.lower() == "no":
            userInput = input("Choose a pangram: ")
            self.check = self.controller.controllerCheckPangram(userInput)
            while(self.check == False):
                    userInput = input("Your pangram doesn't exist within our database, please try again. Enter a pangram: ")
                    self.check = self.controller.controllerCheckPangram(userInput)
            self.controller.controllerRunBaseGame(userInput)
            print("User letters: " + self.controller.controllerGetLetters())
            print("Required letter: " + self.controller.controllerGetReqLetter())
            self.showHoneyComb()
            self.controller.controllerUpdatePuzzleState1()

    def showPuzzle(self):
        if (self.controller.controllerGetPuzzleState() == 0):
            print("No game started!")
        else:
            print("Your letters: " + self.controller.controllerGetLetters())
            print("Required letter: " + self.controller.controllerGetReqLetter())
            print("Guessed words: " + str(self.controller.controllerGetGuessedWordsCLI()))
            self.showHoneyComb()
    def showFoundWords(self):
        if (self.controller.controllerGetPuzzleState() == 0):
                    print("No game started!")
        else:
            print("Guessed words: " + str(self.controller.controllerGetGuessedWordsCLI()))
    
    def shuffleLetters(self):
        if (self.controller.controllerGetPuzzleState() == 0):
                print("No game started!")
        else:
            self.controller.controllerShuffleAuto()
            self.showHoneyComb()
            print("Your letters: " + self.controller.controllerGetLetters())
    def savePuzzle(self):
        if (self.controller.controllerGetPuzzleState() == 0):
                print("No game started!")
        else:
            inputFile = input("Please enter a name for the file: ")
            self.controller.controllerSaveGame(inputFile)
    def loadPuzzle(self):
        if self.controller.controllerGetPuzzleState() == 1:
            wantSave = input("Do you want to save the current game before loading a new puzzle? (yes/no): ")
            if wantSave.lower() == "yes":
                inputFile = input("Please choose a name for the file: ")
                print("Saving your game!")
                self.controller.controllerSaveGame(inputFile)
        inputFile = input("Enter the name of the file you want to load: ")
        checkFile = inputFile + ".json"
        if os.path.exists(checkFile):
            self.controller.controllerGameLoadCLI(inputFile)
            print("Puzzle loaded!")
            self.showHoneyComb()
        else:
            print("Uh-oh! Couldn't find that file. Reenter the load command and try again.")

    def startGame(self):
         #Set this before the loop runs since we only want to show the available commands instead of all of them.
        cmdautocomplete = wrdcmp(self.b4commands,ignore_case=True,match_middle=True)
        self.controller.ensureYesOrNo()
        print('''
Welcome to MediaTek's Spelling Bee! 
- The objective of the game is to guess words based of 7 letters, 1 of them being required in every word.
- The letters can be repeated, but all words are required to be between 4 and 15 letters long. 
- Each puzzle is based on a pangram, which is a word containing 7 unique letters and can be 7 to 15 letters long.

To get started, you can type:
    newpuzzle: To generate a new puzzle. You can even provide your own pangram for puzzle creation!
    loadpuzzle: To load a saved puzzle from a file. You will need to enter the file name of the saved puzzle.
    help: To see the list of all the commands.
    exit: To exit the program.

We hope you enjoy playing!
        ''')
        '''
        Documentation using prompt toolkit for tab-completion of commands
        Completion class:
            wrdcmp (word completer): this bascially just provides a way for auto completion based on specific words (which is self.x list we are passing to it)
            wrdcmp(self.x,ignore_case=True,match_middle=True)
                self.x: list of words we would like for auto completion to use
                ignore_case: case sensitviity variable (set to true since we allow A-Z characters)
                match_middle: variable that allows the command to be matched if the user is in the middle of typing it.
        Prompt class:
            prompt: This libraries wayh to get input from the user
            prompt(message,completer)
                message: some type of text for the user to see
                completer: this is built into the library defined by it, allows the user to press tab and autocomplete the commands we give it)
                Due to this, this is why we set cmdautocomplete = wrdcmp(self.b4commands,ignore_case=True,match_middle=True) because it will allow tab completion to
                happen with word completer.
        '''
        while (True):
            if self.controller.controllerGetPuzzleState() == 1:
                 #once a game is started the user will have access to all of the commands, so uses this instead.
                 cmdautocomplete = wrdcmp(self.commands,ignore_case=True,match_middle=True)
            userInput = prompt("Please enter a guess or command: ",completer=cmdautocomplete)
            checkInput = self.controller.checkInputCLI(userInput)
            while(checkInput == False):
                userInput = prompt("Input can only contain [A-Z], please reenter: ",completer=cmdautocomplete)
                checkInput = self.controller.checkInputCLI(userInput)
            while(len(userInput) < 4) or (len(userInput) > 15):
                userInput = prompt("Input must be between 4 and 15 characters! Please reenter your input: ",completer=cmdautocomplete)
            # controller user guess function

            match userInput.lower():
                case "newpuzzle":
                    self.newPuzzle()
                case "showpuzzle":
                    self.showPuzzle()
                case "showfoundwords":
                    self.showFoundWords()
                case "shuffleletters":
                    self.shuffleLetters()
                case "savepuzzle":
                    self.savePuzzle()
                case "loadpuzzle":
                    if self.controller.controllerGetPuzzleState() == 1:
                        wantSave = input("Do you want to save the current game before loading a new puzzle? (yes/no): ")
                        if wantSave.lower() == "yes":
                            inputFile = input("Please choose a name for the file: ")
                            print("Saving your game!")
                            self.controller.controllerSaveGame(inputFile)
                    inputFile = input("Enter the name of the file you want to load: ")
                    checkFile = inputFile + ".json"
                    if os.path.exists(checkFile):
                        self.controller.controllerGameLoadCLI(inputFile)
                        print("Puzzle loaded!")
                        self.showHoneyComb()
                    else:
                        print("Uh-oh! Couldn't find that file. Reenter the load command and try again.")
                case "showstatus":
                        if (self.controller.controllerGetPuzzleState() == 0):
                            print("No game started!")
                        else:
                            print("Rank: " + self.controller.controllerGetPuzzleRank())
                            print("User Points: " + str(self.controller.controllerGetPoints()))
                            print("Max points possible: " + str(self.controller.controllerGetPuzzleTotal()))
                case "gamehelp":
                       if(self.controller.controllerGetPuzzleState() == 0):
                        self.controller.controllerStartCommands()
                       else:
                        self.controller.controllerHelpCommand()
                case "gameexit":
                        self.controller.controllerGameExit()
                case "showhints":
                    if(self.controller.controllerGetPuzzleState() == 0):
                        print("No game started!")
                    else:
                        self.hint()
                case _:
                    if self.controller.controllerGetPuzzleState() != 1:
                        print('''
To get started, you can type:
    newpuzzle: To generate a new puzzle. You can even provide your own pangram for puzzle creation!
    loadpuzzle: To load a saved puzzle from a file. You will need to enter the file name of the saved puzzle.
    gamehelp: To see the list of all the commands.
    gameexit: To exit the program.
                        ''')
                    else:
                        if userInput in self.controller.controllerGetGuessedWordsGUI():
                            print("This word has already been guessed correctly.")
                        else:
                            self.controller.controllerUserGuess(userInput)
#singleton design pattern
view = view()
view.startGame()
