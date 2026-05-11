import turtle
import time

t = turtle.Turtle()
screen = turtle.Screen()
screen.setup(700,700)
screen.title("pen_up vs pen_down")

for i in range(4):
   t.penup() # Lift the pen from paper.Now turtle moves without drawing.
   t.forward(250)
   time.sleep(1)
   t.left(90)
   t.pendown() # Put the pen back on paper.Now turtle moves with drawing.


turtle.done()