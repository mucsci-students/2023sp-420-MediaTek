from MVC.model import IdentifyBaseWord as np
from MVC.model import wordlist as wl
from MVC.model import Commands as Commands
import random
from MVC.model import loadgame as loadgame

'''
Player class with variables for the whole program.
'''
class player:
    def __init__(self): 
        self.gaUserLetters = ""
        self.gaReqLetter = ""
        self.gameState = 0
        #this will be used for the CLI honeycomb.
        self.displayLetters = []
        self.points = 0
        self.puzzleStarted = 0
        #list of the word bank
        self.getList = list()
        self.showRank = "Noob"
        self.puzzleTotal = 0
        #list to store correctly guessed words.
        self.guessedList = list()

class model:
    #should be called before gameLoad function, becauese it will reset all of the variables to their default state, and then gameLoad will update them
    #with the loaded file.
    def resetGame(self):
        self.p1 = player()

    def __init__(self):
        self.p1 = player()

    
    '''
    Function used for loading a game.
    Just updates the player objects variable with the information inside the file.
    '''  
    def gameLoad(self, loaded):
        self.p1.gaReqLetter = loaded['RequiredLetter']
        self.p1.gaUserLetters = loaded['PuzzleLetters']
        self.p1.points = loaded['CurrentPoints']
        self.p1.puzzleTotal = loaded['MaxPoints']
        self.p1.guessedList = loaded['GuessedWords']
        self.p1.getList = loaded['WordList']

        print("Required Letter: " + self.p1.gaReqLetter.upper())
        print("User Letters: " + self.p1.gaUserLetters.upper())
        print("Points Earned: " + str(self.p1.points))
        print("Total Obtainable Points: " + str(self.p1.puzzleTotal)) 
        print("Guessed Words: " + ", ".join(self.p1.guessedList))
        self.gameRank()
        self.p1.puzzleStarted = 1


    '''
    All of the functions below just return the information that is stored inside of the player class.
    '''
    def getGameState(self):
        return self.p1.gameState
    def getLetter(self):
        return self.p1.gaUserLetters.upper()
    def getReqLetter(self):
        return self.p1.gaReqLetter.upper()
    def getGuessedWords(self):
        return self.p1.guessedList
    def getWordList(self):
        return self.p1.getList
    def getPoints(self):
        return self.p1.points
    def getPuzzleState(self):
        return self.p1.puzzleStarted
    def getPuzzleTotal(self):
        return self.p1.puzzleTotal
    def getPuzzleRank(self):
        return self.p1.showRank
    def getHoneyCombList(self):
        return self.p1.displayLetters
    
    '''
    Update the puzzleStarted variable so we can track if a game has been started or not.
    '''
    def updatePuzzleState1(self):
        self.p1.puzzleStarted = 1
    def updatePuzzleState0(self):
        self.p1.puzzleStarted = 0

    '''
    This function just calculates the total points by checking the length, and if it's a pangram.
    It gets run once when a new game is started, so the total for the puzzle can be calculated 
    '''
    def calculateTotalPoints(self, wordBank):
        for x in wordBank:
            toSet = set(x)
            length = len(x)
            if length == 4:
                self.p1.puzzleTotal += 1
            else:
                if(len(toSet) == 7):
                    self.p1.puzzleTotal += (length + 7)
                else:
                    self.p1.puzzleTotal += length

    '''
    Function will check what the user entered is actually a pangram, then check if it actually exists within the file.
    '''
    def checkPangram(self,input):
        toSet = set(input)
        if (len(toSet) == 7):
            ft = np.ws.checkWord(input)
            return ft
        else:
            return False
        
    '''
    Function will create an automatically generated puzzle for the user, and run the function to calculate the total points
    '''
    def NewPuzzleAuto(self):
        self.p1.gaUserLetters, self.p1.gaReqLetter = np.autoGame()
        self.p1.getList = wl.generateWordList(self.p1.gaReqLetter, self.p1.gaUserLetters)
        self.calculateTotalPoints(self.p1.getList)

    '''
    Function will create a game based on the users input.
    '''
    def NewPuzzleBase(self,userInput):
        self.p1.gaUserLetters, self.p1.gaReqLetter = np.baseGame(userInput)
        self.p1.getList = wl.generateWordList(self.p1.gaReqLetter, self.p1.gaUserLetters)
        self.calculateTotalPoints(self.p1.getList)

    '''
    Function returns a list of the userLetters and removes the required letter from it.
    '''
    def lettersToList(self):
        #remove the required letter from the string.
        self.p1.displayLetters.clear()
        removeReqLetter = self.p1.gaUserLetters.replace(self.p1.gaReqLetter,'')
        #store this new string into a list
        for x in removeReqLetter:
            self.p1.displayLetters.append(x.upper())
    
    '''
    Shuffles the users letters
    '''
    def shuffleAuto(self):
        #SHUFFLE ALGO
        #replace the brackets within the user letters string
        replaceString = self.p1.gaUserLetters.replace("[","").replace("]","")
        #convert it to a list
        toList = list(replaceString)
        #use shuffle with the list to change the positions of the letters.
        random.shuffle(toList)
        #afterwards convert list to a string.
        shuffledLetters = ''.join(toList)
        self.p1.gaUserLetters = shuffledLetters
        #before abcdef, after fedcba
        self.lettersToList()
        return self.p1.gaUserLetters
    
    '''
    This function will take in the user input and check if it's a valid guess.
    It will convert what the user entered into all lower case since the json files given were only lower case words.
    The function also updates the players points variable based on the length and if it's a pangram
    Returns true or false depening on if what the user entered was a correct guess.
    '''
    def userGuess(self, userInput):
        totalPoints = 0
        #search if what the user types exists within the list
        toLower = userInput.lower()
        userInput = toLower
        if self.p1.gaReqLetter in userInput:
            if userInput in self.p1.getList:
                #create set from user input
                toSet = set(userInput)
                #determine length of set to be later to check for 7 unique characters (if a pangram)
                length = len(userInput)
                #store into user word bank

                #append to self.guessedList that I created, moved userWordList into the model.
                self.p1.guessedList.append(userInput)

                #print statements for testing
                print("Word accepted!")
                #remove the word from the word bank.
                self.p1.getList.remove(userInput)
                #generates user points based on the length, if it's a pangram then add an additional 7 points.
                if length == 4:
                    self.p1.points += 1
                else:
                    if(len(toSet) == 7):
                        self.p1.points += (length + 7)
                    else:
                        self.p1.points += length
                self.gameRank()
                return True
            else:
                print("Sorry! Couldn't find that word.")
                return False
        else:
            print("Hey! you didn't use the required letter!")
            return False
        
    '''
    Function calls the savePuzzle which will take in a bunch of important player variables and save them into a json file. 
    '''
    def saveGame(self, inputFile):
        Commands.savePuzzle(self.p1.gaReqLetter, self.p1.gaUserLetters, self.p1.points, self.p1.puzzleTotal, self.p1.guessedList, self.p1.getList,inputFile)
    def startCommands(self):
        Commands.commandsStart()
    def helpCommand(self):
        Commands.help()
    

    '''
    Function that updates the rank as the user points increases.
    '''
    def gameRank(self):
        #variable to store ranks
        #for a game in progress, matches point values to ranks
        calculatePercentage = ((self.p1.points/self.p1.puzzleTotal) * 100)
        if calculatePercentage >= 0 and calculatePercentage <= 1:
            self.p1.showRank = "Beginner"
        elif calculatePercentage > 1 and calculatePercentage <= 3:
            self.p1.showRank = "Good"
        elif calculatePercentage > 3 and calculatePercentage <= 6:
            self.p1.showRank = "Great"
        elif calculatePercentage > 6 and calculatePercentage <= 10:
            self.p1.showRank = "Novice"
        elif calculatePercentage > 10 and calculatePercentage <= 15:
            self.p1.showRank = "Amazing"
        elif calculatePercentage > 15 and calculatePercentage <= 25:
            self.p1.showRank = "Advanced"
        elif calculatePercentage > 25 and calculatePercentage <= 50:
            self.p1.showRank = "Expert"
        elif calculatePercentage > 50 and calculatePercentage < 100:    
            self.p1.showRank = "Master"
        else:
            self.p1.showRank = "Puzzle Finished! Good Job!"