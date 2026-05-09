from tkinter import *

# creating the window
window = Tk()
window.geometry("400x400")
window.title("IT'S MY WINDOW")

# 1.Label
# pack() tells Tkinter: "Put this widget into the window."
Label(window,text="shamshuddin",font=("cascadia code",20,'bold'),bg="purple").pack()

# 2.Entry
Entry(window,font=("cascadia code",40),bg="orange").pack()
Entry(window,font=("cascadia code",40),bg="white").pack()
Entry(window,font=("cascadia code",40),bg="green").pack()
# 3.button
Button(window,text="nokku nannu",font=("cascadia code",22,'bold'),bg="blue").pack()

window.mainloop()