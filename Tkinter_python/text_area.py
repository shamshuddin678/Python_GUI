# text widget you can enter multiple lines
from tkinter import *

win = Tk()
win.geometry("400x400")
t = Text(win)
t.pack()

def submit():
    input1 = t.get("1.0",END) # here 1.0 is a text index position(line.column : line = 1, column = 0)
    print(input1)
Button(win,text="submit",command=submit).pack()



win.mainloop()