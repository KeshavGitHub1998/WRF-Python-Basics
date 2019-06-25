#program to see the data related to the variables
from __future__ import print_function

from netCDF4 import Dataset
from wrf import getvar
from wrf import *
from tkinter import *

#basic tkinter
obj=Tk()
obj.title("Raw Data")
obj.geometry("700x700+100+10")

def OpenRawData():
	ncfile = Dataset("wrfout_d01_2019-01-26_12_00_00")
	d=a.get()
	e=b.get()
	d = getvar(ncfile, e)
	lab3=Label(text=d,font=20).pack()
	print(d)
	return("")
	

#creating the 2 entries
a=StringVar()
b=StringVar()

#creating the label
lab1=Label(text="enter the short form of the variable",font=('times',10,'bold')).pack(anchor=W)
text=Entry(textvariable=a).pack(anchor=W)

lab2=Label(text="enter the previous text again",font=('times',10,'bold')).pack(anchor=W)
text=Entry(textvariable=b).pack(anchor=W)

but1=Button(text="Submit",font=('times',10,'bold'),padx=40,bg='pink',fg='black',command=OpenRawData).pack(anchor=W)


obj.mainloop()
