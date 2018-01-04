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


def parse_fasta_for_meme(dico):
	'''
		Cett fonction permet de découpé un fichier fasta puisque en plusieurs 
		fichier fasta qui seront les entrée de MEME. la taille de la base de données
		de séquence fournit à meme est limiter à 100000 caractère.
		INPUT:
			- dico : dictionnaire contenant en clé le nom de la séquence et en valeur 
			la séquence.
		OUTPUT:
			- fichier fasta de 100000 caractère dans ../data/meme_input. 
	'''
	os.system("mkdir ../data/meme_input")
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
				write_dico_fasta_format(dico_new,"../data/meme_input/file_"+str(i)+".fasta")	
				print("file_"+str(i)+".fasta")

def launch_meme(input_meme, output_meme, max_motif, len_motif):
	'''
		Cette fonction permet de lancer MEME. 
		INPUT:
			- input_meme : nom du fichier fasta
			- output_meme : nom du fchier de sortie
			- max_motif : nombre de motif à rechercher
			- len_motif : taille du motif 
		OUTPUT: 
			- fichier meme.txt qui contient les motifs
	'''
	cmd = "meme {} -oc {} -nmotifs {} -w {}".format(input_meme, output_meme, max_motif, len_motif)
	print(cmd)
	os.system(cmd)

def step_meme(max_motif, len_motif,path_in="../data/meme_input", path_out="../data/meme_output"):
	#path_in = "../data/meme_input"
	#path_out = "../data/meme_output"
	list_meme_input = os.listdir(path_in)
	cmd = "mkdir {}".format(path_out)
	os.system(cmd)
	for file_sel in list_meme_input:
		tmp = file_sel
		tmp = tmp.split(".")
		name_out = tmp[0]
		launch_meme(path_in+"/"+file_sel, path_out+"/"+name_out, max_motif, len_motif)


def recup_exp_reg_motif(meme_output, list_motif_exp_reg, path="../data/meme_output"):
	'''
		Cette fonction permet de parser les sorties de MEME puis de stockes
		dans un dictionnaire l'identifiant du motif et l'expression regulère 
		associé au motif.
		INPUT: 
		- meme_output : sortie de MEME
		- list_motif_exp_reg : mon du fichier
		OUTPUT:
		- dictionnaire avec comme clé l'identifiant du motif et comme valeur 
		l'expression regulère du motif
		- ficher contenant le contenu du dico 
	'''
	#grep -A2 " regular expression" '/home/sdv/m2bi/echan/M2BI/Projet_long/projet_long_ICF/results/test_tools/test_meme_5/meme.txt' > out.txt
	#parse fichier output MEME
	tmp="/home/sdv/m2bi/echan/M2BI/Projet_long/projet_long_ICF/results/test_tools/test_meme_5/out.txt"
	cmd = "grep -A2 'regular expression' {} > {}".format(meme_output, tmp)
	os.system(cmd)	
	# transforme fichier parser en dico
	tmp_file = open(tmp,"r")
	tmp_liste = tmp_file.readlines()
	tmp_file.close()
	new_li=[]
	for elt in tmp_liste:
		if not elt.startswith('-'):
			elt=elt.replace("\n","")
			new_li.append(elt)
			#print(elt)
	print(new_li)
	dico_meme_motif_reg_exp = {}
	for i in range(0, len(new_li)-1, 2):
		key = new_li[i]
		exp_reg_motif = new_li[i+1]
		motif_num = key.split(" ")[2]
		#print motif_num, exp_reg_motif
		dico_meme_motif_reg_exp[motif_num]=exp_reg_motif
	write_dico_to_file(dico_meme_motif_reg_exp, list_motif_exp_reg)
	print(dico_meme_motif_reg_exp)
	return dico_meme_motif_reg_exp


if __name__ == '__main__': 
	dico_all_seq = create_dico_seq_concate_with_fasta("/home/sdv/m2bi/echan/M2BI/Projet_long/fwdfastafiles/Galaxy25-[FASTA_hypo_Zbtb24mut_genes].fasta")
	parse_fasta_for_meme(dico_all_seq)
	#step_meme()
	recup_exp_reg_motif()

# generate_all_motif
t=recup_exp_reg_motif('/home/sdv/m2bi/echan/M2BI/Projet_long/projet_long_ICF/results/test_tools/test_meme_5/meme.txt', "all_motif")

