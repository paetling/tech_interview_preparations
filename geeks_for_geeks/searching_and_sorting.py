import sys
# Max heap to find min K value
# [3, 4, 2, 1, 5, 7, 8, 6]

# k = 2
# 1. MH =  4, 3
# 2. MH = 3, 2
# 3. MH = 2, 1

# k = 6
# MH = 6, 5, 4, 3, 2, 1


# initially - K values sorted by largest
# at end you have a largest set of the k smallest values

def kth_smallest_element_in_an_array(array, k):
    pass


# find the pair of numbers whose sum is closest to sum
# sum = x1 + x2
# sum - x2 = x1
# [10, 22, 28, 29, 30, 40],
# sum = 54 -> 10, 40
# sum = 38 -> 10, 30
# [1, 2, 4, 7, 10] -> 15
# moving left decreases, moving right increases
# move in the direction needed till you cross from less to more or hit values or some other edge case
def sorted_array_closest_sum(sorted_array, goal_sum):
    left_pointer = 0
    right_pointer = len(sorted_array) - 1

    min_diff = sys.maxint
    min_pair = None

    while (left_pointer != right_pointer):
        current_sum = sorted_array[left_pointer] + sorted_array[right_pointer]
        abs_diff = abs(goal_sum - current_sum)
        if abs_diff < min_diff:
            min_diff = abs_diff
            min_pair = (left_pointer, right_pointer)

        if current_sum == goal_sum:
            break

        elif current_sum < goal_sum:

            left_pointer = left_pointer + 1

        else:
            right_pointer = right_pointer - 1

    return sorted_array[min_pair[0]], sorted_array[min_pair[1]]

print sorted_array_closest_sum([10, 22, 28, 29, 30, 40], 54)
print sorted_array_closest_sum([1,2,4,7,10], 15)


