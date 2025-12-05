import getopt
import logging
from math import floor
import sys

logging.basicConfig(level=logging.INFO)

PASSWORD_METHOD = False

# command line arguments
#   -p --password-method: uses the 0x434C49434B password method
opts, args = getopt.getopt(sys.argv[1:], 'p', ['password-method'])

for opt, arg in opts:
    print(opt)
    if opt in ('-p', '--password-method'):
        PASSWORD_METHOD = True

f = open('./puzzle_input')

zeroCount = 0
position = 50

def right(start, clicks):
    position = start

    while(clicks > 0):
        position = position + 1

        if position == 100:
            if PASSWORD_METHOD and clicks != 1:
                global zeroCount
                zeroCount = zeroCount + 1
                logging.debug(f'Bumping zero count {zeroCount}')
            position = 0

        clicks = clicks - 1

    return position

def left(start, clicks):
    position = start

    while(clicks > 0):
        position = position - 1

        if PASSWORD_METHOD and clicks != 1 and position == 0:
            global zeroCount
            zeroCount = zeroCount + 1
            logging.debug(f'Bumping zero count {zeroCount}')

        if position == -1:
            position = 99

        clicks = clicks - 1

    return position

while(True):
    line = f.readline()

    if line == '':
        break

    direction = line[:1]
    clicks = int(line[1:])
    logging.debug(f'Direction: {direction}')
    logging.debug(f'Clicks: {clicks}')

    if direction == 'R':
        position = right(position, clicks)
    else:
        position = left(position, clicks)

    logging.debug(f'New position: {position}')

    if position == 0:
        zeroCount = zeroCount + 1

logging.info(f'Password is: {zeroCount}')
