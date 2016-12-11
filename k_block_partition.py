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

    print path.contains_point((200, 100))
    print path.contains_point((1, 1))

    fig = plt.figure()
    ax = fig.add_subplot(111)
    patch = patches.PathPatch(path, facecolor="white", lw=2)
    ax.add_patch(patch)
    ax.set_xlim(-5,30)
    ax.set_ylim(-5,20)
    tri = Delaunay(points)

    print tri.simplices[1]
    interiorSimplices = []
    for i in range(0,len(tri.simplices)-1):
        triPath = trianglePath(points, tri.simplices[i])
        # testPoint = triangleCenter(TRIANGLE_VERTICES)
        # if path.contains_point(testPoint) and tri_path.contains_point(testPoint):
        #     print "Triangle is within the polygon"
        #     interiorSimplices.append(tri.simplices[i])
        # else:
        #     print "Not in polygon"
    print interiorSimplices[:]

    plt.triplot(points[:,0], points[:,1], tri.simplices.copy())
    plt.plot(points[:,0], points[:,1], 'o')
    plt.show()

def trianglePath(points, pointIndices):
    print points[pointIndices[0]]
    triPoints = [
    [points.item(pointIndices[0],0),points.item(pointIndices[0],1)],
    [points.item(pointIndices[1],0),points.item(pointIndices[1],1)],
    [points.item(pointIndices[2],0),points.item(pointIndices[2],1)],
    [points.item(pointIndices[0],0),points.item(pointIndices[0],1)]
    ]
    print "^^^^^^^^"
    print triPoints
    codes = [Path.MOVETO,
             Path.LINETO,
             Path.LINETO,
             Path.CLOSEPOLY,
             ]
    triPath = Path(triPoints, codes)
    return triPath

def triangleCenter(vertices):
    centerX = (vertices[0][0] + vertices[1][0] + vertices[2][0]) / 3;
    centerY = (vertices[0][1] + vertices[1][1] + vertices[2][1]) / 3;
    return (centerX, centerY)


if __name__ == '__main__':
    main()
