import random
import hashlib
from functools import lru_cache

def generate_seed():
    return random.randint(1, 66 ** 6)

def seed_generator(seed):
    random.seed(seed)
    for _ in range(10):
        yield random.randint(1, 66 ** 6)

@lru_cache(maxsize=None)
def structured_integer(seed, length):
    def generator():
        i = 0
        while True:
            random.seed(hashlib.sha256((str(seed) + str(i)).encode()).digest())
            yield str(random.randint(0, 218749378780555415)).zfill(10)  # pad with zeros
            i += 1

    gen = generator()
    num_blocks = -(-length // 10)  # round up division
    result = ''.join(next(gen) for _ in range(num_blocks))
    result = result[:length]
    return result # truncate to desired length

target = 54387534275
length = len(str(target))

base_seed = generate_seed()
seeds = seed_generator(base_seed)

for seed in seeds:
    number = structured_integer(seed, length)
    print(number)
