from MVC.model import Model as mdl
import sys
import re
import json
import numpy 

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
    The functions below all specifically modify the puzzle in some shape or form.
    Information gets passed from the view, which then the controller passes into the model where all the logic happens to modify everything.
    '''

    '''
    Calls the shuffleAuto function
    Returns the shuffled letters.
    '''
    def controllerShuffleAuto(self):
        return self.model.shuffleAuto()

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
        with open(inputFile) as save:
            loaded = json.load(save)
        self.model.gameLoad(loaded)

    '''
    Calls the game load cli function
    '''
    def controllerGameLoadCLI(self, inputFile):
        with open(inputFile + ".json", "r") as save:
            loaded = json.load(save)
        self.model.gameLoad(loaded)

    '''
    Calls the resetGame function
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
                self.controllerGameExit()
        else:
            print("Okay... bye.")
            exit()
   
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
        if re.match("^[a-zA-Z]*$", userInput) and reqLetter in userInput:
            return True
        else:
            return False
    
    def checkInputCLI(self,userInput):
        if re.match("^[a-zA-Z]*$", userInput):
            return True
        else:
            return False
        
    '''
    Upon the game starting it asks if the user wants to play the game or not.
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

    '''
    Functions displays the total number of words, max points, and pangrams
    '''      
    def totalHint(self):
        lowerList = []
        getLetter = self.controllerGetLetters()
        reqLetter = self.controllerGetReqLetter()
        hexagonLetters = []
        hexagonLetters = self.controllerToList(getLetter,hexagonLetters)
         # Turns hexagons list lowercase
        for letter in hexagonLetters:
            lowerList.append(letter.lower()) 
        # Combines new hexagon list and reqLetter
        totalLetters =  lowerList + [reqLetter.lower()]
        self.words = self.controllerGetWordList()
        totalWords = 0
        self.maxPoints = self.controllerGetPuzzleTotal()
        # Adds up total words
        for word in self.words:
            totalWords += 1
        totPan = 0
        totPerf = 0
        # If all the letters are in a word it adds one to total pangram if one is 7 letters long and a pangram adds to total perfect
        for word in self.words:
            if set(totalLetters).issubset(set(word)):
                if len(word) == 7 and len(set(word)) == 7:
                    totPerf += 1
                totPan += 1
        return totPan,totPerf

    '''
    Function iterates through list of words and finds how many words start with a specific two letters then displays
    the total amount of words that begin with those two letters
    '''
    def firstTwo(self):
        count = {}
        self.totalWords = self.controllerGetWordList()
        # Goes through every wood in the word list and keeps count of the words with the same firs two letters
        for word in self.totalWords:
            two = word[0:2]
            if two in count:
                count[two] +=1
            else:
                count[two] = 1
        return count

    '''
    Displays a matrix where the top row is the lengths of words, the first column is the letters for the puzzle.
    Each row displays the letter the word begins with as well as how many words start with that letter and what their length is.
    The final column combines the total words for each letter and the final row displays the total words with the specific length.
    '''
    def gridHint(self):
        lowerList = []
        length = [4,5,6,7,8,9,10,11,12,13,14,15]
        getLetter = self.controllerGetLetters()
        reqLetter = self.controllerGetReqLetter()
        hexagonLetters = []
        hexagonLetters = self.controllerToList(getLetter,hexagonLetters)
        # Turns hexagons list lowercase
        for letter in hexagonLetters:
            lowerList.append(letter.lower()) 
        # Combines new hexagon list and reqLetter
        totalLetters =  lowerList + [reqLetter.lower()]
        self.totalWords = self.controllerGetWordList()
        # Initializes 9 by 14 matrix with object type
        x = numpy.empty((9,14),dtype=object)
        i = 1
        x[0,0] = ''
        x[0,13] = ''
        # Sets first row excluding the first and last row with letters
        for letter in totalLetters:
            x[i,0] = letter
            i += 1
        j = 1
        for lengths in length:
            x[0][j] = lengths
            # Count the number of words that start with each letter and have the given length
            for i, letter in enumerate(totalLetters):
                count = 0
                for word in self.totalWords:
                    # Compares letter  and checks the length and adds count to cell
                    if word.startswith(letter) and len(word) == lengths:
                        count += 1
                x[i+1, j] = count
            j += 1
        # Adds up rows and sets the value equal to the final element of row
        rowTotal = 0
        for k in range(1,8):
            for m in range(1,12):
                rowTotal += x[k,m]
            x[k,13] = rowTotal
            rowTotal = 0 
        # Adds up columns and sets the value equal to the final element of column   
        colTotal = 0
        wordSum = 0
        # Adds up all words
        for word in self.totalWords:
            wordSum += 1
        for l in range(1,13):
            for n in range(1,8):
                colTotal += x[n,l]
            x[8,l] = colTotal
            colTotal = 0 
        # Sets corner spots to desired values
        x[8,13] = wordSum
        x[8,0] = ""
        return x
   
    '''
    Function that gets total number of words
    '''
    def getTotalWords(self):
        wordSum =len (self.controllerGetWordList())
        return wordSum
        