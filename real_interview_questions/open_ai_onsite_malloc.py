class Node:
    def __init__(self, size, allocated, next_node, prev_node):
        self.size = size
        self.allocated = allocated
        self.next = next_node
        self.prev = prev_node

    def __str__(self):
        return 'size:{}, allocated:{}\nNext:{}'.format(self.size, self.allocated, self.next)



initial_size = 1000
memory = Node(initial_size, False, None, None)

def malloc(needed_size):
    global memory
    current_node = memory

    # print(current_node)
    while(current_node is not None):
        if current_node.size >= needed_size and not current_node.allocated:
            current_nodes_next = current_node.next
            current_nodes_prev = current_node.prev
            # print('allocating', current_node, 'next', current_nodes_next, 'prev', current_nodes_prev)

            new_right_node = Node(current_node.size - needed_size, False, current_nodes_next, None)
            new_left_node = Node(needed_size, True, new_right_node, current_nodes_prev)
            new_right_node.prev = new_left_node
            if current_nodes_prev:
                current_nodes_prev.next = new_left_node
            if current_nodes_next:
                current_nodes_next.prev = new_right_node

            if current_node == memory:
                memory = new_left_node
            return new_left_node

        current_node = current_node.next

    raise Exception('Cannot find memory needed')


def free(node):
    if not node.allocated:
        raise Exception('Memory has already been freed')

    node.allocated = False

    # print('freeing\n')
    node_to_merge = node
    next_node = node.next
    sum_value = node.size
    if node.next is not None and not node.next.allocated:
        # print('right is free')
        next_node = node.next.next
        sum_value += node.next.size

    if node.prev is not None and not node.prev.allocated:
        # print('left is free')
        node_to_merge = node.prev
        sum_value += node.prev.size

    # print ('updates', node_to_merge, next_node, sum_value)
    node_to_merge.next = next_node
    if next_node:
        next_node.prev = node_to_merge
    node_to_merge.size = sum_value


many = [malloc(5) for _ in range(100)]

print(memory)

for ptr in many[:50]:
    free(ptr)

print('hey \n\n\n')
print(memory)

a = malloc(200)
b = malloc(500)

print(memory)



