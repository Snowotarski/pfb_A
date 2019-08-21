#!/usr/bin/env python3 #call python environment automatically
import sys

#run chmod +x python2.2.py on command line to shortcut python 
#run ./python2.2.py inputnumber to run

x = sys.argv[1] # get first command line parameter


y=float(x)	#convert any input to float

if y < 0:
	message = ' is a negative number'
	print (message)
elif y == 0:
	message = ' is zero'
	print(y,message)
elif y > 50:
	message = ' is greater than 50'
	print (y, message)
elif y < 50:
	message= ' is less than 50'
	print (y, message)
else:
	message = ' is 50'
	print(y, message)


