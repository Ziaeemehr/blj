#!/usr/bin/python
from io import StringIO
import numpy as np

ifile = open("report.txt","r")
data = np.genfromtxt(ifile, usecols = (1,4))
a = data[:][0]
print a
#a=[]; b=[]
#for i in range(500):
#    a[i] = a.append(float(data[i][0]))
#    b[i] = b.append(int(data[i][1]))
#    #print a,b
#
#print a
#min_a = min(a)
#print  min_a
#ind = np.argmin(a)
#print ind




