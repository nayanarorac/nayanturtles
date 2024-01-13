import turtle

# Create a turtle screen
screen = turtle.Screen()

# Create a turtle object
turtle1 = turtle.Turtle()
turtle1.pencolor('#800080')

# Function to draw a square
def draw_cone():
    for x in range(4):
        turtle1.forward(2) #1
        turtle1.circle(40-3*x)
        
# Draw the circle
draw_cone()
turtle1.right(90)
draw_cone()

# Keep the window open until it's closed by the user
turtle.done()
