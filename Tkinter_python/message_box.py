from tkinter import *
from tkinter import messagebox


def click():
    messagebox.showinfo(title="bol be ",message="if you click ok your computer can crash")



window = Tk()
window.geometry("400x400")
window.title("importing the messagebox(because it is a sub module)")

Button(window,text="Click me",fg="purple",command=click,font=("casacdia code",30,'bold')).pack()

if(messagebox.askretrycancel(title="if can try retry",message="if you can can try retry click the button ")):
    print("you gotted!")
else:
    print("you failes to know")
window.mainloop()