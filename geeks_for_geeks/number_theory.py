
# given x, y, p, computer the x^y % p
# x ^ y = (i = 1, y) x
# % == remainder when dividing by p
# 3 ^ 4 % 5
# 3 * 3 * 3 * 3 = 81 % 5 = 1
# 3 % 5 = 3 * 3 % 5 = 4 * 3 % 5 = 2 * 3 % 5 = 1
#
# 5 ^ 3 % 16 = 125 = 13
# 5 * 5 % 16 = 9 * 5 % 16 = 13
#
# 25 ^ 2 % 3 = 625 % 3 = 1
# 25 % 3 = 1 * 25 % 3 = 1
#
# a = 24, b = 1 where b = number % p
# number = part below mod (b), part above mod = a
# number = a + b
# number ^ y = (a + b) ^ y = (a + b) * (a + b) ...
# a^2 + 2ab + b2 = (a+b) * (a+b), anything with a is great than
def modular_exponentiation(x, y, p):
    total = 1

    for i in range(y):
        total = (total * (x%p)) % p
    return total


assert(2**3%5 == modular_exponentiation(2,3,5))
assert(15**3%7 == modular_exponentiation(15,3, 7))
assert(2**5%13 == modular_exponentiation(2, 5, 13))
