import tkinter as tk
import controllerrefactor as ctrl
import math
import random
import copy

class View:
    def __init__(self, parent, ctrl):
        self.controller = ctrl.controller()
        self.parent = parent
        # created a frame
        self.myFrame = tk.Frame(parent)
        self.myFrame.pack()
        # created an input box
        self.e = tk.Entry(self.parent, width=50, bg="white", fg="black")
        self.e.pack()
        # Variables that describe size of hexagon
        self.hex_radius = 30
        self.hex_width = math.sqrt(3) * self.hex_radius
        self.hex_height = 2 * self.hex_radius

        # created some buttons
        self.newPuzzleButton = tk.Button(self.parent, text="New Puzzle", command=self.gameplay)
        self.newPuzzleButton.pack(pady=20)
        self.guessButton = tk.Button(self.parent, text="Guess", command=self.makeGuess)
        self.guessButton.pack(padx=40, pady=20)
        self.backButton = tk.Button(self.parent, text="Backspace", command=self.backspace)
        self.backButton.pack(padx=60, pady=20)

        self.hexagonLetters = []
        self.reqLetter = ""

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
    def makeGuess(self):
        input = self.e.get()
        # made it so userGuess returns true/false so that way we only insert valid words into the listbox.
        if self.controller.controllerUserGuess(input) == True:
            self.listBox.insert(tk.END, input)
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

    # this function will have all the necessary things for the game to be played, like mainly to redraw the hexagons
    # as of right now trying to get new puzzle auto-working with it and making a correct guess.
    # and then display the guessed words on the screen somewhere.
    def gameplay(self):
        # clear listbox every time it's run
        self.clearListbox()
        # must clear the letters once a new puzzle is generated
        self.hexagonLetters.clear()
        # then we can run the function and pull the data from model->controller->view
        self.controller.controllerRunAutoGame()
        getLetters = self.controller.controllerGetLetters()
        getLetters = getLetters.replace("[", "").replace("]","")
        #controller function to append letters into a list
        self.hexagonLetters = self.controller.controllerToList(getLetters, self.hexagonLetters)
        print(self.hexagonLetters)

        # Creates a 500 x 500 canvas with a white background along with title
        canvas = tk.Canvas(self.parent, width=500, height=500,bg='#F4F4F4')
        canvas.create_text(250, 25, text="Welcome to MediaTek's Spelling Bee!", fill="black", font=('Helvetica 24 bold'))
        canvas.pack()

        #get required letter
        self.reqLetter = self.controller.controllerGetReqLetter()
        print(self.reqLetter)
        #hoping this removes the required letter from the list.
        self.hexagonLetters.remove(self.reqLetter)
        #create 7 buttons unsure how to make a honeycomb
        self.draw_hexagon(canvas, 250, 250, self.hex_radius, 'yellow', 'black')
        canvas.create_text(250, 250,text = self.reqLetter,fill="black", font=('Helvetica 24 bold'))
        self.draw_hexagon(canvas, 250, 310, self.hex_radius, 'white', 'black')
        canvas.create_text(250, 310,text = self.hexagonLetters[0],fill="black", font=('Helvetica 24 bold'))
        self.draw_hexagon(canvas, 250, 190, self.hex_radius, 'white', 'black')
        canvas.create_text(250, 190,text = self.hexagonLetters[1],fill="black", font=('Helvetica 24 bold'))
        self.draw_hexagon(canvas, 300, 280, self.hex_radius, 'white', 'black')
        canvas.create_text(300, 280,text = self.hexagonLetters[2],fill="black", font=('Helvetica 24 bold'))
        self.draw_hexagon(canvas, 200, 280, self.hex_radius, 'white', 'black')
        canvas.create_text(200, 280,text = self.hexagonLetters[3],fill="black", font=('Helvetica 24 bold'))
        self.draw_hexagon(canvas, 200, 220, self.hex_radius, 'white', 'black')
        canvas.create_text(200, 220,text = self.hexagonLetters[4],fill="black", font=('Helvetica 24 bold'))
        self.draw_hexagon(canvas, 300, 220, self.hex_radius, 'white', 'black')
        canvas.create_text(300, 220,text = self.hexagonLetters[5],fill="black", font=('Helvetica 24 bold'))

        self.btn1 = tk.Button(canvas,text = self.hexagonLetters[0], command = lambda: self.sendInput(self.hexagonLetters[0]))
        self.btn1.place(x=228, y=310)
        self.btn2 = tk.Button(canvas,text = self.hexagonLetters[1], command = lambda: self.sendInput(self.hexagonLetters[1]))
        self.btn2.place(x=228, y=190)
        self.btn3 = tk.Button(canvas,text = self.hexagonLetters[2], command = lambda: self.sendInput(self.hexagonLetters[2]))
        self.btn3.place(x=300, y=280)
        self.btn4 = tk.Button(canvas,text = self.hexagonLetters[3], command = lambda: self.sendInput(self.hexagonLetters[3]))
        self.btn4.place(x=200, y=280)
        self.btn5 = tk.Button(canvas,text = self.hexagonLetters[4], command = lambda: self.sendInput(self.hexagonLetters[4]))
        self.btn5.place(x=200, y=220)
        self.btn6 = tk.Button(canvas,text = self.hexagonLetters[5], command = lambda: self.sendInput(self.hexagonLetters[5]))
        self.btn6.place(x=300, y=220)
        self.btn7 = tk.Button(canvas,text = self.reqLetter, command = lambda: self.sendInput(self.reqLetter))
        self.btn7.place(x=228, y=250)
        self.btn7.configure(bg = "yellow")

        canvas.create_text(220, 360, text="Points:", fill="black", font=('Helvetica 24 bold'))


  



# Runs the GUI
main = tk.Tk()
main.title("MediaTek's Spelling Bee!")
View(main,ctrl)
main.mainloop()


