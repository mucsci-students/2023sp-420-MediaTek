import json
import random
import re
'''
Note for team: to properly run this program, you must have the file in the same directory as your json files. Also make sure your json files match my pangram_files name
Current bug: Bugs out at line 91 sometimes, I couldn't reproduce it but it was some type of out of bounds error something to do with the index.
Author: Austin An, Noah Barger
'''
#in the scenario the user doesn't input their own base word for the game.
#will implement this in at a later time, but pretty sure below code will just be in this functions scope.

#create variable to store pangram files in.
pangram_files = ['7letterpangram.json','8letterpangram.json','9letterpangram.json','10letterpangram.json','11letterpangram.json','12letterpangram.json','13letterpangram.json',
'14letterpangram.json','15letterpangram.json']

def autoGame():
    userLetters = None
    reqLetter = None
    #random variable to choose from a random pangram list
    randNum = random.randint(0,8)
    #use random variable to load json file into data variable.
    #using pattern matching
    #matches randNum to the cases: pretty much similar to a switch statement but I read online switch statements don't exist in python.
    match randNum:
        case 0:
            with open(pangram_files[0], "r") as file:
                data = json.load(file)
        case 1:
            with open(pangram_files[1], "r") as file:
                data = json.load(file)
        case 2:
            with open(pangram_files[2], "r") as file:
                data = json.load(file)
        case 3:
            with open(pangram_files[3], "r") as file:
                data = json.load(file)
        case 4:
            with open(pangram_files[4], "r") as file:
                data = json.load(file)
        case 5:
            with open(pangram_files[5], "r") as file:
                data = json.load(file)
        case 6:
            with open(pangram_files[6], "r") as file:
                data = json.load(file)
        case 7:
            with open(pangram_files[7], "r") as file:
                data = json.load(file)
        case 8:
            with open(pangram_files[8], "r") as file:
                data = json.load(file)
    #store a random word from one of the files above into a variable
    randomPangram = random.choice(data)

    #typecast variable into a string, and store the VALUE of the key "word"
    userPangram = str(randomPangram["word"])


    #added this for extra testing.
    #check pangram file that's selected with the word that selected.
    # for x in range(0,len(userPangram)):
        # print(userPangram[x])


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
    #    print ("USERS REQUIED LETTER : ****" + reqLetter + "****")
    #    print ("LETTERS AVAILABLE FOR USE: " + userLetters)
    test = list(userLetters)
    random.shuffle(test)
    userLetters = str(test)
    userLetters = re.sub(r'[^a-zA-z]+','', str(test))
    return userLetters, reqLetter
    
def baseGame():
    bguserLetters = None
    bgreqLetter = None
    getWords = list()

        #"word": "abhenry"

        #get user input, need to add checks like length, what if it isn't valid etc.
    userInput = input("Please give a valid pangram: ")
    userInput.lower()
    
    while(len(userInput) < 7):
        userInput = input("Input must be at least 7 characters long! Please reenter a guess/command: ")
    
    getLength = len(userInput)
    if (getLength >= 7) and (getLength <= 15):
        fileName = str(getLength) + "letterpangram.json"
        with open (fileName, "r") as file:
            data = json.load(file)
        for word in data:
            getWords.append(str(word["word"]))
        if userInput in getWords:
            letterSet = set(userInput)
            letterSetString = str(letterSet)
            bguserLetters = re.sub(r'[^a-zA-z]+','', letterSetString)
            randReqLetterNum = random.randint(0,(len(bguserLetters)-1))
            bgreqLetter = bguserLetters[randReqLetterNum]
            return bguserLetters, bgreqLetter
        else: 
            print("Uh oh, looks like you didn't enter a pangram that exists with the json file!")
            #bguserLetters = "empty"
            #bgreqLetter = "empty"
            return "empty","empty"
    else:
        print("invalid length, ensure the length of input is 7-15")
        return "empty","empty"





    '''
    
    #use pattern matching to load the file based on the length of the pangram the user gives.
    match getLength:
        #each case is exactly the same but the length determines what file gets loaded.
        case 7:
            #open file from pangram list above
            with open(pangram_files[0], "r") as file:
                data = json.load(file)
            #store each word inside of the json file into a getWords list.
            for word in data:
                getWords.append(str(word["word"]))
            #checks to see if what the user inputs actually exists within getWords.
            if userInput in getWords:
                letterSet = set(userInput)
                letterSetString = str(letterSet)
                bguserLetters = re.sub(r'[^a-zA-z]+','', letterSetString)
                randReqLetterNum = random.randint(0,(len(bguserLetters)-1))
                bgreqLetter = bguserLetters[randReqLetterNum]
                return bguserLetters, bgreqLetter
            else: 
                print("Uh oh, looks like you didn't enter a pangram that exists with the json file!")
                #bguserLetters = "empty"
                #bgreqLetter = "empty"
                return "empty","empty"
        case 8:
            with open(pangram_files[1], "r") as file:
                data = json.load(file)
            for word in data:
                getWords.append(str(word["word"]))
            if userInput in getWords:
                letterSet = set(userInput)
                letterSetString = str(letterSet)
                bguserLetters = re.sub(r'[^a-zA-z]+','', letterSetString)
                randReqLetterNum = random.randint(0,(len(bguserLetters)-1))
                bgreqLetter = bguserLetters[randReqLetterNum]
                return bguserLetters, bgreqLetter
            else: 
                print("Uh oh, looks like you didn't enter a pangram that exists with the json file!")
                return "empty","empty"
        case 9:
            with open(pangram_files[2], "r") as file:
                data = json.load(file)
            for word in data:
                getWords.append(str(word["word"]))
            if userInput in getWords:
                letterSet = set(userInput)
                letterSetString = str(letterSet)
                bguserLetters = re.sub(r'[^a-zA-z]+','', letterSetString)
                randReqLetterNum = random.randint(0,(len(bguserLetters)-1))
                bgreqLetter = bguserLetters[randReqLetterNum]
                return bguserLetters, bgreqLetter
            else: 
                print("Uh oh, looks like you didn't enter a pangram that exists with the json file!")
                return "empty","empty"
        case 10:
            with open(pangram_files[3], "r") as file:
                data = json.load(file)
            for word in data:
                getWords.append(str(word["word"]))
            if userInput in getWords:
                letterSet = set(userInput)
                letterSetString = str(letterSet)
                bguserLetters = re.sub(r'[^a-zA-z]+','', letterSetString)
                randReqLetterNum = random.randint(0,(len(bguserLetters)-1))
                bgreqLetter = bguserLetters[randReqLetterNum]
                return bguserLetters, bgreqLetter
            else: 
                print("Uh oh, looks like you didn't enter a pangram that exists with the json file!")
                return "empty","empty"
        case 11:
            with open(pangram_files[4], "r") as file:
                data = json.load(file)
            for word in data:
                getWords.append(str(word["word"]))
            if userInput in getWords:
                letterSet = set(userInput)
                letterSetString = str(letterSet)
                bguserLetters = re.sub(r'[^a-zA-z]+','', letterSetString)
                randReqLetterNum = random.randint(0,(len(bguserLetters)-1))
                bgreqLetter = bguserLetters[randReqLetterNum]
                return bguserLetters, bgreqLetter
            else: 
                print("Uh oh, looks like you didn't enter a pangram that exists with the json file!")
                return "empty","empty"
        case 12:
            with open(pangram_files[5], "r") as file:
                data = json.load(file)
            for word in data:
                getWords.append(str(word["word"]))
            if userInput in getWords:
                letterSet = set(userInput)
                letterSetString = str(letterSet)
                bguserLetters = re.sub(r'[^a-zA-z]+','', letterSetString)
                randReqLetterNum = random.randint(0,(len(bguserLetters)-1))
                bgreqLetter = bguserLetters[randReqLetterNum]
                return bguserLetters, bgreqLetter
            else: 
                print("Uh oh, looks like you didn't enter a pangram that exists with the json file!")
                return "empty","empty"
        case 13:
            with open(pangram_files[6], "r") as file:
                data = json.load(file)
            for word in data:
                getWords.append(str(word["word"]))
            if userInput in getWords:
                letterSet = set(userInput)
                letterSetString = str(letterSet)
                bguserLetters = re.sub(r'[^a-zA-z]+','', letterSetString)
                randReqLetterNum = random.randint(0,(len(bguserLetters)-1))
                bgreqLetter = bguserLetters[randReqLetterNum]
                return bguserLetters, bgreqLetter
            else: 
                print("Uh oh, looks like you didn't enter a pangram that exists with the json file!")
                return "empty","empty"
        case 14:
            with open(pangram_files[7], "r") as file:
                data = json.load(file)
            for word in data:
                getWords.append(str(word["word"]))
            if userInput in getWords:
                letterSet = set(userInput)
                letterSetString = str(letterSet)
                bguserLetters = re.sub(r'[^a-zA-z]+','', letterSetString)
                randReqLetterNum = random.randint(0,(len(bguserLetters)-1))
                bgreqLetter = bguserLetters[randReqLetterNum]
                return bguserLetters, bgreqLetter
            else: 
                print("Uh oh, looks like you didn't enter a pangram that exists with the json file!")
                return "empty","empty"
        case 15:
            with open(pangram_files[8], "r") as file:
                data = json.load(file)
            for word in data:
                getWords.append(str(word["word"]))
            if userInput in getWords:
                letterSet = set(userInput)
                letterSetString = str(letterSet)
                bguserLetters = re.sub(r'[^a-zA-z]+','', letterSetString)
                randReqLetterNum = random.randint(0,(len(bguserLetters)-1))
                bgreqLetter = bguserLetters[randReqLetterNum]
                return bguserLetters, bgreqLetter
            else: 
                print("Uh oh, looks like you didn't enter a pangram that exists with the json file!")
                return "empty","empty"
    '''

