#!/usr/bin/env python3 #call python environment automatically
  

#run chmod +x python4.2.py on command line to shortcut python
#run ./python4.2.py to run


taxa = 'sapiens, erectus, neaderthalensis'

print('taxa: ', taxa)
print('taxa[1]: ', taxa[1])
print('type(taxa): ', type(taxa))

species = taxa.split(', ')
print('species: ', species)

print('species 1: ',species[1])
print('species type: ', type(species))

print('Sorted species: ',sorted(species, key = len))
