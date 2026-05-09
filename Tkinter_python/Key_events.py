from tkinter import *

window = Tk()

def do_something(event):
    # print("yes you did it!")
    # print(f"you pressed key: {event.keysym}") # here what have you pressent displays that key
    # keysym means the name/symbol of the keyboard key pressed.
    label.config(text=event.keysym) # shows in labels

#  All keyboard events 
window.bind("<Key>",do_something)  # Here .bind() = “attach/connect an event to a function”.
label = Label(window,font=("cascadia code",99))
label.pack()
window.mainloop()