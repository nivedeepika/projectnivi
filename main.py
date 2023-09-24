from tkinter import *
from PIL import ImageTk, Image

root = Tk()
my_img1 = ImageTk.PhotoImage(Image.open("deepi.jpg"))
my_img2 = ImageTk.PhotoImage(Image.open("bfvbdfnvlkfn.jpg"))
my_img3 = ImageTk.PhotoImage(Image.open("titanic.jpg"))
my_img4 = ImageTk.PhotoImage(Image.open("nivi photo.jpg"))
my_list = [my_img1, my_img2, my_img3, my_img4]

my_l = Label(image=my_img1)
my_l.grid(row=0, column=0, columnspan=3)
def forwrd(image_number):
    global my_l
    global button_f
    global button_b

    my_l.grid_forget()
    my_l = Label(image= my_list[image_number-1])
    button_f= Button(root,text=">>", command= lambda: forwrd(image_number+1))
    button_b = Button(root, text="<<", command=lambda: back(image_number-1))
    my_l.grid(row=0, column=0, columnspan=3)
    button_b.grid(row=1, column=0)
    button_f.grid(row=1,column=2)

    if image_number == 4:
        button_f = Button(root, text=">>", state=DISABLED)
def back(image_number):
    global my_l
    global button_f
    global button_b

    my_l.grid_forget()
    my_l = Label(image=my_list[image_number - 1])
    button_f = Button(root, text=">>", command=lambda: forwrd(image_number + 1))
    button_b = Button(root, text="<<", command=lambda: back(image_number - 1))
    my_l.grid(row=0, column=0, columnspan=3)
    button_b.grid(row=1, column=0)
    button_f.grid(row=1, column=2)
    if image_number == 0:
        button_f = Button(root, text="<<", state=DISABLED)


button_b = Button(root, text="<<",command=lambda: back(), state=DISABLED)
button_e = Button(root, text="exit", command=root.quit)
button_f = Button(root, text=">>", command=lambda: forwrd(2))
button_b.grid(row=1, column=0)
button_e.grid(row=1, column=1)
button_f.grid(row=1, column=2)


root.mainloop()
