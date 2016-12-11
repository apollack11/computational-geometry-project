# computational-geometry-project

## Goal
The goal of this program is to take an input file (similar to form in project 1) that had the points of a polygon. Some examples can be seen in the Input txt files.

## Algorithm.py
This file organizes the turn-by-turn based nature of the game. It keeps track of the state of the board which allows it to call other files for directions on where to put the pursuers based on the strategy outlined in the paper.


## Execution
When the programing is running, you can use the following command in terminal:
```
./Algorithm.py PaperInput.txt
```

## k_block_partition.py  
Takes in a set of points from Algorithm.py which represent a polygonal region. Outputs a block graph of the k-block partition of the region. We were unable to get this part of the program completely working due to difficulties with triangulation and conversion of the output into a block graph.
