

# given two numbers and i and j, insert num_2, into num_1 from j at the top bit to i at the bottom bit
# assume that j to i is large enough to fit this value
def insertion(num_1, num_2, j, i):
    one_mask = ((1 << (j-i) + 1) - 1) << i  # j - i ones in a row
    zero_mask = ~one_mask

    return num_1 & zero_mask | num_2 << i

print
print 'insertion'
num_1 = 135114
num_2 = 28
j = 15
i = 10

print bin(num_1)
print bin(num_2)
print bin(insertion(num_1, num_2, j, i))


def print_double(num):
    out_string = ''
    loop_count = 0
    current_num = num

    while len(out_string) < 32 and current_num != 0:
        print current_num
        compare_num = .5 ** (loop_count + 1)
        if compare_num < current_num:
            current_num -= compare_num
            out_string += '1'
        else:
            out_string += '0'

        loop_count += 1

    return out_string

print
print 'print double'
print print_double(.101)
print print_double(.72)


# given a number, you can flip one bit from 0 to 1. Find the longest sequence of ones you can make
# baseline, I could try flipping all 31 bits and then counting which number had the longest sequence
# which is O(N logN)
# could go through and store the length of the sequence with a flip and without a flip as I go through once
# I could circle back through and find the one with longest sequence
#
# Is there a way to do this with just some simple bit change functions? - NO
#
# Could do this more effectively with a current length and previous length variable and then condition
# on if you could span the gap with your one bit flip
def flip_bit_to_win(num):
    count_array = []

    current_num = num
    bit_index = 0
    while current_num > 0:
        current_bit = current_num & 1
        current_num = current_num >> 1
        print current_bit

        if len(count_array) == 0:
            count_array.append((current_bit, 1))
        else:
            last_count_without, last_count_with = count_array[bit_index - 1]
            longest_sequence_without = last_count_without + 1 if current_bit == 1 else 0
            longest_sequence_with = max(last_count_without, last_count_with) + 1 if current_bit == 1 else last_count_without + 1
            count_array.append((longest_sequence_without, longest_sequence_with))

        bit_index += 1

    max_val = 0
    for _, with_length in count_array:
        if with_length > max_val:
            max_val = with_length

    return max_val


print
print 'flip bit to win'
print flip_bit_to_win(1775)



# given a number n, we want to print the next smallest number and the next largest number that have the same number of ones
# as this number
# n = 00001010   smaller - 00001001, larger - 00001100
#
# brute force solution: you count the number of bits, then you decrement number by 1 and count bits till you get the same number of bits
#   works the same for next largest
#
# for next highest number, you need to shift the lowest digit up one without it shifting up another number
#     n = 00001110   - if you just shifted the lowest one up one -> 0001000
#     n = 00010110   - if you just shifted the lowest one up one -> 0001100
#     n = 00000011   - if you just shifted the lowest one up one -> 0000100
# seems like you can shift the lowest bit up one bit, check how many more bits you need and add the lowest value in to get there
#   log N to count the number of bits:
#   steps would be 1: count the initial number of bits, count the index of the lowest bit at the same time.
#       Figure out what to add to shift it up (add 2^i)
#   count the number of bits again and figure out how many more bits you need. If 0, you are all set, if more than that, add (2^number of bits) - 1
#   2 count number of bits = O(log n)
def next_number(n):
    index_of_lowest_bit = None
    count_of_bits = 0
    bit_index = 0
    current_num = n

    while current_num > 0:
        current_bit = current_num & 1

        if current_bit == 1 and index_of_lowest_bit is None:
            index_of_lowest_bit = bit_index
        count_of_bits += current_bit

        current_num = current_num >> 1
        bit_index += 1

    output_num = n + 2**index_of_lowest_bit

    original_count_of_bits = count_of_bits
    count_of_bits = 0
    current_num = output_num
    while current_num > 0:
        current_bit = current_num & 1
        count_of_bits += current_bit
        current_num = current_num >> 1

    if count_of_bits == original_count_of_bits:
        return output_num
    else:
        return output_num + 2**(original_count_of_bits-count_of_bits) - 1

print
print 'next number'
number = 22

print number, bin(number)
output = next_number(number)
print output, bin(output)



# Problem 5:
# Explain what n & (n-1) == 0
#    if n = 00010110
#     n-1 = 00010101
#
#   1 & 0 = 0
#   2 & 1 = 0
#   3 & 2 = 2
#   4 & 3 = 0
#   5 & 4 = 4
#   6 & 5 = 4
#   7 & 6 = 6
#   8 & 7 = 0
#   9 & 8 = 8
#  Checks if it is a multiple of 2




# baseline solution, you loop over every bit and check if you need to flip it or not
# Can you do this in a smarter way?
# xor the numbers and then count how many bits O(logN) but is slightly faster
#
# C & (c-1) flips the least significant bit in a number. Can run that less times then counting all the bits
def number_of_bit_flips_required(n1, n2):
    pass



# swap the odd and even bits in a number
# odd bits move up
# even bits move down
def pairwise_swap(number):
    odd_bit_mask = 1431655765 # masks all odd digits in a number
    even_bit_mask = odd_bit_mask << 1

    return ((number & odd_bit_mask) << 1) | ((number & even_bit_mask) >> 1)


print
print 'pairwise swap'
number = 12341241
print bin(number)
print bin(pairwise_swap(number))








