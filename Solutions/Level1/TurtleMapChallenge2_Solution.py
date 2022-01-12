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

# Wrote a loop to go back and forth 5 times
# To learn more about loops, follow the instructions on the wiki page
for trip_number in range(5):
    # In this loop, wrote the code to go to the school and then to get back
    # (You can use your code you wrote from the instructions in the book!)
    turtle.left(180)
    turtle.forward(510)
    turtle.right(90)
    turtle.forward(220)

    turtle.left(90)
    turtle.forward(490)    
    turtle.right(90)
    turtle.forward(250)

    # Reached the school, and then go back to the house
    turtle.left(180)
    turtle.forward(250)    
    turtle.left(90)
    turtle.forward(490)
    
    turtle.right(90)
    turtle.forward(220)
    turtle.left(90)
    turtle.forward(510)
# End the loop here

# This line stops the window from closing once we make it to the end
turtle.done()
