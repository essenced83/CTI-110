import turtle

# Create a turtle screen and set properties
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Square and Triangle Drawing")

# Create a turtle to draw the shapes
pen = turtle.Turtle()
pen.shape("turtle")
pen.color("blue")
pen.speed(1)

# Function to draw a square
def draw_square():
    for _ in range(4):
        pen.forward(100)
        pen.right(90)

# Function to draw a triangle
def draw_triangle():
    for _ in range(3):
        pen.forward(100)
        pen.left(120)

# Draw the square
draw_square()

# Move the turtle to a new starting position for the triangle
pen.penup()
pen.goto(150, 0)
pen.pendown()

# Draw the triangle
draw_triangle()

# Hide the turtle and display the result
pen.hideturtle()

# Keep the window open until it is closed by the user
turtle.done()
