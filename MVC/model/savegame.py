import json

def savegame(requiredLetter, userLetters, totalPoints, maxPoints, guessedWords, wordBank, inputFile):
    try:
        # If file exists, write to it.
        with open(inputFile + ".json", "w") as save:
            json.dump({"RequiredLetter": requiredLetter, "PuzzleLetters": userLetters, "CurrentPoints": totalPoints, "MaxPoints": maxPoints, "GuessedWords": guessedWords, "WordList": wordBank}, save, indent=4)
    except FileNotFoundError():
        # If not, create the file and them write.
        with open(inputFile + ".json", "x") as save:
            json.dump({"RequiredLetter": requiredLetter, "PuzzleLetters": userLetters, "CurrentPoints": totalPoints, "MaxPoints": maxPoints, "GuessedWords": guessedWords, "WordList": wordBank}, save, indent=4)
'''
Save function that is the encrypted version, believe I might have to add an author field (very minor)
'''
def saveencryptedgame(requiredLetter, userLetters, totalPoints, maxPoints, guessedWords, encryptedBank, author, inputFile):
    try:
        # If file exists, write to it.
        with open(inputFile + ".json", "w") as save:
            json.dump({"RequiredLetter": requiredLetter, "PuzzleLetters": userLetters, "CurrentPoints": totalPoints, "MaxPoints": maxPoints, "GuessedWords": guessedWords, "SecretWordList": encryptedBank, "Author": author}, save, indent=4)
    except FileNotFoundError():
        # If not, create the file and them write.
        with open(inputFile + ".json", "x") as save:
            json.dump({"RequiredLetter": requiredLetter, "PuzzleLetters": userLetters, "CurrentPoints": totalPoints, "MaxPoints": maxPoints, "GuessedWords": guessedWords, "SecretWordList": encryptedBank, "Author": author}, save, indent=4)