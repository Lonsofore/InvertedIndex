import logging
import os
import sys
import time

from appdirs import AppDirs

from invertedindexserver import __version__, CONFIG_NAME, CONFIG_DEFAULT, CONFIG_FORMAT, AUTHOR, PACKAGE_NAME
from .utility import get_script_dir, create_dir_if_not_exists, get_config
from .Server import Server


# init dirs
DIRS = AppDirs(PACKAGE_NAME, AUTHOR)


# init config
CONFIG_PATH_DEFAULT = os.path.join(get_script_dir(), '{}.{}'.format(CONFIG_DEFAULT, CONFIG_FORMAT))
CONFIG_PATH = os.path.join(DIRS.user_config_dir, '{}.{}'.format(CONFIG_NAME, CONFIG_FORMAT))
if not os.path.isfile(CONFIG_PATH):
    create_dir_if_not_exists(CONFIG_PATH)
    conf = open(CONFIG_PATH_DEFAULT, 'r').read()
    conf1 = open(CONFIG_PATH, 'w').write(conf)
CONFIG = get_config(CONFIG_PATH)


# init data dir and log dir
if CONFIG['db']['path'] == '':
    DATA_DIR = DIRS.user_data_dir
else:
    DATA_DIR = CONFIG['db']['path']
    
if CONFIG['log']['path'] == '':
    LOG_DIR = DIRS.user_log_dir
else:
    LOG_DIR = CONFIG['log']['path']
    

# init db
WORDS_TO_DOCS_PATH = os.path.join(DATA_DIR, CONFIG['db']['words_to_docs'])
DOCS_TO_WORDS_PATH = os.path.join(DATA_DIR, CONFIG['db']['docs_to_words'])


# init logs
LOG_PATH = os.path.join(LOG_DIR, '{}.log'.format(CONFIG['log']['name']))
create_dir_if_not_exists(LOG_PATH)

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

logger = logging.getLogger("server")

handler_console = logging.StreamHandler(sys.stdout)
handler_console.setFormatter(formatter_short)
logger.addHandler(handler_console)
logger.setLevel(logging.DEBUG)


def start():
    server = Server(
        port=CONFIG['server']['port'], 
        max_workers=CONFIG['server']['max_workers'],
        words_to_docs_path=WORDS_TO_DOCS_PATH, 
        docs_to_words_path=DOCS_TO_WORDS_PATH
    )
    server.start()
    logger.info('Server started')    
    
    # since server.start() will not block,
    # a sleep-loop is added to keep alive
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop()


if __name__ == '__main__':
    start()
