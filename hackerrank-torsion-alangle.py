import math

class Point(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __sub__(self, no):
        return Point(self.x - no.x, self.y - no.y, self.z - no.z)

    def dot(self, no):
        return self.x * no.x + self.y * no.y + self.z * no.z

    def cross(self, no):
        return Point(self.y * no.z - no.y * self.z,
                     self.z * no.x - no.z * self.x,
                     self.x * no.y - no.x * self.y)

    def absolute(self):
        return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)



if __name__ == '__main__':

    a = Point(0,4,5)
    b = Point(1,7,6)
    c = Point(0,5,9)
    d = Point(1,7,2)

    # points = list()
    # for i in range(4):
    #     a = list(map(float, input().split()))
    #     points.append(a)
    #
    # a, b, c, d = Points(*points[0]), Points(*points[1]), Points(*points[2]), Points(*points[3])

    x = (b - a).cross(c - b)
    y = (c - b).cross(d - c)
    angle = math.acos(x.dot(y) / (x.absolute() * y.absolute()))

    print("%.2f" % math.degrees(angle))
