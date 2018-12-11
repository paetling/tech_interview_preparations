import sys

# describe how you would use a single array to implement three stacks
# If you did not mind wasting items you have an array and then three indices into the array
# Each indice indicates the top of the stack. when you push a new item on, you add three to the indice
# for that specific stack and then add a new item.
# This might end up with a lot of wasted space if the stacks significantly differ in size
#
# better option might be an array that holds indices of the next last item in the list.
# you would store (item, former_index) in the array. You would still need three pointers
# to the three heads. When you need to push a new item it just goes at the next place in the array,
# it stores the last index and the value.
# This does much better for space complexity.
#
# Should ask - can the stack grow in size
# Problem 1




# Problem 2 - stack min. How do you keep a stack that also has a min
# problem is that you need to be able to pop that min to the last value
# if you ever pop the min off the stack
#
# you need all push, pop, and min to operate in O(1) time
# You could make pop and min be O(1) if you used an extra linked list + a hash map
# but your insert would be O(N)
#
# need two things: stack ordered list, a way to always get the min.
# Inserting into a sorted list generally takes log n time
# data structures with constant time access - map, set, linked list, expanding arrays where no values are shifted
# use a second stack to store the min at that time, if you pop the items off, you should still be fine
#
# Needed to use the fact that in a stack only certain operations can happen at a time so you can't arbitrarily remove a value
# I should have walked through an example to get the juices flowing
# Our minimum stack could be smarter about pushes and pops. It only adds or removes if the minimum changes
class MinStack:
    def __init__(self):
        self.value_stack = []
        self.min_stack = []

    def push(self, value):
        new_min = min(value, self.min_stack[-1] if len(self.min_stack) > 0 else sys.maxint)
        self.value_stack.append(value)
        self.min_stack.append(new_min)

    def pop(self):
        self.min_stack.pop()
        return self.value_stack.pop()

    def min(self):
        return self.min_stack[-1]

print
print 'min stack'
min_stack = MinStack()

min_stack.push(5)
min_stack.push(3)
min_stack.push(2)
min_stack.push(8)
min_stack.push(3)

print min_stack.min()
min_stack.pop()
print min_stack.min()
min_stack.pop()
print min_stack.min()
min_stack.pop()
print min_stack.min()
min_stack.pop()
print min_stack.min()
min_stack.pop()




# Problem 3. Set of stacks. when a stack gets to high, we want to create a new stack
# pop and push should operate as if there was just one stack
#
# Example Insert 1,2,3,4,5,6,7 with max_stack_size = 3
# stacks = [1,2,3] [4, 5, 6], [7]
#
# Should have discussed the tradeoffs of some of my stacks not being at full capacity based on pop_at
class StackOfPlates:
    def __init__(self, max_stack_size = 3):
        self.stacks = [[]]
        self.max_stacK_size = max_stack_size

    def push(self, value):
        last_stack = self.stacks[-1]
        if len(last_stack) == self.max_stacK_size:
            last_stack = []
            self.stacks.append(last_stack)

        last_stack.append(value)

    def pop(self):
        return self.pop_at(0)

    # would want to ask which way the index counts from. I am assuming lower numbers is closer to the top
    def pop_at(self, index):
        if index >= len(self.stacks):
            return None

        stack = self.stacks[len(self.stacks) - 1 - index]
        if len(stack) == 1:
            self.stacks.pop(len(self.stacks) - 1 - index)

        return stack.pop()


print
print 'stack of plates'
stack_of_plates = StackOfPlates()
stack_of_plates.push(1)
stack_of_plates.push(2)
stack_of_plates.push(3)
stack_of_plates.push(4)
stack_of_plates.push(5)
stack_of_plates.push(6)
stack_of_plates.push(7)

print stack_of_plates.pop_at(2) # 3
print stack_of_plates.pop_at(2) # 2
print stack_of_plates.pop() # 7 ...
print stack_of_plates.pop()
print stack_of_plates.pop()
print stack_of_plates.pop()
print stack_of_plates.pop()



# Problem 4: Queue via stack
# implement a queue using two stacks
# if I push 1, 2, 3. When I pop, I need to get 1, 2, 3
# if I push 1,2,3 onto a stack you get top: [3, 2, 1]
# If when I pop an item I pull all items off of the one stack onto a second stack
# pop the top item and then push it back, you should be all set
# Could also optimize here by not moving the values until it is clear you need to
#
# Is there a way to do this in less time complexity?
class StackQueueOofN:
    def __init__(self):
        self.stack_order = []
        self.queue_order = []
        self.in_queue_state = False

    def swap_items_in_stacks(self, s1, s2):
        while (len(s1) > 0):
            s2.append(s1.pop())

    def push(self, value):
        if self.in_queue_state:
            self.swap_items_in_stacks(self.queue_order, self.stack_order)
            self.in_queue_state = False

        self.stack_order.append(value)


    def pop(self):
        if not self.in_queue_state:
            self.swap_items_in_stacks(self.stack_order, self.queue_order)
            self.in_queue_state = True

        return self.queue_order.pop()

print
print 'Stack Queue'
stack_queue = StackQueueOofN()
stack_queue.push(1)
stack_queue.push(2)
stack_queue.push(3)
stack_queue.push(4)
stack_queue.push(5)
print stack_queue.pop()
stack_queue.push(6)
print stack_queue.pop()
stack_queue.push(7)
print stack_queue.pop()
print stack_queue.pop()
print stack_queue.pop()
print stack_queue.pop()
print stack_queue.pop()



# Problem 5. Sort stack - sort a stack so that the smallest items are on top. You can only use an additional stack
# stack: top: [5, 3, 8, 1, 4]   other_stack: top: []
# pop the 5 and put it in the other stack.
# pop the three, if it is less than 5, pop the 5 off of the other_stack and put the value into the other stack
# basically want to continue popping values off of other stack till 3 is greater than the value left, push three in, pop all
# values back over

def sort_stack(left_stack):
    if len(left_stack) == 0:
        return stack

    right_stack = []

    while (len(left_stack) > 0):
        stack_value = left_stack.pop()

        popped_values_from_right = 0
        while(len(right_stack) > 0 and right_stack[-1] > stack_value):
            left_stack.append(right_stack.pop())
            popped_values_from_right += 1

        right_stack.append(stack_value)

        while popped_values_from_right > 0:
            right_stack.append(left_stack.pop())
            popped_values_from_right -= 1

    # need to push all values back to the left_stack
    while(len(right_stack)>0):
        left_stack.append(right_stack.pop())

    return left_stack

print
print 'sort stack'
print sort_stack([5,3,8,1,4])
print sort_stack([1,2,3,4,5,6])
print sort_stack([6,5,4,3,2,1])




# Problem 6: Animal Shelter
# use a doubly linked list that has a first dog pointer and a first cat pointer and a first animal pointer
# Could also just use two queues and have all animals have an index of when they are enqueued



