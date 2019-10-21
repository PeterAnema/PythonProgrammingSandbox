import doctest

def cube(n):
    """
    :param n: a number to take the cube of
    :return:

    >>> cube(10)
    1000

    >>> [cube(n) for n in range(10)]
    [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]
    """

    return n**3


if __name__ == "__main__":

    doctest.testmod(verbose=True)
