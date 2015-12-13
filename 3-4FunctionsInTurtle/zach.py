import random
import turtle
shawn = turtle.Turtle()
shawn.speed(0)
shawn.shape("triangle")
length = 100.0
blip = 1000
color = ['red','blue','green','yellow','orange']
while blip  > 0:
    shawn.color(random.choice(color))
    shawn.forward(length)
    shawn.stamp()
    shawn.left(120)
    shawn.forward(length)
    shawn.stamp()
    shawn.left(120)
    shawn.forward(length)
    shawn.stamp()
    shawn.left(120)
    shawn.right(75)
    length = length - .1
    blip = blip - 1
    

