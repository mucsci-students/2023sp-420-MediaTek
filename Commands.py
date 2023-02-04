
userInput = input()

#run function that displays all the commands the user can type
if(userInput == "!help"):
    #make prettier later, I forget how to have a print statement span multiple lines of code.
    print('''
!newpuzzle: This command generates a new puzzle. If you are generating a puzzle from a chosen pangram, enter said pangram along with the command.
!showpuzzle: This command displays the current puzzle.
!showfoundwords: This command lists all of the correctly guessed words.
!guess: Type this command with a word you would like to guess.
!shuffle: This command will shuffle the given letters in a random arangement (except the required letter which stays in the center).
!savepuzzle: This command will save your puzzle to your local machine.
!loadpuzzle: This command allows the you to load a saved puzzle from files, type the file name of the saved puzzle with this command.
!showstatus: This command shows your current status.
!help: You just typed this command. Congrats.
!exit: Exits the game. You will be asked if they are sure/want to save their game.
          ''')
    exit()