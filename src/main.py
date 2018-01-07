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
	parser.add_argument("-fasta_file", type = str, required = True, help = "Fasta format sequence")
	parser.add_argument("-db", type = str, required = True, help = "Database for known pattern search")
	parser.add_argument("-len", type = int, required = False, help = "Search pattern of one size")
	parser.add_argument("-min_len", type = int, required = False, default = 5, help = "Minimum size of the searched pattern; default: 5")
	parser.add_argument("-max_len", type = int, required = False, default = 8, help = "Maximum size of the searched pattern; default: 8")	
	parser.add_argument("-nb_motif", type = int, required = False, default = 100, help = "Maximum number of pattern to search default: 100")
	parser.add_argument("-nb_rep", type = int, required = False, default = 10, help = "Number of times the pattern is found in the sequences; default: 10")			
	args = parser.parse_args()
	return args


if __name__ == '__main__': 
	begin = time.time()
	# def args
	args = init_arguments()
	fasta_fi = args.fasta_file
	db = args.db
	len_motif = args.len
	nb_motif_max = args.nb_motif
	min_len_motif = args.min_len
	max_len_motif = args.max_len
	rep = args.nb_rep	
	# main
	os.system("export PATH=$HOME/meme/bin:$PATH")
	os.system("chmod +x load_meme.sh")
	os.system("./load_meme.sh")
	print("Reead file sequences")	
	dico_all_seq = tools.create_dico_seq_concate_with_fasta(fasta_fi)
	print("Making MEME input")
	meme_suite.parse_fasta_for_meme(dico_all_seq)
	if args.len:
		print("Search pattern of one size")
		#meme_suite.step_meme(25, 5)
		meme_suite.step_meme(nb_motif_max, len_motif)
	else : 
		print("Search pattern in a size range")
		#meme_suite.step_meme_width_min_max(100, 5, 8, 10)
		meme_suite.step_meme_width_min_max(nb_motif_max, min_len_motif, max_len_motif, rep)	
	print("Search for patterns in TOMTOM")
	meme_suite.step_tomtom(db)
	print("Generation of all possible patterns")
	meme_suite.launch_transf_regex_to_motif()
	print("Search for known or unknown patterns")
	meme_suite.launch_find_known_motif()
	dico_knwon_unknown_motif = meme_suite.create_dico_knwon_unknown_motif()
	print("CG search in patterns")
	complement_meme.find_CG_in_motif()
	print("Search overlapping patterns")
	complement_meme.find_motif_overlap(dico_all_seq, "../results/CG_plus_unknown_motif.txt", "../results/CG_plus_known_motif.txt", "CG_plus_known_unknown_motif")
	complement_meme.find_motif_overlap(dico_all_seq, "../results/CG_moins_unknown_motif.txt", "../results/CG_moins_known_motif.txt", "CG_plus_moins_known_unknown_motif")	
	complement_meme.find_motif_overlap(dico_all_seq, "../results/CG_plus_unknown_motif.txt", "../results/CG_plus_unknown_motif.txt", "CG_plus_unknow_unknown_motif")
	complement_meme.find_motif_overlap(dico_all_seq, "../results/CG_moins_unknown_motif.txt", "../results/CG_moins_unknown_motif.txt", "CG_plus_moins_unknown_unknown_motif")
	##meme_suite.launch_dreme(fasta_fi, min_l = 5, path = "../data")		
	end = time.time()
	print("Program duration : {:.2f} secondes".format(end - begin))


'''
python3 main.py -fasta_file "../data/Galaxy25-[FASTA_hypo_Zbtb24mut_genes].fasta" -db "../bin/DB/motif_databases/HUMAN/HOCOMOCOv9.meme" -len 5 
python3 main.py -fasta_file "../data/Galaxy25-[FASTA_hypo_Zbtb24mut_genes].fasta" -db "../bin/DB/motif_databases/HUMAN/HOCOMOCOv9.meme" -min_len 5 -max_len 8
'''

