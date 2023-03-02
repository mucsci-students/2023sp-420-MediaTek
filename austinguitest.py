import tkinter as tk
import controllerrefactor as ctrl
import math
import random
import os
import copy
from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
from tkinter import filedialog
import time

class View:
    def __init__(self, parent, ctrl):
        self.controller = ctrl.controller()
        self.parent = parent
        # created a frame
        self.myFrame = tk.Frame(parent, bg='#F4F4F4')
        self.myFrame.pack()
        #creates background image!
        self.bg = PhotoImage(file="combsbig.png", height=2000, width=2000)
        self.img = Label(parent, image = self.bg)

        self.img.place(x = 0,y = 0)
        # created an input box
        self.e = tk.Entry(self.parent, width=100, bg="white", fg="black", validate ="key", validatecommand=(self.parent.register(self.checkKeys), "%S"))
        self.e.pack()
        self.saved = False

        # Variables that describe size of hexagon
        self.hex_radius = 30
        self.hex_width = math.sqrt(3) * self.hex_radius
        self.hex_height = 2 * self.hex_radius

         # Creates a 500 x 500 canvas with a white background along with title
        self.canvas = tk.Canvas(self.parent, width=500, height=300,bg='#FFFFFF')
        self.canvas.create_text(250, 25, text="Welcome to MediaTek's Spelling Bee!", fill="black", font=('Helvetica 20 bold'))
        self.canvas.pack()

        # created some buttons
        self.newPuzzleButton = tk.Button(self.parent, text="New Puzzle", command=self.gameplay, height=2, width=12)
        self.newPuzzleButton.pack(pady=10, padx=50, side='left')
        self.newPuzzleBaseButton = tk.Button(self.parent, text="New Puzzle Base", command=self.gameplayBase, height=2, width=12)
        self.newPuzzleBaseButton.pack(pady=10, padx=50, side='right')
        self.guessButton = tk.Button(self.parent, text="Enter", command=self.makeGuess)
        self.guessButton.pack(pady=10, side='top')
        self.backButton = tk.Button(self.parent, text="Delete", command=self.backspace)
        self.backButton.pack(pady=10, side='top')
        self.shuffleButton = tk.Button(self.parent, text="Shuffle", command=self.shuffle)
        self.shuffleButton.pack(pady=10, side='top')
        self.playInstructionButton = tk.Button(self.parent, text="How To Play", command=self.playInstructions)
        self.playInstructionButton.pack(side='bottom', pady=10)
        
        #GABE WROTE THIS START
        self.saveButton = tk.Button(self.parent, text="Save", command=self.savePuzzle)
        self.saveButton.pack(padx = 100, side='left')
        self.loadButton = tk.Button(self.parent, text="Load", command=self.loadPuzzle)
        self.loadButton.pack(padx=100, side='right')
        self.exitButton = tk.Button(self.parent, text="Exit", command=self.exitPuzzle, height=2, width=5)
        self.exitButton.pack(pady=20, side='bottom')
        #GABE WROTE THIS END
        

        self.hexagonLetters = []
        self.reqLetter = ""
        self.getLetters = ""
        self.rank = tk.StringVar()
        self.points = tk.IntVar()

        # create a list box which will show the found words
        self.listBox = tk.Listbox(self.parent)
        self.listBox.pack(pady=30)

        self.test = 0
        # empty state for the buttons



    def checkKeys(self, text):
         #ensure the user can back space and use delete button to erase
         #needed to add this as it was broken without.
         if text == ["\b", ""]:
              return True
         #get a list of characters from the model
         letters = list(self.controller.controllerGetLetters())
         #checks if what they user is entering is within the list
         for x in text:
              if x not in letters:
                   return False
         return True



    def clicker(self):
        print(self.controller.controllerGetLetters())

    def sendInput(self, text):
        self.e.insert(tk.END, text)

    def clearInput(self):
        self.e.delete(0, tk.END)

    def clearListbox(self):
        self.listBox.delete(0, tk.END)

    def drawPuzzleUI(self, reqLetter, hexagonLetters):
                self.hexReq = self.draw_hexagon(self.canvas, 250, 180, self.hex_radius, 'yellow', 'black')
                hex1 = self.draw_hexagon(self.canvas, 250, 240, self.hex_radius, 'white', 'black')
                hex2 = self.draw_hexagon(self.canvas, 250, 120, self.hex_radius, 'white', 'black')
                hex3 = self.draw_hexagon(self.canvas, 300, 210, self.hex_radius, 'white', 'black')
                hex4 = self.draw_hexagon(self.canvas, 200, 210, self.hex_radius, 'white', 'black')
                hex5 = self.draw_hexagon(self.canvas, 200, 150, self.hex_radius, 'white', 'black')
                hex6 = self.draw_hexagon(self.canvas, 300, 150, self.hex_radius, 'white', 'black')
                #creates the buttons with the letters and input functionality
                self.btn1 = tk.Button(self.canvas,text = hexagonLetters[0], background="white", font=('Helvetica 18 bold'), relief=FLAT, command = lambda: self.sendInput(hexagonLetters[0]))
                self.btn1.place(x=233, y=215)
                self.btn2 = tk.Button(self.canvas,text = hexagonLetters[1], background="white", font=('Helvetica 18 bold'), relief=FLAT, command = lambda: self.sendInput(hexagonLetters[1]))
                self.btn2.place(x=232, y=95)
                self.btn3 = tk.Button(self.canvas,text = hexagonLetters[2], background="white", font=('Helvetica 18 bold'), relief=FLAT, command = lambda: self.sendInput(hexagonLetters[2]))
                self.btn3.place(x=283, y=185)
                self.btn4 = tk.Button(self.canvas,text = hexagonLetters[3], background="white", font=('Helvetica 18 bold'), relief=FLAT, command = lambda: self.sendInput(hexagonLetters[3]))
                self.btn4.place(x=182, y=185)
                self.btn5 = tk.Button(self.canvas,text = hexagonLetters[4], background="white", font=('Helvetica 18 bold'), relief=FLAT, command = lambda: self.sendInput(hexagonLetters[4]))
                self.btn5.place(x=182, y=125)
                self.btn6 = tk.Button(self.canvas,text = hexagonLetters[5], background="white", font=('Helvetica 18 bold'), relief=FLAT, command = lambda: self.sendInput(hexagonLetters[5]))
                self.btn6.place(x=285, y=125)
                self.btn7 = tk.Button(self.canvas,text = reqLetter, width=1, font=('Helvetica 18 bold'), relief=FLAT, command = lambda: self.sendInput(reqLetter))
                self.btn7.place(x=238, y=155)
                self.btn7.configure(bg = "yellow")
                #text for points and rank
                self.canvas.create_text(220, 50, text="Points:", fill="black", font=('Helvetica 14 bold'))
                self.canvas.create_text(30, 282, text="Rank:", fill="black", font=('Helvetica 12 bold'))

    

    def backspace(self):
        self.e.delete(len(self.e.get()) - 1, tk.END)

    # call user guess from controller, this probably should have been moved into the controller later
    def makeGuess(self, *args):
        input = self.e.get()
        #made it so userGuess returns true/false so that way we only insert valid words into the listbox.
        if self.controller.checkInput(input, self.reqLetter) == True:
            if self.controller.controllerUserGuess(input) == True:
                self.listBox.insert(tk.END,input)
            else:
                messagebox.showinfo("Invalid Guess", "Please re-enter a guess.")
        else:
            messagebox.showinfo("Invalid input", "Ensure each guess uses the required letter, and consists of letters only.")

        self.points.set(self.controller.controllerGetPoints())
        self.rank.set(self.controller.controllerGetPuzzleRank())
        #self.rank.set(str(self.controller.controllerGetPuzzleRank()))
        print(self.controller.controllerGetPuzzleRank())
        print(self.controller.controllerGetPoints())
        self.clearInput()

    # Function that creates a hexagon
    def draw_hexagon(self, canvas, x, y, radius, fill, outline):
        angle = 60
        points = []
        for i in range(6):
            x_i = x + radius * math.cos(math.radians(angle * i))
            y_i = y + radius * math.sin(math.radians(angle * i))
            points.append((x_i, y_i))
        canvas.create_polygon(points, fill=fill, outline=outline)

    #GABE WROTE THIS
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

    #GABE WROTE THIS
    def get_filename(self):
        filename = ""
        while not filename:
            filename = simpledialog.askstring("Load Game", "Enter the name of the file to load:")
            if filename:
                filename = filename.strip()
            elif filename == None:
                break
        return filename
    #GABE WROTE THIS
    def loadPuzzle(self):
            try:
                filename = self.get_filename()
                if filename:
                    checkFile = filename + ".json"
                    if os.path.exists(checkFile):
                        self.controller.controllerGameLoad(filename)
                        messagebox.showinfo("Loaded", "Game loaded successfully!")
                        # clear listbox every time it's run
                        # must clear the letters once a new puzzle is generated
                        self.hexagonLetters.clear()
                        self.clearListbox()
                        #gets points and rank from controller
                        self.points.set(self.controller.controllerGetPoints())
                        self.rank.set(self.controller.controllerGetPuzzleRank())
                        # then we can run the function and pull the data from model->controller->view
                        getLetters = self.controller.controllerGetLetters()
                        getLetters = getLetters.replace("[", "").replace("]","")
                        #controller function to append letters into a list
                        self.hexagonLetters = self.controller.controllerToList(getLetters, self.hexagonLetters)
                        thelist = self.controller.controllerGetGuessedWords().copy()
                        for x in thelist:
                            self.listBox.insert(tk.END, x)
                        #print stmt's for testing
                        #print(self.hexagonLetters)
                        #print(self.controller.controllerGetWordList())
                        #enables use of enter button on keyboard
                        self.e.bind("<Return>",self.makeGuess)
                        #adds the points
                        self.pointLabel = tk.Label(self.canvas, textvariable = self.points, font=('Helvetica 12 bold'), background='#F4F4F4')
                        self.pointLabel.place(x=265,y=40)
                        #adds the rank
                        self.rankLabel = tk.Label(self.canvas, textvariable  = self.rank, font=('Helvetica 12 bold'), background='#F4F4F4')
                        self.rankLabel.place(x=60,y=270)
                        #get required letter
                        self.reqLetter = self.controller.controllerGetReqLetter()
                        print(self.reqLetter)
                        #hoping this removes the required letter from the list.
                        self.hexagonLetters.remove(self.reqLetter)
                        #creates the hexagon shapes
                        self.drawPuzzleUI(self.reqLetter, self.hexagonLetters)
                        self.controller.controllerUpdatePuzzleState1()
                    else:
                        messagebox.showerror("Error", f"Error loading game: File does not exist")
            except Exception as e:
                messagebox.showerror("Error", f"Error loading game: {e}")
            
    #GABE WROTE THIS
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

    #function for how to play button
    def playInstructions(self):
        messagebox.showinfo("How To Play", '''The goal of our Spelling Bee game is to guess words given a choice of 7 letters, with 1 of them (the middle letter!) being required for all created words. Letters may be repeated but words must be 4 to 15 letters.
Each puzzle is based off of a pangram, a 7 to 15 letter word that contains 7 unique letters. You are free to use your own pangram to create a personalized puzzle by pressing the New Puzzle Base button!''')
        

    #shuffle function which just shuffles the list of letters, deletes all the widgets on the canvas and remakes them
    def shuffle(self):
        if (self.controller.controllerGetPuzzleState() != 1):
            return
        else:
            random.shuffle(self.hexagonLetters)
            self.canvas.delete("all")
            self.canvas.create_text(250, 25, text="Welcome to MediaTek's Spelling Bee!", fill="black", font=('Helvetica 20 bold'))
            self.drawPuzzleUI(self.reqLetter, self.hexagonLetters)
    

    # this function will have all the necessary things for the game to be played, like mainly to redraw the hexagons
    # as of right now trying to get new puzzle auto-working with it and making a correct guess.
    # and then display the guessed words on the screen somewhere.
    def gameplay(self):
        #checks if the puzzle state is 1
        #then asks the user if they would like to save
        #if there is some sort of userInput put in, check if it's yes then ask for fileName
        #run save function, else in the end it will generate a new puzzle.
        if(self.controller.controllerGetPuzzleState() == 1):
            answer = messagebox.askyesno("Would you like to save?", "Would you like to save the game?")
            if answer == True:
                    fileName = simpledialog.askstring("Please enter a file name", "File name: ")
                    self.controller.controllerSaveGame(fileName)
            elif answer == False:
                    messagebox.showinfo("Generating a new puzzle", "Time to generate a new puzzle!")
            else:
                messagebox.showinfo("Error", "Choose yes or no!")
                return
        self.controller.controllerNewGame()
        # clear listbox every time it's run
        self.clearListbox()
        # must clear the letters once a new puzzle is generated
        self.hexagonLetters.clear()

        #gets points and rank from controller
        self.points.set(self.controller.controllerGetPoints())
        self.rank.set(self.controller.controllerGetPuzzleRank())

        # then we can run the function and pull the data from model->controller->view
        self.controller.controllerRunAutoGame()
        getLetters = self.controller.controllerGetLetters()
        getLetters = getLetters.replace("[", "").replace("]","")
        
        #controller function to append letters into a list
        self.hexagonLetters = self.controller.controllerToList(getLetters, self.hexagonLetters)
        #print stmt's for testing
        #print(self.hexagonLetters)
        #print(self.controller.controllerGetWordList())

        #enables use of enter button on keyboard
        self.e.bind("<Return>",self.makeGuess)

        #adds the points
        self.pointLabel = tk.Label(self.canvas, textvariable = self.points, font=('Helvetica 12 bold'), background='#FFFFFF')
        self.pointLabel.place(x=265,y=40)


        #adds the rank
        self.rankLabel = tk.Label(self.canvas, textvariable  = self.rank, font=('Helvetica 12 bold'), background='#FFFFFF')
        self.rankLabel.place(x=60,y=270)

        #get required letter
        self.reqLetter = self.controller.controllerGetReqLetter()
        print(self.reqLetter)
        #hoping this removes the required letter from the list.
        self.hexagonLetters.remove(self.reqLetter)
        #creates the hexagon shapes
        self.drawPuzzleUI(self.reqLetter, self.hexagonLetters)
        self.controller.controllerUpdatePuzzleState1()

    def gameplayBase(self):
        if(self.controller.controllerGetPuzzleState() == 1):
            answer = messagebox.askyesno("Would you like to save?", "Would you like to save the game?")
            if answer == True:
                    fileName = simpledialog.askstring("Please enter a file name", "File name: ")
                    self.controller.controllerSaveGame(fileName)
            elif answer == False:
                    messagebox.showinfo("Generating a new puzzle", "Time to generate a new puzzle!")
            else:
                messagebox.showinfo("Error", "Choose yes or no!")
                return
        #self.controller.controllerNewGame()
        input = simpledialog.askstring("Please enter a pangram", "Choose a pangram to use")
        if (input == None):
            return
        #then we can run the function and pull the data from model->controller->view
        #run base game function and input function
        if input == "" or len(input) < 7 or len(input) > 15:
            messagebox.showinfo("Invalid input!", "Ensure the input is an actual pangram (letters only) and the length is between 7-15")
        else:
            self.controller.controllerNewGame()
            self.controller.controllerRunBaseGameGUI(input)
            getLetters = self.controller.controllerGetLetters()
            print("Get letters before: " + getLetters)
            getLetters = getLetters.replace("[", "").replace("]","")
            print("Get letters: " + getLetters)
             # clear listbox every time it's run
            self.clearListbox()
            # must clear the letters once a new puzzle is generated
            self.hexagonLetters.clear()
            #gets points and rank from controller
            self.points.set(self.controller.controllerGetPoints())
            self.rank.set(self.controller.controllerGetPuzzleRank())
            #controller function to append letters into a list
            self.hexagonLetters = self.controller.controllerToList(getLetters, self.hexagonLetters)
            #enables use of enter button on keyboard
            self.e.bind("<Return>",self.makeGuess)
            #adds the points
            self.pointLabel = tk.Label(self.canvas, textvariable = self.points, font=('Helvetica 12 bold'), background='#F4F4F4')
            self.pointLabel.place(x=265,y=40)
            #adds the rank
            self.rankLabel = tk.Label(self.canvas, textvariable  = self.rank, font=('Helvetica 12 bold'), background='#F4F4F4')
            self.rankLabel.place(x=60,y=270)
            #get required letter
            self.reqLetter = self.controller.controllerGetReqLetter()
            print(self.reqLetter)
            #hoping this removes the required letter from the list.
            self.hexagonLetters.remove(self.reqLetter)
            #creates the hexagon shapes
            self.drawPuzzleUI(self.reqLetter, self.hexagonLetters)
            self.controller.controllerUpdatePuzzleState1()


  
# Runs the GUI
main = tk.Tk()
main.title("MediaTek's Spelling Bee!")
View(main,ctrl)
main.mainloop()


