def insort(__iterable):
    dst = [x for x in __iterable]
    if len(dst) < 2:
        return dst

    for j in range(1, len(dst)):
        key = dst[j]
        i = j - 1
        while i >= 0 and dst[i] > key:
            dst[i + 1] = dst[i]
            i -= 1
        dst[i + 1] = key
    return dst


if __name__ == '__main__':
    from utils.time import timeit
    from random import randint

    l = [randint(-2 ** 13, 2 ** 13) for _ in range(2 ** 8)]
    # print(l)
    print(timeit()(insort)(l))
