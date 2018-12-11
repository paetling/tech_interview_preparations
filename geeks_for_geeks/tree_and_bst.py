import sys

class Node:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return 'Value: {}\n{}:Left: {}\n{}:Right: {}'.format(self.value, self.value, self.left, self.value, self.right)


def maximum_path_sum_with_max(tree, max_dict):
    if tree == None:
        return 0

    left_value = maximum_path_sum_with_max(tree.left, max_dict)
    right_value = maximum_path_sum_with_max(tree.right, max_dict)

    max_sub_max = max([tree.value, tree.value + left_value, tree.value + right_value, tree.value + left_value + right_value])

    max_dict['max'] = max(max_dict['max'], max_sub_max)

    return max(left_value, right_value) + tree.value

# given a tree, you want to find the maximum path through an part of that tree
# given a maximum path sum for a sub_node
# for left and right node I had maximum left subsequence, maximum right sequence and its value
# key here is having a max you can reference in recursion and doing two things as you recurse:
#   1. Sending back the longest subpath above
#   2. Given a longest subpath for a node, it can determine its three maxes and see if that is
# greater than the overall max
def maximum_path_sum(tree):
    max_dict = {'max': -sys.maxint}

    maximum_path_sum_with_max(tree, max_dict)
    return max_dict['max']

tree_1 = Node(1, Node(2, None, None), Node(3, None, None))
print maximum_path_sum(tree_1)

tree_2 = Node(
    10,
    Node(
        2,
        Node(20, None, None),
        Node(1, None, None)),
    Node(
        10,
        None,
        Node(
            -25,
            Node(
                3,
                Node(24, None, None),
                None),
            Node(4, None, None)))
)
print maximum_path_sum(tree_2)

# given an array, walk down the tree and the array (using recursion on tree and increasing index)
# if at some point they do not overlap, return
def preorder_traversal_tree(tree):
    if tree == None:
        return []

    return [tree.value] + preorder_traversal_tree(tree.left) + preorder_traversal_tree(tree.right)



def preorder_traversal(tree, array):
    array_for_tree = preorder_traversal_tree(tree)

    if len(array_for_tree) != len(array):
        return False

    for i in range(len(array_for_tree)):
        if array_for_tree[i] != array[i]:
            return False

    return True

tree_3 = Node(
    40,
    Node(
        30,
        None,
        Node(35, None, None)
    ),
    Node(
        80,
        None,
        Node(100, None, None)
    )
)
print
print 'preorder traversal'
print preorder_traversal(tree_3, [40, 30, 35, 80, 100])
print preorder_traversal(tree_3, [40, 30, 35, 20, 80, 100])

tree_4 = Node(
    2,
    Node(
        4,
        Node(3, None, None),
        None
    ),
    None
)
print preorder_traversal(tree_4, [2, 4, 1])
print preorder_traversal(tree_4, [2, 4, 3])


# Given a set of numbers, could they be the preorder traversal of a binary search tree
# [2, 4, 3]
# first value always has to the root of the tree. If second value is left, then you went left, if second value is more than you went right
# if the third value is less
# [40, 30, 35, 80, 100]
def could_be_preorder_traversal(array):
    stack = []
    min_allowable_value = -sys.maxint

    for value in array:
        if value < min_allowable_value:
            return False

        while len(stack) > 0 and stack[-1] < value:
            min_allowable_value = stack.pop()

        stack.append(value)
    return True


print
print 'could be preorder'
print could_be_preorder_traversal([2,4,1])
print could_be_preorder_traversal([2,4,3])
print could_be_preorder_traversal([40, 30, 35, 80, 100])
print could_be_preorder_traversal([40, 30, 35, 20, 80, 100])


# for each node, check if it has two or 0 nodes and return if it does, else false, if both left and right and i are full binary tree
# you win
def is_full_binary_tree(tree):
    if tree == None:
        return True

    current_node_is_full = (tree.left is None and tree.right is None) or (tree.left is not None and tree.right is not None)
    return current_node_is_full and is_full_binary_tree(tree.left) and is_full_binary_tree(tree.right)



print
print 'is full binary tree'

tree_5 = Node(
    40,
    Node(
        30,
        Node(31, None, None),
        Node(35, None, None)
    ),
    Node(
        80,
        Node(90, None, None),
        Node(100, None, None)
    )
)
print is_full_binary_tree(tree_5)

tree_6 = Node(
    40,
    Node(
        30,
        Node(31, None, None),
        None
    ),
    Node(
        80,
        Node(90, None, None),
        Node(100, None, None)
    )
)
print is_full_binary_tree(tree_6)

tree_7 = Node(
    40,
    None,
    Node(
        80,
        Node(90, None, None),
        Node(100, None, None)
    )
)
print is_full_binary_tree(tree_7)


def bottom_view_of_bt_rec(tree, depth, horizontal_distance, current_nodes):
    if tree == None:
        return

    if horizontal_distance not in current_nodes or current_nodes[horizontal_distance][0] <= depth:
        current_nodes[horizontal_distance] = (depth, tree.value)

    bottom_view_of_bt_rec(tree.left, depth + 1, horizontal_distance - 1, current_nodes)
    bottom_view_of_bt_rec(tree.right, depth + 1, horizontal_distance + 1, current_nodes)

# given a horizontal distance (incrememted by -1 to the left and 1 to the right), print the node at the lowest level
# pass in a tree, current_distance, and a depth, and a depth_store a node can figure out its distance and update accordingly
def bottom_view_of_binary_tree_need_sort(tree):
    current_nodes = {}
    bottom_view_of_bt_rec(tree, 0, 0, current_nodes)

    return_values = []
    for key in sorted(current_nodes.keys()):
        return_values.append(current_nodes[key][1])
    return return_values

tree_8 = Node(
    20,
    Node(
        8,
        Node(5, None, None),
        Node(
            3,
            Node(10, None, None),
            Node(14, None, None))
    ),
    Node(
        22,
        None,
        Node(25, None, None)
    )
)

print
print "bottom view of a binary tree"
print bottom_view_of_binary_tree_need_sort(tree_8)

tree_9 = Node(
    20,
    Node(
        8,
        Node(5, None, None),
        Node(
            3,
            Node(10, None, None),
            Node(14, None, None))
    ),
    Node(
        22,
        Node(4, None, None),
        Node(25, None, None)
    )
)
print bottom_view_of_binary_tree_need_sort(tree_9)

# given a tree, want to remove all paths to leafs that are not at least k distance long
# given a current distance, distance for the right path and a distance for the left path disconnect if either path is not far enough
# return this nodes max distance
def remove_length_less_than_k(tree, k, current_distance=1):
    if tree == None:
        return 0

    distance_left = remove_length_less_than_k(tree.left, k, current_distance + 1)
    distance_right = remove_length_less_than_k(tree.right, k, current_distance + 1)
    print tree.value, distance_left, distance_right, current_distance

    if distance_left + current_distance < k:
        tree.left = None
    if distance_right + current_distance < k:
        tree.right = None

    return max(distance_left, distance_right) + 1


tree_10 = Node(
    1,
    Node(
        2,
        Node(4,
            Node(7, None, None),
            None),
        Node(5, None, None)
    ),
    Node(
        3,
        None,
        Node(
            6,
            Node(8, None, None),
            None
        )
    )
)

print
print 'remove_length_less_than_k'
remove_length_less_than_k(tree_10, 4)
print tree_10


def lca_rec(tree, value_1, value_2, depth, max_dict):
    if tree == None:
        return [False, False]

    left_values = lca_rec(tree.left, value_1, value_2, depth + 1, max_dict)
    right_values = lca_rec(tree.right, value_1, value_2, depth + 1, max_dict)

    return_values = [left_values[0] or right_values[0] or value_1 == tree.value, left_values[1] or right_values[1] or value_2 == tree.value]

    if return_values[0] and return_values[1]:
        if max_dict['max'][0] < depth:
            max_dict['max'] = (depth, tree.value)

    return return_values


# given a tree and 2 values, return back a node that is a common ancestor of both
# should involve passing in depth and a max dict that stores the node and the depth of that node
# returning bools on if a subtree contains value1 and value2
def lowest_common_ancestor(tree, value_1, value_2):
    max_dict = {'max': (-1, None)}

    lca_rec(tree, value_1, value_2, 0, max_dict)

    return max_dict['max'][1]

tree_11 = Node(
    20,
    Node(
        8,
        Node(4, None, None),
        Node(
            12,
            Node(10, None, None),
            Node(14, None, None))
    ),
    Node(22, None, None)
)

print
print 'lowest_common_ancestor'
print lowest_common_ancestor(tree_11, 10, 14)
print lowest_common_ancestor(tree_11, 14, 8)
print lowest_common_ancestor(tree_11, 10, 22)

def trees_are_equal(t1, t2):
    if t1 == None:
        return t2 == None
    elif t2 == None:
        return False

    if (t1.value != t2.value):
        return False

    return trees_are_equal(t1.left, t2.left) and trees_are_equal(t1.right, t2.right)

tree_11 = Node(
    20,
    Node(
        2,
        Node(4, None, None),
        None
    ),
    Node(3, None, None)
)

tree_12 = Node(
    20,
    Node(
        2,
        Node(5, None, None),
        None
    ),
    Node(3, None, None)
)

print
print 'trees are equal'
print trees_are_equal(tree_11, tree_11)
print trees_are_equal(tree_11, tree_12)

# given a t1 tree, find if t2 is a subtree of it.
# In order to do that we need to be able to compute if two trees are equivalent
# we can do that using cotraversal, if stuff is not the same return false
# using that, we travers down t1, till we find the start of t2, once we find it we ask if the two trees are equal
def is_sub_tree_n_squared(t1, t2):
    if t1 == None:
        return t2 == None
    if t2 == None:
        return False

    if (t1.value == t2.value):
        return trees_are_equal(t1, t2)

    return is_sub_tree_n_squared(t1.left, t2) or is_sub_tree_n_squared(t1.right, t2)

def is_sub_tree_linear  (t1, t2):
    if t1 == None:
        return t2 == None
    if t2 == None:
        return False

    if (t1.value == t2.value):
        return trees_are_equal(t1, t2)

    return is_sub_tree_n_squared(t1.left, t2) or is_sub_tree_n_squared(t1.right, t2)

print
print 'is sub tree'
tree_13 = Node(50, tree_11, None)
tree_14 = Node(17, tree_12, tree_11)

print is_sub_tree_n_squared(tree_11, tree_12)
print is_sub_tree_n_squared(tree_13, tree_11)
print is_sub_tree_n_squared(tree_14, tree_11)
print is_sub_tree_n_squared(tree_14, tree_12)

def get_bfs_node_list(tree):
    nodes = [tree]
    out_nodes = []

    while len(nodes) > 0:
        node = nodes.pop(0)
        if node.left is not None:
            nodes.append(node.left)
        if node.right is not None:
            nodes.append(node.right)
        out_nodes.append(node)

    return out_nodes

# given a binary tree, return a new binary tree where every other level has been reversed
# if you have a queue and do a depth first traversal, you know how many you need to pop to build each level (1, 2, 4, 8, etc)
# you could know whether to reverse or not based off of the level you are at, you could put your last set of nodes in an array
# and know which one to grab based off of index as well
def reverse_alternate_levels(tree):
    if tree == None:
        return None

    bfs_nodes = get_bfs_node_list(tree)
    first_node = bfs_nodes.pop(0)

    last_nodes = [Node(first_node.value, None, None)]
    new_tree = last_nodes[0]

    level = 2
    while len(bfs_nodes) > 0:
        should_reverse = level % 2 == 0
        count = 0
        temp_last_nodes = []
        while (count < 2**(level-1)):
            popped_node = bfs_nodes.pop(0)
            node = Node(popped_node.value, None, None)


            parent_node = last_nodes[count / 2] if not should_reverse else last_nodes[len(last_nodes) - 1 - (count / 2)]

            if not should_reverse and count % 2 == 0 or should_reverse and count % 2 == 1:
                parent_node.left = node
            else:
                parent_node.right = node

            if not should_reverse:
                temp_last_nodes = temp_last_nodes + [node]
            else:
                temp_last_nodes = [node] + temp_last_nodes
            count +=1

        last_nodes = temp_last_nodes
        level += 1
    return new_tree

print
print 'reverse alternate levels'

tree_13 = Node(
    'a',
    Node(
        'b',
        Node(
            'd',
            Node('h', None, None),
            Node('i', None, None)),
        Node(
            'e',
            Node('j', None, None),
            Node('k', None, None)
            )
    ),
    Node(
        'c',
        Node(
            'f',
            Node('l', None, None),
            Node('m', None, None)),
        Node(
            'g',
            Node('n', None, None),
            Node('o', None, None)
            )
    ),
)

print reverse_alternate_levels(tree_13)
