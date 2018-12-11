#selecting m random integers from a set 0 - N, in order

#1. Not completely random: divide N into m seconds and do randint() for each of those sections - O(M)
#2. Sample N using randInt, insert into sorted array, find your location using binary search or linear search depending on
#3. Use big random number and % N, and then do the insertion described above
