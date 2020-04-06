"""Turtle graphics project file."""
from init import *
import turtle

# Create our screen
SCREEN = turtle.Screen()
SCREEN.title("Napster Spacebook")
SCREEN.setup(1280, 800)
SCREEN.bgpic(get_file("Assets\Background.png"))

# Set the shape to be a car.
SCREEN.register_shape("car", ((-4, 10), (4, 10), (4, -10), (-4, -10)))
turtle.shape("car")

# This code moves the turtle to its starting location.
turtle.penup()
turtle.setx(460)
turtle.sety(-275)
turtle.pendown()

#TODO: Uncomment these lines by removing the hashtags.
#turtle.left(180)
#turtle.forward(510)

#TODO: Copy the two lines Grafika gives you here.

#TODO: Write a couple more lines, following Grafika's instructions.

# This line stops the window from closing once we make it to the end.
turtle.done()