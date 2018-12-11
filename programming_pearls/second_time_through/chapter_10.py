# Sorting

def swap(array, i, j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp

def bubble_sort(array):
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if (array[i] > array[j]):
                swap(array, i, j)
    return array

def insertion_sort(array):
    for i in range(len(array)):
        j = i + 1
        while j -1 >= 0 and j < len(array) and array[j] < array[j-1]:
            swap(array, j, j-1)
            j -= 1
    return array

def selection_sort(array):
    for i in range(len(array)):
        min_val = 100000000000
        min_index = i
        for j in range(i, len(array)):
            val = array[j]
            if val < min_val:
                min_val = val
                min_index = j
        swap(array, i, min_index)

    return array

def merge_sort(array):
    if len(array) <= 1:
        return array

    sorted_left = merge_sort(array[0: len(array)/2])
    sorted_right = merge_sort(array[len(array)/2: len(array)])

    new_array = []
    while len(sorted_left) > 0 and len(sorted_right) > 0:
        if (sorted_left[0] < sorted_right[0]):
            new_array.append(sorted_left.pop(0))
        else:
            new_array.append(sorted_right.pop(0))

    return new_array + sorted_left + sorted_right

import random

# [10, 9, 8, 7, 6, 15, 4, 3, 2, 1]
# [8, 9, 10, 7, 6, 15, 4, 3, 2, 1]
# [8, 1, 10, 7, 6, 15, 4, 3, 2, 9]
# [8, 1, 2, 7, 6, 15, 4, 3, 10, 9]
# [8, 1, 2, 3, 6, 15, 4, 7, 10, 9]
# [8, 1, 2, 3, 7, 15, 4, 6, 10, 9]
# [8, 1, 2, 3, 7, 6, 4, 15, 10, 9]
# [4, 1, 2, 3, 7, 6, 8, 15, 10, 9]


# [10, 9, 8, 7, 8, 9, 10, 11, 12]
def quick_sort(array):
    if len(array) <= 1:
        return array

    pivot_index = random.randint(0, len(array) - 1)
    pivot = array[pivot_index]

    swap(array, 0, pivot_index)

    fixed_left_side = 0
    current_index = len(array) - 1
    while (current_index > fixed_left_side):
        if (array[current_index] < pivot):
            fixed_left_side += 1
            swap(array, current_index, fixed_left_side)
        else:
            current_index -= 1

    swap(array, 0, fixed_left_side)

    array[0:fixed_left_side] = quick_sort(array[0:fixed_left_side])
    array[fixed_left_side+1: len(array)] = quick_sort(array[fixed_left_side+1: len(array)])
    return array

def book_quick_sort(array, l, u):
    if l >= u:
        return array

    swap(array, l, random.randint(l, u))
    pivot = array[l]
    fixed_left = l
    walker = l + 1

    # print array, pivot, l, walker
    while walker <= u:
        if (array[walker] < pivot):
            fixed_left += 1
            swap(array, walker, fixed_left)

        walker += 1

    # print array, l, fixed_left
    swap(array, l, fixed_left)
    # print array

    book_quick_sort(array, l, fixed_left)
    book_quick_sort(array, fixed_left + 1, u)

    return array




print bubble_sort([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print bubble_sort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
print bubble_sort([5, -1, 4, -3, 2, 100, 5000, 15])

print
print
print insertion_sort([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print insertion_sort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
print insertion_sort([5, -1, 4, -3, 2, 100, 5000, 15])

print
print
print selection_sort([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print selection_sort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
print selection_sort([5, -1, 4, -3, 2, 100, 5000, 15])

print
print
print merge_sort([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print merge_sort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
print merge_sort([5, -1, 4, -3, 2, 100, 5000, 15])

print
print
print quick_sort([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print quick_sort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
print quick_sort([5, -1, 4, -3, 2, 100, 5000, 15])

print
print
print book_quick_sort([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0, 9)
print book_quick_sort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 0, 9)
print book_quick_sort([5, -1, 4, -3, 2, 100, 5000, 15], 0, 7)
