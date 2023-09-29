from tkinter import *
root=Tk()
root.title("log in system")
root.geometry('400x400')
root.configure(bg="#6B58A7")

namevar=StringVar()
namel=Label(root,text="Enter Your Name",fg="blue",anchor="center")
namel.grid(row=0,column=0)
txt = Entry(root,textvariable=namevar, width=20,fg="blue",bg="#00FFFF",anchor="CENTER")
txt.grid(column =0, row =1)

emailvar=StringVar()
namel=Label(root,text="Enter Your emailid",fg="blue",anchor="CENTER")
namel.grid(row=2,column=0)
txt = Entry(root, width=20,fg="blue",bg="#00FFFF",textvariable=emailvar,anchor="CENTER")
txt.grid(column =0, row =3)

agevar=IntVar()
namel=Label(root,text="Enter Your age",fg="blue",anchor="CENTER")
namel.grid(row=4,column=0)
txt = Entry(root, width=20,textvariable=agevar,fg="blue",bg="#00FFFF",anchor="CENTER")
txt.grid(column =0, row =5)

phonevar=IntVar()
namel=Label(root,text="Enter Your phone number",fg="blue",anchor="CENTER")
namel.grid(row=6,column=0)
txt = Entry(root,textvariable=phonevar, width=20,fg="blue",bg="#00FFFF",anchor="CENTER")
txt.grid(column =0, row =7)


namel=Label(root,text="Enter Your Qualification",fg="blue",anchor="CENTER")
namel.grid(row=8,column=0)

options=["BE/BTech","BSc","MBBS","BA","BCom","Diplomo","Mtech/ME","Msc","BA","Phd"]
clicked=StringVar()
clicked.set("select an option")
question_menu = OptionMenu(root, clicked, *options,anchor="CENTER")
question_menu.grid(row=9,column=0)
  







