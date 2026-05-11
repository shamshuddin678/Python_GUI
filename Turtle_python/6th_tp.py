import turtle
import time

t = turtle.Turtle()

# t.circle(70) 1 way to draw the circle

#  the 2nd way to dra the circle
time.sleep(1) 
t.goto(-250,0)
t.home() # after it goto 0 to 250 it cmes back to 0 . means start point

t.goto(250,0)
t.home()

t.goto(0,250)
t.home()

t.goto(0,-250)


t.circle(250)

turtle.done()