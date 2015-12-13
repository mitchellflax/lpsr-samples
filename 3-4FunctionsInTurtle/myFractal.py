# square.py

import turtle

def makeSquare(myTurtle, side):
	lines = 0 
	while lines < 4:
		myTurtle.forward(side)
		myTurtle.left(90)
		lines = lines + 1


# make our turtle
squeak = turtle.Turtle()

# buzz makes a square
length = 100
while length > 0:
	makeSquare(squeak, length)
	squeak.right(5)
	length = length - 1

# wait to exit until I've clicked
turtle.exitonclick()
