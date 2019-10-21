from decimal import Decimal

class Currency():

    __slots__ = ['__value', '__prefix']

    def __init__(self, value, prefix = '€'):
        self.__value = Decimal(str(value))
        self.__prefix = prefix

    def __repr__(self):
        return 'Euro(%.2f)' % (self.__value)

    def __str__(self):
        return '%s %.2f' % (self.__prefix, self.__value)

    def __add__(self, other):
        return type(self)(self.__value + Decimal(repr(other)))

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        return type(self)(self.__value - Decimal(repr(other)))

    def __rsub__(self, other):
        return self.__sub__(other)

    def __mul__(self, other):
        if type(other) in (int, float):
            return type(self)(self.__value * Decimal(repr(other)))
        else:
            raise TypeError('unsupported operand type(s) for *')

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        if type(other) in (int, float):
            return type(self)(self.__value / Decimal(repr(other)))
        elif isinstance(other, Currency):
            return self.__value / Decimal(repr(other))
        else:
            raise TypeError('unsupported operand type(s) for *')


class Euro(Currency):

    def __init__(self, value):
        super().__init__(value, '€')


class Dollar(Currency):

    def __init__(self, value):
        super().__init__(value, '$')


# ----------------------------------------- client code

if __name__ == '__main__':

    e1 = Euro(0.1)
    e2 = Euro(0.2)
    e3 = e1 + e2
    e4 = e2 - e1

    print(e1)
    print(e2)
    print(e3)
    print(e4)
    print(e1 + 1)
    print(8 * e2)
    print(1 + e1)
    print(e2 / e1)

    print(Euro(2/3))