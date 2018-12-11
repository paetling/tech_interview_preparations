from random import random

#
# Complete the 'decode_target' function below.
#
# The function is expected to return an INTEGER (target value).
# The function accepts following parameters:
#  1. ANONYMOUS FUNCTION noisy_xor
#  2. INTEGER N (number of bits of target value)
#


# givn an integer and some noisy integer I want to be able to determine the output value with high precisions
# N represents the 2^n bounding value of s. want to find the value of S with very high probability. WAnt to be able to determine the value of
# each bit with very high probability
# 1 bit xored with 1 xored with 1 if third bit is set to 1 (prob .05) else 0
# proceedure would be to check at each bit to ensure this bit is this value with very high precision. use the highest precision for each bit
# can do each bit up to 10,000 / N times

# if I could do that, and control my own inputs or ith bit with 0, 0 if 0, 1 if its 1 and random value: P(1) = .5, P(1 | d) = P(d | 1) * P (1) / P(d)
#
# 42 = 101010

# or it with random values -> get back a number of ones - xor with all ones a bunch of times and xor with all 0s a bunch of times we expect the total number of 1s difference between them to be 0, then we know that this value
# S X
# 0 0  - 0:  if you start with 0s and when you switch to 1s the value of ones increases -> s value was 0
# 1 0  - 1:  if you start with 0s and when you switch to 1s the vaues of ones decreases -> s value was 1 the whole time
# 0 1 -  1
# 1 1 -  0
# .95 percent of the time this will work out, .5 percent of the time it will not

# probability updater function: given a start value, an experiemnt, what is your new expectation for value
# probaiblity of 1 starts at .5, 1 (means the value of ones decreases in two tests),
# P(d | 1):
#   higher, lower: .9025  (random is at 0 both times)
#   same, same: .095(random value is at 0 1 time and 1 other)
#   lower, higher: (value was at 1 both times): .0025

# P(d | 0):
#   higher, lower: .0025 (random is at 0 both times)
#   same, same: .095(random value is at 0 1 time and 1 other)
#   lower, higher: (value was at 1 both times): .9025

# P(1) = old probablity
# P(d) = P(d | 1) + P(d | 2)
# P(new) = bayesian equation above


times_through = 10000
def get_noisy_xor(S, N):
    def noisy_xor(x):
        global times_through
        if times_through <= 0:
            raise 'You cannot call this function anymore'
        times_through -= 1

        noise_value = sum([i**2 if random() < .05 else 0 for i in range(N)])
        return bin(S ^ x ^ noise_value).count("1")
    return noisy_xor

def updated_probability(initial, p_d_initial, p_d):
    return initial * p_d_initial / p_d

def decode_target(noisy_xor, N):
    iterations_per_bit = int(10000 / ((N + 1)*2))
    final_value = 0

    for i in list(range(N + 1)):
        current_probability_1 = .5
        bit_mask_0 = 0
        bit_mask_1 = 2**i

        for iterations in range(iterations_per_bit):
            p_d = 0.0
            p_d_initial = 0.0
            initial_value = noisy_xor(bit_mask_0)
            secondary_value = noisy_xor(bit_mask_1)

            if initial_value < secondary_value:
                p_d_initial = .025
                p_d = current_probability_1 * p_d_initial + (1-current_probability_1) * .9025

            elif initial_value == secondary_value:
                p_d_initial = .095
                p_d = current_probability_1 * p_d_initial + (1-current_probability_1) *.095

            else:
                p_d_initial = .9025
                p_d = current_probability_1 * p_d_initial + (1-current_probability_1) * .025
            current_probability_1 = updated_probability(current_probability_1, p_d_initial, p_d)

        if current_probability_1 > .5:
            final_value += 2**i
    return final_value

x = 285
N = 9
guessed_x = decode_target(get_noisy_xor(x, N), N)
print x, guessed_x
