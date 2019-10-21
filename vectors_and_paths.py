import math
from functools import reduce
import turtle

class Vector:
    """A vector class"""
    
    def __init__(self, x, y):
        self._x = float(x)
        self._y = float(y)
    
    def __str__(self):
        return "(%g,%g)" % (self._x, self._y)
    
    def __repr__(self):
        return "Vector (%g,%g)" % (self._x, self._y)

    def __eq__(self, other):
        return self.length() == other.length()
        
    def __ne__(self, other):
        return self.length() != other.length()
        
    def __lt__(self, other):
        return self.length() < other.length()
        
    def __gt__(self, other):
        return self.length() > other.length()
        
    def __le__(self, other):
        return self.length() <= other.length()

    def __ge__(self, other):
        return self.length() >= other.length()

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

    def __iter__(self):
        yield self._x
        yield self._y

    def length(self):
        """Calculate euclidian distance"""
        return (self._x ** 2 + self._y ** 2) ** 0.5

    def distance(self):
        return self.length()

    def angle(self):
        return math.atan(self._y / self._x)

    def turtle(self):
        turtle.setpos(turtle.pos() + tuple(self))


class Path:
    """A path class where a path consists of a list of vectors"""
    
    def __init__(self, *vectors):
        self._path = []
        vectors = [Vector(*v) for v in vectors]
        self._path.extend(vectors)
    
    def __str__(self):
        return " > ".join(map(lambda x: str(x), self._path))
        
    def __repr__(self):
        return "Path " + self.__str__()
        
    def __eq__(self, other):
        return self.length() == other.length()
        
    def __ne__(self, other):
        return self.length() != other.length()
        
    def __lt__(self, other):
        return self.length() < other.length()
        
    def __gt__(self, other):
        return self.length() > other.length()
        
    def __le__(self, other):
        return self.length() <= other.length()

    def __ge__(self, other):
        return self.length() >= other.length()

    def __iter__(self):
        for v in self._path:
            yield v

    def addVector(self, vector):
        self._path.append(vector)

    def result(self):
        """A vector from the start to the end of the path"""
        if self._path:
            start = self._path[0]
            end = self._path[-1]
            return Vector(end._x - start._x, end._y - start._y)
        else:
            return Vector(0, 0)

    def length(self):
        """Calculate sum of euclidian distances of all vectors"""
        return reduce(lambda x, y: x + y, self._path)

    def distance(self):
        """Calculate the euclidian distances from the start to the end of the path"""
        return self.result().length()

    def turtle(self):
        for v in self._path:
            v.turtle()


# --------------------------------------------------------
# Client code

if __name__ == "__main__":

    v1 = Vector(10,20)
    v2 = Vector(30,40)

    print(v1.length())
    print(v2.length())

    print("v1 is longer" if v1 > v2 else "v2 is longer" if v2 > v1 else "v1 and v2 are equal")

    p1 = Path(v1,v2)

    print(p1)
    print(p1.length())

    p2 = Path(v2,v1)
    p2.addVector(v1)
    p2.addVector(v2)

    print(p2)
    print(p2.length())

    print("p1 is longer" if p1 > p2 else "p2 is longer" if p2 > p1 else "p1 and p2 are equal")


    p3 = Path((100,100), (50,-100), (-300, -200), (100,100), (-100,100))

    p3.turtle()
    turtle.done()