import doctest


def kwadraat(n):
    """Documentatie die bij deze functie hoort!!

    Doctest:
    >>> kwadraat(4)
    16
    >>> [kwadraat(x) for x in range(6)]
    [0, 1, 4, 9, 16, 25]
    """

    return n ** 2

# -------------------------------------------------------------------
    
if __name__ == "__main__":
    doctest.testmod(verbose=True)
    
