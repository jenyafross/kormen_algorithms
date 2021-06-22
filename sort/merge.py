def msort(__iterable, start=None, end=None):
    start = start if start is not None else 0
    end = end if end is not None else len(__iterable)
    if start < end - 1:
        mid = (start + end) // 2
        msort(__iterable, start, mid)
        msort(__iterable, mid, end)
        merge(__iterable, start, mid, end)


def merge(__iterable, p=0, q=0, r=0):
    left = [__iterable[p + i] for i in range(q - p)] + [float('inf')]
    right = [__iterable[q + i] for i in range(r - q)] + [float('inf')]

    i = j = 0
    for k in range(p, r):
        if left[i] <= right[j]:
            __iterable[k] = left[i]
            i += 1
        else:
            __iterable[k] = right[j]
            j += 1


if __name__ == '__main__':
    from utils.time import timeit
    from random import randint

    l = [randint(-2 ** 13, 2 ** 13) for _ in range(2 ** 2 + 1)]
    sl = timeit()(sorted)(l)
    timeit()(msort)(l)
    print(l == sl)
