import turtle
import random

ct = 0
shawn = turtle.Turtle()
while ct < 10:
	turn = random.randint(0,361)
	shawn.forward(10)
	shawn.left(turn)
	ct = ct + 1

turtle.exitonclick()

