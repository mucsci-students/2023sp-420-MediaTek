from MVC.model import IdentifyBaseWord as np
from MVC.model import wordlist as wl
from MVC.model import Commands as Commands
import random
from MVC.model import loadgame as loadgame
from cryptography.fernet import Fernet
import json

'''
Player class with variables for the whole program.
'''
class player:
    def __init__(self): 
        self.gaUserLetters = ""
        self.gaReqLetter = ""
        self.gameState = 0
        #this will be used for the CLI honeycomb.
        self.displayLetters = list()
        self.points = 0
        self.puzzleStarted = 0
        #list of the word bank
        self.getList = list()
        self.showRank = "Noob"
        self.puzzleTotal = 0
        #list to store correctly guessed words.
        self.guessedList = list()
        self.encryptedList = list()
        self.storeKey = None
        self.author = "MediaTek"
        self.game_id = None


class model:
    #should be called before gameLoad function, becauese it will reset all of the variables to their default state, and then gameLoad will update them
    #with the loaded file.
    def resetGame(self):
        self.p1 = player()

    def __init__(self):
        self.p1 = player()

    '''
    If you need more help understanding msg me in discord, or see documentation on functions below.
    Plenty of examples online on using Fernet for encryption/decryption, encode and decode too (geeksforgeeks, tutorialspoint, crypotgraphy.io, programwiz, etc)
    Function will encrypt the user word list
    Fernet(key) - symmetric encryption, ensures that something can't be read without the key, the key will be used to encrypt and decrypt data.
    encrypt(token) - this encrypts the data we pass into it, however the token MUST be in bytes. Our token variable is toBytes
    encode() - converts python string to bytes. *Important because tokens MUST be in bytes.
    decode() - converts the bytes back into the original string. *Important because we want to append the word BACK into the word bank after decrypting it.
    '''
    def encryptWords(self):
        #if the user is trying to encrypt when theres already an encrypted list clear the list beforehand.
        if len(self.p1.encryptedList) > 0:
            self.p1.encryptedList.clear()
        #ensure we grabbed the key for encryption.
        self.grabOurKey()
        #create a Fernet object with the key.
        f = Fernet(self.p1.storeKey)
        #iterate through the list of the word bank.
        for x in self.p1.getList:
            #convert each word (x) into bytes, by default uses utf-8.
            toBytes = x.encode()
            #encrypts the bytes using Fernet.
            encryptedBytes = f.encrypt(toBytes)
            #since we're storing strings into the json file, it's a must to use decode on the encrypted variable.
            #this will give us a string version of the bytes, which can later be used for decryption.
            encryptedString = encryptedBytes.decode()
            #append each new encrypted word into the encrypted list
            self.p1.encryptedList.append(encryptedString)
        
    '''
    Function will decrypt the loaded encrytped list and append it to the word bank.
    Run this only after a user loads in an encrypted puzzle.
    decrypt(token) - we are passing x (word in the list), which is going to be bytes after loading in an encrypted puzzle. 
    which then the function decrypts and gives us the original plaintext.
    '''
    def decryptWords(self):
        #ensure we grabbed the key for decryption
        self.grabOurKey()
        if len(self.p1.getList) > 0:
            self.p1.getList.clear()
        #next create a Fernet object that takes in the key our json file.
        f = Fernet(self.p1.storeKey)
        #iterate through the encrypted list to decrypt each word.
        for x in self.p1.encryptedList:
            #decrypt each byte string that was stored
            decryptByteString = f.decrypt(x)
            #decode the bytes into its original string.
            decryptedWord = decryptByteString.decode()
            #append this word into the word bank as it's a valid guess.
            self.p1.getList.append(decryptedWord)
        if len(self.p1.encryptedList) > 0:
            self.p1.encryptedList.clear()


    '''
    Function just grabs the key from the json file.
    First I created a file that stored the generated key, however just hardcoding it in is fine.
    String is just the ouput from generate_key() function using Fernet.
    '''
    def grabOurKey(self):
        keyAsString = "ipqzBB-cFSlZ4Fu9t7MF6szSBt-iNetGruZba41lCts="
        self.p1.storeKey = keyAsString.encode()
        
    '''
    Function used for loading a game.
    Just updates the player objects variable with the information inside the file.
    '''  
    def gameLoad(self, loaded):
        #checks the json file, if it has a field WordList we know that it's a regular file and not an encrypted one.
        if 'WordList' in loaded:
            self.p1.getList = loaded['WordList']
        else:
            checkAuthor = loaded['author']
            if checkAuthor != "MediaTek":
                self.p1.author = checkAuthor
                return
            self.p1.encryptedList = loaded['secretwordlist']
            self.decryptWords()
        self.p1.gaReqLetter = loaded['RequiredLetter']
        self.p1.gaUserLetters = loaded['PuzzleLetters']
        self.p1.points = loaded['CurrentPoints']
        self.p1.puzzleTotal = loaded['MaxPoints']
        self.p1.guessedList = loaded['GuessedWords']
        self.game_id = self.generateGameID()

        print("Required Letter: " + self.p1.gaReqLetter.upper())
        print("User Letters: " + self.p1.gaUserLetters.upper())
        print("Points Earned: " + str(self.p1.points))
        print("Total Obtainable Points: " + str(self.p1.puzzleTotal)) 
        print("Guessed Words: " + ", ".join(self.p1.guessedList))
        #added print statement below for testing encryption/decryption
        #print(self.p1.getList)
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
    def getAuthorField(self):
        return self.p1.author
    
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
    Generates the unique game id by placing the required letter in front
    followed by the rest of the letters sorted alphabetically, the required
    letter in front each time accounts for the 7 unique puzzles that can be 
    generated by having different required letters for the same 7 letters.
    '''
    def generateGameID(self):
        user_letters = list(self.p1.gaUserLetters)
        user_letters.remove(self.p1.gaReqLetter)
        sorted_letters = sorted(user_letters)
        game_id = f"{self.p1.gaReqLetter.upper()}{''.join(sorted_letters).upper()}"
        return game_id

    '''
    Function will create an automatically generated puzzle for the user, and run the function to calculate the total points
    '''
    def NewPuzzleAuto(self):
        self.p1.gaUserLetters, self.p1.gaReqLetter = np.autoGame()
        self.p1.getList = wl.generateWordList(self.p1.gaReqLetter, self.p1.gaUserLetters)
        self.calculateTotalPoints(self.p1.getList)
        self.game_id = self.generateGameID()

    '''
    Function will create a game based on the users input.
    '''
    def NewPuzzleBase(self,userInput):
        self.p1.gaUserLetters, self.p1.gaReqLetter = np.baseGame(userInput)
        self.p1.getList = wl.generateWordList(self.p1.gaReqLetter, self.p1.gaUserLetters)
        self.calculateTotalPoints(self.p1.getList)
        self.game_id = self.generateGameID()
        
    '''
    Getter function to get the game_id
    '''
    def getGameID(self):
        return self.game_id

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
    def saveEncryptedGame(self, inputFile):
        self.encryptWords()
        Commands.saveSecretPuzzle(self.p1.gaReqLetter, self.p1.gaUserLetters, self.p1.points, self.p1.puzzleTotal, self.p1.guessedList, self.p1.encryptedList, self.p1.author,inputFile)

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
