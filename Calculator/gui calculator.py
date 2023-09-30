from tkinter import *
root=Tk()
root.geometry('270x150')
root.iconbitmap(r'C:\Users\easa\Downloads\parmacy project in python\Calculator_30001 (1).ico')
root.title("gui calculator")
expression=""

def press(num):
 global expression
 expression = expression+str(num)
 equation.set(expression)

def equalpress():
    global expression
    total=str(eval(expression))
    equation.set(total)

def clear():
    global expression
    expression=""
    equation.set("")
    
    

equation=StringVar()
enter=Entry(root,textvariable=equation,bg="#E2FBFA",fg="black")
enter.grid(columnspan=4,ipadx=70)
button1=Button(root,text="1",command=lambda:press(1),bg="black",fg="#E2FBFA", height=1, width=7)
button1.grid(row=2,column=0)

button2=Button(root,text="2",command=lambda:press(2),bg="black",fg="#E2FBFA", height=1, width=7)
button2.grid(row=2,column=1)

button3=Button(root,text="3",command=lambda:press(3),bg="black",fg="#E2FBFA", height=1, width=7)
button3.grid(row=2,column=2)

button4=Button(root,text="4",command=lambda:press(4),bg="black",fg="#E2FBFA", height=1, width=7)
button4.grid(row=3,column=0)

button5=Button(root,text="5",command=lambda:press(5),bg="black",fg="#E2FBFA", height=1, width=7)
button5.grid(row=3,column=1)

button6=Button(root,text="6",command=lambda:press(6),bg="black",fg="#E2FBFA", height=1, width=7)
button6.grid(row=3,column=2)

button7=Button(root,text="7",command=lambda:press(7),bg="black",fg="#E2FBFA", height=1, width=7)
button7.grid(row=4,column=0)

button8=Button(root,text="8",command=lambda:press(8),bg="black",fg="#E2FBFA", height=1, width=7)
button8.grid(row=4,column=1)

button9=Button(root,text="9",command=lambda:press(9),bg="black",fg="#E2FBFA", height=1, width=7)
button9.grid(row=4,column=2)

button0=Button(root,text="0",command=lambda:press(0),bg="black",fg="#E2FBFA", height=1, width=7)
button0.grid(row=5,column=0)

plus=Button(root,text="+",command=lambda:press("+"),bg="black",fg="#E2FBFA", height=1, width=7)
plus.grid(row=2,column=3)

minus=Button(root,text="-",command=lambda:press("-"),bg="black",fg="#E2FBFA", height=1, width=7)
minus.grid(row=3,column=3)

mul=Button(root,text="*",command=lambda:press("*"),bg="black",fg="#E2FBFA", height=1, width=7)
mul.grid(row=4,column=3)

divide=Button(root,text="/",command=lambda:press("/"),bg="black",fg="#E2FBFA", height=1, width=7)
divide.grid(row=5,column=1)

equal=Button(root,text="=",command=equalpress,bg="black",fg="#E2FBFA", height=1, width=7)
equal.grid(row=5,column=2)

divide=Button(root,text="%",command=lambda:press("%"),bg="black",fg="#E2FBFA", height=1, width=7)
divide.grid(row=5,column=3)

clear=Button(root,text="clear",command=clear,bg="black",fg="#E2FBFA", height=1, width=7)
clear.grid(row=6,column=3)





root.mainloop()
