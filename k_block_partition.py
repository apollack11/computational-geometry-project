#!/usr/bin/env python
from scipy.spatial import Delaunay
import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches
import numpy as np

def main():
    points = np.array([
    [0, 0],
    [11, 0],
    [11, -3],
    [16, -3],
    [16, 4],
    [20, 4],
    [20, 1],
    [17, 1],
    [17, -1],
    [27, -1],
    [27, 14],
    [16, 14],
    [16, 11],
    [23, 11],
    [23, 10],
    [19, 10],
    [19, 9],
    [21, 9],
    [21, 8],
    [13, 8],
    [13, 6],
    [6, 6],
    [6, 8],
    [4, 8],
    [4, 10],
    [2, 10],
    [2, 13],
    [0, 13],
    [0, 0]])

    codes = [Path.MOVETO,
             Path.LINETO,
             Path.LINETO,
             Path.LINETO,
             Path.LINETO,
             Path.LINETO,
             Path.LINETO,
             Path.LINETO,
             Path.LINETO,
             Path.LINETO,
             Path.LINETO,
             Path.LINETO,
             Path.LINETO,
             Path.LINETO,
             Path.LINETO,
             Path.LINETO,
             Path.LINETO,
             Path.LINETO,
             Path.LINETO,
             Path.LINETO,
             Path.LINETO,
             Path.LINETO,
             Path.LINETO,
             Path.LINETO,
             Path.LINETO,
             Path.LINETO,
             Path.LINETO,
             Path.LINETO,
             Path.CLOSEPOLY,
             ]

    path = Path(points, codes)

    fig = plt.figure()
    ax = fig.add_subplot(111)
    patch = patches.PathPatch(path, facecolor="white", lw=2)
    ax.add_patch(patch)
    ax.set_xlim(-5,30)
    ax.set_ylim(-5,20)
    tri = Delaunay(points)

    interiorSimplices = []
    for i in range(0,len(tri.simplices)-1):
        part_of_triangulation = True
        tri_path,tri_points = triangle_path(points, tri.simplices[i])
        test_point = triangle_center(tri_points)
        if path.contains_point(test_point) and tri_path.contains_point(test_point):
            print "Triangle is within the polygon"
            interiorSimplices.append(tri.simplices[i])
        else:
            print "Not in polygon"

    plt.triplot(points[:,0], points[:,1], interiorSimplices)
    plt.plot(points[:,0], points[:,1], 'o')
    plt.show()

def triangle_path(points, pointIndices):
    tri_points = [
    [points.item(pointIndices[0],0),points.item(pointIndices[0],1)],
    [points.item(pointIndices[1],0),points.item(pointIndices[1],1)],
    [points.item(pointIndices[2],0),points.item(pointIndices[2],1)],
    [points.item(pointIndices[0],0),points.item(pointIndices[0],1)]
    ]
    codes = [Path.MOVETO,
             Path.LINETO,
             Path.LINETO,
             Path.CLOSEPOLY,
             ]
    tri_path = Path(tri_points, codes)
    return [tri_path,tri_points]

def triangle_center(vertices):
    centerX = (vertices[0][0] + vertices[1][0] + vertices[2][0]) / 3;
    centerY = (vertices[0][1] + vertices[1][1] + vertices[2][1]) / 3;
    return (centerX, centerY)

def line_intersection(line1, line2):
    print line1
    print line2
    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1]) #Typo was here

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)
    return div != 0

if __name__ == '__main__':
    main()
