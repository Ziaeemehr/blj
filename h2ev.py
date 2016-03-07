#!/usr/bin/python
# script to convert hartree to ev
hartree2ev = 27.2114
infile = open("earr.dat",'r')
line = infile.readline().split()
print "%d minimum out of %d has been found" % (int(line[0]),int(line[1]))
line = infile.readline()
line = infile.readline().split()
h = float(line[1])
spg =  int(line[4])
nfile = open("poscur.ascii",'r')
nline = nfile.readline().split()
N = int (nline[0])
print "Energy in hartree is           %25.14e " % h
print "The number of atoms is            %d " % N
print "The energy in ev per atom is:     ", h * hartree2ev / N
print "Space group number is             %d " % spg
