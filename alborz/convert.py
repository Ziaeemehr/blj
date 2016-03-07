#!/usr/bin/python
# a script to conver posout.acf from alborz random structure generator
# to poscur.ascii to be used in Max code
nat = 30
t1 = -8.024828007029274E+00
t2 = -8.024828007029274E+00
t3 = -2.1836668E+02
t4 = -2.1836668E+02
t5 = 2.4233630E+01
ifile = open("posout.acf","r")
ofile  = open ("poscur.ascii","w")
ofile.write("%d %22.15e %22.15e      energy(eV)= %15.8e enthalpy(eV)=  %15.8e  ucvol(ang3)=  %15.8e \n" % (nat,t1,t2,t3,t4,t5))
line = ifile.readline()
line = ifile.readline()
line = ifile.readline()
line = ifile.readline()
line = ifile.readline()
line = ifile.readline()
line = ifile.readline()
line = ifile.readline()
for i in range (0,2):
    line = ifile.readline().split()
    d1 = float(line[0]); 
    d2 = float(line[1]);
    d3 = float (line[2]);
    ofile.write('%22.15e %22.15e %22.15e \n' % (d1,d2,d3))

for line in range(nat):
    cont = ifile.readline().split()
    #print cont
    lable = cont[0]; 
    x = float(cont[1]); 
    y = float(cont[2]); 
    z = float(cont[3]);
    ofile.write('%22.15e %22.15e %22.15e %s \n' % (x,y,z,lable))

ifile.close(); ofile.close()

#  30    -8.024828007029274E+00    -8.024828007029274E+00          energy(eV)= -2.1836668E+02 enthalpy(eV)= -2.1836668E+02 ucvol(ang3)=  2.4233630E+01

