#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# MODULES
import re
import os

def find_GC_in_motif():
	'''
		Cette fonction permet de trouver les motifs qui contienent un GC parmis 
		les motifs connus et de novo
		INPUT:
			- liste motifs connus ou non
		OUTPUT:
			- liste motifs connus ou non avec GC ou non
	'''
	filin1 = open("../results/known_motif.txt","r")
	filin2 = open("../results/unknown_motif.txt","r")
	known_motif = filin1.readlines()
	unknown_motif = filin2.readlines()
	filin1.close()
	filin2.close()
	filout1 = open("../results/GC_plus_known_motif.txt","w")
	filout2 = open("../results/GC_moins_known_motif.txt","w")
	for elt in known_motif: 
		if("GC" in elt):
			filout1.write(elt)
		else:
			filout2.write(elt)
	filout1.close()
	filout2.close()
	filout1 = open("../results/GC_plus_unknown_motif.txt","w")
	filout2 = open("../results/GC_moins_unknown_motif.txt","w")
	for elt in unknown_motif: 
		if("GC" in elt):
			filout1.write(elt)
		else:
			filout2.write(elt)
	filout1.close()
	filout2.close()

if __name__ == '__main__': 