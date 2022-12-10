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

rucksacks_per_group = 3

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
    grouped_rucksacks = []
    current_group = []
    current_count = 0;
    
    for rucksack in input:
        current_group.append(rucksack)
        current_count += 1

        if current_count % rucksacks_per_group == 0:
            grouped_rucksacks.append(current_group)
            current_group = []

    return grouped_rucksacks

def is_item_in_rucksack(item, rucksack):
    return rucksack.find(item) != -1

def find_item_in_group(rucksacks):
    num_in_group = len(rucksacks)

    for item in rucksacks[0]:
        found = True
        for index in range(1, num_in_group):
            if not is_item_in_rucksack(item, rucksacks[index]):
                found = False
        if found:
            return item

def find_group_items(rucksacks):
    items = []

    for group in rucksacks:
        item = find_item_in_group(group)
        items.append(item)
    
    return items

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
    # Part 1
    # print("Example - Input list:", example_input_list)
    example_rucksacks = fill_rucksack_compartments(example_input_list)
    # print("Example - Rucksacks:", example_rucksacks)
    ex_items = found_items(example_rucksacks)
    print("Example - Found items:", ex_items)
    ex_total_priorities = get_total_priorities(ex_items)
    print("Example - Total priorities:", ex_total_priorities)

    # Part 2
    ex_grouped_rucksacks = group_rucksacks(example_input_list)
    # print("Example - Grouped rucksacks:", ex_grouped_rucksacks)
    ex_group_items = find_group_items(ex_grouped_rucksacks)
    print("Example - Found group items:", ex_group_items)
    ex_group_priorities = get_total_priorities(ex_group_items)
    print("Example - Total group priorities:", ex_group_priorities)

    # Part 1
    rucksacks = fill_rucksack_compartments(input_list)
    items = found_items(rucksacks)
    # print("Answer Found items:", items)
    total_priorities = get_total_priorities(items)
    print("Answer - Total Priorities", total_priorities)

    # Part 2
    grouped_rucksacks = group_rucksacks(input_list)
    group_items = find_group_items(grouped_rucksacks)
    total_group_priorities = get_total_priorities(group_items)
    print("Answer - Total Group Priorities", total_group_priorities)


parse_files()
display_answers()