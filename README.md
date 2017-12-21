Investigation bio-informatique du syndrome ICF par analyse de génome

``` {}
# Install MEME
tar zxf meme_4.12.0.tar.gz 
cd meme_4.12.0 
./configure --prefix=$HOME/meme --with-url=http://meme-suite.org --enable-build-libxml2 --enable-build-libxslt 
make 
make test 
make install

export PATH=$HOME/meme/bin:$PATH 
```

