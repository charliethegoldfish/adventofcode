# 2022 - Day 5 Puzzle
# https://adventofcode.com/2022/day/5

# utils.py
import utils

# File names
input_fname = "day_05_input.txt"
ex_input_fname = "day_05_ex_input.txt"

# input_list = []
# ex_input_list = []

layout_input = []
move_input = []

ex_layout_input = []
ex_move_input = []

def split_input(input_var, splitter):
    output = input_var.split(splitter)
    return output

def parse_files():
    ex_file_output = utils.return_file_output(ex_input_fname)
    ex_split_output = split_input(ex_file_output, "\n\n")
    
    # utils.parse_file(ex_input_fname, ex_input_list)
    # utils.parse_file(input_fname, input_list)

def display_answer():
    print("*** Example ***")
    print("Layout String:", ex_layout_input)
    print("Move String:", ex_move_input)

    print()
    
    print("*** Answer ***")

parse_files()
display_answer()