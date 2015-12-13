import random
import turtle

coloor = turtle.Turtle()

pbp = 55
length = 100.0

colors = ['pink','blue','purple','orange','green']
while pbp >0:
        coloor.color(random.choice(colors))
        coloor.forward(length)
        coloor.backward(60)
        coloor.left(120)
        coloor.forward(100)
        coloor.backward(30)
        coloor.left(120)
        length = length - 1
        pbp = pbp -1
exitonclick()

