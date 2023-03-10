import time
import re
from MVC.controller import controllerrefactor as ctrl
from MVC.model import Commands as Commands
import random
import json
from MVC.model import loadgame as loadgame
import sys
import os
import textwrap


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

        while (True):
            userInput = input("Please enter a guess or command, commands start with '!': ")
            checkInput = self.controller.checkInputCLI(userInput)
            while(checkInput == False):
                userInput = input("Input can only contain [!, A-Z], please reenter: ")
                checkInput = self.controller.checkInputCLI(userInput)
            while(len(userInput) < 4) or (len(userInput) > 15):
                userInput = input("Input must be between 4 and 15 characters! Please reenter your input: ")

            if '!' not in userInput:
                #controller user guess function
                if self.controller.controllerGetPuzzleState() != 1:
                     print("Make sure to start a puzzle before guessing")
                else:
                    self.controller.controllerUserGuess(userInput)

            match userInput:
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
                    isAuto = input("Do you want it to be automatically generated?: ")
                    while isAuto.lower() != "yes" and isAuto.lower() != "no":
                        isAuto = input("Do you want it to be automatically generated?: ")
                    
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
          
view = view()
view.startGame()