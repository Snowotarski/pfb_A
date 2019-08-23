#!/usr/bin/env python3 #call python environment automatically
  

#run chmod +x python4.5.py on command line to shortcut python
#run ./python4.5.py to run script


# script using while loop to calculate factorial 1000.

i = 1
factorial =1 
while i < 1001:
  factorial = factorial * i
  i+=1
print('The factorial of 1000 is {}'.format(factorial))
