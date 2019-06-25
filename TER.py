#taking out the variables
from __future__ import print_function
from wrf import pw
from netCDF4 import Dataset
from wrf import getvar

def OpenVariable():
	ncfile = Dataset("wrfout_d01_2019-01-26_12_00_00")
	g=input("enter a variable")
	# Get the model terrain height
	g = getvar(ncfile, g)
	print(g)
	return("")

OpenVariable()

