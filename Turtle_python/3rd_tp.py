import turtle
import time

t = turtle.Turtle()

#  hexagonal in turtle for range(6)
for i in range(6):
   time.sleep(2)
   t.backward(100)
   time.sleep(2)
   t.right(60)

time.sleep(2)
t.circle(60)

turtle.done()