#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# MODULES
import re
import os
import argparse
import time
import tools
import meme_suite
import complement_meme


def init_arguments():
	parser = argparse.ArgumentParser(description="")
	parser.add_argument("-fasta_file", type = str, required = True, help = "Sequence au format fasta")
	parser.add_argument("-db", type = str, required = True, help = "banque de donnée de recherche pour la recherche de motif connus")
	parser.add_argument("-len", required = False, help = "Recheche motif d'une seule taille")
	parser.add_argument("-int_len", required = False, help = "Recheche motif dans un interval de taille")
	args = parser.parse_args()
	return args


if __name__ == '__main__': 
	begin = time.time()
	args = init_arguments()
	fasta_fi = args.fasta_file
	db = args.db
	cmd = "export PATH=$HOME/meme/bin:$PATH"
	os.system(cmd)
	dico_all_seq = tools.create_dico_seq_concate_with_fasta(fasta_fi)
	#dico_all_seq = tools.create_dico_seq_concate_with_fasta("/home/cspe/M2_BI/Projet_long/fwdfastafiles/Galaxy25-[FASTA_hypo_Zbtb24mut_genes].fasta")
	meme_suite.parse_fasta_for_meme(dico_all_seq)
	#meme_suite.step_meme(25, 5)
	#meme_suite.step_meme_width_min_max(100, 5, 8, 10)
	#meme_suite.step_tomtom("../bin/DB/motif_databases/HUMAN/HOCOMOCOv11_full_HUMAN_mono_meme_format.meme")
	#meme_suite.step_tomtom(db)
	##dico_motif_regex = recup_exp_reg_motif('meme.txt', "all_motif")
	##print(dico_motif_regex)
	##t=recup_exp_reg_motif('../results/test_tools/test_meme_5/meme.txt', "all_motif")
	##dico_meme_motif = transf_regex_to_motif('meme.txt')
	##print(dico_meme_motif)
	meme_suite.launch_transf_regex_to_motif()
	#step_tomtom()
	##find_known_motif("2")
	meme_suite.launch_find_known_motif()
	meme_suite.dico_knwon_unknown_motif = meme_suite.create_dico_knwon_unknown_motif()
	##print(dico_knwon_unknown_motif)
	complement_meme.find_GC_in_motif()
	# subprosses.call
	end = time.time()
	print("Duree du programme : {:.2f} secondes".format(end - begin))


'''
python3 main.py -fasta_file "../data/Galaxy25-[FASTA_hypo_Zbtb24mut_genes].fasta" -db "../bin/DB/motif_databases/HUMAN/HOCOMOCOv11_full_HUMAN_mono_meme_format.meme"
'''

