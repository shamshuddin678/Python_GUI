import turtle
import time

t = turtle.Turtle()

time.sleep(0)
t.goto(-250,0)
t.dot(50,'purple') # dot(size_of_dot,color)
t.home()

time.sleep(0)
t.goto(250,0)
t.dot(50,'orange') # dot(size_of_dot,color)
t.home()

time.sleep(0)
t.goto(0,250)
t.dot(50,'green') # dot(size_of_dot,color)
t.home()

time.sleep(0)
t.goto(0,-250)
t.dot(50,'yellow') # dot(size_of_dot,color)


t.circle(250)
t.home()
t.dot(50,'brown') # dot(size_of_dot,color)

turtle.done()