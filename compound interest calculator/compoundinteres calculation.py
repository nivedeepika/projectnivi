from tkinter import *
root=Tk()
root.geometry('400x400')
root.title="COMPOUND INTEREST CALCULATOR"
root.configure(bg="blue")

#this is a label

principal=Label(root,text="Principal Amount",fg="blue")
principal.grid(row=0,column=0,padx=10,pady=10)


rate=Label(root,text="Rate of Interest",fg="blue")
rate.grid(row=3,column=0,padx=10,pady=10)

years=Label(root,text="Years",fg="blue")
years.grid(row=5,column=0,padx=10,pady=10)

compoundla=Label(root,text="Compound Interest",fg="blue")
compoundla.grid(row=9,column=0,padx=10,pady=10)


def calc():
    rin=int(principalentry.get())
    rate=float(rateentry.get())
    year=int(yearsentry.get())
    cal=rin*pow(1+rate/100,year)
    compoundfield.insert(0,cal)

def clear():
    principalentry.delete(0,END)

    rateentry.delete(0,END)

    yearsentry.delete(0,END)

    compoundfield.delete(0,END)

    
    
submitl=Button(root,text="Submit",command=calc,fg="blue")
submitl.grid(row=7,column=1,padx=10,pady=10)

clearall=Button(root,text="Clear all",command=clear,fg="blue")
clearall.grid(row=11,column=1,padx=10,pady=10)

principalentry=Entry(root)
rateentry=Entry(root)
yearsentry=Entry(root)
compoundfield=Entry(root)

principalentry.grid(row=0,column=1)

rateentry.grid(row=3,column=1)

yearsentry.grid(row=5,column=1)

compoundfield.grid(row=9,column=1)

root.mainloop()
