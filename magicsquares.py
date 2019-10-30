import numpy as np

class MagicSquare:

    def __init__(self, n, *, xstep = 1, ystep = -1, flipud=False, fliplr=False, rotate=0):
        self._size = n
        self.xstep = xstep
        self.ystep = ystep
        m = self.generate_magic_square(n, xstep, ystep)
        m = MagicSquare.transform(m, flipud, fliplr, rotate)
        self._magic_square = m

    def __repr__(self):
        return repr(self.magic_square)

    def __str__(self):
        return self.print_matrix(self.magic_square, 2)

    def __len__(self):
        return self.size ** 2

    @property
    def size(self):
        return self._size

    @property
    def magic_sum(self):
        return MagicSquare.calculate_magic_sum(self.size)

    @property
    def magic_square(self):
        return self._magic_square

    @staticmethod
    def calculate_magic_sum(size):
        return int((1 + size ** 2) * (size // 2 + 0.5))

    @staticmethod
    def generate_magic_square(size, xstep = 1, ystep = -1):
        if size % 2 == 0:
            raise Exception('Size must be odd.')

        magic_square = np.zeros((size, size), dtype=int)

        num = 1
        r, c = 0, size//2
        while num <= size**2:
            magic_square[r, c] = num

            num += 1
            new_r, new_c = (r + ystep) % size, (c + xstep) % size
            if magic_square[new_r, new_c]:
                r = (r - ystep) % size
            else:
                r, c = new_r, new_c

        return magic_square

    @staticmethod
    def transform(m, rotate=0, flipud=False, fliplr=False):
        if rotate:
            m = np.rot90(m, k=rotate)
        if flipud:
            m = np.flipud(m)
        if fliplr:
            m = np.fliplr(m)
        return m

    @staticmethod
    def is_valid_magic_square(m):
        if isinstance(m, MagicSquare):
            m = m.magic_square

        size, *__ = m.shape

        magic_sum = MagicSquare.calculate_magic_sum(size)

        is_square = np.all(np.array(m.shape) == size)
        if not is_square: return False

        all_unique = np.unique(m).size == m.size
        if not all_unique: return False

        sums = np.hstack((np.sum(m, 0),
                          np.sum(m, 1),
                          np.sum(m.diagonal()),
                          np.sum(np.fliplr(m).diagonal())))

        all_sums_are_equal = np.all(sums == magic_sum)
        if not all_sums_are_equal: return False

        return True

    @staticmethod
    def info(m):
        if isinstance(m, MagicSquare):
            m = m.magic_square

        size, *__ = m.shape

        return {
            'Shape': m.shape,
            'Size': size,
            'Magic number': MagicSquare.calculate_magic_sum(size),
            'Sum of columns': np.sum(m, 0),
            'Sum of rows': np.sum(m, 1),
            'Sum of diagonals': [np.sum(m.diagonal()), np.sum(np.fliplr(m).diagonal())]
        }

    @staticmethod
    def print_matrix(m, separator_size = 1):
        if isinstance(m, MagicSquare):
            m = m.magic_square

        try:
            maximum = np.max(m)
            spacing = int(np.log10(maximum)) + 1
            separator = ' ' * max(1, separator_size)
            number_format = '%%%dd' % spacing
            return '\n'.join([separator.join([number_format % cell for cell in row]) for row in m])

        except:
            raise Exception('Not a 2D matrix of integers.') from None


class Sudoku(MagicSquare):

    def __init__(self, n = 9, *args, **kwargs):
        super().__init__(n, *args, **kwargs)


    @staticmethod
    def is_valid_magic_square(m):
        if isinstance(m, MagicSquare):
            m = m.magic_square

        size, *__ = m.shape

        magic_number = 3 * int((1 + (size//3) ** 2) * ((size//3) // 2 + 0.5))

        size_is_9 = size == 9
        is_square = np.all(np.array(m.shape) == size)
        is_all_row_sums = np.all(np.sum(m ,0) == magic_number)
        is_all_col_sums = np.all(np.sum(m, 1) == magic_number)
        is_valid = size_is_9 and is_square and is_all_row_sums and is_all_col_sums

        return is_valid

    @staticmethod
    def generate_sudoku(size = 3, xstep = 1, ystep = -1, largest_number = 9):
        m = MagicSquare.generate_magic_square(size, xstep, ystep)
        if largest_number:
            m = m % largest_number + 1
        return m


    @staticmethod
    def rotate(m, rotation = 0):
        return m


# ------------------------------------------------------------------------------------

if __name__ == '__main__':

    size  = 3

    m = MagicSquare(size, xstep = 1, ystep = -1)

    for item in MagicSquare.info(m).items():
        print( '%s: %s' % item)
    print()

    print( m )

    if MagicSquare.is_valid_magic_square(m):
        print("This is a valid Magic Square")
    else:
        print("This is a NOT valid Magic Square!!!")
    print()

    # s = Sudoku()
    #
    # print( s )
    #
    # if Sudoku.is_valid(s):
    #     print("This is a valid Sudoku")
    # else:
    #     print("This is a NOT valid Sudoku!!!")
    # print()

    squares = []

    squares.append( MagicSquare(3) )
    squares.append( MagicSquare(3, flipud=True) )
    squares.append( MagicSquare(3, fliplr=True) )
    squares.append( MagicSquare(3, flipud=True, fliplr=True) )
    squares.append( MagicSquare(3, rotate=1) )
    squares.append( MagicSquare(3, rotate=1, flipud=True) )
    squares.append( MagicSquare(3, rotate=1, fliplr=True) )
    squares.append( MagicSquare(3, rotate=1, flipud=True, fliplr=True) )
    squares.append( MagicSquare(3, rotate=2) )
    squares.append( MagicSquare(3, rotate=2, flipud=True) )
    squares.append( MagicSquare(3, rotate=2, fliplr=True) )
    squares.append( MagicSquare(3, rotate=2, flipud=True, fliplr=True) )
    squares.append( MagicSquare(3, rotate=3) )
    squares.append( MagicSquare(3, rotate=3, flipud=True) )
    squares.append( MagicSquare(3, rotate=3, fliplr=True) )
    squares.append( MagicSquare(3, rotate=3, flipud=True, fliplr=True) )

    for m in squares:
        print(m, '\n')

    for l in sorted([tuple(m.magic_square.flat) for m in squares]):
        print(l)
