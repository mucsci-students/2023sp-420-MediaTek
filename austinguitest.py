import tkinter as tk
import controllerrefactor as ctrl
import math
import random
import copy



class view():
    def __init__(self, parent, ctrl):
        self.controller = ctrl.controller()
        self.parent = parent
        #created a frame
        self.myFrame = tk.Frame(parent)
        self.myFrame.pack()
        #created a inputbox
        self.e = tk.Entry(self.parent,width=50,bg="white", fg="black")
        self.e.pack()

        #created some buttons
        self.newPuzzleButton = tk.Button(self.parent, text = "New Puzzle", command=self.gameplay)
        self.newPuzzleButton.pack(pady=20)
        self.guessButton = tk.Button(self.parent, text = "Guess", command=self.makeGuess)
        self.guessButton.pack(padx=40,pady=20)
        self.backButton = tk.Button(self.parent, text = "Backspace", command=self.backspace)
        self.backButton.pack(padx=60,pady=20)

        self.hexagonLetters = []
        self.reqLetter = ""

        #creatad a list box which will show the found words
        self.listBox = tk.Listbox(self.parent)
        self.listBox.pack(pady=60)

        self.test = 0
        #empty state for the buttons

    def clicker(self):
            print(self.controller.controllerGetLetters())
    def sendInput(self,text):
        self.e.insert(tk.END,text)
    def clearInput(self):
        self.e.delete(0,tk.END)
    def clearListbox(self):
        self.listBox.delete(0,tk.END)

    def backspace(self):
        self.e.delete(len(self.e.get())-1, tk.END)



    #callc user guess from controller, this probably shoulve be moved into controller later
    def makeGuess(self):
         input = self.e.get()
         #made it so userGuess returns true/false so that way we only insert valid words into the listbox.
         if self.controller.controllerUserGuess(input) == True:
              self.listBox.insert(tk.END,input)
         self.clearInput()
         
    #this function will have all the necessary things for the game to be played like mainly to redraw the hexagons
    #as of right now trying to get new puzzle auto working with it and making a correct guess.
    #and then display the guessed words on the screen somewhere.
    def gameplay(self):
        #clear listbox everytime it's run
        self.clearListbox()
        #must clear the letters once a new puzzle is generated
        self.hexagonLetters.clear()
        #then we can run the function and pull the data from model->controller->view
        self.controller.controllerRunAutoGame()
        getLetters = self.controller.controllerGetLetters()
        getLetters = getLetters.replace("[","").replace("]","")
        #controller function to append letters into a list
        self.hexagonLetters = self.controller.controllerToList(getLetters, self.hexagonLetters)
        print(self.hexagonLetters)

        #get required letter
        self.reqLetter = self.controller.controllerGetReqLetter()
        print(self.reqLetter)
        #hoping this removes the required letter from the list.
        self.hexagonLetters.remove(self.reqLetter)
        #create 7 buttons unsure how to make a honeycomb
        self.btn1 = tk.Button(self.parent,text = self.hexagonLetters[0], command = lambda: self.sendInput(self.hexagonLetters[0]))
        self.btn1.place(x=100,y=20)
        self.btn2 = tk.Button(self.parent,text = self.hexagonLetters[1], command = lambda: self.sendInput(self.hexagonLetters[1]))
        self.btn2.place(x=120,y=20)
        self.btn3 = tk.Button(self.parent,text = self.hexagonLetters[2], command = lambda: self.sendInput(self.hexagonLetters[2]))
        self.btn3.place(x=140,y=20)
        self.btn4 = tk.Button(self.parent,text = self.hexagonLetters[3], command = lambda: self.sendInput(self.hexagonLetters[3]))
        self.btn4.place(x=160,y=20)
        self.btn5 = tk.Button(self.parent,text = self.hexagonLetters[4], command = lambda: self.sendInput(self.hexagonLetters[4]))
        self.btn5.place(x=180,y=20)
        self.btn6 = tk.Button(self.parent,text = self.hexagonLetters[5], command = lambda: self.sendInput(self.hexagonLetters[5]))
        self.btn6.place(x=200,y=20)
        self.btn7 = tk.Button(self.parent,text = self.reqLetter, command = lambda: self.sendInput(self.reqLetter))
        self.btn7.place(x=220,y=20)




# Runs the GUI
main = tk.Tk()
main.title("MediaTek's Spelling Bee!")
view(main,ctrl)
main.mainloop()
