def bsearch(__iterable, item):
    low = 0
    high = len(__iterable) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = __iterable[mid]
        if guess > item:
            high = mid - 1
            continue
        if guess < item:
            low = mid + 1
            continue
        if guess == item:
            return mid
    return -1


if __name__ == '__main__':
    from random import choice
    from utils.time import timeit

    l = [x for x in range(2 ** 24)]
    item = choice(l)
    t1, r1 = timeit(ret_time=True)(bsearch)(l, item)
    t2, r2 = timeit(ret_time=True)(l.index)(item)
    print(t2 / t1)
