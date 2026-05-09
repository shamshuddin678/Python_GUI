from tkinter import *

win2 = Tk()
win2.geometry('400x400')
win2.title("Using command func")

def click():
    print("clicked")

# def mouse_events(event):
#     print("left clicked")


button = Button(win2,text="click",font=("cascadia code", 35, 'bold'),fg="orange",command=click)

button.pack()

# button.bind("<Button-1>", mouse_events)



win2.mainloop()