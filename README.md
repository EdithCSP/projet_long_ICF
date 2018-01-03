# Investigation bio-informatique du syndrome ICF par analyse de génome : amélioration de MEME pour l'analyse de séquence avec changement de méthylation du à des mutation associé à une pathologie. 

doc : http://meme-suite.org/doc/install.html?man_type=web#prerequisite 
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

