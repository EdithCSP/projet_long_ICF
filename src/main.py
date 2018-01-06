#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import os
import argparse

parser = argparse.ArgumentParser(description="calculate X to the power of Y")
group = parser.add_mutually_exclusive_group()
group.add_argument("-v", "--verbose", action="store_true")
group.add_argument("-q", "--quiet", action="store_true")
parser.add_argument("z")
parser.add_argument("x", type=int, help="the base")
parser.add_argument("y", type=int, help="the exponent")
args = parser.parse_args()
answer = args.x**args.y

if args.quiet:
    print(answer)
elif args.verbose:
    print("{} to the power {} equals {}".format(args.x, args.y, answer))
else:
    print("{}^{} == {}".format(args.x, args.y, answer))

print(args.x, args.y, args.z)


if __name__ == '__main__': 
	cmd = "export PATH=$HOME/meme/bin:$PATH"
	os.system(cmd)
	dico_all_seq = create_dico_seq_concate_with_fasta("/home/cspe/M2_BI/Projet_long/fwdfastafiles/Galaxy25-[FASTA_hypo_Zbtb24mut_genes].fasta")
	parse_fasta_for_meme(dico_all_seq)
	#step_meme(25, 5)
	step_meme_width_min_max(100, 5, 8, 10)
	step_tomtom("../bin/DB/motif_databases/HUMAN/HOCOMOCOv11_full_HUMAN_mono_meme_format.meme")
	##dico_motif_regex = recup_exp_reg_motif('meme.txt', "all_motif")
	##print(dico_motif_regex)
	##t=recup_exp_reg_motif('../results/test_tools/test_meme_5/meme.txt', "all_motif")
	##dico_meme_motif = transf_regex_to_motif('meme.txt')
	##print(dico_meme_motif)
	launch_transf_regex_to_motif()
	#step_tomtom()
	##find_known_motif("2")
	launch_find_known_motif()
	dico_knwon_unknown_motif = create_dico_knwon_unknown_motif()
	##print(dico_knwon_unknown_motif)
	find_GC_in_motif()
	# subprosses.call

	