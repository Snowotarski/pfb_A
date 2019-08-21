#!/usr/bin/env python3 #call python environment automatically
import sys

x = sys.argv[1] # get first command line parameter

if bool(x) == 1:
        print ('true')
else:
        print('false')
