import turtle
import random




turtle.shape("turtle")
turtle.Screen().bgcolor('red')
turtle.pencolor("blue")

for i in range(40):
    turtle.circle(20+i)
    turtle.forward(10+i)
    turtle.left(i)
    turtle.right(90)


