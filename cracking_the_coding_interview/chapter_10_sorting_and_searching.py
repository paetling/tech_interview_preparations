import sys
# bucket sort after sorting the strings themselves
# loop through all strings and sort them to get their base
# add the string -> anagram in a hash map
#
# loop over the strings and add all like strings to another
# hash_map from anagraph to string array, concat all the arrays
#
# Big O(N * Wlog(w))
def group_anagrams(strings):

    anagram_to_strings = {}
    for string in strings:
        sorted_string = ''.join(sorted(string))
        if sorted_string not in anagram_to_strings:
            anagram_to_strings[sorted_string] = []

        anagram_to_strings[sorted_string].append(string)

    final_strings = []
    for string_list in anagram_to_strings.values():
        final_strings += string_list
    return final_strings


print
print 'group anagrams'
print group_anagrams(['dog', 'god', 'cat', 'act', 'man', 'amn', 'met'])




# given an array that is rotated some number of times
# you need to find a value
#
# find the max value or the min value and then binary search
#
# [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14]
# can I use mods and do the math normally
#     1 is at 0 + i % N
#     25 is at n -1 + i & n
# if i look at the middle value I can tell if it is lower
# than the first value we want to look for
def search_in_rotated_array(rotated_array, value, left, right):
    mid_point = (left + right) / 2
    if rotated_array[mid_point] == value:
        return mid_point
    if right < left:
        return -1

    if rotated_array[left] < rotated_array[mid_point]:
        if (value >= rotated_array[left] and value <= rotated_array[mid_point]):
            return search_in_rotated_array(rotated_array, value, left, mid_point)
        else:
            return search_in_rotated_array(rotated_array, value, mid_point + 1, right)
    else:
        if (value >= rotated_array[mid_point] and value <= rotated_array[right]):
            return search_in_rotated_array(rotated_array, value, mid_point, right)
        else:
            return search_in_rotated_array(rotated_array, value, left, mid_point - 1)
    return -1

def search_in_ra(rotated_array, value):
    return search_in_rotated_array(rotated_array, value, 0, len(rotated_array) - 1)


print
print 'rotate array binary search'
print search_in_ra([15, 16, 19, 20, 25, 1, 3, 4, 5, 7], 5)



# given an array of strings that is interspersed with empty strings,
# find the location of a given string
# The key here is if you hit a '' to search both directions to find the nearest real word
# The worst case run time of this algorithm is O(N) but you cannot do better than that
def sparse_search(string_array):
    pass


# You are given an array with all numbers from 1 to N
# where N is at most 32000 and you have 10 KB of Memory
# Use a bit vector to represent seen values as 1s in the
# bit vector
def find_duplicates():
    pass


# two way binary search
# [1 2 3 4 5]
# [6 7 8 9 10]
# [11 12 13 14 15]
# [16 17 18 19 20]
# [21 22 23 24 25]
def sorted_matrix_sort(matrix, element):
    if len(matrix) == 0:
        return None

    row_top = 0
    row_bottom = len(matrix) - 1

    col_left = 0
    col_right = len(matrix[0]) - 1

    row_to_search = None

    while row_top + 1 < row_bottom:
        row_mid = (row_top + row_bottom) / 2

        if matrix[row_mid][0] == element:
            return row_mid, 0
        elif matrix[row_mid][0] > element:
            row_bottom = row_mid - 1
        else:
            row_top = row_mid

    row_to_search = row_top if matrix[row_bottom][0] > element else row_bottom

    while col_left <= col_right:
        col_mid = (col_left + col_right) / 2

        if matrix[row_to_search][col_mid] == element:
            return row_to_search, col_mid
        elif matrix[row_to_search][col_mid] < element:
             col_left = col_mid + 1
        else:
            col_right = col_mid - 1

    return None

print
print 'sorted matrix sort'
matrix = [
    [1 ,2 ,3 ,4 ,5],
    [6 ,7 ,8 ,9 ,10],
    [11 ,12 ,13 ,14 ,15],
    [16 ,17 ,18 ,19 ,20],
    [21 ,22 ,23 ,24 ,25]
]
print sorted_matrix_sort(matrix, 13)
print sorted_matrix_sort(matrix, 22)
print sorted_matrix_sort(matrix, 26)

















