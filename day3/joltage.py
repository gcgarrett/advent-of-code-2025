import logging

logging.basicConfig(level=logging.DEBUG)

f = open('./puzzle_input')

total_joltage = 0

def find_highest(sub_bank):
    highest_index = -1
    highest_battery = -1

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


while(True):
    bank_str = f.readline().strip()

    if bank_str == '':
        break

    bank = list(map(int, list(bank_str)))
    total_joltage += calculate_joltage(bank)

logging.info(f'Total joltage is: {total_joltage}')
