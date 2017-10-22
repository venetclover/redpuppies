def batch(iterable, n=1):
    l = len(iterable)
    for ind in range(0, l, n):
        yield iterable[ind: min(ind+n, l)]
