from MVC.controller import Controller as ctrl
from MVC.model import Commands as Commands
import random
import os
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter as wrdcmp
from MVC.model.Highscores import saveHighScore
from MVC.model.Highscores import loadHighScore

#see bottom of file for an explanation on our usage of prompt_toolkit
global controller 
controller = ctrl.controller()
class view:        
    instance = None
    '''
    Creates a new single instance for the view if none exists already.
    '''
    def __new__(self):
        if self.instance is None:
              self.instance = super().__new__(self)
        return self.instance

    '''
    Default consturctor for our view.
    '''
    def __init__(self):
        self.controller = controller
        #variable to store user letters into a list for displaying a honeycomb.
        self.displayLetters = []
        self.check = False
        self.b4commands = ["newpuzzle","loadpuzzle","gamehelp","gameexit"]
        self.commands = ["newpuzzle","showpuzzle","showfoundwords","shuffleletters","savepuzzle","loadpuzzle","showstatus","showhints","gamehelp","gameexit","giveup","showhighscore"]

    def hint(self):
        hints = [self.grid(),self.hintCount(),self.totHint()]
        hint = random.choice(hints)

    '''
    Function that asks for user to input a file name they'd like to create a save of.
    * TO PUT INTO NEW CLI FILE.
    '''
    def save(self):
        if (self.controller.controllerGetPuzzleState() == 0):
            print("No game started!")
        else:
            inputFile = input("Please enter a name for the file: ")
            userInput = input("Would you like to encrypt the puzzle? (yes/no): ")
            while userInput.lower() != "yes" and userInput.lower() != "no":
                userInput = input("Invalid input, would you like to encrypt the puzzle? (yes/no): ")
            saveType = None
            if (userInput.lower() == "no"):
                saveType =  ctrl.controller.NonEncryptedSave(self.controller)
            else:
                saveType = ctrl.controller.EncryptedSave(self.controller)
        saveType.execute(inputFile)
                
    '''
    Function loads an existing puzzle into the game.
    
    CHANGES TO PUT IN NOAHS FILE: See *'S BELOW.
    '''
    def load(self):
        if self.controller.controllerGetPuzzleState() == 1:
            check = self.controller.ensureYesOrNoSave()
            if check == True:
                self.save()
        inputFile = input("Enter the name of the file you want to load: ")
        checkFile = inputFile + ".json"
        if os.path.exists(checkFile):
            self.controller.controllerGameLoadCLI(inputFile)
            #*********************
            #print(self.controller.controllerGetDecryptionFlag())
            if(self.controller.controllerGetAuthorField() != "MediaTek") or (self.controller.controllerGetDecryptionFlag() == True):
                print("Hey, we can't decrypt this puzzle! This is because we didn't encrypt it to begin with!")
                self.controller.controllerUpdateAuthorField()
                return
            else:
                print("Puzzle loaded!")
                self.showHoneyComb()
            #*********************
        else:
            print("Uh-oh! Couldn't find that file. Reenter the load command and try again.")

    '''
    Function displays the honeycomb for the CLI
    '''
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
        
    def shuffleLetters(self):
        if (self.controller.controllerGetPuzzleState() == 0):
            print("No game started!")
        else:
            self.controller.controllerShuffleAuto()
            self.showHoneyComb()
            print("Your letters: " + self.controller.controllerGetLetters())

    '''
    Function that just displays the data related to the puzzle.
    '''
    def showPuzzle(self):
        if (self.controller.controllerGetPuzzleState() == 0):
            print("No game started!")
        else:
            print("Your letters: " + self.controller.controllerGetLetters())
            print("Required letter: " + self.controller.controllerGetReqLetter())
            print("Guessed words: " + str(self.controller.controllerGetGuessedWordsCLI()))
            self.showHoneyComb()
    
    '''
    give up function/command that allows the player to say they are finished with a puzzle.
    this sends the game id, player name, and points to the highscore database to update the
    highscore for the puzzle referred to by the unique puzzle id.
    '''   
    def giveUp(self, puzzleFinished=False):
        if not puzzleFinished:
            while True:
                confirm = input("Are you sure you want to give up? (yes/no): ")
                if confirm.lower() == "yes":
                    break
                elif confirm.lower() == "no":
                    print("Continuing the game.")
                    return
                else:
                    print("Invalid input. Please enter 'yes' or 'no'.")

        points = self.controller.controllerGetPoints()
        game_id = self.controller.controllerGetGameID()
        #ask for username
        while True:
            player_name = input("Please enter your 3-character username: ")
            if len(player_name) == 3 and player_name.isalnum():
                player_name = player_name.upper()
                break
            else:
                print("Invalid input. Please enter a 3-character alphanumeric username.")
        #save the highscore
        saveHighScore(game_id, player_name, points)
        #displays the highscores when giving up
        game_id = self.controller.controllerGetGameID()
        highScores = loadHighScore(game_id) 
        print(f"\nHIGH SCORES:\n")
        header = "NAME         SCORE"
        print(header)
        for row in highScores:
            padding = (len(header) - len(row[1])) // 2
            print(f"{row[1]:<13}{row[2]:^{padding}}")
        exit()
                            
    '''
    Displays the top ten local high scores
    '''
    def showHighScore(self):
        game_id = self.controller.controllerGetGameID()
        highScores = loadHighScore(game_id)
        if highScores:
            print(f"\nHIGH SCORES:\n")
            header = "NAME         SCORE"
            print(header)
            for row in highScores:
                padding = (len(header) - len(row[1])) // 2
                print(f"{row[1]:<13}{row[2]:^{padding}}")
        else:
            print(f"No high scores yet!")

    def showStatus(self):
        if (self.controller.controllerGetPuzzleState() == 0):
            print("No game started!")
        else:
            print("Rank: " + self.controller.controllerGetPuzzleRank())
            print("User Points: " + str(self.controller.controllerGetPoints()))
            print("Max points possible: " + str(self.controller.controllerGetPuzzleTotal()))

    def showHelp(self):
        if(self.controller.controllerGetPuzzleState() == 0):
            self.controller.controllerStartCommands()
        else:
            self.controller.controllerHelpCommand()
    
    '''
    Formats return value of grid controller function so that it is clean and visable
    '''
    def grid(self):
        x = self.controller.gridHint()

        # Sets cell with and formats it
        cell_width = 3
        fmt = '{:>' + str(cell_width) + '}'
        # Goes through grid formaating each row
        message = "\n".join(" ".join(fmt.format(col) for col in row) for row in x)
        print("Grid Hint:\n" + message)
        print("\n")
        
    '''
    Formats return value of firstTwo so that brackets and quotes are removed
    '''
    def hintCount (self):
        count = self.controller.firstTwo()
        print("Two Word List:")
        # Iterates through list and removes brackets and quotes
        for key, value in count.items():
            print(f"{key}: {value}")

        print("\n")

    '''
    Displays total words, max points a player can earn
    '''
    def totHint(self):
        x,y = self.controller.totalHint()
        # Prints
        print(f"WORDS:{self.controller.getTotalWords()}\nPOINTS:{self.controller.controllerGetPuzzleTotal()}\nPANGRAMS:{x} ({y} Perfect)")
    
    '''
    Helper function used in new puzzle command runs the game dependent on them answering yes or no for it being automatically generated
    game: a string that will be either yes or no
    Displays the user letter, req letter, and honeycomb in the end.
    '''
    def newPuzzleHelper(self,game):
        if game.lower() == "yes":
            self.controller.controllerRunAutoGame()
        elif game.lower() == "no":
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
    

    '''
    Function for new puzzle command, just asks for input and generates a new puzzle.
    '''
    def newPuzzle(self):
        if(self.controller.controllerGetPuzzleState() == 1):
            wantSave = self.controller.ensureYesOrNoSave()
            if (wantSave == True):
                self.save()
                print("Saving your game!")
            else:
                print("Ok, lets generate a new puzzle! ")
        self.controller.controllerNewGame()
        isAuto  = input("Do you want it to be automatically generated? (yes/no): ")
        while isAuto.lower() != "yes" and isAuto.lower() != "no":
            isAuto = input("Do you want it to be automatically generated? (yes/no): ")
    
        if (isAuto.lower() == "yes") or isAuto.lower() == "no":
            self.newPuzzleHelper(isAuto)

    '''
    Function is the game itself and keeps running until the user exits.
    '''
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
    gamehelp: To see the list of all the commands.
    gameexit: To exit the program.

We hope you enjoy playing!
        ''')

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

            # pattern matching for commands
            match userInput.lower():
                case "newpuzzle":
                    self.newPuzzle()
                case "showpuzzle":
                    self.showPuzzle()
                case "showfoundwords":
                    self.controller.showFoundWords()
                case "shuffleletters":
                    self.shuffleLetters()
                case "savepuzzle":
                    self.save()
                case "loadpuzzle":
                    self.load()
                case "showstatus":
                        self.showStatus()
                case "gamehelp":
                      self.controller.help()
                case "giveup":
                        self.giveUp()
                case "showhighscore":
                        self.showHighScore()
                case "gameexit":
                        self.controller.controllerGameExit()
                case "showhints":
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
                            if self.controller.controllerGetReqLetter().lower() in userInput:
                                self.controller.controllerUserGuessCLI(userInput)
                            else:
                                print("ERROR: Required letter not used!")
                            
                            #check if game is finished, if so call giveUp
                            if self.controller.controllerGetPuzzleRank() == "Puzzle Finished! Good Job!":
                                self.giveUp()
   
#singleton design pattern
view = view()
view.startGame()

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
