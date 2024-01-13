import turtle

# Create a turtle screen
screen = turtle.Screen()

# Create a turtle object
turtle1 = turtle.Turtle()
turtle1.pencolor('#800080')

# Function to draw a square
def draw_square():
    for x in range(4):
        turtle1.forward(60) #1
        turtle1.left(90)    

def draw_rightface():
    turtle1.forward(60) #5
    turtle1.left(40)
    turtle1.forward(40) #6
    turtle1.left(50)
    turtle1.forward(60) #7
    turtle1.left(130)
    turtle1.forward(40) #8

def draw_topface():
    turtle1.right(40)
    turtle1.forward(60) #9
    turtle1.right(90+50)
    turtle1.forward(40) #10
    turtle1.right(40)
    turtle1.forward(60) #11



    
# Draw the circle
draw_square()
draw_rightface()
draw_topface()
turtle1.left(90)
draw_square()

#ok let's draw a triangle in blue
turtle1.pencolor('#000080')
turtle1.forward(60)
turtle1.left(45)
turtle1.forward(40)
turtle1.left(90)
turtle1.forward(40)


# Keep the window open until it's closed by the user
turtle.done()
