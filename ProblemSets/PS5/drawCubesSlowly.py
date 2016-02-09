import turtle

# draw one rhombus
def drawRhombus(myTurtle, color):
	myTurtle.color(color)
	myTurtle.begin_fill()
	count = 0
	while count < 2:
		myTurtle.forward(20)
		myTurtle.left(120)
		myTurtle.forward(20)
		myTurtle.left(60)
		count += 1
	myTurtle.end_fill()

# draw a row of 10 rhombuses
def drawRowOfTops(myTurtle):
	count = 0
	while count < 10:
		myTurtle.penup()
		myTurtle.left(120)
		myTurtle.forward(20)
		myTurtle.left(60)
		myTurtle.forward(20)
		myTurtle.left(180)
		myTurtle.pendown()
		drawRhombus(myTurtle, "dark blue")
		count += 1

# draw a row of 9 sides
def drawRowOfSides(myTurtle):
	count = 0
	while count < 9:
		myTurtle.right(120)
		drawRhombus(myTurtle, "cadet blue")
# get to the top corner
		myTurtle.forward(20)
		myTurtle.left(120)
		myTurtle.forward(20)
		myTurtle.right(60)
# draw one facing the other direction
		drawRhombus(myTurtle, "light blue")
# get to the opposite corner of the rhombus just drawn
		myTurtle.forward(20)
		myTurtle.left(120)
		myTurtle.forward(20)
		myTurtle.right(60)
		count += 1

# make 4 rows of cubes
def drawAllRows(myTurtle):
	count = 0
	while count < 6:
		drawRowOfTops(myTurtle)
		drawRowOfSides(myTurtle)
# navigate up to next row
		myTurtle.penup()
		myTurtle.forward(20)
		myTurtle.left(60)
		myTurtle.forward(20)
		myTurtle.right(60)
		myTurtle.pendown()
		count += 1


shawn = turtle.Turtle()
shawn.speed(1)

# get to the right a bit
shawn.penup()
shawn.forward(75)
shawn.pendown()

# tilt shawn correctly
shawn.left(30)

# go go shawn!
drawAllRows(shawn)


turtle.exitonclick()
