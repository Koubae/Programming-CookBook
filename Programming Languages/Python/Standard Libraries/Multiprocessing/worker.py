import multiprocessing as mp
import math

def worker(nums, out_q):
    outdict = {}
    for n in nums:
        outdict[n] = 2 * n
    out_q.put(outdict)

def mp_factorizer(nums, nprocs):
    out_q = mp.Queue()
    chunksize = int(math.ceil(len(nums) / float(nprocs)))
    procs = []

    for i in range(nprocs):
        p = mp.Process(
                target=worker,
                args=(nums[chunksize * i:chunksize * (i + 1)],
                      out_q))
        procs.append(p)
        p.start()

    resultdict = {}
    for i in range(nprocs):
        resultdict.update(out_q.get())

    for p in procs:
        p.join()

    return resultdict

if __name__ == "__main__":
    print(mp_factorizer(range(100), 3))