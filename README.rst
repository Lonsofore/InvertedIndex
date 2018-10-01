InvertedIndex
==============

Inverted index service on Python using gRPC and shelve.


Functions
---------

* add(text<string>) -> id<int>  -  add document (text) to index, returns id
* search(text<string>) -> ids<list<int>>  -  search for a documents with the text (default limit is 10)
* delete(id<int>) -> status<bool>  -  delete the document from index by id, returns delete status


License
-------

Licensed under the Apache License, Version 2.0
