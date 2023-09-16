from tkinter import*
import tkinter
top=tkinter.Tk()
B1=tkinter.Button(top,text="relief Style:Flat",relief=FLAT)
B2=tkinter.Button(top,text="relief style:Raised",relief=RAISED)
B3=tkinter.Button(top,text="Relief style:Sunken",relief=SUNKEN)
B4=tkinter.Button(top,text="Relief style:Groove",relief=GROOVE)
B5=tkinter.Button(top,text="Relief style:Riding",relief=RIDGE)
B1.pack()
B2.pack()
B4.pack()
B5.pack()
top.mainloop()