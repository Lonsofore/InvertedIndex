import logging
import os
import sys
import time

from invertedindex import CONFIG_NAME
from .utility import get_config
from .Server import Server
from .Client import Client


CONFIG = get_config(CONFIG_NAME)
LOG_PATH = os.path.join(CONFIG['log']['path'], CONFIG['log']['name'])


format_full = '%(asctime)s (%(filename)s:%(lineno)d %(threadName)s) %(levelname)s - %(name)s: "%(message)s"'
format_short = '%(asctime)s %(levelname)s: "%(message)s"'
formatter_short = logging.Formatter(format_short)
formatter_full = logging.Formatter(format_full)

logging.basicConfig(
    level=logging.WARNING,
    format=format_full,
    datefmt='%m-%d %H:%M',
    filename=LOG_PATH,
    filemode='w'
)

logger = logging.getLogger("index")

handler_console = logging.StreamHandler(sys.stdout)
handler_console.setFormatter(formatter_short)
logger.addHandler(handler_console)
logger.setLevel(logging.DEBUG)


def start():
    server = Server(CONFIG['server']['port'], CONFIG['server']['max_workers'])
    server.start()
    logger.info('Server started')
    
    client = Client(CONFIG['client']['host'], CONFIG['client']['port'])
    id=client.add('test line hello world blah')
    client.add('aaaaaaaaassssssssssssssdddddddddddddddddd blah blah')
    client.add('new test line hello again')
    client.add('blah blah blah crap')
    client.add('again test line, make sure it works blah')
    client.add('some shit again')
    client.add('again, make sure it works') 
    # print(client.get_docs_count())
    # print(client.get_all_sorted())
    print(client.search('test blah it'))   
    print(client.delete(id))
    
    
    # since server.start() will not block,
    # a sleep-loop is added to keep alive
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop()


    """
    index = Index(DB_WORDS_TO_DOCS, DB_DOCS_TO_WORDS)
    index.add('test line hello world blah')
    index.add('aaaaaaaaassssssssssssssdddddddddddddddddd blah blah')
    index.add('new test line hello again')
    index.add('blah blah blah crap')
    index.add('again test line, make sure it works blah')
    index.add('some shit again')
    index.add('again, make sure it works')   
    print(index.get_docs_count())
    print(index.get_all_sorted())
    print(index.search('test blah it'))   
    """


if __name__ == '__main__':
    start()
