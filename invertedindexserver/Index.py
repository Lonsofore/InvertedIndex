import os
import shelve
import logging
from collections import Counter

from .config import CONFIG, WORDS_TO_DOCS_PATH, DOCS_TO_WORDS_PATH
from .utility import get_words_set


SEARCH_COUNT = CONFIG['index']['search_count']

logger = logging.getLogger("server")


class Index:

    def __init__(self):
        self.db_words_to_docs = WORDS_TO_DOCS_PATH
        self.db_docs_to_words = DOCS_TO_WORDS_PATH
        self.docs_count = self.get_docs_count_db()
    
    def get_docs_count(self):
        return self.docs_count
            
    def get_docs_count_db(self):
        with shelve.open(self.db_words_to_docs) as db:
            return len(db)
    
    def add(self, line):
        id = self.docs_count
        words = get_words_set(line)
        with shelve.open(self.db_words_to_docs) as db:
            db[str(id)] = words
        with shelve.open(self.db_docs_to_words) as db:
            for word in words:
                if word in db:
                    temp = db[word]
                else:
                    temp = set()                    
                temp.add(id)
                db[word] = temp
        self.docs_count += 1
        logger.info('Added new doc. ID: {}'.format(id))
        return id
        
    def search_with_count(self, line):
        counter = Counter()
        words = get_words_set(line)
        with shelve.open(self.db_docs_to_words) as db:
            for word in words:
                if word in db:
                    for id in db[word]:
                        counter[id] += 1
        return counter.most_common(SEARCH_COUNT)
        
    def search(self, line):
        result = self.search_with_count(line)
        ids = []
        for key, value in result:
            ids.append(key)
        logger.info('Searched for: {}'.format(line))
        return ids
                
    def delete(self, num):
        words = set()
        with shelve.open(self.db_words_to_docs) as db:
            try:
                words = db[str(num)]
            except Exception:
                logger.warning('No ID: {}'.format(num))
                return 1
        logger.debug('Delete num {} from these words: {}'.format(num, words))
        with shelve.open(self.db_docs_to_words) as db:
            for word in words:
                temp = db[word]
                temp.remove(num)
                db[word] = temp
                # if len(db[word]) == 0:
                #    db.remove(word)
        logger.info('Deleted ID: {}'.format(num))
        return 0
