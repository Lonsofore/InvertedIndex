InvertedIndex
==============

Inverted index service on Python using gRPC, shelve and Docker.


Functions
---------

* add(text<string>) -> id<int>  -  add document (text) to index, returns id
* search(text<string>) -> ids<list<int>>  -  search for a documents with the text (default limit is 10)
* delete(id<int>) -> status<bool>  -  delete the document from index by id, returns delete status


Install
-------

Using virtualenv:

* python3 -m venv invertedindex
* cd invertedindex
* source bin/activate
* git clone https://github.com/lonsofore/invertedindex.git
* cd invertedindex
* python3 setup.py install


Using Docker:

* git clone https://github.com/lonsofore/invertedindex.git
* cd invertedindex
* docker build -t invertedindex .


Configure
---------

Linux:

* config dir: '/home/username/.config/invertedindex'
* db dir: '/home/username/.local/share/invertedindex'
* log dir: '/home/username/.cache/invertedindex/log'


Windows:

* config dir: 'C:\\Users\\username\\AppData\\Local\\Lonsofore\\invertedindex'
* db dir: 'C:\\Users\\username\\AppData\\Local\\Lonsofore\\invertedindex'
* log dir: 'C:\\Users\\username\\AppData\\Local\\Lonsofore\\invertedindex\\Logs'


Mac OS:

* config dir: '/Users/username/Library/Application Support/invertedindex'
* db dir: '/Users/username/Library/Application Support/invertedindex'
* log dir: '/Users/username/Library/Logs/invertedindex'


Run
---

Using virtualenv:

* Server:  invertedindexserver
* Client:  invertedindexclient


Using Docker:

* Server:  docker run -it -p *port_out*:*port_in* invertedindex invertedindexserver
* Client:  docker run -it -p *port_out*:*port_in* invertedindex invertedindexclient

replace *port_out* and *port_in* on your ports


If you want to use it on the same machine - replace "-p *port_out*:*port_in*" to "--network=host" or create your own bridge network:

* Server:  docker run -it --network="host" invertedindex invertedindexserver
* Client:  docker run -it --network="host" invertedindex invertedindexclient


License
-------

Licensed under the Apache License, Version 2.0
