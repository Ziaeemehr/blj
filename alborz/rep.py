#!/usr/bin/python
from io import StringIO
import numpy as np

def h2ev(h):
    hartree2ev = 27.2114
    return h * hartree2ev / N

N = 30
ifile = open("report.txt","r")
ofile = open("repinev","w")
# s = StringIO ("report.txt") 
data = np.genfromtxt(ifile, usecols = (1,4))
for i in range(500):
    #a = h2ev(float(data[i][0]))
    a = float(data[i][0])
    b = int(data[i][1])
    print a,b
    ofile.write("%25.15e %d " %(a,b ))
minvalev = np.amin(a)
ind = np.argmin(a)
print ind
#minvalh  = minvalev * N / 27.2114 
minvalh =1.
print "The min energy is %25.15e ev and  %25.15e hartree" % (minvalev,minvalh)




