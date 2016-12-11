#!/usr/bin/env python

import sys

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

class Line2D:
    """ Simple class for a line """
    def __init__(self, p0, p1):
        # TODO: throw exception if either p is not of type Point2D
        self.p0 = p0
        self.p1 = p1

    def set_color(self, color):
        self.color = color

    def __str__(self):
        return "{0} --> {1}".format(self.p0, self.p1)

class Polygon:
    """ Simple class for a polygon """
    def __init__(self, vertices = None):
        self.vertices = []
        self.edges = []
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
