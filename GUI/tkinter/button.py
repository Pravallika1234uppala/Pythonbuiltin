from tkinter import *

root = Tk()

#Input from user
e = Entry(root, width=20, fg="white", bg="grey", borderwidth=7)
e.insert(0, "Enter your name:")
e.pack()

#printing 
def printname():
    myLabel = Label(root, text="Hello "+e.get()).pack()

#button
myButton = Button(root, text="Submit", padx=25, pady=15, command=printname).pack()

root.mainloop()