import turtle

def drawSquare(myTurtle):
	ct = 0
	while ct < 4:
		ct += 1
		myTurtle.forward(20)
		myTurtle.left(90)

shawn = turtle.Turtle()
shawnella = turtle.Turtle()
shawn.color("pink")
shawnella.color("green")

shawn.forward(50)
drawSquare(shawn)

shawnella.left(180)
shawnella.forward(50)
drawSquare(shawnella)

turtle.exitonclick()
