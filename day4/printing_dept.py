import logging

logging.basicConfig(level=logging.INFO)

f = open('./puzzle_input')

PAPER_DIAGRAM = []
ROLL_SPACE = '@'
EMPTY_SPACE = '.'
accessible_rolls = 0

def count_space(x, y):
    logging.debug(f'Checking space: {x}:{y}')
    if y < 0 or y >= len(PAPER_DIAGRAM[x]):
        return 0
    
    if PAPER_DIAGRAM[x][y] == ROLL_SPACE:
        logging.debug(f'{x}:{y} has a roll!')
        return 1
    else:
        logging.debug(f'{x}:{y} is empty!')
        return 0

def count_row(x, y):
    logging.debug(f'Checking row: {x}')
    count = 0

    if x < 0 or x >= len(PAPER_DIAGRAM):
        return count

    count += count_space(x, y - 1)
    count += count_space(x, y)
    count += count_space(x, y + 1)

    return count

def is_roll_accessible(x, y):
    logging.debug(f'Checking: {x}:{y}')
    count = 0

    count += count_row(x - 1, y)
    count += count_row(x, y) - 1 # subtract this roll
    count += count_row(x + 1, y)

    logging.debug(f'Count is: {count}')

    return count < 4

while(True):
    row_str = f.readline().strip()

    if row_str == '':
        break

    row = list(row_str)
    PAPER_DIAGRAM.append(row)

for row, cols in enumerate(PAPER_DIAGRAM):
    for col, space in enumerate(cols):
        if space == ROLL_SPACE and is_roll_accessible(row, col):
            accessible_rolls += 1

logging.info(f'Rolls accessible by forklift: {accessible_rolls}')
