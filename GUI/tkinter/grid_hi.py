from tkinter import *

root = Tk()

myLabel1 = Label(root, text="Hi, Prava!")
myLabel2 = Label(root, text="Actively looking for jobs")

myLabel1.grid(row=0, column=0)
myLabel2.grid(row=3, column=0)

root.mainloop()