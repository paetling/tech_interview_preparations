
def binary_search(array, value):
    lower = 0
    upper = len(array) - 1
    while lower <= upper:
        guess_index = (upper + lower) / 2
        if array[guess_index] ==  value:
            return guess_index
        elif array[guess_index] < value:
            lower = guess_index + 1
        else:
            upper = guess_index - 1

    return - 1

def binary_search_ordered_return(array, value):
    lower = 0
    upper = len(array) - 1

    dummy_value = value - 1
    response = -1
    while lower < upper:
        guess_index = (upper + lower) / 2
        if array[guess_index] ==  dummy_value:
            response =  guess_index
            break
        elif array[guess_index] < dummy_value:
            lower = min(guess_index + 1, upper)
        else:
            upper = max(guess_index - 1, lower)

    if response != -1 and response + 1 < len(array):
        if array[response + 1] == value:
            return response + 1
        else:
            return -1

    if (lower >= 0 and lower < len(array) and array[lower] == value):
        return lower
    if lower + 1 < len(array) and array[lower + 1] == value:
        return lower + 1

    return -1

def recursive_binary_search(array, value):
    # print array, value
    lower = 0
    upper = len(array) - 1
    guess_index = (upper + lower) / 2
    if (guess_index < 0 or guess_index >= len(array)):
        return -1

    if array[guess_index] ==  value:
        return guess_index
    elif array[guess_index] < value:
        found_index = recursive_binary_search(array[guess_index+1:upper+1], value)
        # print 'found_index', found_index
        return found_index if found_index == -1 else found_index + guess_index + 1
    else:
        found_index = recursive_binary_search(array[lower:guess_index], value)
        # print 'found_index', found_index
        return found_index if found_index == -1 else found_index + lower

print binary_search([], 5)
print binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5)
print binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10)
print binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 11)
print binary_search([2, 200, 2000, 2015, 4000, 1000000, 500000000], 4000)
print binary_search([2, 200, 2000, 2015, 4000, 1000000, 500000000], 4001)

print
print binary_search_ordered_return([], 5)
print binary_search_ordered_return([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5)
print binary_search_ordered_return([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10)
print binary_search_ordered_return([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 11)
print binary_search_ordered_return([2, 200, 2000, 2015, 4000, 1000000, 500000000], 4000)
print binary_search_ordered_return([2, 200, 2000, 2015, 4000, 1000000, 500000000], 4001)

print
print recursive_binary_search([], 5)
print recursive_binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5)
print recursive_binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10)
print recursive_binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 11)
print recursive_binary_search([2, 200, 2000, 2015, 4000, 1000000, 500000000], 4000)
print recursive_binary_search([2, 200, 2000, 2015, 4000, 1000000, 500000000], 4001)

print
print binary_search_ordered_return([1, 2, 3, 3, 3, 4, 5, 6], 3)
print binary_search_ordered_return([1, 2, 3, 3, 3, 3,3,3,3,3,3,3,4, 5, 6], 3)
print binary_search_ordered_return([1, 2, 3,4, 5, 6], 3)
print binary_search_ordered_return([1, 2, 3, 3, 3, 3, 3, 3,3 ,3, 3, 3, 3, 3, 3, 3, 3], 3)
