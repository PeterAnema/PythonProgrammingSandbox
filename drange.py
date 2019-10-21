from decimal import Decimal

def drange(start, stop, step = 1, endpoint = False):
    decimal_start = Decimal(str(start))
    decimal_stop = Decimal(str(stop))
    decimal_step = Decimal(str(step))

    r = decimal_start
    while ((decimal_step > 0 and r < decimal_stop) or
           (decimal_step < 0 and r > decimal_stop)):

        yield float(r)
        r += decimal_step

    if endpoint:
        if ((decimal_step > 0 and r <= decimal_stop) or
            (decimal_step < 0 and r >= decimal_stop)):
            yield float(r)


# -----------------------------------------------------------------------

if (__name__ == '__main__'):

    assert list(drange(0, 2, 0.2)) == [0.0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8]
    assert list(drange(0, 2, 0.2, endpoint=True)) == [0.0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0]
    assert list(drange(4, 3, -0.1)) == [4.0, 3.9, 3.8, 3.7, 3.6, 3.5, 3.4, 3.3, 3.2, 3.1]
    assert list(drange(0, 4)) == [0.0, 1.0, 2.0, 3.0]
    assert list(drange(5, 4)) == []
    assert list(drange(0, 4, -1)) == []

    print(list(drange(0, 4, 0.2)))
    print(list(drange(0, 4, 0.2, endpoint=True)))
    print(list(drange(4, 0, -0.1)))

    print(list(drange(0, 4)))
    print(list(drange(0, 4, endpoint=True)))

    print(list(drange(5, 4)))
    print(list(drange(0, 4, -1)))
