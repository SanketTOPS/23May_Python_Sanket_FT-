import tkinter
from tkinter import ttk

window=tkinter.Tk()

window.title("FirstApp")
window.geometry("500x600")
window.config(bg='gold')

#tkinter.Label(text="Firstname:",bg='gold',fg='red',font='Calibri 15 bold').pack()
#tkinter.Label(text="Lastname:",bg='gold',fg='red',font='Calibri 15 bold').pack()

#tkinter.Label(text="Firstname:",bg='gold',fg='red',font='Calibri 15 bold').place(x=0,y=0)
#tkinter.Label(text="Lastname:",bg='gold',fg='red',font='Calibri 15 bold').place(x=0,y=30)

tkinter.Label(text="Firstname:",bg='gold',fg='red',font='Calibri 15 bold').grid(row=0,column=0,sticky='W')
tkinter.Label(text="Lastname:",bg='gold',fg='red',font='Calibri 15 bold').grid(row=1,column=0,sticky='W')

tkinter.Entry().grid(row=0,column=1)
tkinter.Entry().grid(row=1,column=1)

tkinter.Radiobutton(value=0,text="Male",bg='gold',fg='red',font='Calibri 15 bold').grid(row=2,column=0,sticky='W')
tkinter.Radiobutton(value=1,text="Female",bg='gold',fg='red',font='Calibri 15 bold').grid(row=2,column=1,sticky='W')

tkinter.Checkbutton(text='Python',bg='gold',fg='red',font='Calibri 15 bold').grid(row=3,column=0,sticky='W')
tkinter.Checkbutton(text='Android',bg='gold',fg='red',font='Calibri 15 bold').grid(row=4,column=0,sticky='W')
tkinter.Checkbutton(text='PHP',bg='gold',fg='red',font='Calibri 15 bold').grid(row=5,column=0,sticky='W')
tkinter.Checkbutton(text='iOS',bg='gold',fg='red',font='Calibri 15 bold').grid(row=6,column=0,sticky='W')

city=["Ahmedabad","Rajkot","Surat","Baroda","Navsari","Bhavnagar"]

ttk.Combobox(values=city).grid(row=7,column=0,sticky='W')

tkinter.Button(text="Submit",fg='red',font='Calibri 15 bold').place(x=210,y=300)

tkinter.mainloop()