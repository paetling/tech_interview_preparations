
# [-1, 5, 4, 2, 15, -20, 3]
# [5, 4, 2, 15, -20, 3, 15, -10, 18]
# [5] [-5, 4]
#  compare just 5, 5 -5, 5 -5 4 and 4
def maximum_subvector_baseline(array):
    global_current_max = 0
    for i in range(len(array)):
        for j in range(i, len(array)):
            sub_array = array[i:j + 1]
            total = sum(sub_array)
            if(total > global_current_max):
                global_current_max = total
    return global_current_max


# if left sum is < negative value, do not include the negative value
# if left sum is > negative value, but right sum is less then negative value, do not include the negative value
# if both sums are > negative value, include both

def max_left_continues_vector(array):
    if len(array) == 1:
        return array

    vector = max_left_continues_vector(array[1:])
    if sum(vector) > 0:
        return [array[0]] + vector

    return [array[0]]

print max_left_continues_vector([1, 2, 3, -5, 4])
print max_left_continues_vector([1, 2, 3, -5, 6])

def maximum_subvector_bit_better(array):
    start = 0
    end = 0
    racer = 0

    max_sum = 0

    current_sum = 0
    while end < len(array):
        if (array[end] < 0):
            if current_sum + array[end] < 0 or sum(max_left_continues_vector(array[end+1:])) +  array[end] < 0:
                if (current_sum) > max_sum:
                    max_sum = current_sum
                current_sum = 0

        current_sum += array[end]
        end += 1
    return max(max_sum, current_sum)



def maximum_subvector_book_solution(array):
    current_max = 0
    max_ending_at_i = 0

    for i in range(len(array)):
        value = array[i]
        max_ending_at_i = max(max_ending_at_i + value, 0)
        current_max = max(current_max, max_ending_at_i)
    return current_max





print maximum_subvector_baseline([5, -3, 4])
print maximum_subvector_baseline([5, -10, 4])
print maximum_subvector_baseline([5, 5, 4])
print maximum_subvector_baseline([5, 4, 2, 15, -20, 3, 15, -10, 18])

print
print
print maximum_subvector_bit_better([5, -3, 4])
print maximum_subvector_bit_better([5, -10, 4])
print maximum_subvector_bit_better([5, 5, 4])
print maximum_subvector_bit_better([5, 4, 2, 15, -20, 3, 15, -10, 18])

print
print
print maximum_subvector_book_solution([5, -3, 4])
print maximum_subvector_book_solution([-8, 5, -3, 4])
print maximum_subvector_book_solution([5, -3, 2, -1, 5])
print maximum_subvector_book_solution([5, -10, 4])
print maximum_subvector_book_solution([5, 5, 4])
print maximum_subvector_book_solution([5, 4, 2, 15, -20, 3, 15, -10, 18])




# array of costs between distances: [5, 10, 15, 20] - 5 between 0 and 1, 10 between 1 and 2, etc
# [5, 15, 30, 50]
# [i1, i1 + i2, i1 + i2 + i3, i1+ i2 + i3 + i4]
def turn_pike_cost():
    return
