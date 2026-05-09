from tkinter import *
from tkinter import colorchooser

win = Tk()

#  way1 function
def click():
    color = colorchooser.askcolor()
    # print(color)
    # colorHex = color[1]
    # print(colorHex)
    '''    Index	Value
          color[0]	RGB tuple
          color[1]	HEX color string'''
    win.config(bg=color[1]) #  changes the background color

win.geometry("400x400")
win.title("background")
Button(win,text="press the button",command = click,fg="orange",font=("cascadia code",30,'bold')).pack()

win.mainloop()



'''way2 function 

def click():
win.config(bg= colorchooser.askcolor()[1])



'''