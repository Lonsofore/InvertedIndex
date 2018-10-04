import argparse
from subprocess import call


def start():
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--server', action='store_true')
    parser.add_argument('-c', '--client', action='store_true')
    args = parser.parse_args()
    
    try:
        if args.server:
            call('invertedindexserver')
        elif args.client:
            call('invertedindexclient')
        else:
            parser.print_help()
    except KeyboardInterrupt:
        pass
        

if __name__ == '__main__':
    start()
