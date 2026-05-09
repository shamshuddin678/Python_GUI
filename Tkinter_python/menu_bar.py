from tkinter import *

win = Tk()
win.geometry("500x400")

def open_file():
    print("file is opened")

def save_file():
    print("file is saved")

def exit_app():
    print("file is exit")
    win.destroy()

# menubarr creation
menuBar = Menu(win)

win.config(menu=menuBar)

# file menu
filemenu = Menu(
    menuBar,
    tearoff=0,
    font=("MV Boli", 17, 'bold'),
    fg='red'
)

menuBar.add_cascade(
    label='File',
    menu=filemenu
)

filemenu.add_command(label='Open', command=open_file)
filemenu.add_command(label='Save', command=save_file)
filemenu.add_separator()
filemenu.add_command(label='Exit', command=exit_app)

# edit menu
editmenu = Menu(
    menuBar,
    tearoff=0,
    font=("MV Boli", 17, 'bold'),
    fg='red'
)

menuBar.add_cascade(
    label='Edit',
    menu=editmenu
)

editmenu.add_command(label='Undo')
editmenu.add_command(label='Redo')
editmenu.add_separator()
editmenu.add_command(label='Cut')
editmenu.add_command(label='Copy')
editmenu.add_command(label='Select All')

win.mainloop()