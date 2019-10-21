def magic_square(size):
    if size % 2 == 0:
        raise Exception('Size must be odd.')

    magic_square = [[0 for __ in range(size)] for __ in range(size)]

    r = 0
    c = size // 2

    for number in range(1, size**2 + 1):

        magic_square[r][c] = number

        next_r = (r - 1) % size
        next_c = (c + 1) % size

        if magic_square[next_r][next_c]:
            next_r = (r + 1) % size
            next_c = c

        r = next_r
        c = next_c

    return magic_square

def magic_sum(size):
    return int((1 + size**2) * (size//2 + 0.5))

def check_magic_square(m):
    size = len(m)

    sums = [sum(m[r]) for r in range(size)] + \
           [sum(m[r][c] for r in range(size)) for c in range(size)] + \
           [sum(m[r][r] for r in range(size))] + \
           [sum(m[r][-r-1] for r in range(size))]

    return all(sum == magic_sum(size) for sum in sums)

# -----------------------------------------------------------

size = 3

m = magic_square(size)

for row in m:
    for number in row:
        print('%4d' % number, end='')
    print()

print('The magic sum is %d' % magic_sum(size))

if check_magic_square(m):
    print('All sums are equal. This is a magic square!')
else:
    print('Not all sums are equal. This is a not a valid magic square!')