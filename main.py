import logging
import multiprocessing
from multiprocessing import Pool
from multiprocessing.managers import SharedMemoryManager

logger = multiprocessing.log_to_stderr()
logger.setLevel(logging.INFO)


def main():
    smm = SharedMemoryManager()
    smm.start()
    ls = smm.ShareableList(range(2000))
    with Pool(4) as p:
        print(*list(p.imap_unordered(f, ls)), sep='\n')
        # print(p.map(f, [2, 3, 4, 5, 6]))  # lock
        # print(p.map(f, [2, 3, 4, 5, 6]))
    smm.shutdown()


def f(x):
    r = 1
    for i in range(10_000):
        r *= x
    return r  # todo shared_mem


if __name__ == '__main__':
    main()
