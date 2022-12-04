
# Setup variables

# File names
input_fname = "dayOne_input.txt"
example_input_fname = "dayOne_exampleInput.txt"

input_list = []
example_input_list = []

# Function for reading in input
def parse_file(file_name, output):
    file = open(file_name, "r")

    for line in file:
        line_stripped = line.strip('\n')
        output.append(line_stripped)

    file.close()

def parse_files():
    parse_file(input_fname, input_list)
    parse_file(example_input_fname, example_input_list)

def get_elves_calories_each(list):
    elves = [0]
    index = 0

    for item in list:
        if item == "":
            elves.append(0)
            index += 1
            continue
        
        elves[index] = elves[index] + int(item);
    
    return elves

def find_most_calories(elves):
    most_calories = 0

    for elf in elves:
        if elf > most_calories:
            most_calories = elf
    
    return most_calories


def display_answer():
    ex_elves_calories = get_elves_calories_each(example_input_list)
    ex_most_calories = find_most_calories(ex_elves_calories)   
    print("Example - Most Calories:", ex_most_calories)
    
    
    elves_calories = get_elves_calories_each(input_list)
    most_calories = find_most_calories(elves_calories)
    print("Answer - Most Calories:", most_calories)

parse_files()
display_answer()