from tkinter import *

root = Tk()
root.title("Simple Calculator")
root.configure(bg='grey')

e = Entry(root, width=38, fg="white", bg="grey", borderwidth=6)
e.grid(row=0, column=0, rowspan=3, columnspan=3, padx=10, pady=10)


#function-for button action
def button_num(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current)+str(number))

def button_c():
    e.delete(0, END)
    
def button_addition():
    first_number = e.get()
    global fnum
    global match
    match = "add"
    fnum = int(first_number)
    e.delete(0, END)

def button_subtraction():
    first_number = e.get()
    global fnum
    global match
    match = "sub"
    fnum = int(first_number)
    e.delete(0, END)

def button_multi():
    first_number = e.get()
    global fnum
    global match
    match = "mul"
    fnum = int(first_number)
    e.delete(0, END)

def button_division():
    first_number = e.get()
    global fnum
    global match
    match = "div"
    fnum = int(first_number)
    e.delete(0, END)

def button_eq():
    second_number = e.get() #Current
    e.delete(0, END)
    if match == "add":
        e.insert(0, fnum+int(second_number))

    elif match == "sub":
        e.insert(0, fnum-int(second_number))
    elif match == "mul":
        e.insert(0, fnum*int(second_number))
    elif match == "div":
        e.insert(0, fnum/int(second_number))


#buttons:numbers
button_1 = Button(root, text="1", padx=40, pady=10, command=lambda: button_num(1))
button_2 = Button(root, text="2", padx=40, pady=10, command=lambda: button_num(2))
button_3 = Button(root, text="3", padx=40, pady=10, command=lambda: button_num(3))
button_4 = Button(root, text="4", padx=40, pady=10, command=lambda: button_num(4))
button_5 = Button(root, text="5", padx=40, pady=10, command=lambda: button_num(5))
button_6 = Button(root, text="6", padx=40, pady=10, command=lambda: button_num(6))
button_7 = Button(root, text="7", padx=40, pady=10, command=lambda: button_num(7))
button_8 = Button(root, text="8", padx=40, pady=10, command=lambda: button_num(8))
button_9 = Button(root, text="9", padx=40, pady=10, command=lambda: button_num(9))
button_0 = Button(root, text="0", padx=40, pady=10, command=lambda: button_num(0))

#buttonS:operators
button_equal = Button(root, text="=", padx=103, pady=10, command=button_eq)
button_add = Button(root, text="+", padx=40, pady=10, command=button_addition)
button_clear = Button(root, text="C", padx=103, pady=10, command=button_c)
button_sub = Button(root, text="-", padx=40, pady=10, command=button_subtraction)
button_mul = Button(root, text="*", padx=40, pady=10, command=button_multi)
button_div = Button(root, text="/", padx=40, pady=10, command=button_division)

#Arranging buttons:
button_7.grid(row=3,column=0)
button_8.grid(row=3,column=1)
button_9.grid(row=3,column=2)

button_4.grid(row=4,column=0)
button_5.grid(row=4,column=1)
button_6.grid(row=4,column=2)

button_1.grid(row=5,column=0)
button_2.grid(row=5,column=1)
button_3.grid(row=5,column=2)

button_0.grid(row=6,column=0)

button_equal.grid(row=7,column=1,columnspan=2)
button_add.grid(row=7,column=0)
button_clear.grid(row=6,column=1,columnspan=2)
button_sub.grid(row=8,column=0)
button_mul.grid(row=8,column=1)
button_div.grid(row=8,column=2)

root.mainloop()