

# 2 numbers:
# + + : accept both
# - + : take just the postitive
# + - : take just the positive
# - - : reject both

# 3 numbers:
# +++ : accept all
# --- : reject all

# ++- : accept the two positives in a row
# -++

# --+ : accept the one psitive in a row
# +--

# +-+ : if negative is less than than one of the positives you want to take it - it forms a connective positive chain could be useful

# -+-: accept the positive


start_index = -1
end_index = -1
max_max = -1
negative_sum = 0

current_max = 0
current_start = 0
current_end = 0

array = [31, -41, 59,  26, -53, 58, 97, -93, -23, 84]

for index in range(len(array)):
    current_val = array[index]
    print current_val
    print current_max, current_start, current_end

    if (current_val > 0 and ((negative_sum + current_max) >= 0) and (negative_sum + current_val) > 0):
        print '1'
        current_max += current_val + negative_sum
        current_end = index
        negative_sum = 0

    elif ((current_val > 0 and (negative_sum + current_max) >= 0 and (negative_sum + current_val) <= 0) or (current_val > 0 and (negative_sum + current_max) < 0 )):
        print '2'
        if (current_max > max_max):
            max_max = current_max
            start_index = current_start
            end_index = current_end

        current_max = current_val
        current_end = index
        current_start = index
        negative_sum = 0
    elif (current_val < 0 ):
        print '3'
        negative_sum += current_val

    print current_max, current_start, current_end

if (current_max > max_max):
    max_max = current_max
    start_index = current_start
    end_index = current_end
print start_index, end_index, max_max
