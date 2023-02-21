import tkinter as tk
import math
import random
# Create the main window
main = tk.Tk()
main.title("MediaTek's Spelling Bee!")

# Variables that describe size of hexagon
hex_radius = 30
hex_width = math.sqrt(3) * hex_radius
hex_height = 2 * hex_radius

# Function that creates a hexagon
def draw_hexagon(canvas, x, y, radius, fill, outline):
    angle = 60
    points = []
    for i in range(6):
        x_i = x + radius * math.cos(math.radians(angle * i))
        y_i = y + radius * math.sin(math.radians(angle * i))
        points.append((x_i, y_i))
    canvas.create_polygon(points, fill=fill, outline=outline)

# Creates a click event for hexagon
def hexClick(event):
    hexagon = event.widget.find_withtag('current')
    letter = hexagon_letters
    

# Shuffle function
def shuffle():
    random.shuffle(hexagon_letters)
    canvas.delete('all')
    canvas.create_text(250, 25, text="Welcome to MediaTek's Spelling Bee!", fill="black", font=('Helvetica 24 bold'))
    draw_hexagon(canvas, 250, 250, hex_radius, 'yellow', 'black')
    canvas.create_text(250, 250,text = req_letter[0],fill="black", font=('Helvetica 24 bold'))
    draw_hexagon(canvas, 250, 310, hex_radius, 'white', 'black')
    canvas.create_text(250, 310,text = hexagon_letters[0],fill="black", font=('Helvetica 24 bold'))
    draw_hexagon(canvas, 250, 190, hex_radius, 'white', 'black')
    canvas.create_text(250, 190,text = hexagon_letters[1],fill="black", font=('Helvetica 24 bold'))
    draw_hexagon(canvas, 300, 280, hex_radius, 'white', 'black')
    canvas.create_text(300, 280,text = hexagon_letters[2],fill="black", font=('Helvetica 24 bold'))
    draw_hexagon(canvas, 200, 280, hex_radius, 'white', 'black')
    canvas.create_text(200, 280,text = hexagon_letters[3],fill="black", font=('Helvetica 24 bold'))
    draw_hexagon(canvas, 200, 220, hex_radius, 'white', 'black')
    canvas.create_text(200, 220,text = hexagon_letters[4],fill="black", font=('Helvetica 24 bold'))
    draw_hexagon(canvas, 300, 220, hex_radius, 'white', 'black')
    canvas.create_text(300, 220,text = hexagon_letters[5],fill="black", font=('Helvetica 24 bold'))
    canvas.create_text(220, 360, text="Points:", fill="black", font=('Helvetica 24 bold'))

# Creates a 500 x 500 canvas with a white background along with title
canvas = tk.Canvas(main, width=500, height=500, bg='#F4F4F4')
canvas.create_text(250, 25, text="Welcome to MediaTek's Spelling Bee!", fill="black", font=('Helvetica 24 bold'))
canvas.pack()

# Defines letters to be on hexagons, will be shrunk to 6 and the required letter will be added
hexagon_letters = ["A","B","C","D","E","F"]
req_letter = ["Z"]
# Draws the hexagons
draw_hexagon(canvas, 250, 250, hex_radius, 'yellow', 'black')
canvas.create_text(250, 250,text = req_letter[0],fill="black", font=('Helvetica 24 bold'))
draw_hexagon(canvas, 250, 310, hex_radius, 'white', 'black')
canvas.create_text(250, 310,text = hexagon_letters[0],fill="black", font=('Helvetica 24 bold'))
draw_hexagon(canvas, 250, 190, hex_radius, 'white', 'black')
canvas.create_text(250, 190,text = hexagon_letters[1],fill="black", font=('Helvetica 24 bold'))
draw_hexagon(canvas, 300, 280, hex_radius, 'white', 'black')
canvas.create_text(300, 280,text = hexagon_letters[2],fill="black", font=('Helvetica 24 bold'))
draw_hexagon(canvas, 200, 280, hex_radius, 'white', 'black')
canvas.create_text(200, 280,text = hexagon_letters[3],fill="black", font=('Helvetica 24 bold'))
draw_hexagon(canvas, 200, 220, hex_radius, 'white', 'black')
canvas.create_text(200, 220,text = hexagon_letters[4],fill="black", font=('Helvetica 24 bold'))
draw_hexagon(canvas, 300, 220, hex_radius, 'white', 'black')
canvas.create_text(300, 220,text = hexagon_letters[5],fill="black", font=('Helvetica 24 bold'))
# Creates text box on bottom of screen
canvas.create_text(220, 360, text="Points:", fill="black", font=('Helvetica 24 bold'))
text = tk.Text(main, width=10, height=1, font=('Helvetica 24 bold'))
text.pack()

# takes each tagged hexagon and adds click event to each one
for i in range(1, 8):
    hexagon = canvas.find_withtag(i)
    canvas.tag_bind(hexagon, '<Button-1>', hexClick)
    

# Creates Exit button
exit_button = tk.Button(main, text="Exit", command=main.destroy)
exit_button.pack(side='left', padx=10, pady=10)

#Creates Shuffle button
shuff_button = tk.Button(main, text="Shuffle", command= shuffle)
shuff_button.pack(side='right', padx=10, pady=10)

# Runs the GUI
print(*hexagon_letters)
main.mainloop()
