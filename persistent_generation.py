import random

def persistent_generation(seed):
    random.seed(seed)
    for _ in range(1000):
        yield random.randint(1, 10000000)

gen = persistent_generation(12345) # same number will produce same results for persistent generation
for _ in range(1000):
    print(next(gen))
