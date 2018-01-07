# Investigation bio-informatique du syndrome ICF par analyse de génome : amélioration de MEME pour l'analyse de séquence avec changement de méthylation dû à des mutations associé à une pathologie.


### A propos
Outils d'investigation bio-informatique par analyse de génome : amélioration de MEME pour l'analyse de séquence avec changement de méthylation dû à des mutations associé à une pathologie (syndrome ICF).
- INPUT : sequence fasta
- OUTPUT : 12 fichiers de motifs 

### Installation de R 
``` {}
sudo apt-get install r-base-core

# Install R packages 
install.packages("stringr", dependencies=TRUE)
```

### Installation de MEME
lien vers la documentation : http://meme-suite.org/doc/install.html?man_type=web#prerequisite 
``` {}
# Install MEME
tar zxf meme_4.12.0.tar.gz 
cd meme_4.12.0 
#./configure --prefix=$HOME/meme --with-url=http://meme-suite.org --enable-build-libxml2 --enable-build-libxslt 
./configure --prefix=/opt/meme_4.12.0 --enable-web=http://host/opal2/services --enable-webservice --with-url=http://host/meme_4.12.0 --with-prev-url=http://host/meme_4.9.1 --with-prev-ver=4.9.1 --with-db=/opt/meme_db --with-notices=../notices.txt --with-news=../news.txt
make 
make test 
make install

export PATH=$HOME/meme/bin:$PATH 
```

### Utilisation du programme
 
 Exemple de ligne de commande
``` {}
chmod +x src/*
cd src
export PATH=$HOME/meme/bin:$PATH 
# recherche motif de taille unique
python3 main.py -fasta_file "../data/Galaxy25-[FASTA_hypo_Zbtb24mut_genes].fasta" -db "../bin/DB/motif_databases/HUMAN/HOCOMOCOv9.meme" -min_len 5 -max_len 8 -nb_motif 25
# recherche motif de taille variable
python3 main.py -fasta_file "../data/Galaxy26-[FASTA_hypo_Zbtb24mut_intergenic].fasta" -db "../bin/DB/motif_databases/HUMAN/HOCOMOCOv9.meme" -min_len 5 -max_len 8 -nb_motif 25 
```


``` {}
 usage: main.py [-h] -fasta_file FASTA_FILE -db DB [-len LEN]
               [-min_len MIN_LEN] [-max_len MAX_LEN] [-nb_motif NB_MOTIF]
               [-nb_rep NB_REP]

optional arguments:
  -h, --help            show this help message and exit
  -fasta_file FASTA_FILE
                        Fasta format sequence
  -db DB                Database for known pattern search
  -len LEN              Search pattern of one size
  -min_len MIN_LEN      Minimum size of the searched pattern; default: 5
  -max_len MAX_LEN      Maximum size of the searched pattern; default: 8
  -nb_motif NB_MOTIF    Maximum number of pattern to search default: 100
  -nb_rep NB_REP        Number of times the pattern is found in the sequences;
                        default: 10
```


### Auteur
CHAN SOCK PENG Edith M2BI 2017-2018 