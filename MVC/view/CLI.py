import time
import re
from MVC.controller import controllerfile as ctrl
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
    #while loop for the CLI.
    def __init__(self):
        self.controller = ctrl.controller()
        #variable to store user letters into a list for displaying a honeycomb.
        self.displayLetters = []
        self.check = False
        self.b4commands = ["!newpuzzle","!loadpuzzle","!help","!exit"]
        self.commands = ["!newpuzzle","!showpuzzle","!showfoundwords","!shuffle","!savepuzzle","!loadpuzzle","!showstatus","!help","!exit"]



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
    !newpuzzle: To generate a new puzzle. You can even provide your own pangram for puzzle creation!
    !loadpuzzle: To load a saved puzzle from a file. You will need to enter the file name of the saved puzzle.
    !help: To see the list of all the commands.
    !exit: To exit the program.

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
            userInput = prompt("Please enter a guess or command, commands start with '!': ",completer=cmdautocomplete)
            checkInput = self.controller.checkInputCLI(userInput)
            while(checkInput == False):
                userInput = prompt("Input can only contain [!, A-Z], please reenter: ",completer=cmdautocomplete)
                checkInput = self.controller.checkInputCLI(userInput)
            while(len(userInput) < 4) or (len(userInput) > 15):
                userInput = prompt("Input must be between 4 and 15 characters! Please reenter your input: ",completer=cmdautocomplete)



            '''
            In the scenario that a user types in multiple exclamation points, or when using tab completion theres still multiple
            We can just check if the first spot in the string is an exclamation point and if the count of them is > 1, if so we can replace all !'s and just readd it at the end
            '''
            if (userInput[0] == '!') and userInput.count('!') > 1:
                 # replace all !'s with a space, then add a '!' back into the front of it.
                 rstring = userInput.replace("!","")
                 fstring = '!' + rstring
                 userInput = fstring

            if '!' not in userInput:
            # controller user guess function
                if self.controller.controllerGetPuzzleState() != 1:
                    print('''
To get started, you can type:
    !newpuzzle: To generate a new puzzle. You can even provide your own pangram for puzzle creation!
    !loadpuzzle: To load a saved puzzle from a file. You will need to enter the file name of the saved puzzle.
    !help: To see the list of all the commands.
    !exit: To exit the program.
                    ''')
                else:
                    if userInput in self.controller.controllerGetGuessedWordsCLI():
                        print("This word has already been guessed correctly.")
                    else:
                        self.controller.controllerUserGuess(userInput)

            match userInput.lower():
                case "!newpuzzle":
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
                        print("Req letters: " + self.controller.controllerGetReqLetter())
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
                        print("Req letters: " + self.controller.controllerGetReqLetter())
                        self.showHoneyComb()
                        self.controller.controllerUpdatePuzzleState1()
                case "!showpuzzle":
                        #lots of these are just printing stuff can be removed, just for testing purpsoe.
                        if (self.controller.controllerGetPuzzleState() == 0):
                            print("No game started!")
                        else:
                            print("Your letters: " + self.controller.controllerGetLetters())
                            print("Required letter: " + self.controller.controllerGetReqLetter())
                            print("Guessed words: " + str(self.controller.controllerGetGuessedWordsCLI()))
                            self.showHoneyComb()
                case "!showfoundwords":
                        if (self.controller.controllerGetPuzzleState() == 0):
                            print("No game started!")
                        else:
                            print("Guessed words: " + str(self.controller.controllerGetGuessedWordsCLI()))
                case "!shuffle":
                        if (self.controller.controllerGetPuzzleState() == 0):
                            print("No game started!")
                        else:
                            self.controller.controllerShuffleAuto()
                            self.showHoneyComb()
                            print("Your letters: " + self.controller.controllerGetLetters())
                case "!savepuzzle":
                        if (self.controller.controllerGetPuzzleState() == 0):
                            print("No game started!")
                        else:
                            inputFile = input("Please enter a name for the file: ")
                            self.controller.controllerSaveGame(inputFile)
                case "!loadpuzzle":
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
                case "!showstatus":
                        if (self.controller.controllerGetPuzzleState() == 0):
                            print("No game started!")
                        else:
                            print("Rank: " + self.controller.controllerGetPuzzleRank())
                            print("User Points: " + str(self.controller.controllerGetPoints()))
                            print("Max points possible: " + str(self.controller.controllerGetPuzzleTotal()))
                case "!help":
                       if(self.controller.controllerGetPuzzleState() == 0):
                        self.controller.controllerStartCommands()
                       else:
                        self.controller.controllerHelpCommand()
                case "!exit":
                        self.controller.controllerGameExit()
#singleton design pattern
view = view()
view.startGame()
