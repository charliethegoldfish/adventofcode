# Function for reading in input
def parse_file(file_name, output):
    file = open(file_name, "r")

    for line in file:
        line_stripped = line.strip('\n')
        output.append(line_stripped)

    file.close()

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