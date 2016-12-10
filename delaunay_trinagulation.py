#!/usr/bin/env python
from scipy.spatial import Delaunay
import matplotlib.pyplot as plt
import numpy as np

points = np.array([[0, 0], [0, 1.1], [1, 0], [1, 1]])
# points = np.random.rand(30, 2)

tri = Delaunay(points)

print tri.simplices[:]
print len(tri.simplices)

plt.triplot(points[:,0], points[:,1], tri.simplices.copy())
plt.plot(points[:,0], points[:,1], 'o')
plt.show()
