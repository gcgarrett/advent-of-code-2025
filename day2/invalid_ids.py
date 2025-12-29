import logging

logging.basicConfig(level=logging.INFO)

f = open('./puzzle_input')
line = f.readline()
ranges = line.split(',')
invalid_id_total = 0

def is_invald_id(id):
    id = str(id)
    logging.debug(f'ID {id} is of length {len(id)}')
    if len(id) % 2 != 0:
        return False

    midpoint = len(id) // 2
    logging.debug(f'Midpoint: {midpoint}')
    first_half, last_half = id[:midpoint], id[midpoint:]

    return first_half == last_half

for r in ranges:
    logging.debug(f'Range: {r}')
    range_ends = r.split('-')
    start, end = int(range_ends[0]), int(range_ends[1])
    logging.debug(f'Start: {start}; End: {end}')
    for id in range(start, end + 1):
        if is_invald_id(id):
            logging.info(f'Invalid ID found: {id}')
            invalid_id_total += int(id)

logging.info(f'Total is: {invalid_id_total}')
