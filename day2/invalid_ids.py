import getopt
import logging
import sys

logging.basicConfig(level=logging.INFO)

MIN_TWO = False

# command line arguments
#   -m, --min: minimum of two repeats
opts, args = getopt.getopt(sys.argv[1:], 'm', ['min'])

for opt, arg in opts:
    logging.debug(f'Option: {opt}')
    if opt in ('-m', '--min'):
        MIN_TWO = True

f = open('./puzzle_input')
line = f.readline()
ranges = line.split(',')
invalid_id_total = 0

def is_invald_id(id, times_repeated):
    logging.debug(f'Checking pattern repeated {times_repeated}')
    logging.debug(f'ID {id} is of length {len(id)}')
    if len(id) % times_repeated != 0:
        return False

    repeat_len = len(id) // times_repeated
    logging.debug(f'Pattern length is: {repeat_len}')
    segments = [id[i:i+repeat_len] for i in range(0, len(id), repeat_len)]
    pattern = segments[0]
    logging.debug(f'Pattern: {pattern}')

    for j in range(1, len(segments)):
        logging.debug(f'Checking pattern "{pattern}" against "{segments[j]}"')
        if pattern != segments[j]:
            return False

    return True

for r in ranges:
    logging.debug(f'Range: {r}')
    range_ends = r.split('-')
    start, end = int(range_ends[0]), int(range_ends[1])
    logging.debug(f'Start: {start}; End: {end}')
    for id in range(start, end + 1):
        id_str = str(id)
        for times_repeated in range(2, len(id_str) + 1):
            if is_invald_id(id_str, times_repeated):
                logging.info(f'Invalid ID found: {id}')
                invalid_id_total += int(id)
                break
            if not MIN_TWO:
                break

logging.info(f'Total is: {invalid_id_total}')
