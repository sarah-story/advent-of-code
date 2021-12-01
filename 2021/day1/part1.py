import collections
from itertools import islice


def sliding_window_operation(iterable, n, func):
    it = iter(iterable)
    window = collections.deque(islice(it, n), maxlen=n)
    if len(window) == n:
        yield func(*window)
    for x in it:
        window.append(x)
        yield func(*window)


def compare_depths(first, second):
    if second > first:
        return 1
    else:
        return 0


if __name__ == '__main__':
    with open('input.txt') as file:
        depths = [int(line) for line in file]

    print(sum(sliding_window_operation(depths, 2, compare_depths)))

