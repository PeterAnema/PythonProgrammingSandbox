import sys
import math
import pygame
from pygame import Vector2
from pygame import Rect

class LineSegment:

    def __init__(self, p1, p2):
        self.p1 = Vector2(p1)
        self.p2 = Vector2(p2)
        self.vector_from_p1 = Vector2(self.p2.x - self.p1.x, self.p2.y - self.p1.y)

    def __repr__(self):
        return 'LineSegment((%g, %g), (%g, %g))' % (self.p1.x, self.p1.y, self.p2.x, self.p2.y)

    def __str__(self):
        return 'LineSegment from (%g, %g) to (%g, %g))' % (self.p1.x, self.p1.y, self.p2.x, self.p2.y)

    def intersection(self, other):
        if self.is_horizontal():
            if other.is_horizontal():
                return None # parallel lines - no intersection

            elif other.is_vertical():
                intersection_point = Vector2(other.p1.x, self.p1.y)

            else:
                dy = self.p1.y - other.p1.y
                slope = other.inverse_slope()
                intersection_point = Vector2(int(other.p1.x + slope * dy), self.p1.y)

        elif self.is_vertical():
            if other.is_horizontal():
                intersection_point = Vector2(self.p1.x, other.p1.y)

            elif other.is_vertical():
                return None     # parallel lines - no intersection

            else:
                dx = self.p1.x - other.p1.x
                slope = other.slope()
                intersection_point = Vector2(self.p1.x, int(other.p1.y + slope * dx))

        else:
            if other.is_horizontal():
                dy = other.p1.y - self.p1.y
                slope = self.inverse_slope()
                intersection_point = Vector2(int(self.p1.x + slope * dy), other.p1.y)

            elif other.is_vertical():
                dx = other.p1.x - self.p1.x
                slope = self.slope()
                intersection_point = Vector2(other.p1.x, int(self.p1.y + slope * dx))

            else:
                # (y-p1y) = rc1 * (x-p1x) en (y-p2y) = rc1 * (x-p2x)
                # y = rc1 * (x-p1x) + p1y = rc2 * (x-p2x) + p2y
                # rc1 * x - rc2 * x = rc1 * p1x - rc2 * p2x - p1y + p2y
                # x = (rc1 * p1x - rc2 * p2x - p1y + p2y) / (rc1 - rc2)
                slope_self = self.slope()
                slope_other = other.slope()
                x = (slope_self * self.p1.x -
                     slope_other * other.p1.x -
                     self.p1.y +
                     other.p1.y) / (slope_self - slope_other)
                y = slope_self * (x - self.p1.x) + self.p1.y
                intersection_point = Vector2(x, y)

        if self.point_is_in_rect(intersection_point) and \
                other.point_is_in_rect(intersection_point):
            return intersection_point
        else:
            return None

    def rect(self):
        left = min(self.p1.x, self.p2.x)
        right = max(self.p1.x, self.p2.x)
        top = min(self.p1.y, self.p2.y)
        bottom = max(self.p1.y, self.p2.y)
        return Rect(left, top, right - left, bottom - top)

    def point_is_in_rect(self, p):
        d = self.rect()
        return d.left <= p.x <= d.right and d.top <= p.y <= d.bottom

    def is_horizontal(self):
        return self.p1.y == self.p2.y

    def is_vertical(self):
        return self.p1.x == self.p2.x

    def length(self):
        return self.vector_from_p1.length()

    def slope(self):
        if self.p1.x != self.p2.x:
            return (self.p1.y - self.p2.y) / (self.p1.x - self.p2.x)
        else:
            return math.inf

    def inverse_slope(self):
        if self.p1.y != self.p2.y:
            return (self.p1.x - self.p2.x) / (self.p1.y - self.p2.y)
        else:
            return math.inf

    def draw(self, screen, color=(0,0,0), thickness=1):
        pygame.draw.line(screen, color, self.p1, self.p2, thickness)



class Circle:

    def __init__(self, center, radius):
        self.center = Vector2(center)
        self.radius = radius

    def __repr__(self):
        return 'Circle((%g, %g), %g)' % (self.center.x, self.center.y, self.radius)

    def __str__(self):
        return 'Circle with center (%g, %g) and radius %g' % (self.center.x, self.center.y, self.radius)

    def move(self, v):
        self.center += v

    def draw(self, screen, color=(200,0,0), thickness=1):
        pygame.draw.circle(screen, color, (int(self.center.x), int(self.center.y)), self.radius, thickness)

    def bounce(self, l_solid, l_move):
        inter = l_solid.intersection(l_move)
        if inter:
            #Circle(inter, radius).draw(screen, color)
            if l_solid.is_vertical():
                d = Vector2(self.radius, self.radius * l_move.slope())
                if l_move.slope() >= 0 and d.y >= 0 or l_move.slope() <= 0 and d.y <= 0:
                    p_bounce = inter + d
                else:
                    p_bounce = inter - d
                Circle(p_bounce, radius).draw(screen, color)
                v = l_move.p2 - p_bounce
                v.x = -v.x
                end = p_bounce + v
                pygame.draw.line(screen, (0, 0, 0), p_bounce, end)
                Circle(end, radius).draw(screen, color)
                return l_move.p1, p_bounce, end
            if l_solid.is_horizontal():
                d = Vector2(self.radius * l_move.inverse_slope(), self.radius)
                if l_move.inverse_slope() >= 0 and d.x >= 0 or l_move.inverse_slope() <= 0 and d.x <= 0:
                    p_bounce = inter + d
                else:
                    p_bounce = inter - d
                Circle(p_bounce, radius).draw(screen, color)
                v = l_move.p2 - p_bounce
                v.y = -v.y
                end = p_bounce + v
                pygame.draw.line(screen, (0, 0, 0), p_bounce, end)
                Circle(end, radius).draw(screen, color)
                return l_move.p1, p_bounce, end

    def repeated_bounce(self, lines, l_move):
        v = l_move
        while True:
            no_more_intersections = True
            for l in set(lines):
                inter = l.intersection(v)
                if inter:
                    no_more_intersections = False
                    p1, p2, p3 = self.bounce(l, v)
                    v = LineSegment(p2, p3)
            if no_more_intersections:
                break

# =================================================

if __name__ == '__main__':

    l1 = LineSegment((50, 40), (180, 40))
    l2 = LineSegment((50, 40), (50, 180))
    # l3 = LineSegment((100, 170), (100, 20))
    # l3 = LineSegment((60, 170), (170, 10))
    # l3 = LineSegment((170, 170), (100, 10))

    # l3 = LineSegment((160, 100), (10, 100))
    # l3 = LineSegment((180, 170), (10, 60))
    l3 = LineSegment((180, 60), (10, 100))


    print(l3.intersection(l1))
    print(l3.intersection(l2))

    pygame.init()

    screen = pygame.display.set_mode((200, 200))
    screen.fill((255, 255, 255))
    pygame.display.set_caption("Test Collisions")

    l1.draw(screen)
    l2.draw(screen)
    l3.draw(screen)

    inter1 = l1.intersection(l2)
    inter2 = l3.intersection(l1)
    inter3 = l3.intersection(l2)

    radius = 13
    color = (200, 0, 0)
    # if inter1:
    #     Circle(inter1, radius).draw(screen, color)
    # if inter2:
    #     Circle(inter2, radius).draw(screen, color)
    # if inter3:
    #     Circle(inter3, radius).draw(screen, color)

    c = Circle(l3.p1, radius)
    c.draw(screen, color)
    c.move(l3.vector_from_p1)
    c.draw(screen, color)

    # p1, p2, p3 = c.bounce(l2 , l3)
    # p2, p3, p4 = c.bounce(l1, LineSegment(p2, p3))
    #
    # pygame.draw.line(screen, (0,0,200), p1, p2, 3)
    # pygame.draw.line(screen, (0,0,200), p2, p3, 3)
    # pygame.draw.line(screen, (0,0,200), p3, p4, 3)

    c.repeated_bounce([l2,l1], l3)

    # c = Circle(inter3, radius)
    # d = Vector2(c.radius, c.radius * l3.slope())
    # c.move(d)
    # c.draw(screen, color)
    # p_bounce = c.center
    # v = l3.p2 - p_bounce
    # v.x = -v.x
    # v = p_bounce + v
    # pygame.draw.line(screen, (0,0,0), p_bounce, v)
    # c = Circle(v, radius).draw(screen, color)

    pygame.display.flip()

    while True:

        # Handle events
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                sys.exit()
