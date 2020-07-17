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
# To learn more about loops, follow the instructions on the wiki page.

    #TODO: In your loop, write the code to go to the school and then to get back.
    # (You can use your code you wrote from the instructions in the book!)

#TODO: End the loop here.

# This line stops the window from closing once we make it to the end.
turtle.done()
