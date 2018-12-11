# 3 steps are subtracting 1,
# dividing by 2
# dividing by 3
# for 1 - 0
# for 2 - subtract 1 or divide by 1  - 1
# for 3 divide by 3 - 1
# for 4 - subtract one, divide by 2 - both lead to 2
# if i know n -1, n / 2 and n / 3, min of those plus 1
def minimum_steps_to_1_dp(number):
    min_steps = [0, 0, 1, 1]
    for i in range(4, number + 1):
        if i % 2 == 0 and i % 3 == 0:
            min_steps.append(min(min_steps[i-1], min_steps[i/2], min_steps[i/3]) + 1)
        elif i % 2 == 0:
            min_steps.append(min(min_steps[i-1], min_steps[i/2]) + 1)
        elif i % 3 == 0:
            min_steps.append(min(min_steps[i-1], min_steps[i/3]) + 1)
        else:
            min_steps.append(min_steps[i-1] + 1)

    return min_steps[number]


def minimum_steps_to_1_recursion(number):
    if number in [0, 1]:
        return 0
    if number in [2, 3]:
        return 1

    if number % 2 == 0 and number % 3 == 0:
        return min(minimum_steps_to_1_recursion(number-1), minimum_steps_to_1_recursion(number/2), minimum_steps_to_1_recursion(number/3)) + 1
    elif number % 2 == 0:
        return min(minimum_steps_to_1_recursion(number-1), minimum_steps_to_1_recursion(number/2)) + 1
    elif number % 3 == 0:
        return min(minimum_steps_to_1_recursion(number-1), minimum_steps_to_1_recursion(number/3)) + 1
    else:
        return minimum_steps_to_1_recursion(number-1) + 1

print minimum_steps_to_1_dp(10)
print minimum_steps_to_1_dp(15)
print minimum_steps_to_1_dp(25)
print minimum_steps_to_1_dp(200)
print minimum_steps_to_1_dp(5000)
print minimum_steps_to_1_dp(500001)

print minimum_steps_to_1_recursion(15)
print minimum_steps_to_1_recursion(25)
print minimum_steps_to_1_recursion(200)
# print minimum_steps_to_1_recursion(5000)


# find longest subsequence that ends at i, given the longest subsequence that ends at i - 1, either 1 or that subsequence plus 1
def longest_increasing_subsequence(array_of_values):
    if len(array_of_values) == 0:
        return []

    longest_subsequence_ending_at_i = [[array_of_values[0]]]
    for i in range(1, len(array_of_values)):
        if (array_of_values[i] > longest_subsequence_ending_at_i[i-1][-1]):
            longest_subsequence_ending_at_i.append(longest_subsequence_ending_at_i[i-1] + [array_of_values[i]])
        else:
            longest_subsequence_ending_at_i.append([array_of_values[i]])

    longest_size = 0
    longest_subsequence = None
    for subsequence in longest_subsequence_ending_at_i:
        if len(subsequence) > longest_size:
            longest_size = len(subsequence)
            longest_subsequence = subsequence

    return longest_subsequence

print longest_increasing_subsequence([1,2,3,2,4,5,6,3,4,5])



# LCS for input Sequences "BACDGH" and "AEDFHR" is "ADH" of length 3.
# LCS for input Sequences "AGGTAB" and "GXTXAYB" is "GTAB" of length 4.
# LCS for input Sequences "CDA" and "CAD"
#  start at i = 0, C, all possible subsequence on CAD-> [C]
#  at i = 1, D -> [D, CD, C]
#  at i = 2, A, -> [CA, CD]
#
# longest_common_subsequence_ending_at_i, given other word
def longest_common_subsequence(string_1, string_2):
    print string_1, string_2
    all_subsequences = []
    for string_1_letter in string_1:
        # print string_1_letter, all_subsequences
        new_subsequences = []
        for subsequence in all_subsequences:

            number_of_found_letters = 0
            for string_2_letter in string_2:
                # print subsequence, string_2_letter, number_of_found_letters
                if(number_of_found_letters == len(subsequence)) and string_1_letter == string_2_letter:
                    new_subsequences.append(subsequence + string_1_letter)
                elif(number_of_found_letters < len(subsequence)):
                    if subsequence[number_of_found_letters] == string_2_letter:
                        number_of_found_letters += 1
        all_subsequences += new_subsequences

        for string_2_letter in string_2:
            if (string_1_letter == string_2_letter):
                all_subsequences.append(string_1_letter)
                break

    max_len = 0
    max_substring = None
    for substring in all_subsequences:
        if len(substring) > max_len:
            max_len = len(substring)
            max_substring = substring
    return max_substring

# length of longest common subsequence if the ends match L(X[0:n-1], Y[0:m-1])
#   if values match = 1 + L(X[0:n-2], Y[0:m-2])
#   if values do not match = max(L(X[0:n-2], Y[0:m-1]), L(X[0:n-1], Y[0:m-2]))
#
# L(X[0:0], Y[0:n-1]) = 1 +
def longest_common_subsequence_dp(string_1, string_2):
    if len(string_1) == 0 or len(string_2) == 0:
        return 0

    lcs = [[(0, '')] * len(string_2) for i in range(len(string_1))]

    for string_1_index in range(0, len(string_1)):
        for string_2_index in range(0, len(string_2)):
            if (string_1[string_1_index] == string_2[string_2_index]):
                value = (lcs[string_1_index-1][string_2_index-1] if string_1_index >= 1 and string_2_index >= 1 else (0, ''))
                lcs[string_1_index][string_2_index] = (1 + value[0], value[1] + string_1[string_1_index])
            else:
                value1 = lcs[string_1_index-1][string_2_index] if string_1_index >= 1 else (0, '')
                value2 = lcs[string_1_index][string_2_index-1] if string_2_index >= 1 else (0, '')

                if (value1[0] > value2[0]):
                    lcs[string_1_index][string_2_index] = value1
                else:
                    lcs[string_1_index][string_2_index] = value2
    return lcs[len(string_1)-1][len(string_2)-1]



print longest_common_subsequence('ABCDGH', 'AEDFHR')
print longest_common_subsequence('AGGTAB', 'GXTXAYB')

print longest_common_subsequence_dp('ABCDGH', 'AEDFHR')
print longest_common_subsequence_dp('AGGTAB', 'GXTXAYB')


# given str1 and str2 want to convert one to the other
# can insert, remove, or replace
#
# given edit_distance so that the first n letters are the same, what would you need to do so that the
# first n + 1 letters are the same
#   if the letters are already the same, edit_distance(X[0:n+1], Y[0:n+1]) = edit_distance(X[0:n], Y[0:n])
#   if the letters are not the same, edit_distance(X[0:n+1], Y[0:m+1]) = 1 + min(
#       edit_distance(X[0:n], Y[0:n+1]) - remove case
#       edit_distance(X[0:n], Y[0:n]) - replace case
#       edit_distance(X[0:n+1], Y[0:n]) - add case
#   )
def edit_distance(string_1, string_2):
    edit_distance = {"": {"": (0, [])}}

    for index in range(len(string_1)):
        substring = string_1[0:index+1]
        edit_distance[substring] = {"": (len(substring), ['remove']*len(substring))}

    for index in range(len(string_2)):
        substring = string_2[0:index+1]
        edit_distance[""][substring] = (len(substring), ['remove']*len(substring))

    for string_1_end_index in range(len(string_1)):
        for string_2_end_index in range(len(string_2)):
            if string_1[string_1_end_index] == string_2[string_2_end_index]:
                edit_distance[string_1[0:string_1_end_index+1]][string_2[0:string_2_end_index+1]] = edit_distance[string_1[0:string_1_end_index]][string_2[0:string_2_end_index]]
            else:
                insert = edit_distance[string_1[0:string_1_end_index+1]][string_2[0:string_2_end_index]]
                remove = edit_distance[string_1[0:string_1_end_index]][string_2[0:string_2_end_index+1]]
                replace = edit_distance[string_1[0:string_1_end_index]][string_2[0:string_2_end_index]]
                if insert[0] < remove[0] and insert[0] < replace[0]:
                    edit_distance[string_1[0:string_1_end_index+1]][string_2[0:string_2_end_index+1]] = (1 + insert[0], insert[1] + ['insert'])
                elif remove[0] < insert[0] and remove[0] < replace[0]:
                    edit_distance[string_1[0:string_1_end_index+1]][string_2[0:string_2_end_index+1]] = (1 + remove[0], remove[1] + ['remove'])
                else:
                    edit_distance[string_1[0:string_1_end_index+1]][string_2[0:string_2_end_index+1]] = (1 + replace[0], replace[1] + ['replace'])

    return edit_distance[string_1][string_2]

print edit_distance('geek', 'gesek')
print edit_distance('cat', 'cut')
print edit_distance('sunday', 'saturday')


# given a distance in steps, count number of ways to cover that distance, given you can take 1, 2, 3 steps
# N(D) = N(D-3) + N(D-2) + N(D-1)
def count_number_of_ways(distance):
    number_of_ways = [1, 1, 2]
    for i in range(3, distance + 1):
        number_of_ways.append(number_of_ways[i-1] + number_of_ways[i-2] + number_of_ways[i-3])
    return number_of_ways[distance]

print count_number_of_ways(3)
print count_number_of_ways(4)
print count_number_of_ways(7)


# longest sequence ending at (x,y) is
#   if a place next to me has value one less than mine 1 + their longest sequence
#   if a place next to me does not have the longest sequence = 1
# how do you traverse in that order
def longest_path_in_matrix(matrix):
    indices_map = {}

    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            indices_map[matrix[row][col]] = (row, col)

    longest_sequence_ending_at_i = {}

    for number_value in sorted(indices_map.keys()):
        row, col = indices_map[number_value]

        set_value = False
        for new_row, new_col in [(row-1, col), (row, col-1), (row+1, col), (row, col+1)]:
            if new_row < 0 or new_row >= len(matrix) or new_col < 0 or new_col >= len(matrix[new_row]):
                continue
            if matrix[new_row][new_col] == number_value - 1:
                set_value = True
                longest_sequence_ending_at_i[number_value]= (longest_sequence_ending_at_i[number_value-1] + [number_value])

        if not set_value:
            longest_sequence_ending_at_i[number_value] = [number_value]

    max_sequence_len = 0
    max_sequence = None
    for sequence in longest_sequence_ending_at_i.values():
        if len(sequence) > max_sequence_len:
            max_sequence_len = len(sequence)
            max_sequence = sequence

    return max_sequence

print longest_path_in_matrix([
    [1, 2, 9],
    [5, 3, 8],
    [4, 6, 7],
])
print longest_path_in_matrix([
    [1, 2, 9, 10],
    [5, 3, 8, 11],
    [4, 6, 7, 12],
    [13, 14, 15, 16],
])


# given X[0:n] trying to sum a subset to equal sum
# given a value at end, if it is less than sum, you have two options: or X(0: n-1, sum) - ignore this value, X(0: n-1, sum-value) - use this value
def recursive_subset_sum(array, up_to_i, desired_value, memoize):
    if up_to_i < 0:
        return desired_value == 0

    option_1 = recursive_subset_sum(array, up_to_i - 1, desired_value, memoize) # do not include
    option_2 = recursive_subset_sum(array, up_to_i - 1, desired_value - array[up_to_i], memoize) # include value
    memoize[up_to_i][desired_value] = option_1 or option_2

    return memoize[up_to_i][desired_value]

def subset_sum(array, desired_value):
    memoize = {i: {} for i in range(len(array))}
    val = recursive_subset_sum(array, len(array) - 1, desired_value, memoize)
    print memoize
    return val


print subset_sum([3, 34, 4, 12, 5, 2], 9)



# def optimal_strategy_game_rec(row_of_coins, player_payoff, other_player_payoff):
#     if len(row_of_coins) == 0:
#         return 0

#     return max(optimal_strategy_game_rec(row_of_coins[1:], other_player_payoff, player_payoff) + row_of_coins[0], optimal_strategy_game_rec(row_of_coins[0:len(row_of_coins) - 1], other_player_payoff, player_payoff) + row_of_coins[-1])

# minimax on the way down
# given a row of coins Value_player_1 = X[0:n] Max(value(0) + X[1:n], value(n) + X[1:n-1])
# value_player_2 X[0:n-1]
# start from the middle coin values
# if I have a row of coins from 0: i, optimal = max(value(i+1) + X[0:i], value(0)+ X[1:i+1])
# 5 3 4 1 4 6
# (5 3)  - 5 get 5 values
# (5 (3 4) 1) -
# (5 (3 (4 1) 4) 6) -   Pick 6 or 5, max(6 + values left for other to choose, 5 + values left for other to choose)
# player two can choose

def optimal_strategy_game(row_of_coins):
    player_1_value = {}
    player_2_value = {}

    for coin in row_of_coins:
        player_2_value[(coin)] = int(coin)

    for coin_1_index in range(len(row_of_coins) - 1):
        coin_2_index = coin_1_index + 1
        coin_1 = row_of_coins[coin_1_index]
        coin_2 = row_of_coins[coin_2_index]
        player_1_value[(coin_1,coin_2)] = max(int(coin_1), int(coin_2))


    player_turn_index = 1
    value_array = [player_1_value, player_2_value]
    for set_size in range(3, len(row_of_coins) + 1):
        # print player_1_value, player_2_value
        current_player_value = value_array[player_turn_index]
        next_turn_index = (player_turn_index + 1) % 2
        next_player_value = value_array[next_turn_index]

        all_sets = []
        for subset_start_index in range(len(row_of_coins) - (set_size - 1)):
            all_sets.append(row_of_coins[subset_start_index: subset_start_index + set_size])
        # print all_sets

        for specific_set in all_sets:
            left_subset = specific_set[1:]
            # print specific_set
            other_players_value_left = next_player_value[left_subset]
            current_player_value_left = sum(left_subset) - other_players_value_left

            right_subset = specific_set[:len(specific_set) - 1]
            other_players_value_right = next_player_value[right_subset]
            current_player_value_right = sum(right_subset) - other_players_value_right

            current_player_value[specific_set] = max(current_player_value_left + int(specific_set[0]), current_player_value_right + int(specific_set[-1]))

        player_turn_index = next_turn_index

    # print player_1_value
    # print player_2_value
    return player_1_value[row_of_coins]

print optimal_strategy_game((5, 3, 4, 1, 4, 6))
print optimal_strategy_game((5, 3, 7, 10))
print optimal_strategy_game((8, 15, 3, 7))


# maximize the values that can fit in capacity
# given a set of values from 0:n, given a new value n+1, what should you do
# max(taking_item + value, not_taking_the_item)
def knapsack_problem_rec(values, weights, capacity):
    if capacity == 0:
        return 0

    if len(values) == 0:
        return 0

    value_with_item = knapsack_problem_rec(values[:len(values)-1], weights[:len(values)-1], capacity - weights[-1]) + values[-1]
    value_without_item = knapsack_problem_rec(values[:len(values)-1], weights[:len(values)-1], capacity)

    return max(value_with_item, value_without_item)

# either use the ith item or you do not, if you use it capacity is affected
def knapsack_problem_dp(values, weights, capacity):
    data_holder = [[0] * (capacity + 1) for i in range(len(values) + 1)]

    for items_up_to_index in range(len(values) + 1):
        for capacity_of_bag in range(capacity + 1):
            if items_up_to_index == 0 or capacity_of_bag == 0:
                data_holder[items_up_to_index][capacity_of_bag] = 0
            else:
                with_item_index = data_holder[items_up_to_index-1][capacity_of_bag - weights[items_up_to_index-1]] + values[items_up_to_index-1]
                without_item_index = data_holder[items_up_to_index-1][capacity_of_bag]
                data_holder[items_up_to_index][capacity_of_bag] = max(with_item_index, without_item_index)

    return data_holder[len(values)][capacity]


print knapsack_problem_rec([60, 100, 120], [10, 20, 30], 50)
print knapsack_problem_dp([60, 100, 120], [10, 20, 30], 50)


