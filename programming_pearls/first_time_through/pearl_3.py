def binary_search(current_array, target):
    top_index = len(current_array)
    bottom_index = 0;
    while (top_index >= bottom_index and top_index >= 0 and bottom_index  < len(current_array)):
        # print bottom_index, top_index, len(current_array)
        middle_index = (top_index+bottom_index) / 2
        middle_number = current_array[middle_index]
        # print middle_index, middle_number
        if (middle_number == target):
            return middle_index
        elif (middle_number < target):
            bottom_index = middle_index + 1
        else:
            top_index = middle_index - 1

    return -1

print 'first tests'
print binary_search([1,2,3,4,5,6,7,8,9], 1)
print binary_search([1,2,3,4,5,6,7,8,9], 4)
print binary_search([1,2,3,4,5,6,7,8,9], 9)
print binary_search([1,2,3,4,5,6,7,8,9], 10)

print binary_search([1, 5, 9, 15, 27, 105], 4)
print binary_search([1, 5, 9, 15, 27, 105], 9)
print binary_search([1, 5, 9, 15, 27, 105], 105)


def rec_binary_search(current_array, target):
    if (len(current_array) == 0):
        return -1
    if (len(current_array) == 1):
        return 0 if current_array[0] == target else -1

    middle_index = (len(current_array) - 1) / 2
    middle_number = current_array[middle_index]
    if (middle_number == target):
        return middle_index
    elif(middle_number > target):
        found_index = rec_binary_search(current_array[0:middle_index], target)
        return -1 if found_index == -1 else found_index
    else:
        found_index = rec_binary_search(current_array[middle_index+1:], target)
        return -1 if found_index == -1 else found_index + middle_index + 1


print 'second tests'
print rec_binary_search([1,2,3,4,5,6,7,8,9], 1)
print rec_binary_search([1,2,3,4,5,6,7,8,9], 4)
print rec_binary_search([1,2,3,4,5,6,7,8,9], 9)
print rec_binary_search([1,2,3,4,5,6,7,8,9], 10)

print rec_binary_search([1, 5, 9, 15, 27, 105], 4)
print rec_binary_search([1, 5, 9, 15, 27, 105], 9)
print rec_binary_search([1, 5, 9, 15, 27, 105], 105)
