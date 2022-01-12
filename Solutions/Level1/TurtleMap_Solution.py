# Imports the init.py file and the turtle module
from init import *
import turtle

# Creates our screen
SCREEN = turtle.Screen()
SCREEN.title("Mapster Spacebook")
SCREEN.setup(1280, 800)
SCREEN.bgpic(get_file("Assets/Background.gif"))

# Sets the shape to be a green turtle
turtle.shape("turtle")
turtle.color("green") 

# This code moves the turtle to its starting location
turtle.penup()
turtle.setx(460)
turtle.sety(-275)
turtle.pendown()

# Uncommented these lines by removing the hashtags
turtle.left(180)
turtle.forward(510)

# Copied the two lines Grafika gives you here
turtle.right(90)
turtle.forward(220)

# Wrote the last 4 lines, following Grafika's instructions
turtle.left(90)
turtle.forward(490)
turtle.right(90)
turtle.forward(250)

# This line stops the window from closing once we make it to the end
turtle.done()
