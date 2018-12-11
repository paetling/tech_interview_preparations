# Heaps have two properties the smallest value is at the head
# All values are less than their children (below them)
# Shape - terminal values are on at most two levels

# Insert into the last spot in the heap and then swap with the parent until
# it is in the right place
def swap(heap, index1, index2):
    temp = heap[index1]
    heap[index1] = heap[index2]
    heap[index2] = temp

def insert_into_heap(heap, value):
    if len(heap) == 0:
        heap.append(None)

    heap.append(value)
    value_index = len(heap) - 1

    while heap[value_index] < heap[value_index / 2]:
        swap(heap, value_index, value_index/2)
        value_index /= 2
    return heap

def get_left_heap_child(heap, current_index):
    return heap[current_index*2] if (current_index*2) < len(heap) else None

def get_right_heap_child(heap, current_index):
    return heap[current_index*2 + 1] if (current_index*2) + 1 < len(heap) else None

def swap_down_index(heap, current_index):
    current_value = heap[current_index]
    left_child = get_left_heap_child(heap, current_index)
    right_child = get_right_heap_child(heap, current_index)

    if left_child is not None and right_child is not None:
        if (current_value > left_child) and current_value > right_child:
            if left_child < right_child:
                return current_index*2
            else:
                return current_index*2 +1
        elif current_value > left_child and current_value < right_child:
            return current_index*2
        elif current_value < left_child and current_value > right_child:
            return current_index*2+1
    elif left_child is not None and current_value > left_child:
        return current_index*2
    elif right_child is not None and current_value > right_child:
        return current_index*2+1
    else:
        return None

def pop_from_heap(heap):
    if len(heap) <= 1:
        return None
    if len(heap) == 2:
        return heap.pop()

    current_index = 1
    return_val = heap[current_index]
    heap[current_index] = heap.pop()

    swap_index = swap_down_index(heap, current_index)

    while swap_index is not None:
        swap(heap, current_index, swap_index)

        current_index = swap_index
        swap_index = swap_down_index(heap, current_index)

    return return_val


heap1 = []
print insert_into_heap(heap1, 10)
print insert_into_heap(heap1, 15)
print insert_into_heap(heap1, 2)
print insert_into_heap(heap1, 8)
print insert_into_heap(heap1, 1)
print insert_into_heap(heap1, 4)

print pop_from_heap(heap1)
print pop_from_heap(heap1)
print pop_from_heap(heap1)
print pop_from_heap(heap1)
print pop_from_heap(heap1)
print pop_from_heap(heap1)
