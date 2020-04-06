"""Turtle graphics project file."""
import turtle

# Create our screen
SCREEN = turtle.Screen()
SCREEN.title("Napster Spacebook")
SCREEN.setup(1280, 800)
SCREEN.bgpic("assets/Background.png")

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
#turtle.forward(125)

#TODO: Turn right 90 degrees and move forward 105 steps.

#TODO: Turn right 90 degrees and move forward 185 steps.

#TODO: Turn left and move to the end of the road.

#TODO: Turn left and move to the intersection.

#TODO: Write more lines here to navigate the alternate route to school.
# Cross the bridge and stay on the road!

# This line stops the window from closing once we make it to the end.
turtle.done()
