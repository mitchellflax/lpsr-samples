import turtle

def drawColoredSquare(myTurtle, color):
	myTurtle.color(color)
	count = 0
	while count < 4:
		myTurtle.forward(20)
		myTurtle.left(90)
		count += 1

def drawSquareBlock(myTurtle):
	count = 0
	colors = ['red', 'blue', 'green', 'orange']
	while count < 4:
		drawColoredSquare(myTurtle, colors[count])
		myTurtle.right(90)
		count += 1

def drawSlash(myTurtle):
	myTurtle.penup()
	myTurtle.forward(100)
	myTurtle.left(90)
	myTurtle.pendown()
	count = 0
	while count < 5:
		drawSquareBlock(myTurtle)
		myTurtle.penup()
		myTurtle.left(30)
		myTurtle.forward(40)
		myTurtle.right(30)
		myTurtle.pendown()
		count += 1


shawn = turtle.Turtle()
drawSlash(shawn)

turtle.exitonclick()

