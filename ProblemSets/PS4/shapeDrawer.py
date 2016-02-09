# shapeDrawer.py
# draws user-input shapes in random places on the screen
# with random sizes and colors

# bring in the packages of functions we need
import random
import turtle

# -------- functions start here ----------------

def regular_triangle(myTurtle, x, y, side, color):
	myTurtle.penup()
# sends turtle to the given x,y pair on the screen
	myTurtle.goto(x,y)
	myTurtle.pendown()
	myTurtle.color(color)
# creates a variable to count number of sides drawn
	side_count = 0
# while there are fewer than 3 sides drawn, keep drawing
	while side_count < 3:
		myTurtle.forward(side)
# angle can be calculated as 360/(total sides)
		myTurtle.right(120)
		side_count = side_count + 1

def regular_square(myTurtle, x, y, side, color):
	myTurtle.penup()
	myTurtle.goto(x,y)
	myTurtle.pendown()
	myTurtle.color(color)
	side_count = 0
	while side_count < 4:
		myTurtle.forward(side)
		myTurtle.right(90)
		side_count = side_count + 1

def regular_pentagon(myTurtle, x, y, side, color):
	myTurtle.penup()
	myTurtle.goto(x,y)
	myTurtle.pendown()
	myTurtle.color(color)
	side_count = 0
	while side_count < 5:
		myTurtle.forward(side)
		myTurtle.right(72)
		side_count = side_count + 1

def regular_hexagon(myTurtle, x, y, side, color):
	myTurtle.penup()
	myTurtle.goto(x,y)
	myTurtle.pendown()
	myTurtle.color(color)
	side_count = 0
	while side_count < 6:
		myTurtle.forward(side)
		myTurtle.right(60)
		side_count = side_count + 1

def regular_octagon(myTurtle, x, y, side, color):
	myTurtle.penup()
	myTurtle.goto(x,y)
	myTurtle.pendown()
	myTurtle.color(color)
	side_count = 0
	while side_count < 8:
		myTurtle.forward(side)
		myTurtle.right(45)
		side_count = side_count + 1

def circle(myTurtle, x, y, radius, color):
	myTurtle.penup()
	myTurtle.goto(x,y)
	myTurtle.pendown()
	myTurtle.color(color)
	myTurtle.circle(radius)

# -------- execution starts here ----------------

print("Welcome to the random shape drawer!")
print("You choose the shapes, and we choose the position, color, and size.")

# create our turtle object
squirt = turtle.Turtle()

# list of colors to be randomly chosen
colors = ['red', 'blue', 'purple', 'orange', 'yellow', 'grey', 'green']

shape = ""
while shape != "exit":
	print("Enter a shape - your choices are triangle, square, pentagon, hexagon, octagon, and circle.")
	print("If you're done making shapes, just type 'exit'.")
	shape = raw_input()

# choose the random position (x,y) for the shape
# choose the random side length or radius & random color
	randx = random.randint(-200,200)
	randy = random.randint(-200,200)
	randside = random.randint(5,100)
	randcolor = random.choice(colors)

# decide which function to call based on the user's input
	if shape == 'triangle':
		regular_triangle(squirt, randx, randy, randside, randcolor) 
	elif shape == 'square':
		regular_square(squirt, randx, randy, randside, randcolor) 
	elif shape == 'pentagon':
		regular_pentagon(squirt, randx, randy, randside, randcolor) 
	elif shape == 'hexagon':
		regular_hexagon(squirt, randx, randy, randside, randcolor) 
	elif shape == 'octagon':
		regular_octagon(squirt, randx, randy, randside, randcolor) 
	elif shape == 'circle':
		circle(squirt, randx, randy, randside, randcolor) 
