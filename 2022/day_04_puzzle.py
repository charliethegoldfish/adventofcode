# utils.py
import utils

# File names
input_fname = "day_04_input.txt"
ex_input_fname = "day_04_ex_input.txt"

input_list = []
ex_input_list = []

def parse_files():
    utils.parse_file(ex_input_fname, ex_input_list)
    utils.parse_file(input_fname, input_list)

def get_list_of_pairs(input):
    pairs_list = []
    for pair in input:
        split_pair = pair.split(',')
        pairs_list.append(split_pair)
    return pairs_list

def is_range_inside_range(start_range, end_range, start_other_range, end_other_range):
    if start_range >= start_other_range and end_range <= end_other_range:
        return True
    return False

def is_overlappingg_range(pair):
    first_range = pair[0].split('-')
    second_range = pair[1].split('-')

    first_start = int(first_range[0])
    first_end = int(first_range[1])

    second_start = int(second_range[0])
    second_end = int(second_range[1])

    if is_range_inside_range(first_start, first_end, second_start, second_end):
        return True
    elif is_range_inside_range(second_start, second_end, first_start, first_end):
        return True
    else:
        return False

def total_overlapping_ranges(pairs):
    total = 0
    for pair in pairs:
        if is_overlappingg_range(pair):
            total += 1
    return total

def display_answer():
    # Part 1 - Example
    ex_pairs = get_list_of_pairs(ex_input_list)
    print("Example - Pairs:", ex_pairs)
    ex_total = total_overlapping_ranges(ex_pairs)
    print("Example - Total Overlaps:", ex_total)

    pairs = get_list_of_pairs(input_list)
    total = total_overlapping_ranges(pairs)
    print("Answer - Total Overlaps:", total)

parse_files()
display_answer()