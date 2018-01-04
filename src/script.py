#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# MODULES
import re
import os

def create_dico_seq_concate_with_fasta(fasta_file):
	'''
		Cette fonction permet de créer un dictionnaire à partir d'un fichier fasta 
		avec en clé le nom de la sequences et en valeur la séquence concaténées.
		INPUT: 
		- fasta_file : fichier fasta
		OUTPUT: 
		- un dictionnaire avec en clé le nom de la sequences et en valeur la séquence concaténées.
	'''
	fa_file = open(fasta_file, "r")
	liste_fa = fa_file.readlines()
	fa_file.close()
	dico_name_seq = {}
	new_seq = '>'
	flag = False
	for line in liste_fa:
		if re.search(new_seq, line):
			flag = True
			name = line.replace("\n","")
			name = name.replace(">","")
			li = ""
			dico_name_seq[name] = li
		elif(flag == True):
			line = line.replace("\n","")
			li = li + line
			dico_name_seq[name] = li
	return dico_name_seq	


def write_dico_fasta_format(dico, output_file):
	'''
		Cette fonction permet d'ecrire un dictionnaire au format fasta.
		INPUT : 
		- dico : dictionnaire
		- output_file : nom fichier sortie 
		OUTPUT : 	
		- fichier format fasta
	'''
	filout = open(output_file, "w")
	for key, val in dico.items():
		#print key, val
		filout.write(">{}\n".format(key))
		filout.write("{}\n".format(val))
	filout.close()


def parse_fasta_for_meme(dico):
	'''
		Cett fonction permet de découpé un fichier fasta puisque en plusieurs 
		fichier fasta qui seront les entrée de MEME. la taille de la base de données
		de séquence fournit à meme est limiter à 100000 caractère.
		INPUT:
			- dico : dictionnaire contenant en clé le nom de la séquence et en valeur 
			la séquence.
		OUTPUT:
			- fichier fasta de 100000 caractère dans ../results/meme_input. 
	'''
	os.system("mkdir ../results/meme_input")
	compt = 0
	i = 1
	for key, val in dico.items():
		#print(key, val)
		if(compt == 0):
			dico_new = {}
			compt = compt + 1
		elif(compt >= 100000):
			i = i + 1
			compt = 0
			#print(i,compt)
		else:
			dico_new[key] = val 
			#print(val)
			compt = compt + len(val)			
			if(compt == 100001):
				write_dico_fasta_format(dico_new,"../results/meme_input/file_"+str(i)+".fasta")	
				print("file_"+str(i)+".fasta")




if __name__ == '__main__': 
	dico_all_seq = create_dico_seq_concate_with_fasta("/home/sdv/m2bi/echan/M2BI/Projet_long/fwdfastafiles/Galaxy25-[FASTA_hypo_Zbtb24mut_genes].fasta")
	parse_fasta_for_meme(dico_all_seq)



