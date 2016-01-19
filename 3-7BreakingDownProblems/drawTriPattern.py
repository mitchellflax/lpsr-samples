import turtle

def drawTriangle(myTurtle):
	count = 0
	while count < 3:
		myTurtle.forward(10)
		myTurtle.left(120)
		count += 1

def drawCluster(myTurtle):
	count = 0
	while count < 4:
		myTurtle.pendown()
		drawTriangle(myTurtle)
		myTurtle.penup()
		myTurtle.forward(30)
		count += 1

def drawQuarterOfClusters(myTurtle):
	count = 0
	while count < 3:
		drawCluster(myTurtle)
		myTurtle.left(30)
		myTurtle.goto(0,0)
		count += 1

def drawTwoQuarters(myTurtle):
	drawQuarterOfClusters(myTurtle)
	myTurtle.left(90)
	drawQuarterOfClusters(myTurtle)

shawn = turtle.Turtle()
drawTwoQuarters(shawn)

turtle.exitonclick()
