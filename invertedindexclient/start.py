import logging
import os
import sys
import time

from appdirs import AppDirs
from grpc import RpcError

from invertedindexclient import __version__, CONFIG_NAME, CONFIG_DEFAULT, CONFIG_FORMAT, AUTHOR, PACKAGE_NAME
from .utility import get_script_dir, get_package_name, create_dir_if_not_exists, get_config
from .Client import Client


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


def start():
    client = Client(CONFIG['host'], CONFIG['port'])
    print('{}\n{} {}\n{} {}\n{} {}\n{}\n{}'.format(
        'Waiting for commands. You can use:',
        'add', str,
        'search', str,
        'delete', int,
        'exit',
        '----------------------------------'
    ))
    line = ''
    while line != 'exit':
        try:
            line = input()
        except KeyboardInterrupt:
            break
        arr = line.split(' ')
        if len(arr) >= 2:
            cmd = arr[0]
            arg = ' '.join(arr[1:])
            try:
                if cmd == 'add':
                    result = client.add(arg)
                    print('Doc ID: {}'.format(result))
                elif cmd == 'search':
                    result = client.search(arg)
                    print('Found in docs: {}'.format(result))
                elif cmd == 'delete':
                    result = client.delete(int(arr[1]))
                    if result:
                        print('Error, wrong ID')
                    else:
                        print('Deleted')
                else:
                    print('Unknown command')
            except RpcError as e:
                print('* RPC error. Check your connection. *')
        else:
            print('* Invalid command *')
    print('Exit...')

if __name__ == '__main__':
    start()
