import turtle
import time

t = turtle.Turtle()


t.turtlesize(2) # turtle pen size double
t.pensize(10) # line size is 10
t.color("orange","blue") # here line color is orange and 2nd parameter is turtle object color.

t.shape('turtle') # shape of turtle object

# square creation
for i in range(4):
    time.sleep(0)
    t.forward(200)
    time.sleep(0)
    t.left(90)



turtle.done()