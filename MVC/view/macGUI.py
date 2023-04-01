import tkinter as tk
from turtle import width
from MVC.controller import Controller as ctrl
import math
import random
import os
from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
from tkinter import filedialog
from numpy import *
from tkinter import Toplevel, Label

class View:
    '''
    Default constructor. Contains all the set up needed for the TKinter GUI. 
    '''
    def __init__(self, parent, ctrl):
        self.controller = ctrl.controller()
        self.parent = parent

        # created a frame
        self.myFrame = tk.Frame(parent, bg='#F4F4F4')
        self.myFrame.pack()

        #find the path for the background image.
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

        # Creates frame for buttons
        buttonFrame = tk.Frame(self.parent)
        buttonFrame.pack(pady=5)
        
        # created some buttons
        self.guessButton = tk.Button(buttonFrame, text="Enter", command=self.makeGuess,width=5, height=3)
        self.guessButton.pack(side='left', padx=5, fill='none', expand=False)
        self.backButton = tk.Button(buttonFrame, text="Delete", command=self.backspace,width=5, height=3)
        self.backButton.pack(side='left', padx=5, fill='none', expand=False)
        self.shuffleButton = tk.Button(buttonFrame, text="Shuffle", command=self.shuffle,width=5, height=3)
        self.shuffleButton.pack(side='left', padx=5, fill='none', expand=False)
  
        #menu
        file_menu = tk.Menu(self.menu)
        self.menu.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New Puzzle",command = self.gameplay)
        file_menu.add_separator()
        file_menu.add_command(label="New Puzzle Base",command=self.gameplayBase)
        file_menu.add_separator()
        file_menu.add_command(label="Open",command = self.loadPuzzle)
        file_menu.add_separator()
        file_menu.add_command(label="Save",command = self.savePuzzle)
        file_menu.add_separator()
        file_menu.add_command(label="Exit",command=self.exitPuzzle)
        
        help_menu = tk.Menu(self.menu)
        self.menu.add_cascade(label="Help",menu=help_menu)
        help_menu.add_command(label = "How to play",command = self.playInstructions)
        help_menu.add_separator()
        help_menu.add_command(label = "Hints",command = self.pickHint)

        # create the frame
        self.frame = tk.Frame(self.parent)
        self.frame.pack(fill='both', expand=True)
        
        self.totalWords = []
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
        
    '''
    Function created to only allow users to type in the letters given for the puzzle
    '''
    def checkKeys(self,text):
        #Allow the user to also use backspace key to remove letters
        if text == ["\b", ""]:
            return True
        #create a list of the given letters for the puzzle
        letters = list(self.controller.controllerGetLetters())
        #using list comprehension, we can check if the keys being pressed aren't in the list regardless of them entering capital letters.
        for x in text:
            if str(x).lower() not in [str(letter).lower() for letter in letters]:
                return False
        return True

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
    def createButton(self, x):
        return tk.Button(self.canvas, text= x, width=3, height=2, background="white", font=('Helvetica 18 bold'), relief=FLAT, command= lambda: self.sendInput(x))

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
                self.btn1 = self.createButton(hexagonLetters[0])
                self.btn1.place(x=342, y=340)
                self.btn2 = self.createButton(hexagonLetters[1])
                self.btn2.place(x=342, y=110)
                self.btn3 = self.createButton(hexagonLetters[2])
                self.btn3.place(x=231, y=282)
                self.btn4 = self.createButton(hexagonLetters[3])
                self.btn4.place(x=452, y=282)
                self.btn5 = self.createButton(hexagonLetters[4])
                self.btn5.place(x=231, y=168)
                self.btn6 = self.createButton(hexagonLetters[5])
                self.btn6.place(x=452, y=168)
                self.btn7 = tk.Button(self.canvas,text = reqLetter, width=3, height=2, font=('Helvetica 18 bold'), relief=FLAT, command = lambda: self.sendInput(reqLetter))
                self.btn7.place(x=342, y=225)

                #text for points and rank
                self.canvas.create_text(365, 50, text="Points:", fill="black", font=('Helvetica 20 bold'))
                self.canvas.create_text(30, 485, text="Rank:", fill="black", font=('Helvetica 20 bold'))

    
    '''
    Function deletes the right most character from the inputbox
    '''
    def backspace(self):
        self.e.delete(len(self.e.get()) - 1, tk.END)

    '''
    Function stores user input then runs through controller -> model guess function to see if they made a correct one or not.
    '''
    # call user guess from controller, this probably should have been moved into the controller later
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

        #update the points and rank after every guess.
        self.points.set(self.controller.controllerGetPoints())
        self.rank.set(self.controller.controllerGetPuzzleRank())
        print(self.controller.controllerGetPuzzleRank())
        print(self.controller.controllerGetPoints())
        #clears the input box everytime.
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
    else throws errrors.
    '''
    def savePuzzle(self):
         if(self.controller.controllerGetPuzzleState() == 0):
                messagebox.showinfo("Error!", "No game started!")
                return
         else:   
            try:
                filename = filedialog.asksaveasfilename(defaultextension="")
                if filename:
                    self.controller.controllerSaveGame(filename)
                    messagebox.showinfo("Saved", "Game saved successfully!")
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
    Parameters are simple checks for some subtle 1 line differences between gameplay, gameplaybase, and loadHelper.
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
        # then we can run the function and pull the data from model->controller->view
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
        #adds the points
        self.pointLabel = tk.Label(self.canvas, textvariable = self.points, font=('Helvetica 20 bold'), background='#FFFFFF', foreground='#000000')
        self.pointLabel.place(x=410,y=40)
        #adds the rank
        self.rankLabel = tk.Label(self.canvas, textvariable  = self.rank, font=('Helvetica 20 bold'), background='#FFFFFF', foreground='#000000')
        self.rankLabel.place(x=60,y=474)
        #get required letter
        self.reqLetter = self.controller.controllerGetReqLetter()
        print(self.reqLetter)
        #removes the required letter from the list.
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
        messagebox.showinfo("Loaded", "Game loaded successfully!")
        self.gameHelper(0, 0, 1, 0)

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
                    exit()
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
    Function that creates the hints popup.
    '''
    def pickHint(self):
        if (self.controller.controllerGetPuzzleState() != 1):
            return
        hints = [self.grid(),self.hintCount(),self.totHint()]
        hint = random.choice(hints)

    '''
    Function that creates the pop up windows for hints.
    '''
    def hintDisplay(self,title,message,width,height):
        # Creates top level message
        hintMessage = Toplevel()
        hintMessage.title(title)
         # set the size of the message
        hintMessage.geometry(f"{width}x{height}")
        # create a label and change font
        label = Label(hintMessage, text=message, font=("Courier New",12))
        # Add padding
        label.pack(padx=40, pady=40)

    '''
    Function that creates the matrix of letters and their counts.
    '''
    def grid(self):
        x = self.controller.gridHint()
        cell_width = 2
        fmt = '{:>' + str(cell_width) + '}'
        message = "\n".join(" ".join(fmt.format(col) for col in row) for row in x)
        self.hintDisplay("Grid Hint:", message, 400, 200)
        
    '''
    Function that creates the list of two letters in words and their counts.
    '''
    def hintCount (self):
        count = self.controller.firstTwo()
        # Formats how the list will print when transferred to a window
        message = "Two Letter List Hint:\n" + "\n".join([f"{k}: {v}" for k, v in count.items()])
        print(self.controller.controllerGetWordList())
        self.hintDisplay("First Two Letters Hint:",message,250,700)
    
    '''
    Function that finds the total number of words, points, and pangrams.
    '''
    def totHint(self):
        x,y = self.controller.totalHint()
        # Formats message to display propertly on message window 
        message = f"WORDS: {self.controller.getTotalWords()}\nPOINTS: {self.controller.controllerGetPuzzleTotal()}\nPANGRAMS: {x} ({y} Perfect)"
        self.hintDisplay("Puzzle Total Hint:", message, 250, 150)

    '''
    Function is meant for automatically generating a puzzle for the user to play.
    '''
    def gameplay(self):
        #if puzzle in progress, prompt for saving, otherwise create new puzzle
        if(self.controller.controllerGetPuzzleState() == 1):
            answer = messagebox.askyesno("Would you like to save?", "Would you like to save the current game?")
            if answer == True:
                self.savePuzzle()
        self.gameHelper(1, 0, 0, 1)

    '''
    Function generates a new puzzle based off of what the user types in for their pangram.
    '''
    def gameplayBase(self):
        if(self.controller.controllerGetPuzzleState() == 1):
            answer = messagebox.askyesno("Would you like to save?", "Would you like to save the game?")
            if answer == True:
                    self.savePuzzle()
        #self.controller.controllerNewGame()
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
        #run base game function and input function
        if input == "" or len(input) < 7 or len(input) > 15:
            messagebox.showinfo("Invalid input!", "Ensure the input is an actual pangram (letters only) and the length is between 7-15")
            return
        else:
           self.gameHelper(2, input, 0, 1)

# Runs the GUI
main = tk.Tk()
main.title("MediaTek's Spelling Bee!")
View(main,ctrl)
main.mainloop()