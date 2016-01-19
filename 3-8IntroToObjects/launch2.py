import turtle

def drawSquare(ourTurtle):
    ct = 0
    while ct < 4:
        ourTurtle.forward(100)
        ourTurtle.left(90)
        ct = ct + 1
 
shawn = turtle.Turtle()
shawn.backward(200)
drawSquare(shawn)

turtle.exitonclick()
