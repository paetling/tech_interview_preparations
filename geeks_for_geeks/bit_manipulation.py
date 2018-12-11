
# given an array of numbers find the maximum xor subarry off those numbers
# maximum xor subarray ending at i, that includes i
# x ^ y ^ y = x
# [1, 2, 3, 4, 5]
# [0001, 0010, 0011, 0100, 0101]
# [1, 1^2, 1^2^3, 1^2^3^4, 1^2^3^4^5]
# 1 ^ 2 vs 1 ^ 2 ^ 3
#
# [1, 2, 3, 4]
# [0001, 0010, 0011, 0100]
#
# make a new array of xor old value if greater than current value, loop through again and find the max
#
#NOTE: NOT CORRECT
def maximum_xor_subarray(array):
    if len(array) == 0:
        return 0

    new_array = [array[0]]
    for index in range(1, len(array)):
        item = array[index]
        new_array.append(max(item, item^new_array[index-1]))

    print new_array
    return max(new_array)

print maximum_xor_subarray([1,2,3,4])
print maximum_xor_subarray([1,2,3,4,5])
print maximum_xor_subarray([8,1,2,12,7,6])
print maximum_xor_subarray([8, 24, 11])

# magic numbers are multiples of 5, or sums of multiples of 5
# magic numbers: 5, 25, 5 + 25, 125, 125 + 5, 125 + 25, 125 + 30, 625, 625 + 5, 625 + 25, 625 +
# can be represented as bits -> 00000 -> 5: 00001, 25: 00010, 30: 00011, 125: 00100, 130: 00101
def find_nth_magic_number(n):
    total = 0

    power = 1
    while n > 0:
        total += 5 ** power * (n&1)

        n = n >> 1
        power += 1
    return total

print find_nth_magic_number(2)
print find_nth_magic_number(5)
print find_nth_magic_number(7)


# given an array of numbers, return a count of the number of bit differnces across all pairs
# number and itself is always 0
# [1, 2, 3] -> useful pairs 2* ((1,2) (1,3), (2,3)) n choose 2 unique pairs = n! / (n-2)! * 2 = (n * n-1) / 2
# [1, 1 ^ 2, 1 ^ 2 ^ 3, 1^2^3^4]
# 1 ^ 2, 3 ^ 4   vs 1 ^ 2, 1 ^ 3, 2 ^ 3  === [0001] ^ [0010], [0001] ^ [0011], [0010] ^ [0011] === [0011], [0010] === 2, 1, 1
# ored them all together I would get the total number of bits they have
# 1 ^ 2 = 2, 1^3 = 1, 1 ^ 4 = 2 = 5 bits 1 ^ 111 = 2 bits
# 2 ^ 1, 2, 2 ^ 3 = 1, 2 ^ 4 = 2 = 5 bits 10 ^ 111 = 2 bits
# 3 ^ 1 = 1, 3 ^ 2 = 1, 3 ^ 4 = 3 = 5 bits
# 4 ^ 1 = 2, 4 ^ 2 = 2, 4 ^ 3 = 3 = 7 bits

# given 8 in the set combo and 15 in the not set combo, how many combos can you choose 8 * 15 * 2(plus order reversal)
def sum_of_bit_differences(numbers):
    total_count = 0
    for i in range(32):
        ith_bit_set_count = 0
        for number in numbers:
            ith_bit_set_count += (number >> i) & 1

        total_count += (ith_bit_set_count * (len(numbers) - ith_bit_set_count)) * 2
    return total_count

print
print 'sum of bit differences'
print sum_of_bit_differences([1,2])
print sum_of_bit_differences([1,2,3,4])
print sum_of_bit_differences([1,3,5])



# given a number, count total set bits for all numbers up to and including that number
# 1 -> 1 = 1 number / 2
# 2 -> 1 = 2
# 3 -> 2 = 4
# 4 -> 1 = 5
# 5 -> 2 = 7
# 6 -> 2 = 9
# 7 -> 3 = 12
# 8 -> 1 = 13
# 0000  0 0 0 0
# 0001  0 0 0 1
# 0010  0 0 1 1
# 0011  0 0 2 2
# 0100  0 1 2 2   4
# 0101  0 2 2 3
# 0110  0 3 3 3
# 0111  0 4 4 4
# 1000  1 4 4 4   8
# for the one bit, number / 2, for the 2 bit = number / 4, for the 4 bit number / 8
# way numbers work in binary: given a bit, it is off or on every other time

# 3 C 1 + 2* 3 C 2 + 3* 3 C 3
def count_total_set_bits(n):
    total_count = 0
    for i in range(32):
        i_bit_count = 0


# given a number find the next number (including this one) which is sparse. Sparse means two bits are not next to each other
# baseline worse case you just loop through and see if it is sparse
# if sparse -> x ^ x << 1 == x | x << 1
# 0000  S
# 0001  S
# 0010  S
# 0011  N
# 0100  S
# 0101  S
# 0110  N
# 0111  N
# 1000  S
def next_sparse_number(n):
