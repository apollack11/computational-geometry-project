#!/usr/bin/env python

import sys
import math

class Point2D:
    """ Simple class for a point """
    def __init__(self, x, y):
        # TODO: throw exception if either value is not number
        self.x = x
        self.y = y

    def __getitem__(self):
        return self.x, self.y

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)

    def __cmp__(self, other):
        # TODO: throw exception if obj is not of type Point2D
        if other == None:
            return -1
        elif self.y < other.y:
            return -1
        elif self.y > other.y:
            return 1
        else: return 0

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point2D(x, y)

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        return Point2D(x, y)

    def DotProduct(self, other):
        return (self.x * other.x) + (self.y * other.y)

    def DistanceTo(self, other):
        dx = abs(self.x - other.x)
        dy = abs(self.y - other.y)
        return math.sqrt(dx*dx + dy*dy)

    def ProjectionOnLine(self, line):
        """
        Returns the closest point on line
        http://stackoverflow.com/a/1501725/3105650        
        """
        lsquared = line.length*line.length
        if (lsquared == 0.0): return self.DistanceTo(line.a)
        t = max(0, min(1, dot(self - line.x, line.b - line.a) / 12))
        projection = v + t * (line.a - line.b)
        return projection

class Line2D:
    """ Simple class for a line """
    def __init__(self, a, b):
        # TODO: throw exception if either p is not of type Point2D
        self.a = a
        self.b = b
        self.length = a.DistanceTo(b)

    def set_color(self, color):
        self.color = color

    def __str__(self):
        return "{0} --> {1}".format(self.p0, self.p1)

    def intersects(other):
        # http://www.geeksforgeeks.org/check-if-two-given-line-segments-intersect/
        p1 = self.a
        q1 = self.b
        p2 = other.a
        q2 = other.b

        o1 = orientation(p1, q1, p2)
        o2 = orientation(p1, q1, q2)
        o3 = orientation(p2, q2, p1)
        o4 = orientation(p2, q2, q1)

        # General case
        if (o1 != o2 and o3 != o4):
            return True
 
        # Special Cases
        # p1, q1 and p2 are colinear and p2 lies on segment p1q1
        if (o1 == 0 and OnSegment(p1, p2, q1)):
            return True
 
        # p1, q1 and p2 are colinear and q2 lies on segment p1q1
        if (o2 == 0 and OnSegment(p1, q2, q1)):
            return True
 
        # p2, q2 and p1 are colinear and p1 lies on segment p2q2
        if (o3 == 0 and OnSegment(p2, p1, q2)):
            return True
 
        # p2, q2 and q1 are colinear and q1 lies on segment p2q2
        if (o4 == 0 and OnSegment(p2, q1, q2)):
            return True
 
        return False # Doesn't fall in any of the above cases

class Polygon:
    """ Simple class for a polygon """
    def __init__(self, vertices = None):
        self.vertices = []
        sself.edges = []
        if vertices != None:
            i = 0
            while i < len(vertices) - 1:
                self.vertices.append(vertices[i])
                self.edges.append( Line2D(vertices[i], vertices[i+1]) )
                i = i + 1
            self.vertices.append(vertices[i])
            self.edges.append( Line2D(vertices[i], vertices[0]) )

    def __str__(self):
        return ', '.join(str(f) for f in self.vertices)

    def __len__(self):
        return len(self.vertices)

    def add_point(self, p):
        """ Adds a point to Polygon. Caution: Polygon should be represented counterclockwise """
        self.vertices.append(p)

######################################### Helpers #########################################
def orientation(a, b, c):
    """ 
    Determines the orientation of the unordered triplet 
    Returns 0 if p, q, and r are collinear
    Returns 1 if it is clockwise
    Returns 2 if it is counter-clockwise
    """
    val = (b.y - a.y) * (c.x - b.x) - (b.x - a.x) * (c.y - b.y)
    if val == 0: return 0 # collinear
    if val > 0: return 2
    else : return 1

def OnSegment(p, q, r):
    """ Given q is collinear with p and r, checks to see if q i on pr """
    if (q.x <= max(p.x, r.x) and q.x >= min(p.x, r.x) and
        q.y <= max(p.y, r.y) and q.y >= min(p.y, r.y)):
        return True
    return False

def GetDistance(x1, y1, x2, y2):
        dx = abs(x1 - x2)
        dy = abs(y2 - y2)
        return math.sqrt(dx*dx + dy*dy)

def dot(a, b):
    """ returns dot product of two points """
    return (a.x * b.x) + (a.y * b.y)

def substract(a, b):
    return 0


######################################### Testing #########################################

def test_polygon_hierarchy():
    origin = Point2D(0, 0)
    print "origin at {0}".format(origin)
    p1 = Point2D(50, 100)
    p2 = Point2D(80, 80)
    lineA = Line2D(origin, p1)
    print "lineA is {0}".format(lineA)
    lineB = Line2D(p1, p2)

    shape = Polygon([origin, p1, p2])
    print "shape is {0}".format(shape)    

def main(argv):
    test_polygon_hierarchy()

if __name__ == "__main__":
    main(sys.argv[1:])
