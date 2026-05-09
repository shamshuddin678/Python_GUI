from tkinter import *

window = Tk()
window.geometry("400x400")

def click(event):
    print("yes ! you right clicked ")

'''
| Event               | Meaning             |
| ------------------- | ------------------- |
| `<Button-1>`        | left click          |
| `<Button-3>`        | right click         |
| `<Double-Button-1>` | double click        |
| `<Key>`             | keyboard press      |
| `<Enter>`           | mouse enters widget |
| `<Leave>`           | mouse leaves widget |

'''

window.bind("<Button-3>",click)

window.mainloop()