library(stringr)

### Repartition des motifs connus/ inconnues 
known_motif = read.table("../results/known_motif.txt")
unknown_motif = read.table("../results/unknown_motif.txt")

len_known_motif = dim(known_motif)[1]
len_unknown_motif = dim(unknown_motif)[1]

png("../results/Pie_Chart_of_all_patterns.png")
slices = c(len_known_motif, len_unknown_motif)
lbls = c("known pattern", "unknown pattern")
pct = round(slices/sum(slices)*100)
lbls <- paste(lbls, pct) # add percents to labels 
lbls <- paste(lbls,"%",sep="") # ad % to labels
pie(slices,labels = lbls, col=rainbow(length(lbls))) 
dev.off()

### Repartition de la taille des motifs 
# connues
taille_connus = NULL
for ( i in seq(1:len_known_motif) ) {
	a = nchar(as.character(known_motif[i,1]))
	taille_connus = c(taille_connus,a)
}

# inconnues 
taille_inconnus = NULL
for ( i in seq(1:len_unknown_motif) ) {
	a = nchar(as.character(unknown_motif[i,1]))
	taille_inconnus = c(taille_inconnus,a)
}
png("../results/Pattern_length_histogram.png")
p1 = hist(taille_connus, plot=F)
p2 = hist(taille_inconnus, plot=F)
plot(p1, col="blue", xlab ="length pattern", xlim=c(5,8), main ="",freq=T)
plot(p2, col="red", add=T)
dev.off()

### Repartition des motfis connues ou non en fonction de la précense de CG
known_motif_CG_plus = read.table("../results/CG_plus_known_motif.txt")
known_motif_CG_moins = read.table("../results/CG_moins_known_motif.txt")
unknown_motif_CG_plus = read.table("../results/CG_plus_unknown_motif.txt")
unknown_motif_CG_moins = read.table("../results/CG_moins_unknown_motif.txt")

len_known_motif_CG_plus = dim(known_motif_CG_plus)[1]
len_known_motif_CG_moins = dim(known_motif_CG_moins)[1]
len_unknown_motif_CG_plus = dim(unknown_motif_CG_plus)[1]
len_unknown_motif_CG_moins = dim(unknown_motif_CG_moins)[1]

png("../results/CG_content_in_all_patterns.png")
slices = c(len_known_motif_CG_plus, len_known_motif_CG_moins, len_unknown_motif_CG_plus, len_unknown_motif_CG_moins)
lbls = c( paste("known CG+\n", len_known_motif_CG_plus), paste("known CG-\n", len_known_motif_CG_moins), paste("unknown CG+\n", len_unknown_motif_CG_plus), paste("unknown CG-\n", len_unknown_motif_CG_moins))
barplot(slices, names.arg=lbls, col=c(1,2,3,4))
dev.off()

### Reparttion des motifs 
# overlap 
CG_plus_known_unknown_motif_overlap = read.table("../results/CG_plus_known_unknown_motif_overlap.txt", sep="\n")
CG_moins_known_unknown_motif_overlap = read.table("../results/CG_moins_known_unknown_motif_overlap.txt",  sep="\n")
CG_plus_unknown_unknown_motif_overlap = read.table("../results/CG_plus_unknown_unknown_motif_overlap.txt",  sep="\n")
CG_moins_unknown_unknown_motif_overlap = read.table("../results/CG_moins_unknown_unknown_motif_overlap.txt", sep="\n")

len_CG_plus_known_unknown_motif_overlap = 0
len_CG_moins_known_unknown_motif_overlap = 0
len_CG_plus_unknown_unknown_motif_overlap = 0
len_CG_moins_unknown_unknown_motif_overlap = 0

len_CG_plus_known_unknown_motif_overlap = dim(CG_plus_known_unknown_motif_overlap)[1]
len_CG_moins_known_unknown_motif_overlap = dim(CG_moins_known_unknown_motif_overlap)[1]
len_CG_plus_unknown_unknown_motif_overlap = dim(CG_plus_unknown_unknown_motif_overlap)[1]
len_CG_moins_unknown_unknown_motif_overlap = dim(CG_moins_unknown_unknown_motif_overlap)[1]

png("../results/overlap.png")
slices1 = c(len_CG_plus_known_unknown_motif_overlap, len_CG_moins_known_unknown_motif_overlap, len_CG_plus_unknown_unknown_motif_overlap, len_CG_moins_unknown_unknown_motif_overlap)
lbls1 = c( paste("kn unk\nCG+ ", len_CG_plus_known_unknown_motif_overlap), paste("kn unk\nCG- ", len_CG_moins_known_unknown_motif_overlap), paste("unk unk\nCG+ ", len_CG_plus_unknown_unknown_motif_overlap), paste("unk unk\nCG- ", len_CG_moins_unknown_unknown_motif_overlap))
barplot(slices1, names.arg=lbls1, col=c(1,2,3,4))
dev.off()

# no_overlap 
CG_plus_known_unknown_motif_no_overlap = read.table("../results/CG_plus_known_unknown_motif_no_overlap.txt", sep="\n")
CG_moins_known_unknown_motif_no_overlap = read.table("../results/CG_moins_known_unknown_motif_no_overlap.txt",  sep="\n")
CG_plus_unknown_unknown_motif_no_overlap = read.table("../results/CG_plus_unknown_unknown_motif_no_overlap.txt",  sep="\n")
CG_moins_unknown_unknown_motif_no_overlap = read.table("../results/CG_moins_unknown_unknown_motif_no_overlap.txt", sep="\n")

len_CG_plus_known_unknown_motif_no_overlap = 0
len_CG_moins_known_unknown_motif_no_overlap = 0
len_CG_plus_unknown_unknown_motif_no_overlap = 0
len_CG_moins_unknown_unknown_motif_no_overlap = 0

len_CG_plus_known_unknown_motif_no_overlap = dim(CG_plus_known_unknown_motif_no_overlap)[1]
len_CG_moins_known_unknown_motif_no_overlap = dim(CG_moins_known_unknown_motif_no_overlap)[1]
len_CG_plus_unknown_unknown_motif_no_overlap = dim(CG_plus_unknown_unknown_motif_no_overlap)[1]
len_CG_moins_unknown_unknown_motif_no_overlap = dim(CG_moins_unknown_unknown_motif_no_overlap)[1]

png("../results/no_overlap.png")
slices2 = c(len_CG_plus_known_unknown_motif_no_overlap, len_CG_moins_known_unknown_motif_no_overlap, len_CG_plus_unknown_unknown_motif_no_overlap, len_CG_moins_unknown_unknown_motif_no_overlap)
lbls2 = c( paste("kn unk\nCG+ ", len_CG_plus_known_unknown_motif_no_overlap), paste("kn unk\nCG- ", len_CG_moins_known_unknown_motif_no_overlap), paste("unk unk\nCG+ ", len_CG_plus_unknown_unknown_motif_no_overlap), paste("unk unk\nCG- ", len_CG_moins_unknown_unknown_motif_no_overlap))
barplot(slices2, names.arg=lbls2, col=c(1,2,3,4))
dev.off()
