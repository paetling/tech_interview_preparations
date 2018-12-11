def swap(array, index1, index2):
    val = array[index1]
    array[index1] = array[index2]
    array[index2] = val

def insertion_sort(array):
    for i in range(len(array)):
        j = i
        while j > 0 and array[j-1] > array[j]:
            swap(array, j-1, j)
            j -=1

def bubble_sort(array):
    for i in range(len(array)):
        for j in range(i +1 , len(array)):
            if (array[i] > arary[j]):
                swap(array, i, j)

def quick_sort(array, l, u):
    if (l >= u):
        return array

    comparator = array[l]

    m = l
    for i in range(l+1, u + 1):
        if (array[i] < comparator):
            m+=1
            swap(array, m, i)
    swap(array, l, m)

    quick_sort(array, l, m - 1)
    quick_sort(array, m + 1, u)




array = []
from random import *
for i in range(10000):
    array.append(randint(1, 10000))

quick_sort(array, 0, len(array) - 1)
print array
