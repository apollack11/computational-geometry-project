#!/usr/bin/env python
import random
import math
from k_block_partition import points


def getDistance():
    # assigning coordinates of pursuers and evader
    # will need to compare points to positions of pursuers and evader
    ex = random.randint(0, 26)
    ey = random.randint(-2, 13)
    p_x = random.randint(0, 26)
    p_y = random.randint(-2, 13)

    px = []
    py = []

    for p_x in range(1, n):
        for p_y in range(1, n):
            px = px.append(p_x)
            py = py.append(p_y)

    #calculating the euclidean distance of each pursuer to evader
    eucdistl = []

    for i in range(1, n):
        i = i - 1
        dx = ex - px(i)
        dy = ey - py(i)
        eucdist = math.sqrt(dx*dx+dy*dy)
        eucdistl = eucdistl.append(eucdist)


def detCapture(eucdistl):

    #checking if all pursuers are at distance of 1 to the evader
    if all(x <= 1 for x in eucdistl):
            print("The evader has been captured")
    #determine how pursuer and evader will move
    #else
       #if
       #else


if __name__ == '__getDistance__':
    getDistance()
