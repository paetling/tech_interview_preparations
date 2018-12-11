
# given 2 strings, we want to check if string_2 is in string_1. Want to do that in linear time
# "dogogogadog", "ogoga"
# lps['ogoga'] = [0, 0, 1, 2, 0]
def substring(string_1, string_2):
    pass

# want to reverse a string while leaving the alpha numeric characters alone
def reverse_string(string_array):
    if len(string_array) == 0:
        return []

    start = 0
    end = len(string_array) - 1
    character_list  = ['*', '=', '\\', '&', ',', '$']
    while start < end:
        if string_array[start] in character_list:
            start += 1
        elif string_array[end] in character_list:
            end -= 1
        else:
            temp = string_array[start]
            string_array[start] = string_array[end]
            string_array[end] = temp

            start += 1
            end -= 1
    return string_array

print reverse_string(['a', ',', 'b', '$', 'c'])
print reverse_string(['A', 'b', ',', 'c', ',', 'd', 'e', '*', '$'])


def find_sub_sum_in_sorted(number_array, target):
    if len(number_array) == 0:
        return False

    start = 0
    end = len(number_array) - 1

    while start < end:
        if (number_array[start] + number_array[end] < target):
            start += 1
        elif (number_array[start] + number_array[end] > target):
            end -= 1
        else:
            return True
    return False

print
print 'find sub sum'
print find_sub_sum_in_sorted([1,2,3,4,5,6,7,8,9], 10)
print find_sub_sum_in_sorted([1,2,3,14,5,6,7,8,9], 11)
print find_sub_sum_in_sorted([1,2,3,5,6,7,8,9,21], 24)
print find_sub_sum_in_sorted([1,2,3,5,6,7,8,9,21], 33)

# given an array of numbers this returns true if there is a pythagorean triplet in the group
# can I find a sum in an array in linear time,
# [1, 2, 3, 4, 5], 8
def pythagorean_triplet(number_array):
    values_squared = []
    for value in number_array:
        values_squared.append(value ** 2)

    values_squared.sort()

    for i in range(len(values_squared)):
        search_number = values_squared[i]
        array_to_search_in = values_squared[:i]+values_squared[i+1:]
        exists = find_sub_sum_in_sorted(array_to_search_in, search_number)
        if exists:
            return True
    return False

print
print 'pythagorean triplet'
print pythagorean_triplet([3, 1, 4, 6, 5])
print pythagorean_triplet([10, 4, 6, 12, 5])


# given an array, find the length of the longest subarray that can be arranged in contiguous order
# for each iterm find longest subarray ending at i, take the longest one overall
# store a distance, max, min value
# NOTE: this works only if the array values are sorted
def length_of_longest_contiguous(array):
    meta_data_array = []

    for index in range(len(array)):
        value = array[index]

        if len(meta_data_array) == 0:
            meta_data_array.append((1, value, value))
        else:
            past_metadata_value = meta_data_array[index - 1]
            print past_metadata_value, value
            if value >= past_metadata_value[1] - 1 and value <= past_metadata_value[2] + 1:
                meta_data_array.append((past_metadata_value[0] + 1, min(value, past_metadata_value[1]), max(value, past_metadata_value[2])))
            else:
                meta_data_array.append((1, value, value))
    max_value = 0
    for meta_data in meta_data_array:
        if meta_data[0] > max_value:
            max_value = meta_data[0]

    return max_value

print
print 'length of longest contiguous'
print length_of_longest_contiguous([10, 12, 11])
