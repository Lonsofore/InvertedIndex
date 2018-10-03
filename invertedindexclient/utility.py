import os
import sys
import inspect

from ruamel import yaml


NOTSPLIT = ["'", '-']


# split by all non-alphabet chars (except chars in array NOTSPLIT)
def get_words_set(line):
    words = set()
    word = ''
    for letter in line:
        # if it's a letter  OR  it's an exception char after letter
        if letter.isalpha() or (letter in NOTSPLIT and word != ''):
            word += letter.lower()
        else:
            if word != '':
                words.add(word)
            word = ''
    if word != '':
        words.add(word)
    return words

    
def get_script_dir(follow_symlinks=True):
    if getattr(sys, 'frozen', False): # py2exe, PyInstaller, cx_Freeze
        path = os.path.abspath(sys.executable)
    else:
        path = inspect.getabsfile(get_script_dir)
    if follow_symlinks:
        path = os.path.realpath(path)
    return os.path.dirname(path)
    
    
def get_config(path):
    return yaml.safe_load(open(path, "r"))
    

def get_package_name():
    return os.path.basename(sys.argv[0])

    
def create_dir_if_not_exists(d):
    basedir = os.path.dirname(d)
    if not os.path.exists(basedir):
        os.makedirs(basedir)
    open(d, 'a').close()
