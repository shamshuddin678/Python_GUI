from tkinter import *

win = Tk()

# function for command = submit
def submit():
    print("you have clicked the ")
    print(listbox.get(listbox.curselection()))

# function for command = add

def add():
    listbox.insert(listbox.size(),entryBox.get())
    listbox.config(height= listbox.size())



# listbox
listbox = Listbox(win,font=("cascadia code", 28,'bold'),fg="green",bg="pink")

# way 1 inserting the elements
listbox.insert(1, "BMW")
listbox.insert(2, "FERRARI")
listbox.insert(3, "PORRSCHE")
listbox.insert(4, "FORMULA F1")

'''way 2 inserting the elements
cars = ['BMW','FERRARI','PORSHE','FORMULA F1'] 
listbox.config(END,*cars)

-> here stroing the elements in tuple_or_list
-> congif() means it will replace it .(means update it)
-> END means it appends at last
'''

listbox.config(height=listbox.size())
listbox.pack()

submitbutton = Button(win,text="Submit",command=submit).pack()


entryBox = Entry(win)
entryBox.pack()

addbutton = Button(win,text="add",command=add)
addbutton.pack()

win.mainloop()