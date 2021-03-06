#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# MODULES
import re
import os
import tools
import complement_meme


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
				tools.write_dico_fasta_format(dico_new,"../data/meme_input/file_"+str(i)+".fasta")	
				print("file_"+str(i)+".fasta")
	tools.write_dico_fasta_format(dico_new,"../data/meme_input/file_"+str(i)+".fasta")	
	print("file_"+str(i)+".fasta")	



def launch_meme(input_meme, output_meme, max_motif, len_motif, min_rep = 10):
	'''
		Cette fonction permet de lancer MEME. 
		INPUT:
			- input_meme : nom du fichier fasta
			- output_meme : nom du fchier de sortie
			- max_motif : nombre de motif à rechercher
			- len_motif : taille du motif 
			- min_rep : nombre de répétition par sites 
		OUTPUT: 
			- fichier meme.txt qui contient les motifs
	'''
	cmd = "meme {} -oc {} -nmotifs {} -w {} -minsites {}".format(input_meme, output_meme, max_motif, len_motif, min_rep)
	print(cmd)
	os.system(cmd)


def launch_meme_width_min_max(input_meme, output_meme, max_motif, min_len, max_len, min_rep = 10):
	'''
		Cette fonction permet de lancer MEME. 
		INPUT:
			- input_meme : nom du fichier fasta
			- output_meme : nom du fchier de sortie
			- max_motif : nombre de motif à rechercher
			- min_len : taille du motif minimal
			- max_len : taille du motif maximal
			- nb_procces : nombre de processus a utiliser
			- min_rep : nombre de répétition par sites
		OUTPUT: 
			- fichier meme.txt qui contient les motifs
	'''
	cmd = "meme {} -oc {} -nmotifs {} -minw {} -maxw {} -minsites {}".format(input_meme, output_meme, max_motif, min_len, max_len, min_rep)
	print(cmd)
	os.system(cmd)


def step_meme(max_motif, len_motif, nb_procces = 2, min_rep = 10 ,path_in="../data/meme_input", path_out="../data/meme_output"):
	'''
		Cette fonction permet de lancer MEME sur tout les fichiers fasta et placer les resultats 
		dans data dans des dossiers séparer
		INPUT: 
			- max_motif : nombre de motif à rechercher
			- len_motif : taille du motif 
			- path_in : chemin vers les fichiers d'entrée de MEME
			- path_out : chemin vers les fichiers de sortie de MEME	
			- min_rep : nombre de répétition par sites
		OUTPUT:
			- meme.txt 	
	'''
	#path_in = "../data/meme_input"
	#path_out = "../data/meme_output"
	list_meme_input = os.listdir(path_in) # liste des fichiers fasta
	cmd = "mkdir {}".format(path_out)
	os.system(cmd)
	for file_sel in list_meme_input:
		tmp = file_sel
		tmp = tmp.split(".")
		name_out = tmp[0]
		launch_meme(path_in+"/"+file_sel, path_out+"/"+name_out, max_motif, len_motif, min_rep)


def step_meme_width_min_max(max_motif, min_len, max_len, min_rep = 10, path_in="../data/meme_input", path_out="../data/meme_output"):
	'''
		Cette fonction permet de lancer MEME sur tout les fichiers fasta et placer les resultats 
		dans data dans des dossiers séparer
		INPUT: 
			- max_motif : nombre de motif à rechercher
			- min_len : taille du motif minimal
			- max_len : taille du motif maximal
			- path_in : chemin vers les fichiers d'entrée de MEME
			- path_out : chemin vers les fichiers de sortie de MEME
			- min_rep : nombre de répétition par sites
		OUTPUT:
			- meme.txt 	
	'''
	#path_in = "../data/meme_input"
	#path_out = "../data/meme_output"
	list_meme_input = os.listdir(path_in) # liste des fichiers fasta
	cmd = "mkdir {}".format(path_out)
	os.system(cmd)
	for file_sel in list_meme_input:
		tmp = file_sel
		tmp = tmp.split(".")
		name_out = tmp[0]
		launch_meme_width_min_max(path_in+"/"+file_sel, path_out+"/"+name_out, max_motif, min_len, max_len, min_rep)			



def launch_tomtom(input_tomtom, output_tomtom, db):
	'''
		Cette fonction permet de lancer TOMTOM. 
		INPUT:
			- input_tomtom :sortie de meme
			- output_tomtom : nom du fchier de sortie
			- db : base de données dans laquelle les motifs sont recherchés
		OUTPUT: 
			- fichier tomtom.txt qui contient les motifs retrouvé dans la base de données
	'''
	cmd = "tomtom -xalph -oc {} {}/meme.txt {}".format(output_tomtom, input_tomtom, db)
	print(cmd)
	os.system(cmd)


def step_tomtom(db,path_in="../data/meme_output", path_out="../data/tomtom_output"):
	'''
		Cette fonction permet de lancer TOMTOM sur tout les fichiers fasta et placer les resultats 
		dans data dans des dossiers séparer
		INPUT: 
			- db : base de données dans laquelle les motifs sont recherchés		
			- path_in : chemin vers les fichiers d'entrée de TOMTOM (sortie de MEME)
			- path_out : chemin vers les fichiers de sortie de TOMTOM	
		OUTPUT:
			- tomtom.txt 	
	'''
	list_meme_input = os.listdir(path_in)
	cmd = "mkdir {}".format(path_out)
	os.system(cmd)
	for file_sel in list_meme_input:
		launch_tomtom(path_in+"/"+file_sel, path_out+"/"+file_sel, db)


def recup_exp_reg_motif(meme_output, list_motif_exp_reg, num_file="1", path="../data/meme_output"):
	'''
		Cette fonction permet de parser les sorties de MEME puis de stockes
		dans un dictionnaire l'identifiant du motif et l'expression regulère 
		associé au motif.
		INPUT: 
			- meme_output : sortie de MEME
			- list_motif_exp_reg : mon du fichier de sortie
			- num_file numero du fichier
		OUTPUT:
			- dictionnaire avec comme clé l'identifiant du motif et comme valeur 
			l'expression regulère du motif
			- ficher contenant le contenu du dico 
	'''
	#grep -A2 " regular expression" '/home/sdv/m2bi/echan/M2BI/Projet_long/projet_long_ICF/results/test_tools/test_meme_5/meme.txt' > out.txt
	#parse fichier output MEME
	#tmp="/home/sdv/m2bi/echan/M2BI/Projet_long/projet_long_ICF/results/test_tools/test_meme_8/out.txt"
	tmp = path+"/file_"+num_file+"/out.txt"
	meme_output_f = path+"/file_"+num_file+"/"+meme_output
	cmd = "grep -A2 'regular expression' {} > {}".format(meme_output_f, tmp)
	os.system(cmd)	
	#print(cmd)
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
	#print(new_li)
	dico_meme_motif_reg_exp = {}
	for i in range(0, len(new_li)-1, 2):
		key = new_li[i]
		exp_reg_motif = new_li[i+1]
		motif_num = key.split(" ")[2]
		#print motif_num, exp_reg_motif
		dico_meme_motif_reg_exp[motif_num]=exp_reg_motif
	tools.write_dico_to_file(dico_meme_motif_reg_exp, list_motif_exp_reg)
	print(dico_meme_motif_reg_exp)
	return dico_meme_motif_reg_exp


def transf_regex_to_motif(meme_output, num_file="1", path="../data/meme_output"):
	'''
		Cette fonction permet de generer la liste de tous les motifs a partir des expressions régulières
		retrouvé par meme.
			INPUT: 
			- meme_output : sortie de MEME
			- num_file numero du fichier
				OUTPUT:
			- dictionnaire avec comme clé l'identifiant du motif et comme valeur 
			l'expression regulère du motif
			- ficher contenant le contenu du dico 
	'''
	dico_meme_motif = {}
	#dico_motif_regex = recup_exp_reg_motif('meme.txt', "all_motif")
	dico_motif_regex = recup_exp_reg_motif(meme_output, "motif_regex.txt", num_file)
	print(dico_motif_regex)
	for key, val in dico_motif_regex.items():
		#print(key, val)
		cmd = "python ../bin/exrex.py {} > motif.txt".format(val)
		#print(cmd)
		os.system(cmd)
		filin = open("motif.txt","r")
		motif = filin.readlines()
		filin.close()
		for mot in motif:
			#print(key, val, mot)
			mot = mot.replace("\n","")
			if key not in dico_meme_motif:
				dico_meme_motif[key] = []
				dico_meme_motif[key].append(mot)
			else :
				dico_meme_motif[key].append(mot)
		#print(dico_meme_motif)		
		list_motif = list(dico_meme_motif.values())
	os.system("mkdir ../data/motifs") 	
	filout = open("../data/motifs/list_motif_file_"+num_file+".txt","w")
	for elt in list_motif:
		if(len(elt)>1):
				for elt2 in elt:
					filout.write(elt2+"\n")
		else:
			filout.write(elt[0]+"\n")
	filout.close()
	return dico_meme_motif	


def launch_transf_regex_to_motif(path="../data/meme_output"):
	"""
	Cette fonction permet de récuperer tous les motifs associés au 
	différents fichiers fasta
	INPUT :
		-  path : chemin vers la liste des fichiers de sorties de meme 
	OUTPUT : 
		- differents fichiers contenant tous les motifs
		- 1 fichier contenant tous les motifs concaténées 
	"""
	list_file = os.listdir(path)
	for elt in list_file:
		#print(elt)
		elt = elt.split("_")
		num_file = elt[1]
		#print(num_file)
		dico_meme_motif = transf_regex_to_motif('meme.txt', num_file)
	os.system("rm ../data/motifs/concat_motif.txt")
	os.system("cat ../data/motifs/* > ../data/motifs/concat_motif.txt")


def find_known_motif(num_file="1"):
	'''
		Cette fonction permet d'analyse la sortie de tomtom pour trouver les motifs
		connus pour un fichier
		INPUT: 
			- num_file : numero du fichier
		OUTPUT : 
			- liste des motifs connues dans un fichier  
	'''
	list_known_motif = []
	fillin = open("../data/tomtom_output/file_"+num_file+"/tomtom.txt","r")
	tmtm_out = fillin.readlines()
	fillin.close()
	for elt in tmtm_out[1:]:
		#print(elt)
		elt = elt.split("\t")
		motif = elt[0]
		if motif not in list_known_motif:
			list_known_motif.append(motif)
	os.system("mkdir ../data/tomtom_motif")
	filout = open("../data/tomtom_motif/known_motifs_file_"+num_file+".txt","w")
	for elt2 in list_known_motif:
		filout.write(elt2+"\n")
	filout.close()
	

def launch_find_known_motif(path="../data/tomtom_output"):
	"""
		Cette fonction permet de récuperer tous les motifs connues dans 
		tous les fichiers sorties de TOMTOM
		INPUT :
			-  path : chemin vers la liste des fichiers de sorties de tomtom 
		OUTPUT : 
			- differents fichiers contenant tous les motifs connues 
			- 1 fichier contenant tous les motifs connues concaténées 
	"""
	list_file = os.listdir(path)
	for elt in list_file:
		print(elt)
		elt = elt.split("_")
		num_file = elt[1]
		#print(num_file)
		dico_meme_motif = find_known_motif(num_file)
	os.system("rm ../data/tomtom_motif/concat_known_motif.txt")
	os.system("cat ../data/tomtom_motif/* > ../data/tomtom_motif/concat_known_motif.txt")


def create_dico_knwon_unknown_motif():
	'''
		Cette fonction permet de créer un dictionnaire permettant de 
		différenciés les motifs connus des motifs inconnus.
		OUPUT:
			- dictionnaire permettant de différenciés les motifs connus des motifs inconnus.
	'''
	filin1 = open("../data/motifs/concat_motif.txt","r") # tous les motifs
	filin2 = open("../data/tomtom_motif/concat_known_motif.txt", "r") # motifs connus
	all_motif = filin1.readlines()
	known_motif = filin2.readlines()
	filin1.close()
	filin2.close()
	# recherche motifs connus ou non
	known_motif_c = []
	for elt in known_motif:
		elt = elt.replace("\n","")
		elt = elt.replace(" ","")		
		known_motif_c.append(elt)
	unknown_motif = []
	for elt in all_motif:
		elt = elt.replace("\n","")
		elt = elt.replace(" ","")
		if elt not in known_motif_c:
			unknown_motif.append(elt)
	# dico 
	dico_motif_knwon_unknown_motif = {}
	dico_motif_knwon_unknown_motif["known_motif"] = known_motif_c
	dico_motif_knwon_unknown_motif["unknown_motif"] = unknown_motif
	#ecris dans un fichier la liste des motifs connus
	filout1 = open("../results/known_motif.txt","w")
	for elt in dico_motif_knwon_unknown_motif["known_motif"]:
		filout1.write(elt+"\n")
	filout1.close()
	#ecris dans un fichier la liste des motifs inconnues
	filout2 = open("../results/unknown_motif.txt","w")	
	for elt in dico_motif_knwon_unknown_motif["unknown_motif"]:
		filout2.write(elt+"\n")
	filout2.close()	
	return dico_motif_knwon_unknown_motif


def launch_dreme(input_dreme, min_l = 5, path = "../data"):
	'''
		Cette fonction permet de lancer TOMTOM. 
		INPUT:
			- input_dreme : fichier de séquence au format fasta 
			- output_dreme : nom du fchier de sortie
			- min_l : taille minimal du motif 
		OUTPUT: 
			- fichier dreme.txt qui contient les motifs enrichi dans le fichier
	'''
	#os.system("mkdir "+path+"/output_dreme")
	output_dreme = path+"/output_dreme"
	cmd = "dreme -oc {} -p {} -m {}".format(output_dreme, input_dreme, min_l)
	print(cmd)
	os.system(cmd)

#if __name__ == '__main__':