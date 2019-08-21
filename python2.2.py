#!/usr/bin/env python3 #call python environment automatically
import sys

#run chmod +x python2.2.py on command line to shortcut python 
#run ./python2.2.py inputnumber to run

x = sys.argv[1] # get first command line parameter


y=float(x)	#convert any input to float

if y < 0:
	message = ' is a negative number'
	condition1 = 0
	condition3 = 0
	print (message)
elif y == 0:
	message = ' is zero'
	condition1 = 0
	condition3 = 0
	print(y,message)
elif y > 50:
	message = ' is greater than 50'
	condition1 = 0
	condition3 = 0
	print (y, message)
elif y < 50:
	message2 = ' is less than 50'
	condition1 = 1
	condition3 = 0
else:
	message = ' is 50'
	condition1 = 0
	condition3 = 1
	print(y, message)

#check even or odd by using modulus and boolean 

state = bool(y%2)

if state == 0:
	condition2 = 1
else:
	print (y, 'is an odd number')

#print out message if it is an even number less than 50

if condition1 + condition2 == 2:
	print(y, ' is less than 50 and is even')
elif condition2 + condition3 == 2:
	print (y, ' is 50 and also is an even number')
else:
	print(y, ' is not 50 or an even number less than 50')

