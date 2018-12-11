class Node:
    def __init__(self, value, next, prev):
        self.value = value
        self.next = next
        self.prev = prev

    def __str__(self):
        return 'Value: {}\nNext: {}'.format(self.value, self.next)


# write code to remove duplicates from an unsorted linked list
# Baseline is that you have a dictionary that stores values you have seen
# if you see a value that has already been seen, remove it

#
def remove_dups_dict(ll):
    seen_values = {}

    node = ll
    while node != None:
        seen_values[node.value] = True

        # need to remove the node
        if node.next and node.next.value in seen_values:
            node.next = node.next.next

        node = node.next

# how to write if a temporary buffer is not allowed
# nodes with duplicate values are not anywhere in the list
# sort the nodes first using merge sort
# walk down and compare - this would end up not returning the list in the correct order
#
# Easiest solution is n^2. Basically you have one pointer start at the first element and
# then have another pointer walk down and remove all of those elements
# rinse and repeat
#
#
def remove_dups_no_buffer(ll):
    seen_values = {}

    node = ll
    while node != None:
        value = node.value

        runner_node = node
        while runner_node != None:
            if runner_node.next and runner_node.next.value == value:
                runner_node.next = runner_node.next.next
            runner_node = runner_node.next
        node = node.next

node_5_1 = Node(5, None, None)
node_5_2 = Node(5, node_5_1, None)
node_4 = Node(4, node_5_2, None)
node_3_1 = Node(3, node_4, None)
node_3_2 = Node(3, node_3_1, None)
node_2 = Node(2, node_3_2, None)
node_1 = Node(1, node_2, None)

print
print 'remove dups'
print node_1
remove_dups_no_buffer(node_1)
print node_1



# baseline solution would be to store the last k elements in a list of size K.
# as you go down the list swap items down the list. Keep the kth item at the head
#
# Needed to ask what 1 would have meant in this context
# Needed to ask if we knew the size of the ll
#
# If I wanted to use less space, I could have looped till the end and then gone back some number of spaces if I had double linked
# or used recursion
def return_kth_to_last(ll, k):
    holder_array = [None] * k

    node = ll
    while node != None:
        for i in range(1, k):
            holder_array[i-1] = holder_array[i]
        holder_array[k-1] = node.value
        node = node.next

    return holder_array[0]

print
print 'return kth to last'

node_5_1 = Node(5, None, None)
node_5_2 = Node(5, node_5_1, None)
node_4 = Node(4, node_5_2, None)
node_3_1 = Node(3, node_4, None)
node_3_2 = Node(3, node_3_1, None)
node_2 = Node(2, node_3_2, None)
node_1 = Node(1, node_2, None)

print return_kth_to_last(node_5_1, 5)
print return_kth_to_last(node_1, 5)
print return_kth_to_last(node_1, 6)
print return_kth_to_last(node_1, 1)



# delete a node that is passed in that happens in the middle of the ll
# first question would be is this a doubly linked list.  My guess would be no
#
# a -> b -> c -> d -> e and c is passed in, you should modify the list to be
# a -> b -> d -> e
# I can swap values from the next node all the way up and then delete the final node
def delete_middle_node(ll_node):
    node = ll_node
    while ll_node.next.next != None:
        ll_node.value = ll_node.next.value
        ll_node = ll_node.next
    ll_node.value = ll_node.next.value
    ll_node.next = None

print
print 'delete middle node'

node_5= Node(5, None, None)
node_4 = Node(4, node_5, None)
node_3 = Node(3, node_4, None)
node_2 = Node(2, node_3, None)
node_1 = Node(1, node_2, None)
print node_1
delete_middle_node(node_2)
print node_1



# first thought is that you make a new linked list with all values >= x as you go down. Once you get to the end you point your end at your new
# ll
# if we do not care about ordering, then we do not need to keep track of 4 variables to make this work
def partition(ll, x):
    if ll == None:
        return

    final_ll = None
    final_node = None

    greater_than_ll = None
    greater_than_node = None


    node = ll
    while node != None:
        if node.value >= x:
            if (greater_than_ll == None):
                greater_than_ll = Node(node.value, None, None)
                greater_than_node = greater_than_ll
            else:
                greater_than_node.next = Node(node.value, None, None)
                greater_than_node = greater_than_node.next

        else:
            if (final_ll == None):
                final_ll = Node(node.value, None, None)
                final_node = final_ll
            else:
                final_node.next = Node(node.value, None, None)
                final_node = final_node.next
        node = node.next

    final_node.next = greater_than_ll

    return final_ll

print
print 'parition'

node_1= Node(1, None, None)
node_2 = Node(2, node_1, None)
node_3 = Node(3, node_2, None)
node_4 = Node(4, node_3, None)
node_5 = Node(5, node_4, None)
print node_5
print partition(node_5, 3)



# have two lls that store a number in reverse order. You want to sum them and return a new linked list with the values
# First thought is you need a carry, new_ll, new_ll_end to go through these values
def sum_lists_backwards(ll1, ll2):
    carry = 0
    new_ll = None
    new_ll_end = None

    node_1 = ll1
    node_2 = ll2

    while node_1 is not None or node_2 is not None:
        new_sum = carry
        if node_1 is not None:
            new_sum += node_1.value
            node_1 = node_1.next
        if node_2 is not None:
            new_sum += node_2.value
            node_2 = node_2.next

        value_to_add = new_sum %10
        carry = new_sum /10

        if new_ll is None:
            new_ll = Node(value_to_add, None, None)
            new_ll_end = new_ll
        else:
            new_ll_end.next = Node(value_to_add, None, None)
            new_ll_end = new_ll_end.next

    return new_ll

# if we had to sum the lists forwards we could still do it. You would just need to add the overhang to the previous node,
# so you would have to keep track of the previous as you looped down
# but you would need to pad the shorter list with 0s to ensure that the plus' were operating on the correct values
def sum_lists_forwards(ll1, ll2):
    pass

print
print 'sum lists backwards'


node_1= Node(1, None, None)
node_2 = Node(2, node_1, None)
node_3_1 = Node(3, node_2, None)

node_3 = Node(3, None, None)
node_4 = Node(4, node_3, None)
node_8 = Node(8, node_4, None)

print sum_lists_backwards(node_8, node_3_1)




# given a link list, check if it is a palindrome.
# Baseline solution. I start walking down the array and adding letters to an array.
#
# walk down the array one way, walk down the array the other way and then return two strings that are one backwards
# one forwards and see if the strings are equal
def is_palindrome_rec(ll):
    if ll == None:
        return '', ''

    forward, backward = is_palindrome_rec(ll.next)

    return ll.value + forward, backward + ll.value

def is_palindrome(ll):
    forward, backward = is_palindrome_rec(ll)
    return forward == backward


print
print 'is palindrome'

node_r_1 = Node('r', None, None)
node_a_1 = Node('a', node_r_1, None)
node_c_1 = Node('c', node_a_1, None)
node_e = Node('e', node_c_1, None)
node_c_2 = Node('c', node_e, None)
node_a_2 = Node('a', node_c_2, None)
node_r_2 = Node('r', node_a_2, None)

node_g = Node('g', None, None)
node_o = Node('o', node_g, None)
node_d = Node('d', node_o, None)

print is_palindrome(node_r_2)
print is_palindrome(node_d)


# given two linked lists see if the two linked lists intersect (by reference)
# easiest way seems to be to walk both and store the map from values to node
# if the second walking ever finds a matching node return true. this is better done
# with a set
def intersection_dict(ll1, ll2):
    nodes = set([])

    node_1 = ll1
    while node_1 is not None:
        nodes = nodes.union(set([node_1]))

        node_1 = node_1.next

    node_2 = ll2
    while node_2 is not None:
        if node_2 in nodes:
            return node_2
        node_2 = node_2.next

    return None

# can I do this without a set
# could do an N*M algorithm where you walk down the second linked list multiple times
#
#
def intersection(ll1, ll2):
    pass

print
print 'intersection_dict'

node_1= Node(1, None, None)
node_2 = Node(2, node_1, None)
node_3 = Node(3, node_2, None)
node_4 = Node(4, node_3, None)
node_5 = Node(5, node_4, None)

node_6 = Node(6, node_3, None)
node_7 = Node(6, node_6, None)

node_8 = Node(8, None, None)
node_9 = Node(9, node_8, None)

print intersection_dict(node_5, node_7)
print intersection_dict(node_5, node_9)
print intersection_dict(node_7, node_9)



#
def loop_detection(ll1):


