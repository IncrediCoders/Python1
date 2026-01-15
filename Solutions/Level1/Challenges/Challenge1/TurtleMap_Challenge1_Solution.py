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
turtle.forward(125)

# Turned right 90 degrees and moved forward 105 steps
turtle.right(90)
turtle.forward(105)

# Turned right 90 degrees and moved forward 185 steps
turtle.right(90)
turtle.forward(185)

# Turned left and moved to the end of the road
turtle.left(90)
turtle.forward(385)

# Turned left and moved to the intersection
turtle.left(90)
turtle.forward(65)

# Wrote more lines here to navigate the alternate route to school
# Crossed the bridge and stayed on the road!
turtle.right(90)
turtle.forward(105)

turtle.left(90)
turtle.forward(435)

turtle.left(90)
turtle.forward(105)

turtle.right(90)
turtle.forward(195)

turtle.right(90)
turtle.forward(80)

turtle.left(90)
turtle.forward(170)

# This line stops the window from closing once we make it to the end
turtle.done()
