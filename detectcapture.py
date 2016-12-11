#!/usr/bin/env python
import random
import math
from k_block_partition import points
import GZ_geometry
import Algorithm

def getDistance(e, ps):
    # assigning coordinates of pursuers and evader
    # will need to compare points to positions of pursuers and evader
    ex, ey =  e.x, e.y
    p_x = random.randint(0, 26)
    p_y = random.randint(-2, 13)

    px = []
    py = []

    for p in ps:
        px = px.append(p.x)
        py = py.append(p.y)

    #calculating the euclidean distance of each pursuer to evader
    eucdistl = []

    for i in range(1, n):
        i = i - 1
        dx = ex - px(i)
        dy = ey - py(i)
        eucdist = math.sqrt(dx*dx+dy*dy)
        eucdistl = eucdistl.append(eucdist)
    
    return eucdistl


def detCapture(eucdistl):

    #checking if all pursuers are at distance of 1 to the evader
    if all(x <= 1 for x in eucdistl):
            print("The evader has been captured")
            return True
    #determine how pursuer and evader will move
    #else
       #if
       #else


def CanCapture(evader, pursuers):
    e = evader
    ps = pursuers
    eucdistl = getDistance(e, ps):
    return detCapture(eucdistl)
    

    

if __name__ == '__getDistance__':
    getDistance()
