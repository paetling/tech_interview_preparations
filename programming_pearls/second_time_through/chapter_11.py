import random

def rand_sequence(N, M):
    indices = range(N)
    random_numbers = []
    for i in range(M):
        index = random.randint(0, len(indices) - 1)
        random_numbers.append(indices.pop(index))

    return random_numbers

print rand_sequence(10000, 5)


def in_order_random_sequence(N, M):
    random_numbers = []
    for i in range(N):
        if (random.random() < ((M - len(random_numbers)) * 1.0 / (N - i))):
            random_numbers.append(i)
            if len(random_numbers) == M:
                break
    return random_numbers

print in_order_random_sequence(10000, 5)
