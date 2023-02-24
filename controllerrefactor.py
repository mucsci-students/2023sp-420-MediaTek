import modelrefactor as mdl
import sys
import re

class controller:
    def __init__(self):
        self.model = mdl.model()

    #GETTERS
    #functions will return the data that is stored within the object.
    def controllerGetLetters(self):
        return self.model.getLetter()
    def controllerGetGuessedWords(self):
        return self.model.getGuessedWords()
    def controllerGetWordList(self):
        return self.model.getWordList()
    def controllerShuffleAuto(self):
        return self.model.shuffleAuto()
    def controllerGetReqLetter(self):
        return self.model.getReqLetter()
    def controllerGetPoints(self):
        return self.model.getPoints()
    def controllerGetPuzzleState(self):
        return self.model.getPuzzleState()
    def controllerGetPuzzleTotal(self):
        return self.model.getPuzzleTotal()
    def controllerGetPuzzleRank(self):
        return self.model.getPuzzleRank()
    def controllerGetGameState(self):
        return self.model.getGameState()
    

    
    
    #UPDATE
    #these functions will update the game state/variables of the puzzle
    #as of right now trying to limit the amount of states we need, but an important one is puzzleStarted.
    def controllerShuffleAuto(self):
        return self.model.shuffleAuto()
        
    def controllerShuffleBase(self,userLetters):
        return self.model.shuffleBase(userLetters)

    def controllerUserGuess(self,userInput):
        return self.model.userGuess(userInput)

    def controllerGameRank(self,puzzleRank, getTotal):
        return self.model.gameRank(puzzleRank, getTotal)

    def controllerUpdatePuzzleState1(self):
        self.model.updatePuzzleState1()
    def controllerUpdatePuzzleState0(self):
        self.model.updatePuzzleState0()   
    def controllerRunAutoGame(self):
        self.model.NewPuzzleAuto()
    def controllerRunBaseGame(self):
        self.model.NewPuzzleBase()
    def controllerSaveGame(self, inputFile):
        self.model.saveGame(inputFile)
    def controllerGameLoad(self, inputFile):
        self.model.gameLoad(inputFile)
    def controllerNewGame(self):
        self.model.resetGame()
    def controllerStartCommands(self):
        self.model.startCommands()
    def controllerHelpCommand(self):
        self.model.helpCommand()
    def controllerGameExit(self):
        self.model.gameExit()


    
    #for hexagon letters in view
    def controllerToList(self,letters,viewList):
        for x in letters:
            viewList.append(x)
        return viewList


    #Checks to see if the string only contains letters and !
    def checkInput(self,userInput):
        if re.match("^[a-zA-Z!]*$", userInput):
            return True
        else:
            return False
    #For when starting the game
    def ensureYesOrNo(self):
        userInput = input("Would you like to play the game? (yes/no): ")
        while (userInput.lower() != 'yes') and (userInput.lower() != 'no'):
            print("Invalid input please enter yes or no!")
            userInput = input("Would you like to play our game? (yes/no): ")
        if userInput == "no":
            self.controllerGameExit()
        else:
            return
        