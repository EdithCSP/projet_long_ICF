#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# MODULES
import re


fa_file = open("../../fwdfastafiles/Galaxy25-[FASTA_hypo_Zbtb24mut_genes].fasta", "r")
liste_fa = fa_file.readlines()
filout =  open("../results/test.fasta", "w")

new_seq = '>'
flag = False
for line in liste_fa:
	if re.search(new_seq, line):
		flag = True
		#filout.write(line)
		print(line)
		li = ""
	elif(flag == True):
		line = line.replace("\n","")
		#filout.write(line)
		li = li + line
	print(li)
	
	filout.write("\n")
filout.close()
fa_file.close()
    
if __name__ == '__main__': 
