import turtle
import time

# t = turtle.Turtle() means  it creates a turtle object and store it in a variable 't
t = turtle.Turtle() # without turtle.done suddenly the window closes

# rectangle or sqaure for rrange(4)
for i in range(4): # 4 times for sqaure 
   time.sleep(2) # starts after 2sec
   t.forward(200) # go forawrd
   time.sleep(2) # stop and starts after 2sec
   t.left(90) # turn left




turtle.done() # Program finished, but keep the turtle window open