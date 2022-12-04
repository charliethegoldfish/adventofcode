# utils.py
import utils

# Setup variables

# File names
input_fname = "dayOne_input.txt"
example_input_fname = "dayOne_exampleInput.txt"

input_list = []
example_input_list = []

def parse_files():
    utils.parse_file(input_fname, input_list)
    utils.parse_file(example_input_fname, example_input_list)

def get_elves_calories_each(list):
    elves = [0]
    index = 0

    for item in list:
        if item == "":
            elves.append(0)
            index += 1
            continue
        
        elves[index] += int(item);
    
    return elves

def find_most_calories(elves):
    most_calories = 0

    for elf in elves:
        if elf > most_calories:
            most_calories = elf
    
    return most_calories

def top_elves_most_calories(elves, top_count):
    top_elves = []

    for i in range(0, top_count):
        if i >= len(elves):
            break

        top_elves.append(elves[-(i + 1)])

    return top_elves

def get_total_calories(elves):
    total_calories = 0

    for elf in elves:
        total_calories += elf
    
    return total_calories


def display_answer():
    ex_elves_calories = get_elves_calories_each(example_input_list)
    ex_most_calories = find_most_calories(ex_elves_calories)   
    print("Example - Most Calories:", ex_most_calories)

    ex_elves_len = len(ex_elves_calories)
    utils.merge_sort(ex_elves_calories, 0, ex_elves_len - 1)
    ex_top_elves = top_elves_most_calories(ex_elves_calories, 3)
    ex_top_elves_total_cals = get_total_calories(ex_top_elves)
    print("Example - Sorted Elves:", ex_elves_calories)
    print("Example - Top Elves", ex_top_elves)
    print("Example - Top Elves Total Calories:", ex_top_elves_total_cals)
    
    
    elves_calories = get_elves_calories_each(input_list)
    most_calories = find_most_calories(elves_calories)
    print("Answer - Most Calories:", most_calories)

    elves_len = len(elves_calories)
    utils.merge_sort(elves_calories, 0, elves_len - 1)
    top_elves = top_elves_most_calories(elves_calories, 3)
    top_elves_total_cals = get_total_calories(top_elves)
    print("Example - Top Elves", top_elves)
    print("Example - Top Elves Total Calories:", top_elves_total_cals)

parse_files()
display_answer()