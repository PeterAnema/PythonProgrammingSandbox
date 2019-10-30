import math

class Vector:
    """A vector class"""

    __slots__ = ['_x', '_y']

    def __init__(self, x, y):
        self._x = x
        self._y = y

    def __repr__(self):
        return "Vector(%s,%s)" % (self._x, self._y)

    def __str__(self):
        return "[%s,%s]" % (self._x, self._y)

    def __add__(self, other):
        return Vector(self._x + other._x, self._y + other._y)
    def __sub__(self, other):
        return Vector(self._x - other._x, self._y - other._y)
    def __abs__(self):
        return self.magnitude()
    def __neg__(self):
        return Vector(-self._x, -self._y)
    def __pos__(self):
        return self

    def __eq__(self, other):
        return self._x == other._x and self._y == other._y
    def __ne__(self, other):
        return self.magnitude() != other.magnitude()
    def __lt__(self, other):
        return self.magnitude() < other.magnitude()
    def __le__(self, other):
        return self.magnitude() <= other.magnitude()
    def __gt__(self, other):
        return self.magnitude() > other.magnitude()
    def __ge__(self, other):
        return self.magnitude() >= other.magnitude()

    def magnitude(self):
        return (self._x ** 2 + self._y ** 2) ** 0.5
    def length(self):
        return self.magnitude()

    def angle(self, degrees=False):
        a = math.atan(self._y / self._x)
        if degrees:
            return math.degrees(a)
        else:
            return a

# =========================================

v1 = Vector(2,2)
v2 = Vector(-1,3)

print('v1 is %s' % v1)
print('v2 is %s' % v2)

v3 = v1 + v2

print('v1 + v2 is %s' % v3)

print('angle of v1 is %g°' % v1.angle(degrees=True))
print('length of v1 is %g' % v1.length())
