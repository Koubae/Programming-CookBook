import random
from multiprocessing import Pool, cpu_count
from math import sqrt
from timeit import default_timer as timer

# Calculate Estimate of π: 

def pi_part(n):
    print(n)

    count = 0

    for i in range(int(n)):

        x, y = random.random(), random.random()

        r = sqrt(pow(x, 2) + pow(y, 2))

        if r < 1:
            count += 1

    return count


def main():

    start = timer()

    np = cpu_count()
    print(f'You have {np} cores')

    n = 100_000_000

    part_count = [n/np for i in range(np)]

    with Pool(processes=np) as pool:

        count = pool.map(pi_part, part_count)
        pi_est = sum(count) / (n * 1.0) * 4

        end = timer()

        print(f'elapsed time: {end - start}')
        print(f'π estimate: {pi_est}')

if __name__=='__main__':
    main()
