''' This is my boilerplate config that I use in all of my projects '''
import logging
import argparse
from pathlib import Path



''' SET UP LOGGING '''
class Fmt(logging.Formatter):
    COLORS = {'DEBUG': '\033[1;45m', 'INFO': '\033[1;32m', 'WARNING': '\033[1;33m', 'ERROR': '\033[1;41m'}
    def format(self, record):
        color = self.COLORS.get(record.levelname, '')
        record.levelname = f"{color}{record.levelname}\033[1;0m"
        return super().format(record)

def setup_logger():
    logger = logging.getLogger('main')
    logger.setLevel(logging.INFO)
    ch = logging.StreamHandler()
    ch.setFormatter(Fmt('%(asctime)s|%(levelname)s|%(filename)s:%(lineno)d|%(message)s', '%d-%m-%Y|%H:%M:%S'))
    logger.addHandler(ch)


''' READ CONFIGURATIONS (FROM ARGPARSE) '''
def parse_args() -> dict:
    # define parser
    parser = argparse.ArgumentParser()

    # define arguments
    parser.add_argument('--specify-zone', action='store_true', help="Specify the restricted zone before detection")

    # parse args
    args = parser.parse_args()

    return vars(args)
