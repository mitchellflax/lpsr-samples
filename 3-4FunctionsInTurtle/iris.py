import turtle

t = turtle.Turtle()
turtle.colormode(255)

c = 50

while c > 0:
  t.speed(10)
  t.color(128,0,0)
  t.forward(c * 3)
  t.color(0,225,225)
  t.right(135)
  t.forward(c * 3)
  c = c - 1

turtle.exitonclick()
