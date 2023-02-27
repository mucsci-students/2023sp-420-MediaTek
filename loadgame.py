# For each defined function here, return a value based on the key-value pairs given in the JSON file.
# Order: User Letters, Required Letter, Guessed Words, Word Bank, Total Points

def loadUserLetters(save):
    return str(save["PuzzleLetters"])
        
def loadRequiredLetter(save):
    return str(save["RequiredLetter"])

# Unlike the previous two entities, the next two need to be stored as lists.
def loadGuessedWords(save):
    return list((save["GuessedWords"]))

def loadWordBank(save):
    return list((save["WordList"]))

# Total points needs to be stored as an integer value.
def loadTotalPoints(save):
    return int(save["CurrentPoints"])

def loadMaxPoints(save):
    return int(save["MaxPoints"])