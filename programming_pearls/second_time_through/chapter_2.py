def array_rotate_naive(initial_array, rotate_distance):
    new_array = ['']*len(initial_array)
    for i in range(len(initial_array)):
        new_array[i] = initial_array[(i + rotate_distance) % len(initial_array)]
    return new_array

# [a]
# [a b]
# [a b c]
# for all i in the array
#   a[i] = a[i - rotate distance]
# ['a', 'b', 'c'] ['d', 'e', 'f', 'g']
# ['c', 'b', 'a'] ['g', 'f', 'e', 'd']

# AB -> BA     (ArBr)r

# 1 / 2 + 1 = 0 []
# 2 / 2 + 1 = 1 [0]
# 3 / 2 + 1 = 1 [0]
# 4/ 2 = 2 [0, 1]

# A[0, i] A[i+1, j] A[J, len(A)]
# reverse A[i, 0] A[j, i+1] A[len(a), j]
def _array_reverse(array):
    for i in range(len(array)/2):
        end_index = len(array) - 1 - i

        temp = array[i]
        array[i] = array[end_index]
        array[end_index] = temp
    return array


def array_rotate_based_off_of_subarrays(initial_array, rotate_distance):
    initial_array[0: rotate_distance] = _array_reverse(initial_array[0: rotate_distance])
    initial_array[rotate_distance: len(initial_array)] = _array_reverse(initial_array[rotate_distance: len(initial_array)])
    return _array_reverse(initial_array)


print array_rotate_naive(['a', 'b', 'c', 'd', 'e', 'f', 'g'], 0)
print array_rotate_naive(['a', 'b', 'c', 'd', 'e', 'f', 'g'], 3)
print array_rotate_naive(['a', 'b', 'c', 'd', 'e', 'f', 'g'], 6)

print array_rotate_better(['a', 'b', 'c', 'd', 'e', 'f', 'g'], 0)
print array_rotate_better(['a', 'b', 'c', 'd', 'e', 'f', 'g'], 3)
print array_rotate_better(['a', 'b', 'c', 'd', 'e', 'f', 'g'], 6)
