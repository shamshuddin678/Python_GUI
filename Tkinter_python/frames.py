# frame is a rectangular container to group and hold all the widgets
from tkinter import *

window = Tk()
window.geometry("400x400")

frame = Frame(window,bg="brown",bd=6,relief=SUNKEN)
# frame.pack() # here we can use pack(BOTTOM) is ate frame
frame.place(x=0,y=0)

Button(frame,text="S",font=("casacdia code",27,'bold'),fg="orange",width=3).pack(side=TOP)
Button(frame,text="H",font=("casacdia code",27,'bold'),fg="purple",width=3).pack(side=LEFT)
Button(frame,text="A",font=("casacdia code",27,'bold'),fg="green",width=3).pack(side=LEFT)
Button(frame,text="M",font=("casacdia code",27,'bold'),fg="pink",width=3).pack(side=LEFT)

window.mainloop()