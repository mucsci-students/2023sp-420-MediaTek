#This file will count the total points of a given puzzle using wordlist.py, uses those points to then assign titles like 'Beginner', 'Novice', etc. which the user can check at any time
#using the command !showstatus and will recieve intermittent messages exclaiming their progress once a threshold is passed.
import wordlist


#not sure if needed
pangram_files = ['7letterpangram.json','8letterpangram.json','9letterpangram.json','10letterpangram.json','11letterpangram.json','12letterpangram.json','13letterpangram.json',
'14letterpangram.json','15letterpangram.json']

userScore = 0
userInput = input()
wordLength = len(userInput)
#user input can only be counted towards the point total IF >=4 letters, valid word from list, valid word in puzzle


if (userInput != "!"):
    #match on length, if 4 then 4 points etc. if in pangram list, length * 2
    #assuming guess is valid (done within guess task?)
    match wordLength:
        case 4:
            userScore += 4
        case 5:
            userScore += 5
        case 6:
            userScore += 6
        case 7:
            userScore += 7
        case 8:
            userScore += 8
        case 9:
            userScore += 9
        case 10:
            userScore += 10
        case 11:
            userScore += 11
        case 12:
            userScore += 12
        case 13:
            userScore += 13
        case 14:
            userScore += 14
        case 15:
            userScore += 15

#if userInput = pangram ??? how do
#then just add length again

#print(total_points)

#creating ranks based on percentages
#also add messages for when user reaches a new rank to congratulate them!
puzzleRank = ""
totalPoints = 0
#need to use wordlist to get list of words in the puzzle to add points



        




    
