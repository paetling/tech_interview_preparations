class Node:
    def __init__(self, value, next_node, prev_node):
        self.value = value
        self.next = next_node
        self.prev = prev_node

    def __str__(self):
        return 'Value: {}\nNext: {}\n'.format(self.value, self.next)

g = Node('g', None, None)
e1 = Node('e', None, g)
g.next = e1
e2 = Node('e', None, e1)
e1.next = e2
k = Node('k', None, e2)
e2.next = k
s = Node('s', None, k)
k.next = s
a = Node('a', None, s)
s.next = a

f_g = Node('g', None, None)
f_e1 = Node('e', None, f_g)
f_g.next = f_e1
f_e2 = Node('e', None, f_e1)
f_e1.next = f_e2
f_k = Node('k', None, f_e2)
f_e2.next = f_k
f_s = Node('s', None, f_k)
f_k.next = f_s


def string_compare(ll1, ll2):
    node1 = ll1
    node2 = ll2
    while (node1 is not None and node2 is not None):
        if node1.value < node2.value:
            return -1
        elif node1.value > node2.value:
            return 1
        else:
            node1 = node1.next
            node2 = node2.next

    if node1 is not None:
        return 1
    elif node2 is not None:
        return -1

    return 0

print string_compare(g, f_g)

def walk_linked_list(ll):
    node = ll
    while (node is not None):
        print node.value
        node = node.next

# take in two numbers as linked list
# traverse both to get their numbers, add those numbers together, make a new linked list for those numbers
def number_add(ll_number_1, ll_number_2):
    number_1 = 0
    node_1 = ll_number_1
    while (node_1 is not None):
        number_1 = number_1 * 10 + node_1.value
        node_1 = node_1.next

    number_2 = 0
    node_2 = ll_number_2
    while (node_2 is not None):
        number_2 = number_2 * 10 + node_2.value
        node_2 = node_2.next

    total = number_1 + number_2
    last_node = None
    while total > 0:
        ones_digit = total % 10
        last_node = Node(ones_digit, last_node, None)
        total /= 10

    return last_node

three = Node(3, None, None)
six = Node(6, three, None)
five = Node(5, six, None)

two = Node(2, None, None)
eight = Node(8, two, None)
four = Node(4, eight, None)

print
print 'number add'
walk_linked_list(number_add(five, four))


# given two linked lists I want to merge parts of second list into the third by alternating linked lists
# start with pointers to start of first linked list. Each time through I want to grab a new node from ll_2 and add it after current node and before the
# next node
def merge_linked_lists(ll_1, ll_2):
    node_1 = ll_1
    node_2 = ll_2
    while (node_1 is not None):
        if (node_2 is None):
            break
        old_1_next = node_1.next
        old_2_next = node_2.next

        node_2.next = old_1_next
        node_1.next = node_2

        node_1 = old_1_next
        node_2 = old_2_next

    walk_linked_list(ll_1)
    print
    walk_linked_list(node_2)
    return

eleven = Node(11, None, None)
thirteen = Node(13, eleven, None)
seventeen = Node(17, thirteen, None)
seven = Node(7, seventeen, None)
five = Node(5, seven, None)

six = Node(6, None, None)
four = Node(4, six, None)
two = Node(2, four, None)
ten = Node(10, two, None)
twelve = Node(12, ten, None)

print
print
merge_linked_lists(five, twelve)

three = Node(3, None, None)
two = Node(2, three, None)
one = Node(1, two, None)


eight = Node(8, None, None)
seven = Node(7, eight, None)
six = Node(6, seven, None)
five = Node(5, six, None)
four = Node(4, five, None)

print
print 'merge'
merge_linked_lists(one, four)



# given a linked list, you want to write a function that can reverse every k_nodes of the linked list
# start a pointer at ll, as you walk for k_nodes, create a reverse list. when you hit the final node, the old set with the new set
# you are creating a new linked list with these reversal sections
# -> [3, 2, 1]
# -> [4, 5, 6]
def reverse_linked_list(ll, k_nodes):
    node = ll

    new_linked_list = None

    current_reversal_ll = None
    end_of_reversal_ll = None
    count = 0
    while (node is not None):
        count += 1

        current_reversal_ll = Node(node.value, current_reversal_ll, None)
        if count == 1:
            if end_of_reversal_ll is None:
                end_of_reversal_ll = current_reversal_ll
            else:
                end_of_reversal_ll.next = current_reversal_ll

        print current_reversal_ll, new_linked_list, end_of_reversal_ll
        if count == k_nodes:
            if new_linked_list == None:
                new_linked_list = current_reversal_ll
            else:
                old_next = end_of_reversal_ll.next
                end_of_reversal_ll.next = current_reversal_ll
                end_of_reversal_ll = old_next

            current_reversal_ll = None
            count = 0

        node = node.next

    if count < k_nodes:
        end_of_reversal_ll.next = current_reversal_ll

    return new_linked_list

eight = Node(8, None, None)
seven = Node(7, eight, None)
six = Node(6, seven, None)
five = Node(5, six, None)
four = Node(4, five, None)
three = Node(3, four, None)
two = Node(2, three, None)
one = Node(1, two, None)

print
print 'reverse'
walk_linked_list(reverse_linked_list(one, 5))


# walk down the list and record each value. If the next value is ever a value I have seen, set next to None and return true
# if no link is found, return false
def remove_loop(ll):
    node = ll
    seen_values = {}
    while(node is not None):
        seen_values[node.value] = True
        if node.next is not None and node.next.value in seen_values:
            node.next = None
            return True

        node = node.next
    return False

eight = Node(8, None, None)
seven = Node(7, eight, None)
six = Node(6, seven, None)

five = Node(5, None, None)
four = Node(4, five, None)
three = Node(3, four, None)
two = Node(2, three, None)
one = Node(1, two, None)
five.next = two

print
print 'remove_loop'
print remove_loop(six)
print remove_loop(one)
walk_linked_list(one)

def split_ll_in_half(ll):
    length_of_ll = 0
    node = ll
    while(node is not None):
        length_of_ll += 1
        node = node.next

    new_node_l = ll
    node = ll
    for i in range(length_of_ll / 2 - 1):
        node = node.next

    new_node_r = node.next
    node.next = None
    return (new_node_l, new_node_r)

print
print 'split ll in half'
eight = Node(8, None, None)
seven = Node(7, eight, None)
six = Node(6, seven, None)
five = Node(5, six, None)
four = Node(4, five, None)
three = Node(3, four, None)
two = Node(2, three, None)
one = Node(1, two, None)

ret_one, ret_two = split_ll_in_half(one)
walk_linked_list(ret_one)
print
walk_linked_list(ret_two)

def merge_sorted_linked_lists(ll_1, ll_2):
    node_1 = ll_1
    node_2 = ll_2

    merged_ll = None
    current_merged_node = None
    while (node_1 is not None and node_2 is not None):
        value = None
        if (node_1.value < node_2.value):
            value = node_1.value
            node_1 = node_1.next
        else:
            value = node_2.value
            node_2 = node_2.next


        if merged_ll is None:
            merged_ll = Node(value, None, None)
            current_merged_node = merged_ll
        else:
            new_node = Node(value, None, None)
            current_merged_node.next = new_node
            current_merged_node = new_node

    if node_1 is not None:
        current_merged_node.next = node_1

    elif node_2 is not None:
        current_merged_node.next = node_2
    return merged_ll

print
print 'merge sorted lls'

seven = Node(7, None, None)
five = Node(5, seven, None)
three = Node(3, five, None)
one = Node(1, three, None)

eight = Node(8, None, None)
six = Node(6, eight, None)
four = Node(4, six, None)
two = Node(2, four, None)

walk_linked_list(merge_linked_lists(one, two))

def linked_list_merge_sort(ll):
    if ll is None or ll.next == None:
        return ll

    left, right = split_ll_in_half(ll)

    sorted_left = linked_list_merge_sort(left)
    sorted_right = linked_list_merge_sort(right)
    return merge_sorted_linked_lists(sorted_left, sorted_right)

print
print 'merge sort'


seven = Node(7, None, None)
six = Node(6, seven, None)
one = Node(1, six, None)
four = Node(4, one, None)
three = Node(3, four, None)
eight = Node(8, three, None)
two = Node(2, eight, None)
five = Node(5, two, None)

walk_linked_list(linked_list_merge_sort(five))
