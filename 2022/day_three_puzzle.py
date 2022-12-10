# utils.py
import utils

# File names
input_fname = "dayThree_input.txt"
example_input_fname = "dayThree_exampleInput.txt"

input_list = []
example_input_list = []

# priorities are: 
# a - z = 1 - 26
# A - Z = 27 - 52
priority_string = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def parse_files():
    utils.parse_file(example_input_fname, example_input_list)
    utils.parse_file(input_fname, input_list)

def fill_rucksack_compartments(input):
    rucksacks = []
    for rucksack in input:
        first, second = rucksack[:len(rucksack)//2], rucksack[len(rucksack)//2:]
        compartments = [first, second]
        rucksacks.append(compartments)
    return rucksacks

def group_rucksacks(input):
    pass

def find_item_in_group(rucksacks):
    pass

def find_item_in_both_compartments(rucksack):
    for item in rucksack[0]:
        if rucksack[1].find(item) != -1:
            return item

def found_items(rucksacks):
    items = []

    for rucksack in rucksacks:
        item = find_item_in_both_compartments(rucksack)
        items.append(item)
    
    return items

def get_total_priorities(items):
    total = 0
    for item in items:
        total += priority_string.index(item) + 1
    return total


def display_answers():
    # print("Example - Input list:", example_input_list)
    example_rucksacks = fill_rucksack_compartments(example_input_list)
    # print("Example - Rucksacks:", example_rucksacks)
    ex_items = found_items(example_rucksacks)
    print("Example - Found items:", ex_items)
    ex_total_priorities = get_total_priorities(ex_items)
    print("Example - Total priorities:", ex_total_priorities)

    rucksacks = fill_rucksack_compartments(input_list)
    items = found_items(rucksacks)
    print("Answer Found items:", items)
    total_priorities = get_total_priorities(items)
    print("Answer - Total Priorities", total_priorities)

parse_files()
display_answers()