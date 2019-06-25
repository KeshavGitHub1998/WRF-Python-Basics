#taking out the variables
from __future__ import print_function

#tkinter use
from tkinter import *
ObjTkinter=Tk()
ObjTkinter.title("Getting the variables in raw form")
ObjTkinter.geometry("1000x1000+30+10")

#defining open variable
def OpenVariable():
	ncfile = Dataset("wrfout_d01_2019-01-26_12_00_00")
	# Get the variable here
	b=input("enter the value again in double quoted form")
	t = getvar(ncfile, b)
	print(t)
	s=t.get()
	print(s)
	lab2=Label(text=s).pack()
	return("")

from netCDF4 import Dataset
from wrf import getvar


#tkinter label
lab1=Label(text="Enter the variable of your choice").pack(anchor=W)



#tkinter entry
t=StringVar()
text=Entry(textvariable=t).pack()


#tkinter button
but1=Button(text="Submit Variable",font=20,command=OpenVariable).pack(anchor=W)


print(t)
#tkinter mainloop
ObjTkinter.mainloop()
