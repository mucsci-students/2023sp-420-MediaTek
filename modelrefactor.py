import time
import re
import IdentifyBaseWord as np
import wordlist as wl
import Commands
import random
import json
import loadgame
import sys
import os

#controller file should use model functions to manipulate the data 
#controller file should also have a method for every single function that is inside of the model class
#instantiate player and model at correct time.
class player:
    def __init__(self): 
        self.gaUserLetters = ""
        self.gaReqLetter = ""
        self.gameState = 0
        #self.checkAuto = 0
        #self.checkBase = 0
        self.points = 0
        self.puzzleStarted = 0
        #list of the word bank
        self.getList = list()
        self.showRank = "Noob"
        self.puzzleTotal = 0
        #self.isLoaded = 0
        #list to store correctly guessed words.
        self.guessedList = list()

class model:
    #should be called before gameLoad function, becauese it will reset all of the variables to their default state, and then gameLoad will update them
    #with the loaded file.
    def resetGame(self):
        self.p1 = player()

    def __init__(self):
        self.p1 = player()

    def gameLoad(self, inputFile):
        # open the json file and load its contents
        loadGame = list()
        with open(inputFile + ".json", "r") as save:
            loaded = json.load(save)
        
        # for each element in a file, make it a separate entry in the list.
        for l in loaded:
            loadGame.append(l)
        
        # assign values based on the position of each element in the list.
        self.p1.gaUserLetters = loadgame.loadUserLetters(loadGame[0])
        self.p1.gaReqLetter = loadgame.loadRequiredLetter(loadGame[1])
        self.p1.guessedList = loadgame.loadGuessedWords(loadGame[2])
        self.p1.getList = loadgame.loadWordBank(loadGame[3])
        self.p1.points = loadgame.loadTotalPoints(loadGame[4])
        self.p1.puzzleStarted = 1

    def test1(self,userInput):
        self.p1.gaUserLetters = userInput  

    
    def getGameState(self):
        return self.p1.gameState
    def getLetter(self):
        return self.p1.gaUserLetters
    def getReqLetter(self):
        return self.p1.gaReqLetter
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
    
    #
    def updatePuzzleState1(self):
        self.p1.puzzleStarted = 1
    def updatePuzzleState0(self):
        self.p1.puzzleStarted = 0

    #calculates total points within the players word bank.
    #will only be run once per new puzzle.
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
    
    def NewPuzzleAuto(self):
        self.p1.gaUserLetters, self.p1.gaReqLetter = np.autoGame()
        self.p1.getList = wl.generateWordList(self.p1.gaReqLetter, self.p1.gaUserLetters)
        self.calculateTotalPoints(self.p1.getList)

    def NewPuzzleBase(self):
        self.p1.gaUserLetters, self.p1.gaReqLetter = np.baseGame()
        while (self.p1.gaUserLetters == "empty") and (self.p1.gaReqLetter == "empty"):
             self.p1.gaUserLetters, self.p1.gaReqLetter = np.baseGame()
        self.p1.getList = wl.generateWordList(self.p1.gaReqLetter, self.p1.gaUserLetters)
        self.calculateTotalPoints(self.p1.getList)
        print(self.p1.getList)


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
        return self.p1.gaUserLetters

    def shuffleBase(self,userLetters):
        #SHUFFLE ALGO
        replaceString = userLetters.replace("[","").replace("]","")
        toList = list(replaceString)
        random.shuffle(toList)
        shuffledLetters = ''.join(toList)
        self.p1.gaUserLetters = shuffledLetters
        return self.p1.gaUserLetters

    def userGuess(self, userInput):
        totalPoints = 0
        #search if what the user types exists within the list
        #print(self.p1.getList)
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
            else:
                print("Sorry! Couldn't find that word.")
        else:
            print("Hey! you didn't use the required letter!")
    def saveGame(self, inputFile):
        Commands.savePuzzle(self.p1.gaUserLetters, self.p1.gaReqLetter, self.p1.guessedList, self.p1.getList, self.p1.points, inputFile)
    def startCommands(self):
        Commands.commandsStart()
    def helpCommand(self):
        Commands.help()
    

    #This needs to be rewritten.
    def gameRank(self):
        #variable to store ranks
        #for a game in progress, matches point values to ranks
        #redo so that we take words from userunique, get point values (can yoink code above ^) for total value, use that value to do like getTotal < value * .10 (ten percent?) etc...
        calculatePercentage = ((self.p1.points/self.p1.puzzleTotal) * 100)
        if calculatePercentage >= 0 and calculatePercentage <= 20:
            self.p1.showRank = "Beginner"
        elif calculatePercentage > 20 and calculatePercentage <= 40:
            self.p1.showRank = "Novice"
        elif calculatePercentage > 40 and calculatePercentage <= 60:
            self.p1.showRank = "Advanced"
        elif calculatePercentage > 60 and calculatePercentage <= 80:
            self.p1.showRank = "Expert"
        else:    
            self.p1.showRank = "Master"