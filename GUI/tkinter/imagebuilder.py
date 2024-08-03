from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Profile")
root.iconbitmap("images/icon.jpg")

my_img = ImageTk.PhotoImage(Image.open("images/profile.png"))
my_label = Label(root, image=my_img)
my_label.grid(row=5, column=10, columnspan=10)

button_quit = Button(root, text="Exit", command=root.quit).grid(row=20, column=13, columnspan=5)
root.mainloop()