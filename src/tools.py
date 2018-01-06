#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# MODULES
import re
import os
import meme_suite
import complement_meme

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


def write_dico_to_file(dico, output_file):
	'''
		Cette fonction permet d'ecrire un dictionnaire au format fasta.
		INPUT : 
			- dico : dictionnaire
			- output_file : nom fichier sortie 
		OUTPUT : 	
			- fichier fichier
	'''
	filout = open(output_file, "w")
	for key, val in dico.items():
		filout.write("{}\t{}\n".format(key, val))		
	filout.close()


#if __name__ == '__main__':
