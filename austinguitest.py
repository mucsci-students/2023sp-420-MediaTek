import tkinter as tk
import controllerrefactor as ctrl
import math
import random
import copy
from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
import time

class View:
    def __init__(self, parent, ctrl):
        self.controller = ctrl.controller()
        self.parent = parent
        # created a frame
        self.myFrame = tk.Frame(parent, bg='#F4F4F4')
        self.myFrame.pack()
        # created an input box
        self.e = tk.Entry(self.parent, width=100, bg="white", fg="black")
        self.e.pack()
        
        # Variables that describe size of hexagon
        self.hex_radius = 30
        self.hex_width = math.sqrt(3) * self.hex_radius
        self.hex_height = 2 * self.hex_radius

         # Creates a 500 x 500 canvas with a white background along with title
        self.canvas = tk.Canvas(self.parent, width=500, height=300,bg='#F4F4F4')
        self.canvas.create_text(250, 25, text="Welcome to MediaTek's Spelling Bee!", fill="black", font=('Helvetica 20 bold'))
        self.canvas.pack()

        # created some buttons
        self.newPuzzleButton = tk.Button(self.parent, text="New Puzzle", command=self.gameplay)
        self.newPuzzleButton.pack(pady=10, side='top')
        self.newPuzzleBaseButton = tk.Button(self.parent, text="New Puzzle Base", command=self.gameplayBase)
        self.newPuzzleBaseButton.pack(pady=10, side='top')
        self.guessButton = tk.Button(self.parent, text="Enter", command=self.makeGuess)
        self.guessButton.pack(pady=10, side='top')
        self.backButton = tk.Button(self.parent, text="Delete", command=self.backspace)
        self.backButton.pack(pady=10, side='top')
        self.shuffleButton = tk.Button(self.parent, text="Shuffle", command=self.shuffle)
        self.shuffleButton.pack(pady=10, side='top')
        self.exitButton = tk.Button(self.parent, text="Exit", command=main.destroy)
        self.exitButton.pack(pady=10, side='bottom')

        self.hexagonLetters = []
        self.reqLetter = ""
        self.rank = tk.StringVar()
        self.points = tk.IntVar()

        # create a list box which will show the found words
        self.listBox = tk.Listbox(self.parent)
        self.listBox.pack(pady=60)

        self.test = 0
        # empty state for the buttons

    def clicker(self):
        print(self.controller.controllerGetLetters())

    def sendInput(self, text):
        self.e.insert(tk.END, text)

    def clearInput(self):
        self.e.delete(0, tk.END)

    def clearListbox(self):
        self.listBox.delete(0, tk.END)
    

    def backspace(self):
        self.e.delete(len(self.e.get()) - 1, tk.END)

    # call user guess from controller, this probably should have been moved into the controller later
    def makeGuess(self, *args):
        input = self.e.get()
        #made it so userGuess returns true/false so that way we only insert valid words into the listbox.
        if self.controller.checkInput(input) == True:
            if self.controller.controllerUserGuess(input) == True:
                self.listBox.insert(tk.END,input)
            else:
                messagebox.showinfo("Invalid Guess", "Please re-enter a guess.")
        else:
            messagebox.showinfo("Invalid input", "Letters only!")

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

    #shuffle function which just shuffles the list of letters, deletes all the widgets on the canvas and remakes them
    def shuffle(self):
        #self.canvas.delete(self.btn1)
        random.shuffle(self.hexagonLetters)
        self.canvas.delete("all")

        self.canvas.create_text(250, 25, text="Welcome to MediaTek's Spelling Bee!", fill="black", font=('Helvetica 20 bold'))

        self.hexReq = self.draw_hexagon(self.canvas, 250, 180, self.hex_radius, 'yellow', 'black')
        self.canvas.create_text(250, 180,text = self.reqLetter,fill="black", font=('Helvetica 24 bold'))
        hex1 = self.draw_hexagon(self.canvas, 250, 240, self.hex_radius, 'white', 'black')
        self.canvas.create_text(250, 240,text = self.hexagonLetters[0],fill="black", font=('Helvetica 24 bold'))
        hex2 = self.draw_hexagon(self.canvas, 250, 120, self.hex_radius, 'white', 'black')
        self.canvas.create_text(250, 120,text = self.hexagonLetters[1],fill="black", font=('Helvetica 24 bold'))
        hex3 = self.draw_hexagon(self.canvas, 300, 210, self.hex_radius, 'white', 'black')
        self.canvas.create_text(300, 210,text = self.hexagonLetters[2],fill="black", font=('Helvetica 24 bold'))
        hex4 = self.draw_hexagon(self.canvas, 200, 210, self.hex_radius, 'white', 'black')
        self.canvas.create_text(200, 210,text = self.hexagonLetters[3],fill="black", font=('Helvetica 24 bold'))
        hex5 = self.draw_hexagon(self.canvas, 200, 150, self.hex_radius, 'white', 'black')
        self.canvas.create_text(200, 150,text = self.hexagonLetters[4],fill="black", font=('Helvetica 24 bold'))
        hex6 = self.draw_hexagon(self.canvas, 300, 150, self.hex_radius, 'white', 'black')
        self.canvas.create_text(300, 150,text = self.hexagonLetters[5],fill="black", font=('Helvetica 24 bold'))

        self.btn1 = tk.Button(self.canvas,text = self.hexagonLetters[0], background="white", font=('Helvetica 18 bold'), relief=FLAT, command = lambda: self.sendInput(self.hexagonLetters[0]))
        self.btn1.place(x=233, y=215)
        self.btn2 = tk.Button(self.canvas,text = self.hexagonLetters[1], background="white", font=('Helvetica 18 bold'), relief=FLAT, command = lambda: self.sendInput(self.hexagonLetters[1]))
        self.btn2.place(x=232, y=95)
        self.btn3 = tk.Button(self.canvas,text = self.hexagonLetters[2], background="white", font=('Helvetica 18 bold'), relief=FLAT, command = lambda: self.sendInput(self.hexagonLetters[2]))
        self.btn3.place(x=283, y=185)
        self.btn4 = tk.Button(self.canvas,text = self.hexagonLetters[3], background="white", font=('Helvetica 18 bold'), relief=FLAT, command = lambda: self.sendInput(self.hexagonLetters[3]))
        self.btn4.place(x=182, y=185)
        self.btn5 = tk.Button(self.canvas,text = self.hexagonLetters[4], background="white", font=('Helvetica 18 bold'), relief=FLAT, command = lambda: self.sendInput(self.hexagonLetters[4]))
        self.btn5.place(x=182, y=125)
        self.btn6 = tk.Button(self.canvas,text = self.hexagonLetters[5], background="white", font=('Helvetica 18 bold'), relief=FLAT, command = lambda: self.sendInput(self.hexagonLetters[5]))
        self.btn6.place(x=285, y=125)
        self.btn7 = tk.Button(self.canvas,text = self.reqLetter, width=1, font=('Helvetica 18 bold'), relief=FLAT, command = lambda: self.sendInput(self.reqLetter))
        self.btn7.place(x=238, y=155)
        self.btn7.configure(bg = "yellow")

        self.canvas.create_text(220, 50, text="Points:", fill="black", font=('Helvetica 14 bold'))
        self.canvas.create_text(30, 282, text="Rank:", fill="black", font=('Helvetica 12 bold'))


    # this function will have all the necessary things for the game to be played, like mainly to redraw the hexagons
    # as of right now trying to get new puzzle auto-working with it and making a correct guess.
    # and then display the guessed words on the screen somewhere.
    def gameplay(self):
        #checks if the puzzle state is 1
        #then asks the user if they would like to save
        #if there is some sort of userInput put in, check if it's yes then ask for fileName
        #run save function, else in the end it will generate a new puzzle.
        if(self.controller.controllerGetPuzzleState() == 1):
            userinput = simpledialog.askstring("Would you like to save your game?",  "yes/no?")
            if userinput:
                if userinput.lower() == "yes":
                    fileName = simpledialog.askstring("Please enter a file name", "File name: ")
                    self.controller.controllerSaveGame(fileName)
                else:
                    print("Ok, lets generate a new puzzle! ")
            else:
                print("No input provided")
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
        self.hexReq = self.draw_hexagon(self.canvas, 250, 180, self.hex_radius, 'yellow', 'black')
        self.canvas.create_text(250, 180,text = self.reqLetter,fill="black", font=('Helvetica 24 bold'))
        hex1 = self.draw_hexagon(self.canvas, 250, 240, self.hex_radius, 'white', 'black')
        self.canvas.create_text(250, 240,text = self.hexagonLetters[0],fill="black", font=('Helvetica 24 bold'))
        hex2 = self.draw_hexagon(self.canvas, 250, 120, self.hex_radius, 'white', 'black')
        self.canvas.create_text(250, 120,text = self.hexagonLetters[1],fill="black", font=('Helvetica 24 bold'))
        hex3 = self.draw_hexagon(self.canvas, 300, 210, self.hex_radius, 'white', 'black')
        self.canvas.create_text(300, 210,text = self.hexagonLetters[2],fill="black", font=('Helvetica 24 bold'))
        hex4 = self.draw_hexagon(self.canvas, 200, 210, self.hex_radius, 'white', 'black')
        self.canvas.create_text(200, 210,text = self.hexagonLetters[3],fill="black", font=('Helvetica 24 bold'))
        hex5 = self.draw_hexagon(self.canvas, 200, 150, self.hex_radius, 'white', 'black')
        self.canvas.create_text(200, 150,text = self.hexagonLetters[4],fill="black", font=('Helvetica 24 bold'))
        hex6 = self.draw_hexagon(self.canvas, 300, 150, self.hex_radius, 'white', 'black')
        self.canvas.create_text(300, 150,text = self.hexagonLetters[5],fill="black", font=('Helvetica 24 bold'))

        #creates the buttons with the letters and input functionality
        self.btn1 = tk.Button(self.canvas,text = self.hexagonLetters[0], background="white", font=('Helvetica 18 bold'), relief=FLAT, command = lambda: self.sendInput(self.hexagonLetters[0]))
        self.btn1.place(x=233, y=215)
        self.btn2 = tk.Button(self.canvas,text = self.hexagonLetters[1], background="white", font=('Helvetica 18 bold'), relief=FLAT, command = lambda: self.sendInput(self.hexagonLetters[1]))
        self.btn2.place(x=232, y=95)
        self.btn3 = tk.Button(self.canvas,text = self.hexagonLetters[2], background="white", font=('Helvetica 18 bold'), relief=FLAT, command = lambda: self.sendInput(self.hexagonLetters[2]))
        self.btn3.place(x=283, y=185)
        self.btn4 = tk.Button(self.canvas,text = self.hexagonLetters[3], background="white", font=('Helvetica 18 bold'), relief=FLAT, command = lambda: self.sendInput(self.hexagonLetters[3]))
        self.btn4.place(x=182, y=185)
        self.btn5 = tk.Button(self.canvas,text = self.hexagonLetters[4], background="white", font=('Helvetica 18 bold'), relief=FLAT, command = lambda: self.sendInput(self.hexagonLetters[4]))
        self.btn5.place(x=182, y=125)
        self.btn6 = tk.Button(self.canvas,text = self.hexagonLetters[5], background="white", font=('Helvetica 18 bold'), relief=FLAT, command = lambda: self.sendInput(self.hexagonLetters[5]))
        self.btn6.place(x=285, y=125)
        self.btn7 = tk.Button(self.canvas,text = self.reqLetter, width=1, font=('Helvetica 18 bold'), relief=FLAT, command = lambda: self.sendInput(self.reqLetter))
        self.btn7.place(x=238, y=155)
        self.btn7.configure(bg = "yellow")
        self.controller.controllerUpdatePuzzleState1()

        #text for points and rank
        self.canvas.create_text(220, 50, text="Points:", fill="black", font=('Helvetica 14 bold'))
        self.canvas.create_text(30, 282, text="Rank:", fill="black", font=('Helvetica 12 bold'))
    def gameplayBase(self):
        if(self.controller.controllerGetPuzzleState() == 1):
            userinput = simpledialog.askstring("Would you like to save your game?",  "yes/no?")
            if userinput:
                if userinput.lower() == "yes":
                    fileName = simpledialog.askstring("Please enter a file name", "File name: ")
                    self.controller.controllerSaveGame(fileName)
                else:
                    print("Ok, lets generate a new puzzle! ")
            else:
                print("No input provided")
        self.controller.controllerNewGame()
        input = self.e.get()
        # clear listbox every time it's run
        self.clearListbox()
        # must clear the letters once a new puzzle is generated
        self.hexagonLetters.clear()

        #gets points and rank from controller
        self.points.set(self.controller.controllerGetPoints())
        self.rank.set(self.controller.controllerGetPuzzleRank())

        # then we can run the function and pull the data from model->controller->view
        #run base game function and input function
        self.controller.controllerRunBaseGameGUI(input)
        getLetters = self.controller.controllerGetLetters()
        getLetters = getLetters.replace("[", "").replace("]","")
        if getLetters == "" or len(input) < 7 or len(input) > 15:
            messagebox.showinfo("Invalid input!", "Ensure the input is an actual pangram (letters only) and the length is between 7-15")
        else:
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
            self.hexReq = self.draw_hexagon(self.canvas, 250, 180, self.hex_radius, 'yellow', 'black')
            self.canvas.create_text(250, 180,text = self.reqLetter,fill="black", font=('Helvetica 24 bold'))
            hex1 = self.draw_hexagon(self.canvas, 250, 240, self.hex_radius, 'white', 'black')
            self.canvas.create_text(250, 240,text = self.hexagonLetters[0],fill="black", font=('Helvetica 24 bold'))
            hex2 = self.draw_hexagon(self.canvas, 250, 120, self.hex_radius, 'white', 'black')
            self.canvas.create_text(250, 120,text = self.hexagonLetters[1],fill="black", font=('Helvetica 24 bold'))
            hex3 = self.draw_hexagon(self.canvas, 300, 210, self.hex_radius, 'white', 'black')
            self.canvas.create_text(300, 210,text = self.hexagonLetters[2],fill="black", font=('Helvetica 24 bold'))
            hex4 = self.draw_hexagon(self.canvas, 200, 210, self.hex_radius, 'white', 'black')
            self.canvas.create_text(200, 210,text = self.hexagonLetters[3],fill="black", font=('Helvetica 24 bold'))
            hex5 = self.draw_hexagon(self.canvas, 200, 150, self.hex_radius, 'white', 'black')
            self.canvas.create_text(200, 150,text = self.hexagonLetters[4],fill="black", font=('Helvetica 24 bold'))
            hex6 = self.draw_hexagon(self.canvas, 300, 150, self.hex_radius, 'white', 'black')
            self.canvas.create_text(300, 150,text = self.hexagonLetters[5],fill="black", font=('Helvetica 24 bold'))
            #creates the buttons with the letters and input functionality
            self.btn1 = tk.Button(self.canvas,text = self.hexagonLetters[0], background="white", font=('Helvetica 18 bold'), relief=FLAT, command = lambda: self.sendInput(self.hexagonLetters[0]))
            self.btn1.place(x=233, y=215)
            self.btn2 = tk.Button(self.canvas,text = self.hexagonLetters[1], background="white", font=('Helvetica 18 bold'), relief=FLAT, command = lambda: self.sendInput(self.hexagonLetters[1]))
            self.btn2.place(x=232, y=95)
            self.btn3 = tk.Button(self.canvas,text = self.hexagonLetters[2], background="white", font=('Helvetica 18 bold'), relief=FLAT, command = lambda: self.sendInput(self.hexagonLetters[2]))
            self.btn3.place(x=283, y=185)
            self.btn4 = tk.Button(self.canvas,text = self.hexagonLetters[3], background="white", font=('Helvetica 18 bold'), relief=FLAT, command = lambda: self.sendInput(self.hexagonLetters[3]))
            self.btn4.place(x=182, y=185)
            self.btn5 = tk.Button(self.canvas,text = self.hexagonLetters[4], background="white", font=('Helvetica 18 bold'), relief=FLAT, command = lambda: self.sendInput(self.hexagonLetters[4]))
            self.btn5.place(x=182, y=125)
            self.btn6 = tk.Button(self.canvas,text = self.hexagonLetters[5], background="white", font=('Helvetica 18 bold'), relief=FLAT, command = lambda: self.sendInput(self.hexagonLetters[5]))
            self.btn6.place(x=285, y=125)
            self.btn7 = tk.Button(self.canvas,text = self.reqLetter, width=1, font=('Helvetica 18 bold'), relief=FLAT, command = lambda: self.sendInput(self.reqLetter))
            self.btn7.place(x=238, y=155)
            self.btn7.configure(bg = "yellow")
            #text for points and rank
            self.canvas.create_text(220, 50, text="Points:", fill="black", font=('Helvetica 14 bold'))
            self.canvas.create_text(30, 282, text="Rank:", fill="black", font=('Helvetica 12 bold'))
            self.controller.controllerUpdatePuzzleState1()


  



# Runs the GUI
main = tk.Tk()
main.title("MediaTek's Spelling Bee!")
View(main,ctrl)
main.mainloop()