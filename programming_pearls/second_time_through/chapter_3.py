def ans(a_list, c_list, N):
    sum_array = [0]
    a_list = [1] + a_list
    for i in range(N):
        c = c_list[len(c_list) - 1 -i]
        new_total = sum_array[i] + a_list[i] * c

        sum_array.append( sum_array[i] + a_list[i] * c)
        if (i + 1 >= len(a_list)):
            a_list.append(new_total)
    return a_list[1:], sum_array

print ans([1, 2, 3], [4, 5, 6, 7, 8, 9, 10, 11], 8)


def date_since_1970(date):
    return (date[2] - 1970) * 365 + sum(months_of_year[0:date[1]]) + date[0]

months_of_year = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
def date_difference(date_1, date_2):

    return abs(date_since_1970(date_1) - date_since_1970(date_2))

print date_difference([1, 0, 1970], [2, 0, 1970])
print date_difference([1, 5, 2005], [2, 6, 2006])
print date_difference([1, 5, 2005], [2, 6, 2010])



number_mapping = {
    0: [1, 0, 1, 1, 1, 1, 1],
    1: [0, 0, 0, 0, 1, 0, 1],
    2: [1, 1, 1, 0, 1, 1, 0],
    3: [1, 1, 1, 0, 1, 0, 1],
    4: [0, 1, 0, 1, 1, 0, 1],
    5: [1, 1, 1, 1, 0, 0, 1],
    6: [1, 1, 1, 1, 0, 1, 1],
    7: [0, 0, 1, 0, 1, 0, 1],
    8: [1, 1, 1, 1, 1, 1, 1],
    9: [0, 1, 1, 1, 1, 0, 1],
}
def print_number(seven_segment_sequence):
    for i in range(5):
        if i == 0 and (seven_segment_sequence[2]):
                print 'x'*5
        elif i == 1:
            if(seven_segment_sequence[3] and seven_segment_sequence[4]):
                print 'x' + ' '*3 + 'x'
            elif(seven_segment_sequence[3]):
                print 'x' + ' '*4
            elif(seven_segment_sequence[4]):
                print ' '*4 + 'x'
            else:
                print ' '* 5
        elif i == 2 and (seven_segment_sequence[1]):
                print 'x'*5
        elif i == 2:
            if((seven_segment_sequence[3] or seven_segment_sequence[5]) and (seven_segment_sequence[4] or seven_segment_sequence[6])):
                print 'x' + ' '*3 + 'x'
            elif(seven_segment_sequence[3]):
                print 'x' + ' '*4
            elif(seven_segment_sequence[4]):
                print ' '*4 + 'x'
            elif(seven_segment_sequence[5]):
                print 'x' + ' '*4
            elif(seven_segment_sequence[6]):
                print ' '*4 + 'x'
            else:
                print ' '* 5
        elif i == 3:
            if(seven_segment_sequence[5] and seven_segment_sequence[6]):
                print 'x' + ' '*3 + 'x'
            elif(seven_segment_sequence[5]):
                print 'x' + ' '*4
            elif(seven_segment_sequence[6]):
                print ' '*4 + 'x'
            else:
                print ' '* 5
        elif i == 4 and (seven_segment_sequence[0]):
                print 'x'*5
        elif i == 4:
            if(seven_segment_sequence[5] and seven_segment_sequence[6]):
                print 'x' + ' '*3 + 'x'
            elif(seven_segment_sequence[5]):
                print 'x' + ' '*4
            elif(seven_segment_sequence[6]):
                print ' '*4 + 'x'
            else:
                print ' '* 5
    print
    print

def print_integer(integer):
    if integer == 0:
        print_number(number_mapping[0])

    numbers_to_print = []
    while integer > 0:
        value = integer%10
        numbers_to_print.insert(0, value)
        integer /= 10

    for number in numbers_to_print:
        print_number(number_mapping[number])

print_integer(15)
print_integer(1235)
