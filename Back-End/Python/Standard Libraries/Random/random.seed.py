import random


def generate_random(seed=None):

    random.seed(seed)
    result = []

    # Randint
    for _ in range(5):
        result.append(random.randint(0, 5))

    # Shuffle
    characters = ['a', 'b', 'c', 'd']
    random.shuffle(characters)
    result.append(characters)

    # Gaussian distribution
    for _ in range(5):
        result.append(random.gauss(0, 1))

    return result


# print(generate_random())

print(generate_random(0))