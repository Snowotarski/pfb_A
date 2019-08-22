#!/usr/bin/env python3 #call python environment automatically
  

#run chmod +x python3.13.py on command line to shortcut python
#run ./python3.13.py to run

# write a script that prints out the reverse complement of a DNA string

dna ='ATGCAGGGGAAACATGATTCAGGAC'

dna = dna.lower() #make all lowercase
dna_comp = dna.replace('a', 'T').replace('c','G').replace('g', 'C').replace('t','A')
print(dna_comp[::-1])
