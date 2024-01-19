import turtle
turtleqp = turtle.Turtle()
turtleqp.shape('square')
turtleqp.pencolor("#FFA500")
# Function to draw a square
def draw_cone():
    for x in range(4):
        turt1eqp.forward(2) #1
        turtleqp.circle(40-3*x)
draw_cone()
turtleqp.forward(100)
draw_cone()
