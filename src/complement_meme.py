#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# MODULES
import re
import os
import tools
import meme_suite

def find_CG_in_motif():
	'''
		Cette fonction permet de trouver les motifs qui contienent un CG parmis 
		les motifs connus et de novo
		INPUT:
			- liste motifs connus ou non
		OUTPUT:
			- liste motifs connus ou non avec CG ou non
	'''
	filin1 = open("../results/known_motif.txt","r")
	filin2 = open("../results/unknown_motif.txt","r")
	known_motif = filin1.readlines()
	unknown_motif = filin2.readlines()
	filin1.close()
	filin2.close()
	filout1 = open("../results/CG_plus_known_motif.txt","w")
	filout2 = open("../results/CG_moins_known_motif.txt","w")
	for elt in known_motif: 
		if("CG" in elt):
			filout1.write(elt)
		else:
			filout2.write(elt)
	filout1.close()
	filout2.close()
	filout1 = open("../results/CG_plus_unknown_motif.txt","w")
	filout2 = open("../results/CG_moins_unknown_motif.txt","w")
	for elt in unknown_motif: 
		if("CG" in elt):
			filout1.write(elt)
		else:
			filout2.write(elt)
	filout1.close()
	filout2.close()


# si les 2 motifs sont la seq 

def find_motif_overlap(dico_all_seq, file1, file2):
	#dico_all_seq = tools.create_dico_seq_concate_with_fasta("../data/Galaxy25-[FASTA_hypo_Zbtb24mut_genes].fasta")
	#filin1 = open("../results/CG_plus_unknown_motif.txt","r")
	#filin2 = open("../results/CG_plus_known_motif.txt","r")
	filin1 = open(file1,"r")
	filin2 = open(file2,"r")
	list_unknown_motif = filin1.readlines()
	list_known_motif = filin2.readlines()
	filin1.close()
	filin2.close()
	dico_overlap = {} 
	dico_no_overlap = {} 
	for known_motif in list_known_motif:
		for unknown_motif in list_unknown_motif:
			known_motif = known_motif.replace("\n","")
			unknown_motif = unknown_motif.replace("\n","")
			for key, val in dico_all_seq.items():
				if (known_motif in val) and (unknown_motif in val):
					#print (key)
					#print (known_motif, unknown_motif)
					#print (val) 
					val = val.upper()
					begin_kn = val.index(known_motif)
					begin_unkn = val.index(unknown_motif)
					end_kn = begin_kn + len(known_motif)
					end_unkn = begin_unk + len(unknown_motif)
					int_kn = set(range (begin_kn, end_kn))
					int_unkn = set(range (begin_unkn, end_unkn))
					len_overlap = len(int_kn.intersection(int_unkn))
					if len_overlap > 0:
						if(known_motif not in dico_overlap.keys()):
							dico_overlap[known_motif] = []
							dico_overlap[known_motif].append(unknown_motif)
						else:
							dico_overlap[known_motif].append(unknown_motif)
					else:
						if(known_motif not in dico_no_overlap.keys()):
							dico_no_overlap[known_motif] = []
							dico_no_overlap[known_motif].append(unknown_motif)
						else:
							dico_no_overlap[known_motif].append(unknown_motif)


val = "tagaaGCTATCTAAGAGTTAATCAAGTTGCCCCGCCCCCCCCCCCTCCCCGAGTCATAACAAGCTGCTGCCGATTTACTGGGCTGTATAAATTGTAGGAA"
known_motif = "CCCGCC"
unknown_motif = "GCCCCGCC" 
'''
dico_overlap = {} 
dico_no_overlap = {} 
for known_motif in list_known_motif:
	for unknown_motif in list_unknown_motif:
		known_motif = known_motif.replace("\n","")
		unknown_motif = unknown_motif.replace("\n","")
		for key, val in dico_all_seq.items():
			if (known_motif in val) and (unknown_motif in val):
				#print (key)
				#print (known_motif, unknown_motif)
				#print (val) 
				val = val.upper()
				begin_kn = val.index(known_motif)
				begin_unkn = val.index(unknown_motif)
				end_kn = begin_kn + len(known_motif)
				end_unkn = begin_unk + len(unknown_motif)
				int_kn = set(range (begin_kn, end_kn))
				int_unkn = set(range (begin_unkn, end_unkn))
				len_overlap = len(int_kn.intersection(int_unkn))
				if len_overlap > 0:
					if(known_motif in dico_overlap.keys()):
						dico_overlap[known_motif] = []
						dico_overlap[known_motif].append(unknown_motif)
					else:
						dico_overlap[known_motif].append(unknown_motif)
				else:
					if(known_motif in dico_no_overlap.keys()):
						dico_no_overlap[known_motif] = []
						dico_no_overlap[known_motif].append(unknown_motif)
					else:
						dico_no_overlap[known_motif].append(unknown_motif)
'''
#if __name__ == '__main__': 