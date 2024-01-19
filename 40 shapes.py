import turtle

# Create a turtle screen
screen = turtle.Screen()

# Create a turtle object
turtle1 = turtle.Turtle()
turtle1.pencolor('#FFFFFF')
turtle1.setpos(-500, turtle.window_height() / 2)
turtle1.pencolor('#800080')
def draw_circles():
    for x in range(40):
        turtle1.forward(2)
        turtle1.circle(40-3*x)


def draw_squares():
    for x in range(40):
        turtle1.forward(2)
        turtle1.square(40-3*x)
        
draw_circles()
turtle1.pencolor('#FFFFFF')
turtle1.setpos(500,turtle.window_height() /2)
turtle.pencolor('#FFA500')
draw_squares()

turtle.done()
