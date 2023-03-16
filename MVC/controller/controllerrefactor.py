from MVC.model import modelrefactor as mdl
import sys
import re

class controller:
    def __init__(self):
        self.model = mdl.model()

    '''
    Each function below is a getter that just returns the information stored/returns function values
    '''
    def controllerGetLetters(self):
        return self.model.getLetter()
    
    
    def controllerGetGuessedWordsGUI(self):
        return self.model.getGuessedWords()
    def controllerGetGuessedWordsCLI(self):
        words = self.model.getGuessedWords()
        return ', '.join(words)

        
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
    def controllerGetHoneyCombList(self):
        return self.model.getHoneyCombList()
    
    

    def controllerToHoneyComblist(self):
        self.model.lettersToList()

    

    '''
    These functions below all specifically modify the puzzle in some shape or form.
    Information gets passed from the view, which then the controller passes into the model where all the logic happens to modify everything.
    '''

    '''
    Calls the shuffleAuto function
    Returns the shuffled letters.
    '''
    def controllerShuffleAuto(self):
        return self.model.shuffleAuto()
        
    '''
    Calls the shuffleBase function
    Returns the shuffled letters.
    '''
    def controllerShuffleBase(self,userLetters):
        return self.model.shuffleBase(userLetters)

    '''
    Calls the userGuess function and will pass the userinput from view into it.
    Returns a boolean based on whether or not the user made a correct guess.
    '''
    def controllerUserGuess(self,userInput):
        return self.model.userGuess(userInput)
    
    '''
    Calls the gameRank function that will update the rank of the player.
    '''
    def controllerGameRank(self):
        return self.model.gameRank()


    '''
    Calls the updatPuzzleState1 function, which just updates the puzzleStarted variable.
    '''
    def controllerUpdatePuzzleState1(self):
        self.model.updatePuzzleState1()
    '''
    Calls the updatePuzzleState0 function, which just updates the puzzleStarted variable.
    '''
    def controllerUpdatePuzzleState0(self):
        self.model.updatePuzzleState0()  
    '''
    Calls the New Puzzle Auto function
    ''' 
    def controllerRunAutoGame(self):
        self.model.NewPuzzleAuto()
    '''
    Calls the New Puzzle Base function
    '''
    def controllerRunBaseGame(self,userInput):
        self.model.NewPuzzleBase(userInput)
    '''
    Calls the save game function
    '''
    def controllerSaveGame(self, inputFile):
        self.model.saveGame(inputFile)
    '''
    Calls the game load gui function
    '''
    def controllerGameLoadGUI(self, inputFile):
        self.model.gameLoadGUI(inputFile)
    '''
    calls the game load cli function
    '''
    def controllerGameLoadCLI(self, inputFile):
        self.model.gameLoadCLI(inputFile)
    '''
    calls the resetGame function
    '''
    def controllerNewGame(self):
        self.model.resetGame()
    '''
    Calls the start commands function
    '''
    def controllerStartCommands(self):
        self.model.startCommands()
    '''
    Calls the help command function
    '''
    def controllerHelpCommand(self):
        self.model.helpCommand()
    '''
    Calls the gameExit function
    '''
    def controllerGameExit(self):
        '''
           if self.p1.puzzleStarted:
            gamesave = input("Do you wish to save your game? (yes/no): ")
            if gamesave == "yes":
                # if so, save it
                inputFile = input("Please enter a name for the save file: ")
                self.saveGame(inputFile)
                print("Puzzle saved! Goodbye!")
                exit()
            elif gamesave == "no":
                # if not, don't.
                print("Okay! See you on the other side!")
                exit()
            else:
                print("Please enter \"yes\" or \"no\"!")
                self.gameExit()
        # If a puzzle isn't loaded, just leave.
        else:
            print("Okay... bye.")
            exit()
        '''
        if self.model.getPuzzleState() == 1:
            gamesave = input("Do you wish to save your game? (yes/no): ")
            if gamesave == "yes":
                # if so, save it
                inputFile = input("Please enter a name for the save file: ")
                self.model.saveGame(inputFile)
                print("Puzzle saved! Goodbye!")
                exit()
            elif gamesave == "no":
                # if not, don't.
                print("Okay! See you on the other side!")
                exit()
            else:
                print("Please enter \"yes\" or \"no\"!")
                self.gameExit()
        else:
            print("Okay... bye.")
            exit()

        #self.model.gameExit()
    '''
    Calls the new puzzle base gui function, passing userInput.
    '''
    '''def controllerRunBaseGameGUI(self,userInput):
        self.model.NewPuzzleBaseGUI(userInput)'''

    
    '''
    Funciton calls the checkPangram function and passes user input into it
    '''

    def controllerCheckPangram(self,input):
        return self.model.checkPangram(input)


    
    '''
     Both functions will append the puzzle letters into a list so they can be used to display on the honeycombs.
     Returns: list of letters
    '''
    def controllerToList(self,letters,viewList):
            for x in letters:
                viewList.append(x)
            return viewList
    
    def controllerToListCLI(self,cliList):
            letters = self.controllerGetLetters()
            for x in letters:
                cliList.append(x)
            return cliList



    '''
    Both functions check if the input making sure it just contains letters 
    One takes in a required letter, because within the CLI that's already checked. However in the GUI we use a input box
    Checking for the req letter here is much easier due to that.
    Returns true or false.
    '''
    def checkInput(self,userInput, reqLetter):
        print(userInput)
        print(reqLetter)
        if re.match("^[a-zA-Z!]*$", userInput) and reqLetter in userInput:
            return True
        else:
            return False
    
    def checkInputCLI(self,userInput):
        if re.match("^[a-zA-Z!]*$", userInput):
            return True
        else:
            return False
    '''
    Upon the game starting it asks if the user wants to play the game or not.
    Added this to not clutter the CLI
    '''
    def ensureYesOrNo(self):
        userInput = input("Would you like to play the game? (yes/no): ")
        while (userInput.lower() != 'yes') and (userInput.lower() != 'no'):
            print("Invalid input please enter yes or no!")
            userInput = input("Would you like to play our game? (yes/no): ")
        if userInput == "no":
            self.controllerGameExit()
        else:
            return
        