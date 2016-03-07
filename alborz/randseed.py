#!/usr/bin/python
# a script to give random seed integers to input.ini file
# in order to creat random posout.acf file.
# script seek for "seed in input.ini" and replace integer after '=' 
# with a random integer. 
from random import randint

randseed = randint(0,1000000)
f = open('input.ini','r')
lines = f.readlines()
f.close()
f = open('input.ini','w')
for line in lines:
     if "seed" in line:
     # You need to include a newline if you're replacing the whole line
         line = "seed = " + str(randseed)+'\n'
     f.write(line)
f.close()
