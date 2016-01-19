import turtle
from Tkinter import *

# create the root Tkinter window and a Frame to go in it
root = Tk()
frame = Frame(root, height=100, width=100)

# create our turtle
shawn = turtle.Turtle()

# make some simple buttons
fwd = Button(frame, text='fwd', fg='red', command=lambda: shawn.forward(50))
left = Button(frame, text='left', command=lambda: shawn.left(90))

# put it all together
fwd.pack(side=LEFT)
left.pack(side=LEFT)
frame.pack()

turtle.exitonclick()
