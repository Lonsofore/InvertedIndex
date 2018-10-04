import time

from grpc import RpcError

from .config import CONFIG
from .Client import Client


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
                # print(e)
        elif len(arr) == 1 and arr[0] == 'exit':
            break
        else:
            print('* Invalid command *')
    print('Exit...')

if __name__ == '__main__':
    start()
