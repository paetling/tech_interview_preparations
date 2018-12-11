

# child is running up the stairs and can either run
# one step, two steps or three steps at a time
# implement a method to figure out number
# of ways to run up the stairs
#
# If there is 0 steps - 1
# if there is 1 step the answer is 1
# if there is 2 steps the answer is 2
# For all other cases, number of ways if you take one step, plus the number of ways if you take 2 steps, plus the number of ways if you
# take 3 steps
def triple_step(stairs_to_run):
    steps_to_ways = [1, 1, 2]

    for i in range(3, stairs_to_run + 1):
        steps_to_ways.append(steps_to_ways[i-1] + steps_to_ways[i-2] + steps_to_ways[i-3])

    return steps_to_ways[stairs_to_run]

def triple_step_rec(stairs_to_run):
    if stairs_to_run == 0 or stairs_to_run == 1:
        return 1

    if stairs_to_run == 2:
        return 2

    return triple_step_rec(stairs_to_run - 1) + triple_step_rec(stairs_to_run - 2) + triple_step_rec(stairs_to_run - 3)

print
print 'triple step'
print triple_step(4), triple_step_rec(4)


# given a robot in a grid, with some cells off limits, how do you get it down
# to the bottom right
# grid will have True for paths it can take and false otherwise
#
# bruter force solution is you try all the paths, if you are at the end, return that path
#
# To make this a DP algorithm, you store the points you have already visited as failed points
def robot_in_grid_rec(grid, current_path, current_location):
    if current_location[0] == len(grid) - 1 and current_location[1] == len(grid[current_location[0]]) - 1:
        return current_path

    for new_row, new_col in [(current_location[0] + 1, current_location[1]), (current_location[0], current_location[1] + 1)]:
        if new_row >= len(grid) or new_col >= len(grid[new_row]) or not grid[new_row][new_col]:
            continue

        found_path = robot_in_grid_rec(grid, current_path + [(new_row, new_col)], (new_row, new_col))
        if found_path:
            return found_path

def robot_in_grid(grid):
    return robot_in_grid_rec(grid, [(0,0)], (0,0))


print
print 'robot in grid'
grid_1 = [
    [True, True, True, False],
    [False, True, False, False],
    [False, True, False, False],
    [False, True, True, True],
]
grid_2 = [
    [True, True, True, False],
    [True, True, True, True],
    [True, True, True, True],
    [True, True, True, True],
]
print robot_in_grid(grid_1)
print robot_in_grid(grid_2)



# Magic index is array[i] = i. Given sorted distinct array
# Find a magic index
# Brute force solution: you just walk through the whole array O(N)
#
# binary search it
def magic_index(array):
    if len(array) == 0:
        return None

    bottom = 0
    top = len(array) - 1

    while bottom <= top:
        guess_index = (bottom + top) / 2
        if array[guess_index] == guess_index:
            return guess_index

        elif array[guess_index] > guess_index:
            top = guess_index - 1
        else:
            bottom = guess_index + 1

    return None

print
print 'magic index'
print magic_index([-10, -4, -2, 0, 4, 6, 8, 10])
print magic_index([-10, -4, -2, 0, 5, 7, 8, 9, 10])


# give all 2^n sets
# Given this setup, the run time is O(N^4)
#   1, N, N C 2, N C 3..., N^2 / 2 - each of those does N work   N C X = N! / (N-X!) X!
def power_set(object_set):
    sub_sets = [[()]]
    for i in range(1, len(object_set)+1):
        sets_of_size_i = []
        for sub_set in sub_sets[i-1]:
            for value in object_set:
                if value not in sub_set and (len(sub_set) > 0 and value > sub_set[-1] or len(sub_set) == 0):
                    sets_of_size_i.append(sub_set + (value,))
        sub_sets.append(sets_of_size_i)
    return sub_sets

print
print 'power set'
print power_set(['a', 'b', 'c'])
print
print power_set(['a', 'b', 'c', 'd', 'e'])



# given two numbers do multiplication using recursion but no actual use of value
def recursive_multiply_slow(num_1, num_2):
    if num_2 == 0:
        return 0

    return num_1 + recursive_multiply_slow(num_1, num_2 - 1)

# multiplication means you need num_2 copies of num_1 (or the opposite. they are the same)
# count half of it, then double if even
#
# x x x x
# x x x x
# x x x x
# x x x x
# x x x x
#
#
def recursive_multiply_faster(num_1, num_2):
    if num_2 == 0 or num_1 == 0:
        return 0
    if num_2 == 1:
        return num_1

    half = recursive_multiply_faster(num_1 / 2, num_2)
    # print 'half', half, num_1, num_2

    return half + half if num_1 % 2 == 0 else half + half + num_2


print
print 'recursive multiply'
print recursive_multiply_slow(3,4)
print recursive_multiply_slow(514,216)

print recursive_multiply_faster(3,4)
print recursive_multiply_faster(514,216)


# given three towers (stacks), N disks, of increasing sizes and
# a smaller disk cannot be set on a larger disk. How do you move
# all values from one tower to the next
#
# if you just have 1, you move it
#
# [1,2] [] [] -> [2] [1] [] -> [] [1] [2] -> [] [] [1 2]
#
# [1, 2, 3] [] [] -> [3] [] [1, 2]
# algorithm -> move everyone but the bottom one, you move the bottom one over, you move all the values over to this new column

def get_middle_stack(start_stack, end_stack):
    return list(set([0, 1,2])-set([start_stack, end_stack]))[0]

def move_starting_at_index(stacks, start_stack, end_stack, index):
    if index == 1:
        stacks[end_stack].append(stacks[start_stack].pop())
        return

    middle_stack = get_middle_stack(start_stack, end_stack)

    move_starting_at_index(stacks, start_stack, middle_stack, index-1)
    stacks[end_stack].append(stacks[start_stack].pop())
    move_starting_at_index(stacks, middle_stack, end_stack, index-1)

def towers_of_hannoi(stacks):
    move_starting_at_index(stacks, 0, 2, len(stacks[0]))
    return stacks


print
print 'towers of hannoi'
print towers_of_hannoi([[2, 1], [], []])
print towers_of_hannoi([[5, 4, 3, 2, 1], [], []])



# get all permutations of a string of unique characters
# baseline recursive solution, you get all permutations without this letter and then add this letter
# to all possible places in the string

def get_possible_indices_chars(num_chars, string_len):
    if num_chars == 1:
        indices = []
        for i in range(string_len):
            indices.append([i])
        return indices

    smaller_possible = get_possible_indices_chars(num_chars - 1, string_len)

    return_indices = []
    for indices in smaller_possible:
        for index in set(range(string_len)) - set(indices):
            if index > indices[-1]:
                return_indices.append(indices + [index])
    return return_indices

print
print 'possible indices'
print get_possible_indices_chars(1, 5)
print get_possible_indices_chars(2, 5)
print get_possible_indices_chars(3, 5)


def permutations_rec(sorted_string):
    if sorted_string == '':
        return ['']

    char = sorted_string[0]
    start_index = 0
    non_inclusive_end = 1
    while non_inclusive_end < len(sorted_string) and sorted_string[non_inclusive_end] == sorted_string[start_index]:
        non_inclusive_end += 1

    all_permutations = permutations_rec(sorted_string[non_inclusive_end:])

    return_permutations = []
    for permutation in all_permutations:
        for indices in get_possible_indices_chars(non_inclusive_end - start_index, len(sorted_string)):
            initial_list = list(permutation)
            for index in indices:
                initial_list.insert(index, char)

            return_permutations.append(''.join(initial_list))
    return return_permutations

def permutations(string):
    return permutations_rec(''.join(sorted(string)))

print
print 'permutaitons without dups'
print permutations('dog')
print permutations('ddd')
print permutations('dddefgh')



# given a number of parens, you need to print all valid orderings of parens
# baseline - could generate all combos and then have code to do the checking on
# if a combo is valid
#
# 2 - ()(), (())
# NOTE: Does not work. Actual solution involves adding a new parenthesis inside all other parenthesis and then at the beginning
def parens_rec(number, seen_before):
    if number == 1:
        return ['()']

    all_sub_combos = parens_rec(number - 1, seen_before)

    return_combos = []
    for sub_combo in all_sub_combos:

        surround_string = '(' + sub_combo + ')'
        if surround_string not in seen_before:
            seen_before[surround_string] = True
            return_combos.append(surround_string)

        before_string = '()' + sub_combo
        if before_string not in seen_before:
            seen_before[before_string] = True
            return_combos.append(before_string)

        after_string = sub_combo + '()'
        if after_string not in seen_before:
            seen_before[after_string] = True
            return_combos.append(after_string)
    return return_combos


def parens(number):
    return parens_rec(number, {})

print
print 'parens'
print parens(2)
print parens(3)
print parens(4)



# given quarters, dimes, nickles, and pennies, how many ways can you represent n cents
def coins(n_cents):
    cents_to_ways = [1]

    for i in range(1, n_cents+1):
        ways = cents_to_ways[i-1]

        if i - 5 >= 0:
            ways += cents_to_ways[i-5]
        if i - 10 >= 0:
            ways += cents_to_ways[i-10]
        if i - 25 >= 0:
            ways += cents_to_ways[i-25]
        cents_to_ways.append(ways)
    return cents_to_ways[n_cents]

print
print 'coins'
print coins(1)
print coins(5)
print coins(10)
print coins(25)
print coins(30)



# given an array of boxes (l, w, h). you want to find the tallest stack possible
# if you can only stack smaller boxes on larger boxes
# given all boxes from [0:i] what is the tallest stack you can make,
# if you add a new box i + 1, how do you figure out the new tallest height
#
# baseline is that you generate all combinations and then start checking for valid box orderings in order of height
#
# given two boxes - if one is strictly larger -> height = 2 box heights
#       if one is not strictly larger -> height = max of the 2 box heights
# add a third box - if first two boxes stacked, if this stacks as well - 3 box heights
#       if first two boxes stacked and this does not stack - max(2 box heights, third box height)
#       if two boxes did not stack but this one stacks with one of them - max(2 box heights, third box height)
#       if no boxes stack - max(3 box heights)
#
# given box j, you could figure out whether or not all other boxes are bigger, smaller, or non stackable
#
#
# given all stacks, you add the box to all of them that will fit.
#
# You could also use a strategy where you compare using this box to not using this box and use
# the largest height and recurse down
def compare_two_boxes(box_1, box_2):
    if box_1[0] > box_2[0] and box_1[1] > box_2[1] and box_1[2] > box_2[2]:
        return 1

    if box_1[0] < box_2[0] and box_1[1] < box_2[1] and box_1[2] < box_2[2]:
        return -1

    return 0

def stack_of_boxes_rec(boxes):
    if len(boxes) == 1:
        return [boxes]

    current_box = boxes[0]
    sub_stacks = stack_of_boxes_rec(boxes[1:])

    return_stacks = []
    can_stack = False
    for stack in sub_stacks:
        # can stack with this stack
        if (compare_two_boxes(current_box, stack[0]) == 1):
            can_stack = True
            return_stacks.append([current_box] + stack)
        else:
            return_stacks.append(stack)
    if not can_stack:
        return_stacks.append([current_box])

    return return_stacks

def height_of_box_stack(box_stack):
    height = 0
    for box in box_stack:
        height += box[2]
    return height

def sum_of_l_w_h(boxes):
    return boxes[0] + boxes[1] + boxes[2]

def stack_of_boxes(boxes):
    box_comparison = [[0]* len(boxes) for i in range(len(boxes))]

    sorted_boxes = sorted(boxes, key=sum_of_l_w_h, reverse=True)
    all_tallest_stacks = stack_of_boxes_rec(sorted_boxes)

    max_height = 0
    for stack in all_tallest_stacks:
        height = height_of_box_stack(stack)
        if height > max_height:
            max_height = height

    return max_height

print
print 'stack of boxes'
print stack_of_boxes([(1,2,3), (3,4,5), (6,7,8), (3,2,1)])









