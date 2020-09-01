import itertools
import numpy as np

def calculate_magic_sum(size):
    return int((1 + size**2) * (size//2 + 0.5))

def is_valid_magic_square(m):
    size, *__ = m.shape

    is_square = np.all(np.array(m.shape) == size)
    if not is_square: return False

    all_unique = np.unique(m).size == m.size
    if not all_unique: return False

    sums = np.hstack((np.sum(m, 0),
                      np.sum(m, 1),
                      np.sum(m.diagonal()),
                      np.sum(np.fliplr(m).diagonal())))

    magic_sum = calculate_magic_sum(size)

    all_sums_are_equal = np.all(sums == magic_sum)
    if not all_sums_are_equal: return False

    return True

all = [
    (2, 7, 6, 9, 5, 1, 4, 3, 8),
    (2, 9, 4, 7, 5, 3, 6, 1, 8),
    (4, 3, 8, 9, 5, 1, 2, 7, 6),
    (4, 9, 2, 3, 5, 7, 8, 1, 6),
    (6, 1, 8, 7, 5, 3, 2, 9, 4),
    (6, 7, 2, 1, 5, 9, 8, 3, 4),
    (8, 1, 6, 3, 5, 7, 4, 9, 2),
    (8, 3, 4, 1, 5, 9, 6, 7, 2)
]

all = itertools.product(*(list(range(1,10)) for __ in range(1,10)))

found = set()
for i, t in enumerate(all):
    a = np.array(t).reshape(3,3)
    if is_valid_magic_square(a):
        found.add(t)
        print(a)
    if i % 10000 == 0:
        print(i)

print("%d magic squares found" % len(found))
for a in found:
    print(a)

