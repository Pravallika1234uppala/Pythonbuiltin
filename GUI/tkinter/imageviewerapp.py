from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("ImageBuilder")
root.iconbitmap("Images/icon.jpg")

my_img1 = ImageTk.PhotoImage(Image.open("images/profile.png"))
my_img2 = ImageTk.PhotoImage(Image.open("images/image1.png"))
my_img3 = ImageTk.PhotoImage(Image.open("images/image2.png"))
my_img4 = ImageTk.PhotoImage(Image.open("images/image3.png"))
my_img5 = ImageTk.PhotoImage(Image.open("images/image4.png"))
my_img6 = ImageTk.PhotoImage(Image.open("images/image5.png"))


#To scroll through images:
images_list = [my_img1, my_img2, my_img3, my_img4, my_img5, my_img6]



my_label = Label(root, image=images_list[0])
my_label.grid(row=0, column=0, columnspan=3)

def forward(image_num):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(root, image=images_list[image_num-1])
    button_forward = Button(root, text=">>", command=lambda: forward(image_num+1))
    button_back = Button(root, text="<<", command=lambda: backward(image_num-1))
    if image_num == 6:
        button_forward = Button(root, text=">>", state=DISABLED)
    
    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)


def backward(image_num):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(root, image=images_list[image_num-1])
    button_forward = Button(root, text=">>", command=lambda: forward(image_num+1))
    button_back = Button(root, text="<<", command=lambda: backward(image_num-1))
    if image_num == 1:
        button_back = Button(root, text="<<", state=DISABLED)
    
    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)

#Buttons:
button_back = Button(root, text="<<", command=backward, state=DISABLED)
button_exit = Button(root, text="EXIT", command=root.quit)
button_forward = Button(root, text=">>", command=lambda: forward(2))

button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2)

root.mainloop()