import turtle
import time

t = turtle.Turtle()

screen = turtle.Screen()
screen.bgcolor("pink")

t.turtlesize(4)
t.pensize(10)
t.color("yellow","green")
t.shape("turtle")

time.sleep(0)
t.goto(-250,0)
t.dot(50,"blue")
t.home()

time.sleep(0)
t.goto(250,0)
t.dot(50,"sky blue")
t.home()

time.sleep(0)
t.goto(0,250)
t.dot(50,"brown")
t.home()

time.sleep(0)
t.goto(0,-250)
t.dot(50,"purple")


t.circle(250)

turtle.done()
