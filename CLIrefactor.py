import time
import re
import controllerrefactor as ctrl
import Commands
import random
import json
import loadgame
import sys
import os

#create controller object
controller = ctrl.controller()
print("Hello! Welcome to MediaTek's Spelling bee!")
print("The goal of this game is to guess as many words as you can to accumulate points!")
controller.ensureYesOrNo()

#while loop for the CLI.
while (True):
    userInput = input("Please enter a guess or command, commands start with '!': ")
    checkInput = controller.checkInput(userInput)
    while(checkInput == False):
        userInput = input("Input can only contain [!, A-Z], please reenter: ")
        checkInput = controller.checkInput(userInput)
    while(len(userInput) < 4) or (len(userInput) > 15):
        userInput = input("Input must be between 4 and 15 characters! Please reenter your input: ")

    if '!' not in userInput:
          #controller user guess function
          controller.controllerUserGuess(userInput)

    match userInput:
        case "!newpuzzle":
            if(controller.controllerGetPuzzleState() == 1):
                wantSave = input("Hey do you want to save the game? (yes/no): ")
                if (wantSave.lower() == "yes"):
                    inputFile = input("Please choose a name for the file: ")
                    print("Saving your game!")
                    controller.controllerSaveGame(inputFile)
                else:
                      print("Ok, lets generate a new puzzle! ")
            controller.controllerNewGame()
                  
            isAuto = input("Do you want it to be automatically generated?: ")
            if (isAuto.lower() == "yes"):
                controller.controllerRunAutoGame()
                print("User letters: " + controller.controllerGetLetters())
                print("Req letters: " + controller.controllerGetReqLetter())
                controller.controllerUpdatePuzzleState1()
            if (isAuto.lower() == "no"):
                controller.controllerRunBaseGame()
                controller.controllerUpdatePuzzleState1()
        
        case "!showpuzzle":
                #lots of these are just printing stuff can be removed, just for testing purpsoe.
                print("Your letters: " + controller.controllerGetLetters())
                print("Required letter: " + controller.controllerGetReqLetter())
                print("Guessed words: " + str(controller.controllerGetGuessedWords()))
                print("Word Bank: " + str(controller.controllerGetWordList()))
                print("User Points: " + str(controller.controllerGetPoints()))
                print("Max points possible: " + str(controller.controllerGetPuzzleTotal()))
        case "!showfoundwords":
                print("Guessed words: " + str(controller.controllerGetGuessedWords()))
        case "!shuffle":
                 controller.controllerShuffleAuto()
                 print("Your letters: " + controller.controllerGetLetters())
        case "!savepuzzle":
                inputFile = input("Please enter a name for the file: ")
                controller.controllerSaveGame(inputFile)
        case "!loadpuzzle":
                inputFile = input("Enter the name of the file you want to load: ")
                checkFile = inputFile + ".json"
                if (os.path.exists(checkFile)):
                    controller.controllerGameLoad(inputFile)
                    print("Puzzle loaded!")
                else:
                    #Tell the user the file doesn't exist
                    print("Uh-oh! Couldn't find that file. Reenter the load command and try again.")
        case "!showstatus":
                print("Rank: " + controller.controllerGetPuzzleRank())
        case "!help":
                print("help")
        case "!exit":
                exit()
          


