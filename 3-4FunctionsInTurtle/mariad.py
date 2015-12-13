import turtle

marmar = turtle.Turtle()

color = 0
marmar.speed(450)
while color < 450:
        turtle.colormode(255)
        marmar.color(235, 101, 252)
        marmar.color(1, 252, 101)
        marmar.forward(100)
        marmar.color(235, 245, 42)
        marmar.right(53)
        marmar.forward(50)
        marmar.pu()
        marmar.pd()
        marmar.color(33, 11, 227)
        marmar.fd(50)
        marmar.left(45)
        marmar.fd(30)
        marmar.left(40)
        marmar.right(43)
        marmar.pu()
        marmar.pd()
        marmar.radians()
        marmar.begin_fill()
        marmar.end_fill()
        color = color + 1
turtle.exitonclick()

#2 
import turtle

marmar = turtle.Turtle()

color = 0
marmar.speed(150)
while color < 200:
        turtle.colormode(255)
        marmar.color(235, 101, 252)
        marmar.forward(50)
        marmar.right(50)
        marmar.color(1, 252, 101)
        marmar.forward(100)
        marmar.color(235, 245, 42)
        marmar.right(53)
        marmar.forward(50)
        marmar.pu()
        marmar.pd()
        marmar.color(33, 11, 227)
        marmar.fd(50)
        marmar.left(45)
        marmar.fd(30)
        marmar.left(40)
        marmar.right(43)
        marmar.pu()
        marmar.pd()
        marmar.radians()
        marmar.begin_fill()
        marmar.end_fill()
        color = color + 1
turtle.exitonclick()
