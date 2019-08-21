#!/usr/bin/env python3 #call python environment automatically
import sys

# run chmod +x python2.2.py on command line to shortcut python 
#run ./python2.2.py inputnumber to run

x = sys.argv[1] # get first command line parameter

y=float(x) 
if y > 0 :
	message = 'postive'
	print (message)
else :
	message = 'negative'
	print(message)

