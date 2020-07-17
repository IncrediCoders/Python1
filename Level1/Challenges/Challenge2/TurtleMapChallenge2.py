"""Turtle graphics project file."""
from init import *
import turtle

# Create our screen
SCREEN = turtle.Screen()
SCREEN.title("Napster Spacebook")
SCREEN.setup(1280, 800)
SCREEN.bgpic("Assets/Background.png")

# Set the shape to be a green turtle.
turtle.shape("turtle")
turtle.color("green") 

# This code moves the turtle to its starting location.
turtle.penup()
turtle.setx(460)
turtle.sety(-275)
turtle.pendown()

#TODO: Write a loop to go back and forth 5 times.
# If you don't know what to do, come back after you learn loops.

    #TODO: In your loop, write code to go to the school and then back
    # (You can use your easy solution for a lot of this!)

#TODO: End the loop here.

# This line stops the window from closing once we make it to the end.
turtle.done()
