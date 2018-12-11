def problem_3(number_array):
    bitmap = [0]*100000

    for number in number_array:
        bitmap_index = number >> 4
        bit_to_turn_on = number & 15
        bitmap[bitmap_index] |= (1 << bit_to_turn_on)

    output_list = []
    for bitmap_index in range(len(bitmap)):
        bitmap_number = bitmap[bitmap_index]

        for bit_index in range(16):
            bit = (bitmap_number >> bit_index) & 1
            if (bit == 1):
                output_list.append((bitmap_index << 4) | bit_index)
    return output_list

print problem_3([5, 4, 3, 2, 1])
print problem_3([1000, 500, 125, 1025, 5, 1, 10000])
print problem_3([2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768])



