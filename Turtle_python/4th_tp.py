import turtle
import time

t = turtle.Turtle() 

#  coordiates (x,y)
#  for tiangle
time.sleep(1)
t.goto(0,200)
print(t.pos())

time.sleep(1)
t.setposition(200,0)
print(t.pos())

time.sleep(1)
t.setposition(0,0)
print(t.pos())


turtle.done()