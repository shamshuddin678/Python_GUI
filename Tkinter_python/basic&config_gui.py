from tkinter import *

shamshu = Tk()
shamshu.geometry("400x400") # Tkinter internally reads it "width x height". otherwise not in quotes 400*400(multiply it)
shamshu.title("label vs config function")

label = Label(shamshu,text="hlo shamshu",font=("cascadia code",30,'bold'),fg="orange")
label.pack()

# “configure/change settings”
label.config(text="i have change the text",fg="purple")



shamshu.mainloop()