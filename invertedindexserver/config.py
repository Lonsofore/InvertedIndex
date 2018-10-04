import os
import sys

from appdirs import AppDirs
import nltk

from invertedindexserver import CONFIG_NAME, CONFIG_DEFAULT, CONFIG_FORMAT, AUTHOR, PACKAGE_NAME
from .utility import get_script_dir, create_dir_if_not_exists, get_config


# init dirs
DIRS = AppDirs(PACKAGE_NAME, AUTHOR)


# init config
CONFIG_PATH_DEFAULT = os.path.join(get_script_dir(), '{}.{}'.format(CONFIG_DEFAULT, CONFIG_FORMAT))
CONFIG_PATH = os.path.join(DIRS.user_config_dir, '{}.{}'.format(CONFIG_NAME, CONFIG_FORMAT))
if not os.path.isfile(CONFIG_PATH):
    create_dir_if_not_exists(CONFIG_PATH)
    conf = open(CONFIG_PATH_DEFAULT, 'r').read()
    conf1 = open(CONFIG_PATH, 'w').write(conf)
    
    # to use it just once
    nltk.download('punkt') 
CONFIG = get_config(CONFIG_PATH)


# init data
if CONFIG['db']['path'] == '':
    DATA_DIR = DIRS.user_data_dir
else:
    DATA_DIR = CONFIG['db']['path']
create_dir_if_not_exists('{}/'.format(DATA_DIR))
    
WORDS_TO_DOCS_PATH = os.path.join(DATA_DIR, CONFIG['db']['words_to_docs'])
DOCS_TO_WORDS_PATH = os.path.join(DATA_DIR, CONFIG['db']['docs_to_words'])
    
    
# init logs
if CONFIG['log']['path'] == '':
    LOG_DIR = DIRS.user_log_dir
else:
    LOG_DIR = CONFIG['log']['path']
    
LOG_PATH = os.path.join(LOG_DIR, '{}.log'.format(CONFIG['log']['name']))
create_dir_if_not_exists(LOG_PATH)