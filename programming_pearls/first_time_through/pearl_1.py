from bitmap import BitMap

import random
array = range(100)

randomArray = []

while(len(array)> 0):
    index = random.randint(0, len(array) - 1)
    randomArray.append(array.pop(index))

print randomArray

size = 10000
mp = BitMap(size)

for i in randomArray:
    mp.set(i)

for i in range(size):
    if mp.test(i):
        print i
