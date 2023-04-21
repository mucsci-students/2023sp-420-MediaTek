import platform
import tkinter as tk
from MVC.controller import Controller as ctrl
from MVC.controller import GameObserver
import math
import random
import os
from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
from tkinter import filedialog
from PIL import ImageGrab
from tkinter import PhotoImage, Label, Canvas
from MVC.model.Highscores import saveHighScore
from MVC.model.Highscores import loadHighScore
import time


class ViewFactory:

    '''
    Factory method that defines the basic behavior of creating labels.
    '''
    def createLabels(self, canvas, points, rank, fontstyle, pointsx, pointsy, rankx, ranky):

        self.pointLabel = tk.Label(canvas, textvariable = points, font=(fontstyle), background='#FFFFFF')
        self.pointLabel.place(x=pointsx,y=pointsy)
 
        self.rankLabel = tk.Label(canvas, textvariable  = rank, font=(fontstyle), background='#FFFFFF')
        self.rankLabel.place(x=rankx,y=ranky)

    '''
    Factory method that defines the basic behavior of creating text.
    '''
    def createText(self, canvas, ex, why, label, fontstyle):
        canvas.create_text(ex, why, text=label, fill="black", font=(fontstyle))
    
    '''
    Factory method that defines the basic behavior of placing buttons.
    '''
    def placeButtons(self, name, ex, why):
        name.place(x=ex, y=why)


class WindowsFactory:

    '''
    Uses the Factory method to define specific values for windows labels.
    '''
    def windowsLabels(self, canvas, points, rank):
        return ViewFactory.createLabels(self, canvas, points, rank, 'Helvetica 12 bold', 410, 40, 60, 474)
    
    '''
    Uses the Factory method to define specific values for windows text.
    '''
    def windowsText(self, canvas, ex, why, label):
        return ViewFactory.createText(self, canvas, ex, why, label, 'Helvetica 14 bold')


class MacFactory:

    '''
    Uses the Factory method to define specific values for mac labels.
    '''
    def macLabels(self, canvas, points, rank):
        return ViewFactory.createLabels(self, canvas, points, rank, 'Helvetica 20 bold', 410, 46, 60, 471)
    
    '''
    Uses the Factory method to define specific values for mac text.
    '''
    def macText(self, canvas, ex, why, label):
        return ViewFactory.createText(self, canvas, ex, why, label, 'Helvetica 20 bold')


class GUI:
    '''
    Default constructor. Contains all the set up needed for the TKinter GUI. 
    '''
    def __init__(self, parent, ctrl, game_controller):

        self.controller = ctrl.controller()
        self.parent = parent

        #assigns game_model instance passed to view
        self.game_controller = game_controller
        #create new instance of GameObserver, passing self.observerLoad as a callback
        #GameObserver calls this whenever receives an update from the model
        game_observer = GameObserver(self.observerLoad)
        #attaches game_observer instance to game_model by calling the attach 
        self.game_controller.attach(game_observer)

        # created a frame
        self.myFrame = tk.Frame(parent, bg='#F4F4F4')
        self.myFrame.pack()

        #find the path for the background image
        check_dir = os.path.dirname(os.path.abspath(__file__))
        db_dir = os.path.join(check_dir,".","combsbig.png")
        abs_path = os.path.abspath(db_dir)

        #creates background image!
        self.bg = PhotoImage(file=abs_path, height=2000, width=2000)
        self.img = Label(parent, image = self.bg)
        self.img.place(x = 0,y = 0)

        #menu
        self.menu = tk.Menu(self.parent)
        self.parent.config(menu=self.menu)

        # created an input box
        self.inputFrame = tk.Frame(self.parent)
        self.inputFrame.pack(side='top', padx=5, pady=5)
        self.label = tk.Label(self.inputFrame, text="Guess:", font=('Helvetica 14 bold'))
        self.label.pack(side='left', padx=5, pady=5)
        self.e = tk.Entry(self.inputFrame, width=50, bg="white", fg="black", validate ="key", validatecommand=(self.parent.register(self.checkKeys), "%S"))
        self.e.pack(side='left', padx=5, pady=5)
        self.saved = False
        self.check = None

        # Variables that describe size of hexagon
        self.hex_radius = 60
        self.hex_width = math.sqrt(3) * self.hex_radius
        self.hex_height = 2 * self.hex_radius

         # Creates a 500 x 500 canvas with a white background along with title
        self.canvas = tk.Canvas(self.parent, width=750, height=500,bg='#FFFFFF')
        self.canvas.create_text(375, 25, text="Welcome to MediaTek's Spelling Bee!", fill="black", font=('Helvetica 20 bold'))
        self.canvas.pack()

        #Frame for buttons
        self.buttonFrame = tk.Frame(self.parent, bg='#FFFFFF')
        self.buttonFrame.pack(pady=5)

        # created some buttons
        self.guessButton = tk.Button(self.buttonFrame, text="Enter", command=self.makeGuess, relief=FLAT)
        self.guessButton.pack(pady=10, padx=15, side='left')
        self.backButton = tk.Button(self.buttonFrame, text="Delete", command=self.backspace, relief=FLAT)
        self.backButton.pack(pady=10, padx=15, side='left')
        self.shuffleButton = tk.Button(self.buttonFrame, text="Shuffle", command=self.shuffle, relief=FLAT)
        self.shuffleButton.pack(pady=10, padx=15, side='left')

        #menu
        self.fileMenu = tk.Menu(self.menu)
        self.menu.add_cascade(label='File', menu=self.fileMenu)
        self.fileMenu.add_command(label="New Puzzle",command = self.gameplay)
        self.fileMenu.add_separator()
        self.fileMenu.add_command(label="New Puzzle Base",command=self.gameplayBase)
        self.fileMenu.add_separator()
        self.fileMenu.add_command(label="Open",command = self.loadPuzzle)
        self.fileMenu.add_separator()
        self.fileMenu.add_command(label="Save",command = self.savePuzzle)
        self.fileMenu.add_separator()
        self.fileMenu.add_command(label="Export Score",command=self.screenShot)
        self.fileMenu.add_separator()
        self.fileMenu.add_command(label="Give Up",command = self.giveUp)
        self.fileMenu.add_separator()
        self.fileMenu.add_command(label="Exit",command=self.exitPuzzle)
        
        self.helpMenu = tk.Menu(self.menu)
        self.menu.add_cascade(label="Help",menu=self.helpMenu)
        self.helpMenu.add_command(label = "How to play",command = self.playInstructions)
        self.helpMenu.add_separator()
        self.helpMenu.add_command(label = "Hints",command = self.displayAll)
        self.helpMenu.add_separator()
        self.helpMenu.add_command(label = "High Scores",command= self.displayHighScores)
        
        #variables for displaying information to the screen
        self.hexagonLetters = []
        self.reqLetter = ""
        self.getLetters = ""
        self.rank = tk.StringVar()
        self.points = tk.IntVar()

        # create a list box which will show the found words
        self.listBox = tk.Listbox(self.parent, width=20, height=8, font='Helvetica 24', justify='center')
        self.listBox.pack(pady=5, padx=300, fill='y', expand=True)

        self.test = 0
        # empty state for the buttons

        self.os_name = platform.system()

    '''
    Function created to only allow users to type in the letters given for the puzzle
    '''
    def checkKeys(self,text):
        #Allow the user to also use backspace key to remove letters
        if text == ["\b", ""]:
            return True
        #create a list of the given letters for the puzzle
        letters = list(self.controller.controllerGetLetters())
        #using list comprehension, we can check if the keys being pressed aren't in the list regardless of them entering capital letters
        # ITERATOR DESIGN PATTERN
        myIter = iter(text)
        for x in myIter:
            if str(x).lower() not in [str(letter).lower() for letter in letters]:
                return False
        return True
    
    '''
    Function that adds the letter of the hexagon button to the input box.
    '''
    def clicker(self):
        print(self.controller.controllerGetLetters())
    
    '''
    Function inserts the text at the end of the input box.
    '''
    def sendInput(self, text):
        self.e.insert(tk.END, text)

    '''
    Function clears the input box completely.
    '''
    def clearInput(self):
        self.e.delete(0, tk.END)

    '''
    Function clears the list box completely.
    '''
    def clearListbox(self):
        self.listBox.delete(0, tk.END)
    
    '''
    Function to create hexagons.
    '''
    def drawHex(self, x, y):
        return self.draw_hexagon(self.canvas, x, y, self.hex_radius, 'white', 'black')
    
    '''
    Function to create buttons.
    '''
    def createButton(self, hex, name, ex, why):
        name = tk.Button(self.canvas, text= hex, width=3, height=2, background="white", font=('Helvetica 18 bold'), relief=FLAT, command= lambda: self.sendInput(hex))
        ViewFactory.placeButtons(self, name, ex, why)

    '''
    Function creates the hexagons and buttons for the puzzles.
    '''
    def drawPuzzleUI(self, reqLetter, hexagonLetters):
            self.canvas.create_text(375, 25, text="Welcome to MediaTek's Spelling Bee!", fill="black", font=('Helvetica 20 bold'))
            hexReq = self.draw_hexagon(self.canvas, 375, 250, self.hex_radius, 'yellow', 'black')
            hex1 = self.drawHex(375, 365)
            hex2 = self.drawHex(375, 135)
            hex3 = self.drawHex(270, 307.5)
            hex4 = self.drawHex(480, 307.5)
            hex5 = self.drawHex(270, 194)
            hex6 = self.drawHex(480, 194)
            #creates the buttons with the letters and input functionality
            if (self.os_name == 'Windows'): 
                self.createButton(hexagonLetters[0], "btn1", 349, 325)
                self.createButton(hexagonLetters[1], "btn2", 349, 94)
                self.createButton(hexagonLetters[2], "btn3", 242, 270)
                self.createButton(hexagonLetters[3], "btn4", 452, 270)
                self.createButton(hexagonLetters[4], "btn5", 242, 158)
                self.createButton(hexagonLetters[5], "btn5", 452, 158)
                self.btn7 = tk.Button(self.canvas, text = reqLetter, width=3, height=2, font=('Helvetica 18 bold'), relief=FLAT, command = lambda: self.sendInput(reqLetter))
                self.btn7.place(x=349, y=210)
                self.btn7.configure(bg = "yellow")
            else:
                self.createButton(hexagonLetters[0], "btn1", 342, 340)
                self.createButton(hexagonLetters[1], "btn2", 342, 110)
                self.createButton(hexagonLetters[2], "btn3", 235, 282)
                self.createButton(hexagonLetters[3], "btn4", 446, 282)
                self.createButton(hexagonLetters[4], "btn5", 235, 168)
                self.createButton(hexagonLetters[5], "btn6", 446, 168)
                self.btn7 = tk.Button(self.canvas,text = reqLetter, width=3, height=2, font=('Helvetica 18 bold'), relief=FLAT, command = lambda: self.sendInput(reqLetter))
                self.btn7.place(x=342, y=225)

            #text for points and rank
            if (self.os_name == 'Windows'):
                WindowsFactory.windowsText(self, self.canvas, 365, 50, "Points:")
                WindowsFactory.windowsText(self, self.canvas, 30, 485, "Rank:")
            else:
                MacFactory.macText(self, self.canvas, 365, 60, "Points:")
                MacFactory.macText(self, self.canvas, 30, 485, "Rank:")
   
    '''
    Function deletes the right most characte from the inputbox
    '''
    def backspace(self):
        self.e.delete(len(self.e.get()) - 1, tk.END)

    '''
    Function stores user input then runs through controller -> model guess function to see if they made a correct one or not.
    '''
    def makeGuess(self, *args):
        input = self.e.get()
        # Check if the input is within the required length range
        if len(input) < 4 or len(input) > 15:
            messagebox.showinfo("Invalid guess", "Word must be between 4 and 15 letters.")
        # Check if the word has already been guessed correctly
        elif input.lower() in self.listBox.get(0, tk.END):
            messagebox.showinfo("Already Guessed", "This word has already been guessed correctly.")
        # Check if the input is valid
        elif self.controller.checkInput(input.lower(), self.reqLetter.lower()) == True:
            # Check if the guess is correct
            if self.controller.controllerUserGuess(input) == True:
                self.listBox.insert(tk.END,input.lower())
            else:
                messagebox.showinfo("Invalid Guess", "Word is not in list.")
        else:
            messagebox.showinfo("Invalid input", "Required letter was not used.")

        #update the points and rank after every guess and clear input
        self.points.set(self.controller.controllerGetPoints())
        self.rank.set(self.controller.controllerGetPuzzleRank())
        self.clearInput()

    '''
    Function that creates the hexagons according to size.
    '''
    def draw_hexagon(self, canvas, x, y, radius, fill, outline):
        angle = 60
        points = []
        for i in range(6):
            x_i = x + radius * math.cos(math.radians(angle * i))
            y_i = y + radius * math.sin(math.radians(angle * i))
            points.append((x_i, y_i))
        canvas.create_polygon(points, fill=fill, outline=outline)

    '''
    Function shows up message asking if the user would like to save
    If so then it runs from view->controller->model save function.
    '''
    def savePuzzle(self):
         if(self.controller.controllerGetPuzzleState() == 0):
                messagebox.showinfo("Error!", "No game started!")
                return
         else: 
            try:
                answer = messagebox.askyesno("Save", "Would you like to encrypt your puzzle?")
                filename = filedialog.asksaveasfilename(defaultextension="")
                if filename and (not answer):
                    if filename == "":
                        return
                    self.controller.controllerSaveGame(filename)
                    messagebox.showinfo("Saved", "Game saved successfully!")
                else:
                    if filename == "":
                        return
                    self.controller.controllerSaveEncryptedGame(filename)
                    messagebox.showinfo("Saved", "Encrypted Game saved successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"Error saving game: {e}")
                
    '''
    Function gets the filename from the user.
    '''
    def get_filename(self):
        filename = ""
        while not filename:
            filename = simpledialog.askstring("Load Game", "Enter the name of the file to load:")
            if filename:
                filename = filename.strip()
            elif filename == None:
                break
        return filename
    
    '''
    Function used in new game generation, which clears the canvas and its elements and gets data from the controller.
    Parameters are simple checks for some subtle 1 line differences between gameplay, gameplaybase, and loadHelper (used in if stmts).
    '''
    def gameHelper(self, x, y, z, a):
        self.clearInput()
        if a == 1:
            self.controller.controllerNewGame()
        self.clearListbox()
        self.hexagonLetters.clear()
        #gets points and rank from controller
        self.points.set(self.controller.controllerGetPoints())
        self.rank.set(self.controller.controllerGetPuzzleRank())
        #then we can run the function and pull the data from model->controller->view
        if x == 1:
            self.controller.controllerRunAutoGame()
        elif x == 2:
            self.controller.controllerRunBaseGame(y)
        getLetters = self.controller.controllerGetLetters()
        getLetters = getLetters.replace("[", "").replace("]","")
        #controller function to append letters into a list
        self.hexagonLetters = self.controller.controllerToList(getLetters, self.hexagonLetters)
        if z == 1:
            thelist = self.controller.controllerGetGuessedWordsGUI().copy()
            for x in thelist:
                self.listBox.insert(tk.END, x)
        #enables use of enter button on keyboard
        self.e.bind("<Return>",self.makeGuess)

        #create points and rank labels
        if (self.os_name == 'Windows'):
            WindowsFactory.windowsLabels(self, self.canvas, self.points, self.rank)
        else:
            MacFactory.macLabels(self, self.canvas, self.points, self.rank)

        #get required letter
        self.reqLetter = self.controller.controllerGetReqLetter()
        #hoping this removes the required letter from the list
        self.hexagonLetters.remove(self.reqLetter)
        #creates the hexagon shapes
        self.canvas.delete("all")
        self.drawPuzzleUI(self.reqLetter, self.hexagonLetters)
        self.controller.controllerUpdatePuzzleState1()

    '''
    Function asks if the user wants to save first, end result is loading data from a json file into the game.
    '''
    def loadHelper(self,filename): 
        self.controller.controllerGameLoadGUI(filename)
        if(self.controller.controllerGetAuthorField() != "MediaTek") or (self.controller.controllerGetDecryptionFlag() == True):
            messagebox.showinfo("Error", "Can't decrypt, author of the file must be MediaTek!")
            self.controller.controllerUpdateAuthorField()
            return
        else:
            #Notify the observer when the game is loaded
            self.game_controller.notify()
            self.gameHelper(0, 0, 1, 0)

    '''
    Passed as a callback to GameObserver; calls observerLoad which indicates the puzzle was loaded successfully.
    '''
    def observerLoad(self):
        messagebox.showinfo("Loaded", "Game loaded successfully!")

    '''
    Function that prompts for loading and executes the proper action.
    '''
    def loadPuzzle(self):
        #if puzzle in progress, prompt for saving
        if(self.controller.controllerGetPuzzleState() == 1):
            try:
                answer = messagebox.askyesnocancel("Open", "Do you want to save the game before loading a new one?")
                if answer is None:
                    # User clicked Cancel, do nothing
                    return
                elif answer:
                    # User clicked Yes, prompt to save and exit
                    self.savePuzzle()
                # User clicked No or has already saved the game
                # Close the application
                try:
                    filename = filedialog.askopenfilename(defaultextension=".json", filetypes=(("JSON Files", "*.json"), ("All Files", "*.*")))
                    if filename:
                        self.loadHelper(filename)
                except Exception as e:
                    messagebox.showerror("Error", f"Error loading game: {e}")
            except Exception as e:
                messagebox.showerror("Error", f"Error exiting game: {e}")
        else:
            try:
                filename = filedialog.askopenfilename(defaultextension=".json", filetypes=(("JSON Files", "*.json"), ("All Files", "*.*")))
                if filename:
                    self.loadHelper(filename)
            except Exception as e:
                messagebox.showerror("Error", f"Error loading game: {e}")
         
    '''
    Function will prompt user if they'd like to save, exits the program.
    '''
    def exitPuzzle(self):
        if(self.controller.controllerGetPuzzleState() == 0):
                main.destroy()
        else:
            try:
                answer = messagebox.askyesnocancel("Exit", "Do you want to save the game before exiting?")
                if answer is None:
                    # User clicked Cancel, do nothing
                    return
                elif answer:
                    # User clicked Yes, prompt to save and exit
                    self.savePuzzle()
                # User clicked No or has already saved the game
                # Close the application
                main.destroy()
            except Exception as e:
                messagebox.showerror("Error", f"Error exiting game: {e}")

    '''
    Function that displays How To Play text.
    '''
    def playInstructions(self):
        messagebox.showinfo("How To Play", '''The goal of our Spelling Bee game is to guess words given a choice of 7 letters, with 1 of them (the middle letter!) being required for all created words. Letters may be repeated but words must be 4 to 15 letters.
Each puzzle is based off of a pangram, a 7 to 15 letter word that contains 7 unique letters. You are free to use your own pangram to create a personalized puzzle by pressing the New Puzzle Base button!''')

    '''
    Function that shuffles letters which works by deleting and remaking the whole canvas.
    '''
    def shuffle(self):
        if (self.controller.controllerGetPuzzleState() != 1):
            return
        else:
            random.shuffle(self.hexagonLetters)
            self.canvas.delete("all")
            self.canvas.create_text(375, 25, text="Welcome to MediaTek's Spelling Bee!", fill="black", font=('Helvetica 20 bold'))
            self.drawPuzzleUI(self.reqLetter, self.hexagonLetters)

    '''
    Function that takes screenshot of tkinter canvas
    '''
    def screenShot(self):
        if (self.controller.controllerGetPuzzleState() == 0):
            messagebox.showinfo("Error!", "No game started!")
            return
        else:
            try:
                x,y = self.canvas.winfo_rootx(),self.canvas.winfo_rooty()
                w,h = x + self.canvas.winfo_width(), y + self.canvas.winfo_height()
                time.sleep(.4)
                img = ImageGrab.grab(bbox=(x, y, w, h))

                file_path = filedialog.asksaveasfilename(defaultextension=".png")
                if file_path:
                    img.save(file_path)
                    messagebox.showinfo("Screenshot Saved", "Screenshot saved successfully!")
                else:
                    messagebox.showinfo("Screenshot Canceled", "Screenshot was not saved.")
            except Exception as e:
                messagebox.showerror("Error", f"Error taking screenshot: {e}")


    '''
    Function that creates the pop up windows for hints.
    '''
    def hintDisplay(self,title, message1, message2, message3, width, height):
        # Creates top level message
        hintMessage = Toplevel()
        hintMessage.title(title)
         # set the size of the message
        hintMessage.geometry(f"{width}x{height}")
        # create a label and change font
        gridLabel = Label(hintMessage, text=message1, font=("Courier New",12))
        twoLabel = Label(hintMessage, text=message2, font=("Courier New",12))
        totalLabel = Label(hintMessage, text=message3, font=("Courier New",12))
        # Add padding
        gridLabel.pack(padx=40, pady=10)
        twoLabel.pack(padx=40, pady=10)
        totalLabel.pack(padx=40, pady=10)

    '''
    Function that creates the matrix of letters and their counts.
    '''
    def grid(self):
        x = self.controller.gridHint()
        cell_width = 3
        fmt = '{:>' + str(cell_width) + '}'
        message = "Grid Hint: \n" + "\n".join(" ".join(fmt.format(col) for col in row) for row in x)
        return message
        
    '''
    Function that creates the list of two letters in words and their counts.
    '''
    def hintCount (self):
        count = self.controller.firstTwo()
        # Formats how the list will print when transferred to a window
        message = "Two Letter List Hint:\n" + "\n".join([f"{k}: {v}" for k, v in count.items()])
        return message
    
    '''
    Function that finds the total number of words, points, and pangrams.
    '''
    def totHint(self):
        x,y = self.controller.totalHint()
        # Formats message to display propertly on message window 
        message = f"WORDS: {self.controller.getTotalWords()}\nPOINTS: {self.controller.controllerGetPuzzleTotal()}\nPANGRAMS: {x} ({y} Perfect)"
        return message 
    
    '''
    Function that displays all hints
    '''
    def displayAll(self):
        if(self.controller.controllerGetPuzzleState() == 0):
                messagebox.showinfo("Error!", "No game started!")
                return
        else:
            # Sets functions to variables
            hint1 = self.grid()
            hint2 = self.hintCount()
            hint3 = self.totHint()

            # Displays all hints
            self.hintDisplay("Hints", hint1, hint2, hint3, 1000, 1000)
    
    '''
    Function that creates the pop up windows for high scores.
    '''
    def highScoreWindow(self, title, message1, width, height):
        # Creates top level message
        highScoreMessage = Toplevel()
        highScoreMessage.title(title)
         # set the size of the message
        highScoreMessage.geometry(f"{width}x{height}")
        # create a label and change font
        highScoreLabel = Label(highScoreMessage, text=message1, font=("Courier New",20))
        # Add padding
        highScoreLabel.pack(padx=40, pady=10)
    
    '''
    give up function/command that allows the player to say they are finished with a puzzle.
    this sends the game id, player name, and points to the highscore database to update the
    highscore for the puzzle referred to by the unique puzzle id.
    '''   
    def giveUp(self):
        if(self.controller.controllerGetPuzzleState() == 0):
                messagebox.showinfo("Error!", "No game started!")
                return
        else:
            confirm = messagebox.askyesno("Give up", "Are you sure you want to give up?")
            if confirm:
                points = self.controller.controllerGetPoints()
                game_id = self.controller.controllerGetGameID()
                while True:
                    player_name = simpledialog.askstring("Username", "Please enter your 3-character username: ")
                    if player_name and len(player_name) == 3 and player_name.isalnum():
                        player_name = player_name.upper()
                        break
                    else:
                        messagebox.showerror("Error", "Invalid input. Please enter a 3-character alphanumeric username.")
                # Save the highscore
                saveHighScore(game_id, player_name, points)
                # Display high scores
                self.displayHighScores()
                # Close the window
            else:
                return
    '''
    Function that returns the top ten local high scores
    '''
    def getHighScores(self):
        game_id = self.controller.controllerGetGameID()
        highScores = loadHighScore(game_id)
        display_scores = []
        if highScores:
            header = "NAME    SCORE"
            display_scores.append(header)
            for row in highScores:
                display_scores.append(f"{row[1]:<7}{row[2]:>5}")
        else:
            display_scores.append("No high scores yet!")
        return display_scores
    
    '''
    Displays the top ten local high scores in the window
    '''
    def displayHighScores(self):
        if(self.controller.controllerGetPuzzleState() == 0):
                messagebox.showinfo("Error!", "No game started!")
                return
        else:
            highScores = self.getHighScores()
            highScores_str = "\n".join(highScores)
            self.highScoreWindow("High Scores", highScores_str, 350, 300)

    '''
    Function is meant for automatically generating a puzzle for the user to play.
    '''
    def gameplay(self):
        #if puzzle in progress, prompt for saving, otherwise create new puzzle
        if(self.controller.controllerGetPuzzleState() == 1):
            answer = messagebox.askyesno("Would you like to save?", "Would you like to save the current game?")
            if answer == True:
                self.savePuzzle()
        #see gameHelper's documentation for an explanation on parameters
        self.gameHelper(1, 0, 0, 1)

    '''
    Function generates a new puzzle based off of what the user types in for their pangram.
    '''
    def gameplayBase(self):
        if(self.controller.controllerGetPuzzleState() == 1):
            answer = messagebox.askyesno("Would you like to save?", "Would you like to save the game?")
            if answer == True:
                    self.savePuzzle()

        input = simpledialog.askstring("Please enter a pangram", "Choose a pangram to use")
        if (input == None):
            return
        self.check = self.controller.controllerCheckPangram(input.lower())
        while (self.check == False):
            input = simpledialog.askstring("Entered an invalid pangram", "Choose a pangram to use (7 unique letters)")
            if input == None:
                 return
            self.check = self.controller.controllerCheckPangram(input)     

        #then we can run the function and pull the data from model->controller->view
        if input == "" or len(input) < 7 or len(input) > 15:
            messagebox.showinfo("Invalid input!", "Ensure the input is an actual pangram (letters only) and the length is between 7-15")
            return
        else:
           #see gameHelper's documentation for an explanation on parameters
           self.gameHelper(2, input, 0, 1)

# Runs the GUI
if __name__ == "__main__":
    main = tk.Tk()
    main.title("MediaTek's Spelling Bee!")
    game_controller = ctrl.controller()
    GUI(main, ctrl, game_controller)
    main.mainloop()
