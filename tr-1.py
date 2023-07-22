import random
import hashlib
from functools import lru_cache

def calculate_average():
    c = (66 ** 6)
    d = (66 ** 6) ** 6
    e = (66 ** 6)
    f = (66 ** 6) ** 6

    def generate_seed():
        a = random.randint(c, d)
        b = random.randint(1, c)
        return random.randint(b, a)

    def seed_generator(n):
        seed = generate_seed()
        random.seed(seed)
        for _ in range(n):
            yield random.randint(e, f)

    @lru_cache(maxsize=None)
    def structured_integer(seed, length):
        def generator():
            i = 0
            while True:
                random.seed(hashlib.sha256((str(seed) + str(i)).encode()).digest())
                yield str(random.randint(e, f)).zfill(10)  # pad with zeros
                i += 1
        v = random.randint(1, 12)
        gen = generator()
        num_blocks = -(-length // v)  # round up division
        result = ''.join(next(gen) for _ in range(num_blocks))
        result = result * v
        result = result[:length]
        return result  # truncate to desired length

    length = 80
    base_seed = generate_seed()
    seeds = seed_generator(base_seed)
    cumulative = 0
    n = random.randint(1, 9999999)
    c = random.randint(1, 999)
    count = 0

    for seed in seeds:
        if count == c:
            break
        number = structured_integer(seed, length)
        cumulative += int(number)
        count += 1

    cumulative = cumulative * c
    length2 = len(str(cumulative))
    length = length2 - length 
    cumulative = str(cumulative)
    cumulative = cumulative[length:]
    average = int(cumulative) // c
    return average

average = calculate_average()
print(average)
