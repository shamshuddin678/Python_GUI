from tkinter import *
from tkinter import ttk # ttk means Tk Themed Widgets

window = Tk()
window.geometry("400x400")
'''
| ttk Widget        | Purpose         |
| ----------------- | --------------- |
| `ttk.Button`      | modern button   |
| `ttk.Label`       | styled label    |
| `ttk.Entry`       | modern entry    |
| `ttk.Combobox`    | dropdown box    |
| `ttk.Progressbar` | loading bar     |
| `ttk.Treeview`    | table/data view |
| `ttk.Notebook`    | tabs            |
'''

# Notebook is a container widget that holds all tjhe multiple pages.each page = 1 tab
notebook = ttk.Notebook(window)
tab1  = Frame(notebook) # new frame for tab1
tab2  = Frame(notebook) # new frame for tab2

notebook.add(tab1,text="TAB1")
notebook.add(tab2,text="TAB2")
notebook.pack()

Label(tab1,text="Here is tab1 & hearty welcome to my first tab1",width=50,height=27,fg="green").pack()
Label(tab2,text="Here is tab2 & hearty welcome to my first tab2",width=50,height=27,fg="blue").pack()

window.mainloop()