#Turtle graphics project file
from init import *
import turtle

#Create our screen
SCREEN = turtle.Screen()
SCREEN.title("Mapster Spacebook")
SCREEN.setup(1280, 800)
SCREEN.bgpic(get_file("Assets/Background.gif"))

#Set the shape to be a green turtle
turtle.shape("turtle")
turtle.color("green") 

#This code moves the turtle to its starting location
turtle.penup()
turtle.setx(460)
turtle.sety(-275)
turtle.pendown()

#Uncomment these lines by removing the hashtags
turtle.left(180)
turtle.forward(125)

#Turn right 90 degrees and move forward 105 steps
turtle.right(90)
turtle.forward(105)

#Turn right 90 degrees and move forward 185 steps
turtle.right(90)
turtle.forward(185)

#Turn left and move to the end of the road
turtle.left(90)
turtle.forward(385)

#Turn left and move to the intersection
turtle.left(90)
turtle.forward(65)

#Write more lines here to navigate the alternate route to school
#Cross the bridge and stay on the road!
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

#This line stops the window from closing once we make it to the end
turtle.done()
