import getopt
import logging
import sys
from functools import reduce

logging.basicConfig(level=logging.DEBUG)

JOLTAGE_LIMIT_SAFETY_OVERRIDE = False

# command line arguments
#   -o --override: overrides the joltage safety limit
opts, args = getopt.getopt(sys.argv[1:], 'o', ['override'])

for opt, arg in opts:
    print(opt)
    if opt in ('-o', '--override'):
        JOLTAGE_LIMIT_SAFETY_OVERRIDE = True

f = open('./puzzle_input')

total_joltage = 0

def find_highest(sub_bank):
    highest_index = -1
    highest_battery = -1

    logging.debug(f'Sub bank: {sub_bank}')

    for index, battery in enumerate(sub_bank):
        if battery > highest_battery:
            highest_index = index
            highest_battery = battery

    return highest_index, highest_battery

def calculate_joltage(bank):
    logging.debug(f'Batteries are: {bank}')
    first_battery_index, first_battery = find_highest(bank[:-1])
    logging.debug(f'First index: {first_battery_index}; first battery: {first_battery}')

    second_start_index = first_battery_index + 1
    second_battery_index, second_battery = find_highest(bank[second_start_index:])
    logging.debug(f'Second index: {second_battery_index}; second battery: {second_battery}')

    return (first_battery * 10) + second_battery

def calculate_largest_joltage(bank):
    joltages = []
    start_index = 0

    while len(joltages) < 12:
        remaining = 12 - (len(joltages) + 1)
        end_index = len(bank) - remaining
        highest_index, highest_battery = find_highest(bank[start_index:end_index])
        joltages.append(highest_battery)
        start_index = start_index + highest_index + 1

    logging.debug(f'Joltages: {joltages}')
    return reduce(lambda x, y: (x * 10) + y, joltages)

while(True):
    bank_str = f.readline().strip()

    if bank_str == '':
        break

    bank = list(map(int, list(bank_str)))

    if not JOLTAGE_LIMIT_SAFETY_OVERRIDE:
        total_joltage += calculate_joltage(bank)
    else:
        total_joltage += calculate_largest_joltage(bank)

logging.info(f'Total joltage is: {total_joltage}')
