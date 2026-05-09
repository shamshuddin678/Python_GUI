from tkinter import *

root = Tk()
Label(root,text="Hello shamshuddin",font=("cascadia code",24),bg="orange",).pack()

a = IntVar()
b = IntVar()
# radiobutton
Radiobutton(root,text="BMW",variable = a,value="BMW").pack()

# checkbutton
Checkbutton(root,text="BMW",variable = a).pack()

root.mainloop()
