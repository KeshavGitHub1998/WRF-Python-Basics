#done
from __future__ import print_function

from netCDF4 import Dataset
from wrf import getvar
from wrf import *

ncfile = Dataset("wrfout_d01_2019-01-26_12_00_00")

b=input("enter the variable")
c=input("enter the same variable again, in the double quotes")
# Get the Sea Level Pressure
b = getvar(ncfile, c)

print(b)
