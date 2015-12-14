# square.py

import turtle

# make our turtle
rocky = turtle.Turtle()

# rocky makes a square
lines = 0
while lines < 4:
	rocky.forward(150)
	rocky.left(90)
	lines = lines + 1

# wait to exit until I've clicked
turtle.exitonclick()
