def loadUserLetters(save):
    return str(save["userLetters"])
        
def loadRequiredLetter(save):
    return str(save["requiredLetter"])

def loadGuessedWords(save):
    return list((save["guessedWords"]))

def loadWordBank(save):
    return list((save["wordBank"]))

def loadTotalPoints(save):
    return int(save["totalPoints"])