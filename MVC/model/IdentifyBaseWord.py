import random
import re
from MVC.model import wordstuff as ws
from MVC.model import pangramdb as pgdb

'''
Note for team: to properly run this program, you must have the file in the same directory as your json files. Also make sure your json files match my pangram_files name
Current bug: Bugs out at line 91 sometimes, I couldn't reproduce it but it was some type of out of bounds error something to do with the index.
Author: Austin An, Noah Barger
'''
#in the scenario the user doesn't input their own base word for the game.
#will implement this in at a later time, but pretty sure below code will just be in this functions scope.
#create variable to store pangram files in.

def autoGame():
    userLetters = None
    reqLetter = None

    #set pangram equal to the returned value from randomBase, type casted into string just in case unsure if needed.
    userPangram = str(pgdb.randomBase())

    #remove unwanted characters from set so only the string will only consist of letters 
    #using a set, it removes all duplicate letters that exist in the value.
    letterSet = set(userPangram)
    letterSetString = str(letterSet)
    #regular expression to filter out unncessary characters from the string, since it's a set it has ', {, and spaces etc...
    userLetters = re.sub(r'[^a-zA-z]+','', letterSetString)

    #choose one of the letters to be a required letter
    #some weird out of bounds bug that happens, unsure how to fix as of right now.  
    randReqLetterNum = random.randint(0,(len(userLetters)-1))
    reqLetter = userLetters[randReqLetterNum]
    test = list(userLetters)
    random.shuffle(test)
    userLetters = str(test)
    userLetters = re.sub(r'[^a-zA-z]+','', str(test))
    replaceString = userLetters.replace("[","").replace("]","")
    userLetters = replaceString
    return userLetters, reqLetter
    

def baseGame(input):
    bguserLetters = None
    bgreqLetter = None
    userInput = input.lower()
    getWords = list()

    getSet = set(userInput)
    if len(getSet) != 7:
        return "",""
    
    #get length of input
    getLength = len(userInput)
    #input must be between 7 and 15
    if (getLength >= 7) and (getLength <= 15):
        #convert length into string and concatenate with the string
        #check if user input is within the list
        #if so it's a pangram.
        if ws.checkWord(userInput):
            letterSet = set(userInput)
            letterSetString = str(letterSet)
            bguserLetters = re.sub(r'[^a-zA-z]+','', letterSetString)
            randReqLetterNum = random.randint(0,(len(bguserLetters)-1))
            bgreqLetter = bguserLetters[randReqLetterNum]
            return bguserLetters, bgreqLetter
        #so when the pangram they enter doesn't exist
        else: 
            return "",""
    #if they enter an invalid length
    else:
        return "",""