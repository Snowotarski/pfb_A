#!/usr/bin/env python3 #call python environment automatically
  

#run chmod +x python3.14.py on command line to shortcut python
#run ./python3.14.py to run

#write script to find starting BP site of an EcoRI site

ecoRI_F = 'GAATTC'
ecoRI_R = 'CTTAAG'

dna = 'GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTCTAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACGCTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCCTCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAATGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATTCGCCAGAGGCTGCTCCCCCCGTGGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCTGTCATCTTCTGTCCCTTCCCAGAAAACCTACCAGGGCAGCTACGGTTTCCGTCTGGGCTTCTTGCATTCTGGGACAGCCAAGTCTGTGACTTGCACGTACTCCCCTGCCCTCAACAAGATGTTTTGCCAACTGGCCAAGACCTGCCCTGTGCAGCTGTGGGTTGATTCCACACCCCCGCCCGGCACCCGCGTCCGCGCCATGGCCATCTACAAGCAGTCACAGCACATGACGGAGGTTGTGAGGCGCTGCCCCCACCATGAGCGCTGCTCAGATAGCGATGGTCTGGCCCCTCCTCAGCATCTTATCCGAGTGGAAGGAAATTTGCGTGTGGAGTATTTGGATGACAGAAACACTTTTCG'


#find ecoRI_F in dna
locate1= dna.find(ecoRI_F)
index_fix1 = locate1-1

#find ecoRI_R in dna
locate2 = dna.find(ecoRI_R)
index_fix2 = locate2-1

#LOOK FOR FORWARD ECORI SEQ
if locate1 == - 1:
	print ('EcoRI site in 5 to 3 orientation is NOT present in the sequence')
else:
	print('EcoRI site in 5 to 3 orientation starts at nucleotide position: ', index_fix1)  
	print ('The end position of the EcoRI site is:', index_fix1-len(ecoRI_F))

#LOOK FOR REVERSE ECORI SEQ
if locate2 == -1:
	print('EcoRI site in 3-5 orientation is not present in this sequence.')
else:
	print ('EcoRI site in 3-5 orientation starts at nucleotide postion: ', index_fix2)
	print ('The end position of the EcoRI site is:', index_fix2-len(ecoRI_F))