# implement an algorithm to determine if a string has all unique characters.
# brute force is you loop over all combos and see if there are any duplicates
#
# hash map is very useful here - you just add every element in and if you see a duplicate you return false: O(n)
#
# What if you cannot use additional data structures
# Sort the array first and see if you find a value to the right that equals this value: O(n log(n))
# [1, 2 4, 2, 7, 8]
def is_unique(array):
    contains_array = {}
    for value in array:
        if value in contains_array:
            return False

        contains_array[value] = True

    return True

print 'is unique'
print is_unique([1,2,4,2,7,8])
print is_unique([1,2,4,7,8])


# given two strings, write a method to detrmine if one is permutation of the other
# brute force - you create all permutations of string 1 and compare to string 2. O(n!)
# you can check the string size initially to compare the two strings more cheaply

# If you sort the first string and the second string you have (nlogn + m log m) and then walk down them in tandem
# You could do (m + n)log n if you just sort the bigger one.
#
# I can do this in n + m time if I can use a hashmap and walk over one and add to the hash map and then look for values in
# the second in the hash map
def check_permutation(str1, str2):
    if len(str1) != len(str2):
        return False

    sorted_string_1 = sorted(str1)
    sorted_string_2 = sorted(str2)

    for i in range(len(sorted_string_1)):
        if sorted_string_1[i] != sorted_string_2[i]:
            return False

    return True

print
print 'check permutations'
print check_permutation('abcdef', 'acebdf')
print check_permutation('abcdef', 'acebda')
print check_permutation('abcdef', 'acebdz')


# want to replace all blank values in a string with %20.
# easiest way to do this is a simple loop through all characters to check if empty string and then replace. This will end up copying
# values a ton of times

# would love the ability to place all values in their final position in O(N) time.
# you can go through once and determine numbrer of spaces. If you then loop through the items in reverse and move all items that number
# of spaces you should move all items once
def urlify(string):
    space_count = 0

    for char in string:
        if char == ' ':
            space_count += 1

    new_array_len = len(string) + 2*space_count
    new_array = [''] * new_array_len

    proceeding_spaces = space_count
    for i in range(len(string) - 1, -1, -1):
        char = string[i]

        if char != ' ':
            new_array[i + proceeding_spaces * 2] = char
        else:
            proceeding_spaces -= 1
            start_index = i + proceeding_spaces * 2
            new_array[start_index: start_index + 3] = '%20'

    return new_array


print
print 'urlify'
print urlify('hey how are you')
print urlify('I am fine, thanks!')


# given a string, check if it is a permutation of a palindrome
# ask about string comparison and camel case and such
# base_line solution is you create all palindromes and then see if any are a palindrome: creating all palindromes are n!,
# see if any are a palindrome is (n * n!) - very very slow
#
# palindrome means that all letters need multiples of two except for one which can be 1
# You could loop through the list once and add items to a hashmap. Keep a count, if at the end any have odd numbers you
# do not have a palindrome - O(n)
#
# if you can only use O(1) extra space - you could sort the list and then loop over checking for the same logic above O(n logn)
def palindrome_permutation(word):
    char_count = {}

    for char in word:
        if char not in char_count:
            char_count[char] = 0
        char_count[char] += 1

    number_of_odds = 0
    for value in char_count.values():
        if (value % 2) == 1:
            number_of_odds += 1

        if number_of_odds == 2:
            return False
    return True


print
print 'palindrome permutation'
print palindrome_permutation('racecar')
print palindrome_permutation('amanaplanacanalpanama')
print palindrome_permutation('alcanpmanaaaanplanama')
print palindrome_permutation('dog')


# three edits that can be performed on a string, insert, remove, or replace
# write a function to check if two strings are one or zero edits away
#
# base_line solution check if the string lengths are more than 1 apart, if so, false
# go through all possible additions, all possible subtractions and all possible swaps and see if any string 1 equals string 2, O(n^2) with
# a very large constant
#
# if you sort both and then walk through and find just one difference extra character or changed character could work O(n logn)
# if you use a hash_map and add the letters from one into it and then try removing the letters from another if you have more than
# one negative and one positive (if equal) or other conditions for otehr cases you know you cannot do it. O(n + m)
#
# Could do this even more cleanly by walking over both strings at once and ensuring you only find one difference. O(n) - n is the
# length of the shorter string
def one_away(string_1, string_2):
    char_exists = {}

    if abs(len(string_1) - len(string_2)) >= 2:
        return False

    for char in string_1:
        char_exists[char] = True


    missing_char = 0
    for char in string_2:
        if char not in char_exists:
            missing_char += 1
        if missing_char >= 2:
            return False
    return True

print
print 'one away'
print one_away('pale', 'ple')
print one_away('pales', 'pale')
print one_away('pale', 'bale')
print one_away('pale', 'bake')



# given a string of characters create a new string where you replace characters in a row with character counts
# if new string is shorter, return original string
# string concat is slow and works in O(n^2) you will need special logic to make sure that you are copying the strings in a better way
# a good way would be to add to an auto resizing list and then compress to a single string
def string_compression(string):
    if len(string) == 0:
        return ''

    new_string_array = []

    current_char = string[0]
    current_char_count = 1
    for index in range(1, len(string)):
        char = string[index]

        if current_char != char:
            new_string_array += [current_char, str(current_char_count)]
            current_char = char
            current_char_count = 1
        else:
            current_char_count += 1
    new_string_array += [current_char, str(current_char_count)]
    new_string = ''.join(new_string_array)

    return new_string if len(new_string) < len(string) else string


print
print 'simple string compression'
print string_compression('aabcccccaaa')
print string_compression('dog')
print string_compression('aaaaaaaaaaaa')


# given an image represented by an NxN matrix, each pixel is 4 bytes, write a method to rotate the image 90 degrees
# should be able to loop over the matrix from 0 -> 1/2 and 0 -> 1/2 and do the rotate in a sub loop that does 4 rotates
# would need to ask, clockwise or counter clockwise. This would take n^2 time
#
# NOTE: Does NOT WORK
def rotate_matrix(matrix):
    for i in range(len(matrix) / 2):
        for j in range(len(matrix[i]) / 2):

            temp = matrix[i][j]
            matrix[i][j] = matrix[j][len(matrix) - 1 - i]
            matrix[j][len(matrix) - 1 - i] = matrix[len(matrix) - 1 - i][len(matrix) - 1 - j]
            matrix[len(matrix) - 1 - i][len(matrix) - 1 - j] = matrix[i][len(matrix) - 1 - j]
            matrix[len(matrix) - 1 - j][i] = temp
    return matrix

print
print 'rotate matrix'
print rotate_matrix([[1, 2], [3, 4]])
print rotate_matrix([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
])


# write an algorithm such that if, value of x is 0, values of row and column are set to 0
# baseline: loop over the matrix and record all rows and columns that need set to 0 in a two arrays of length m and n
# loop through the array and set all values to 0 O(nXm)
#
# Could optimize space usage by storing if row 0 and col 0 have 0s in them and then using those arrays as are should
# vector
def zero_matrix(matrix):
    if len(matrix) == 0:
        return matrix

    should_set_row_to_0 = [False] * len(matrix)
    should_set_col_to_0 = [False] * len(matrix[0])

    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == 0:
                should_set_row_to_0[row] = True
                should_set_col_to_0[col] = True

    for row_index in range(len(should_set_row_to_0)):
        if should_set_row_to_0[row_index]:
            for col in range(len(matrix[row_index])):
                matrix[row_index][col] = 0

    for col_index in range(len(should_set_col_to_0)):
        if should_set_col_to_0[col_index]:
            for row in range(len(matrix)):
                matrix[row][col_index] = 0

    return matrix


print
print 'zero matrix'
print zero_matrix([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
])
print zero_matrix([
    [0, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 0, 12],
    [13, 14, 15, 16]
])



# you have a function isSubstirng and two strings. write code to check if s2 is a rotation of s1 using only one call to isSubstring
# if you string 2 is a rotation of string 1 then string 1 and string two have parts a and b
# string_1 : ab
# string_2: ba
# string_2+string_2 = ba+ ba = baba which should contain the original string
def string_rotation(string_1, string_2):
    return string_1 in (string_2+string_2)

print
print 'string rotation'
print string_rotation('waterbottle', 'erbottlewat')
print string_rotation('waterbottle', 'erbottlewats')
print string_rotation('waterbottle', 'dog')

