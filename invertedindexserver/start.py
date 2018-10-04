import sys
import logging
import time

from .config import CONFIG, LOG_PATH
from .Server import Server


# init logs
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
        max_workers=CONFIG['server']['max_workers']
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
        
    logger.info('Server stopped')


if __name__ == '__main__':
    start()
