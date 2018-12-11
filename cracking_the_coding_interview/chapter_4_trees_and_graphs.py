import sys
import random

# given a directed graph, figure out if there is a route between node 1 or node 2

# What representation am I expected to work with here? lets assume adjacency matrix
# can just do dfs from both nodes
def dps(graph, node_1, goal_node, seen_so_far):
    if node_1 == goal_node:
        return True

    if node_1 >= len(graph):
        return False

    if node_1 in seen_so_far:
        return False

    seen_so_far[node_1] = True

    for node_2 in range(len(graph[node_1])):
        if graph[node_1][node_2] == 1:
            if (dps(graph, node_2, goal_node, seen_so_far)):
                return True

    return False


def route_between_nodes(graph, node_1, node_2):
    return dps(graph, node_1, node_2, {}) or dps(graph, node_2, node_1, {})


graph_1 = [
    [1, 0, 1, 1],
    [0, 0, 1, 0],
    [1, 0, 0, 1],
    [0, 0, 0, 1],
]

print
print 'route_between_nodes'
print route_between_nodes(graph_1, 0, 1)
print route_between_nodes(graph_1, 1, 2)
print route_between_nodes(graph_1, 2, 1)
print route_between_nodes(graph_1, 0, 3)


graph_2 = [
    [1, 0, 1, 1],
    [0, 0, 0, 0],
    [1, 0, 0, 1],
    [0, 0, 0, 1],
]
print
print route_between_nodes(graph_2, 0, 1)
print route_between_nodes(graph_2, 1, 2)
print route_between_nodes(graph_2, 2, 1)
print route_between_nodes(graph_2, 0, 3)



class Node:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return 'Value:{}\n{}\'s Left: {}\n{}\'s Right: {}'.format(self.value, self.value, self.left, self.value, self.right)

# tree should not be empty
def insert_value_into_bst(tree, value):

    if value < tree.value:
        if tree.left is None:
            tree.left = Node(value, None, None)
        else:
            insert_value_into_bst(tree.left, value)
    else:
        if tree.right is None:
            tree.right = Node(value, None, None)
        else:
            insert_value_into_bst(tree.right, value)


def create_bst_from_array(array):
    if len(array ) == 0:
        return None

    tree = Node(array[0], None, None)

    for index in range(1, len(array)):
        value = array[index]
        insert_value_into_bst(tree, value)
    return tree

print
print 'create_bst_from_array'
print create_bst_from_array([5,4, 6, 3, 7, 2, 8, 1])


# given a sorted increasing order array, write an algorithm to create a binary search tree with minimum height
# if I insert in order I will always add to the right
# given a sorted array [1, 2, 3, 4, 5, 6, 7]. Minimum tree is complete
#         4
#      2     6
#    1   3 5   7

# [1, 2, 3, 4, 5, 6, 7, 8]
#         4                 5
#      2     6            3   7
#    1   3 5   7        2  4 6  8
#               8      1
def recursive_order_on_array(array):
    if len(array) == 0:
        return []

    mid_index = len(array) / 2
    return [array[mid_index]] + recursive_order_on_array(array[:mid_index]) + recursive_order_on_array(array[mid_index+1:])

print
print 'recursive_order_on_array'
print recursive_order_on_array([1,2,3,4,5,6,7])
print recursive_order_on_array([1,2,3,4,5,6,7,8])
print recursive_order_on_array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])

# Could save time on construction if we created the tree on the fly while figuring out the array ordering
def minimal_tree(array):
    return create_bst_from_array(recursive_order_on_array(array))

print
print 'minimal tree'
print minimal_tree([1,2,3,4,5,6,7])
print minimal_tree([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
print minimal_tree([1,20, 300, 4000, 50000, 600000, 7000000])


class LL_Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next

    def __str__(self):
        return 'Value: {}\nNext:{}'.format(self.value, self.next)

# create a set of linked lists for each depth
# do a breadth first search including the depth of the node
# when you pull a node add it to that tree, push its children into the queue with their depths
#
# You could have also solved this with dps if you know what level you are at
def list_of_depths(tree):
    queue = [(tree, 1)]

    lls = []

    while len(queue) > 0:
        node, depth = queue.pop(0)

        if len(lls) < depth:
            lls.append(LL_Node(node.value, None))
        else:
            lls[depth-1] = LL_Node(node.value, lls[depth-1])

        if node.left:
            queue.append((node.left, depth+1))
        if node.right:
            queue.append((node.right, depth+1))

    return lls

print
print 'list of depths'
tree_1 = Node(
    1,
    Node(
        2,
        Node(3, None, None),
        Node(4, None, None),
    ),
    Node(
        5,
        Node(6,None, None),
        Node(7, None,None),
    )
)
lls = list_of_depths(tree_1)
for ll in lls:
    print ll



# check if the tree is balanced, ensure that the heights of a given node
# never differ by more than 1.
# can do a dfs and return its height and whether it is balanced
def check_balanced_rec(tree):
    if tree == None:
        return (0,True)

    left_data = check_balanced_rec(tree.left)
    right_data = check_balanced_rec(tree.right)

    return (max(left_data[0], right_data[0])+1, left_data[1] and right_data[1] and abs(left_data[0] - right_data[0]) < 2)

def check_balanced(tree):
    return check_balanced_rec(tree)[1]

print
print 'check balanced'
tree_2 = Node(
    1,
    Node(
        2,
        Node(3, None, None),
        Node(4, None, None),
    ),
    Node(
        5,
        Node(6,None, None),
        Node(7, None,None),
    )
)

tree_3 = Node(
    1,
    Node(
        2,
        Node(3, None, None),
        Node(4, None, None),
    ),
    Node(5, None, None),
)

tree_4 = Node(
    1,
    Node(
        2,
        Node(3, None, None),
        Node(4, None, None),
    ),
    None,
)

print check_balanced(tree_2)
print check_balanced(tree_3)
print check_balanced(tree_4)



# given a tree, this method checks to make sure it is a bst
# you can check that this node value is greater than left and less than right
# recurse for the left and right and and them all together
#
# should ask if I need to handle duplicate values
# We actually need to ensure that all values to the left of a node are less than that node
def validate_bst(tree, min_val=-sys.maxint, max_val=sys.maxint):
    if tree == None:
        return True

    node_is_bst = tree.value >= min_val and tree.value < max_val
    if tree.left is not None and tree.left.value > tree.value:
        node_is_bst = False
    if tree.right is not None and tree.right.value < tree.value:
        node_is_bst = False

    return node_is_bst and validate_bst(tree.left, min_val, min(max_val, tree.value)) and validate_bst(tree.right, max(min_val, tree.value), max_val)

print
print 'validate_bst'

tree_5 = Node(
    1,
    Node(
        2,
        Node(3, None, None),
        Node(4, None, None),
    ),
    Node(
        5,
        Node(6,None, None),
        Node(7, None,None),
    )
)

tree_6 = Node(
    4,
    Node(
        2,
        Node(1, None, None),
        Node(3, None, None),
    ),
    Node(
        6,
        Node(5,None, None),
        Node(7, None,None),
    )
)

tree_7 = Node(
    20,
    Node(
        10,
        None,
        Node(25, None, None),
    ),
    Node(30, None, None)
)
print validate_bst(tree_5)
print validate_bst(tree_6)
print validate_bst(tree_7)



#
def build_order(projects, dependencies):
    output_ordering = []

    while True:
        ind_projects = set(projects) - set(output_ordering)
        initial_size = len(ind_projects)

        for ind_proj, dep_proj in dependencies:
            if ind_proj not in output_ordering:
                ind_projects = ind_projects - set([dep_proj])

        if initial_size == len(ind_projects):
            break

        output_ordering += list(ind_projects)

    print output_ordering
    return output_ordering if len(output_ordering) == len(projects) else None

print
print 'build order'
print build_order(['a', 'b', 'c', 'd', 'e', 'f'], [('a', 'd'), ('f', 'b'), ('b', 'd'), ('f', 'a'), ('d', 'c')])




# given a tree you want to print all possible orderings of an array that could produce that tree
# root node always had to come first. Get the root node and then all possible orderings of the left and all possible orderings of the right
# combine those possible orderings and then add the root node first
def all_possible_orderings(tree):
    if tree == None:
        return []

    if tree.left == None and tree.right == None:
        return [[tree.value]]

    root_value = tree.value

    left_orderings = all_possible_orderings(tree.left)
    right_orderings = all_possible_orderings(tree.right)

    all_orderings = []
    for l_o in left_orderings:
        for r_o in right_orderings:
            all_orderings.append([root_value] + l_o + r_o)
            all_orderings.append([root_value] + r_o + l_o)
    return all_orderings

print
print 'all possible orderings'
tree_8 = Node(
    2,
    Node(1,None,None),
    Node(3, None, None)
)

tree_9 = Node(
    1,
    Node(
        2,
        Node(3, None, None),
        Node(4, None, None),
    ),
    Node(
        5,
        Node(6,None, None),
        Node(7, None,None),
    )
)

print all_possible_orderings(tree_8)
print all_possible_orderings(tree_9)



def trees_are_equal(t1, t2):
    if t1 == None:
        return t2 == None
    elif t2 == None:
        return False

    return t1.value == t2.value and trees_are_equal(t1.left, t2.left) and trees_are_equal(t1.right, t2.right)

print
print 'trees are equal'
print trees_are_equal(tree_8, tree_8)
print trees_are_equal(tree_8, tree_9)
print trees_are_equal(tree_9, tree_9)

# t1 is much larger than t2. Want to check if t2 is a subtree of t1
# First blush solution is you search down t2 till you find if the value at t1 equals the
# value at t2. If so, you check if the two subtrees are equal. rinse and repeat.
#
# I could also have done the inorder traversal of both trees and compared those
#    I could have then talked tradeoffs and big Os with the interviewer
def check_subtree(t1, t2):
    if t1 == None:
        return False

    if t1.value == t2.value and trees_are_equal(t1, t2):
        return True

    return check_subtree(t1.left, t2) or check_subtree(t1.right, t2)


print
print 'check subtree'
print check_subtree(Node(15, tree_8, None), tree_8)
print check_subtree(Node(15, None, tree_8), tree_8)
print check_subtree(Node(15, tree_9, None), tree_8)
print check_subtree(Node(15, None, tree_9), tree_9)



# you want to design an algorithm where you can return a random node, where all nodes are equally likely
# If you know the number of nodes in your tree, you could use a random number generator to generate a
# random node number. That node number could be the count of the node in a bfs
#
# how do you ensure you are counting the nodes properly, you just have a count as you go through nodes
#
# Other questions ask how I would implement
#     Insert: Adds a node to try and keep the system balanced
#     find: dfs of tree
#     delete: dfs of tree looking at children to see if they are equal to the node, probably need to balance afterwards
# This runs in O(N) time
#
# We could also have each node store its size. You could then determne a random int based off of size and traverse down
# the tree to find out which node it is, instead of having to count as you iterate through them all. The thing
# you need to make this work is the count of values at each node
def get_random_node(tree, num_nodes):
    random_node_index = random.randint(0, num_nodes-1)

    current_node_index = 0
    queue = [tree]

    while len(queue) > 0:
        current_node = queue.pop(0)

        if current_node_index == random_node_index:
            return current_node

        current_node_index += 1
        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)


# Given a tree, count how many paths can sum to a goal sum
# runs in O(N * log n) time with O(log n) space
#
# We could instead have a hash map which stores the values to ensure we only have to recurse one time through
# each node
def paths_with_sum_rec(tree, current_sum, goal_sum, count_dict):
    if tree == None:
        return

    if tree.value + current_sum == goal_sum:
        count_dict['count'] += 1

    paths_with_sum_rec(tree.left, current_sum, goal_sum, count_dict)
    paths_with_sum_rec(tree.right, current_sum, goal_sum, count_dict)

    paths_with_sum_rec(tree.left, current_sum + tree.value, goal_sum, count_dict)
    paths_with_sum_rec(tree.right, current_sum + tree.value, goal_sum, count_dict)


def paths_with_sum(tree, goal_sum):
    count_dict = {'count': 0}
    paths_with_sum_rec(tree, 0, goal_sum, count_dict)

    return count_dict['count']


print
print 'paths with sum'
tree_10 = Node(
    15,
    Node(
        7,
        Node(8,
            Node(-15, None, None),
            None),
        Node(
            9,
            Node(-1,None, None),
            Node(2, None, None)),
    ),
    Node(
        5,
        Node(10,None, None),
        Node(-5, None,None),
    )
)
print paths_with_sum(tree_10, 15)
