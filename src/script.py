#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# MODULES
import re


fa_file = open("/home/cspe/M2_BI/Projet_long/fwdfastafiles/Galaxy25-[FASTA_hypo_Zbtb24mut_genes].fasta", "r")
liste_fa = fa_file.readlines()
filout =  open("/home/cspe/M2_BI/Projet_long/fwdfastafiles/test.fasta", "w")

new_seq = '>'
flag = False
for line in liste_fa:
    if re.search(new_seq, line):
        flag = True
        filout.write(line)
    elif(flag == True):
        line = line.replace("\n","")
        filout.write(line)
    filout.write("\n")
filout.close()
fa_file.close()
    
if __name__ == '__main__': 
