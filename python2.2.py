#!/usr/bin/env python3 #call python environment automatically
import sys

# run chmod +x python2.2.py on command line to shortcut python 
#run ./python2.2.py inputnumber to run

x = sys.argv[1] # get first command line parameter


y=float(x)	#convert any input to float

if y > 0:
	message = 'postive'
	print (message)
elif y < 0:
	message = 'negative'
	print(message)
else:
	message = 'input was 0'
	print(message)


