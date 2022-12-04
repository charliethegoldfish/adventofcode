
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
        
        elves[index] += int(item);
    
    return elves

def find_most_calories(elves):
    most_calories = 0

    for elf in elves:
        if elf > most_calories:
            most_calories = elf
    
    return most_calories

# Merge Sort algorithm
def merge(arr, left, mid, right):
    left_length = mid - left + 1
    right_length = right - mid

    # temp arrays
    left_array = [0] * left_length
    right_array = [0] * right_length

    for i in range(0, left_length):
        left_array[i] = arr[left + i]

    for j in range(0, right_length):
        right_array[j] = arr[mid + 1 + j]

    i = 0
    j = 0
    k = left

    while i < left_length and j < right_length:
        if left_array[i] < right_array[j]:
            arr[k] = left_array[i]
            i += 1
        else:
            arr[k] = right_array[j]
            j += 1
        k += 1

    while i < left_length:
        arr[k] = left_array[i]
        i += 1
        k += 1

    while j < right_length:
        arr[k] = right_array[j]
        j += 1
        k += 1

def merge_sort(arr, left, right):
    if left < right:
        mid = left + (right - left) // 2

        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)
        merge(arr, left, mid, right)

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
    merge_sort(ex_elves_calories, 0, ex_elves_len - 1)
    ex_top_elves = top_elves_most_calories(ex_elves_calories, 3)
    ex_top_elves_total_cals = get_total_calories(ex_top_elves)
    print("Example - Sorted Elves:", ex_elves_calories)
    print("Example - Top Elves", ex_top_elves)
    print("Example - Top Elves Total Calories:", ex_top_elves_total_cals)
    
    
    elves_calories = get_elves_calories_each(input_list)
    most_calories = find_most_calories(elves_calories)
    print("Answer - Most Calories:", most_calories)

    elves_len = len(elves_calories)
    merge_sort(elves_calories, 0, elves_len - 1)
    top_elves = top_elves_most_calories(elves_calories, 3)
    top_elves_total_cals = get_total_calories(top_elves)
    print("Example - Top Elves", top_elves)
    print("Example - Top Elves Total Calories:", top_elves_total_cals)

parse_files()
display_answer()