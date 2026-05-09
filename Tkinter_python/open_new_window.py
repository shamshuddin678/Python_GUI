from tkinter import *

window = Tk()

def create_window():
    # new_window = Tk() here if we use this the main window will be closes and new window(sub window) not closes
    # new_window = Toplevel() # here if we use it if we closes main window it automatically closes the new window(sub window) also
    new_window = Tk()
    window.destroy() # it destroys the old window which we have creted the first.


Button(window,text="create new window",font=("cascadia code",25,'bold'),fg="brown",command=create_window).pack()

window.mainloop()