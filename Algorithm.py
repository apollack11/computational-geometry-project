#!/usr/bin/env python


import sys
from GZ_geometry import Polygon as Polygon
from GZ_geometry import Line2D as Line
from GZ_geometry import Point2D as Point2D

SPEED = 1 # can make this a choice later where var is initialized at max_speed

# Enum like structures
class GameState:
    P_TURN, E_TURN, GAME_OVER = range(3)
class AlgoState:
    K_PART = 0     # during construction of k-blocks
    SWEEP = 1      # sweeping block graph until the evader is trapped in an extended block B+
                   # any move across the cut for B+e is a k-critical move
    CAPTURE = 2   # find and capture evader in B+

class Game:
    """
    Controls the state of the BattleGround through turn based interaction

    block_graph is a binary tree of the adjacency graph of the k-partition
    nodes are triangles, and connections are the cut edges
    """
    def __init__(self, polygon):
        self.bg = BattleGround(polygon) # model
        self.view = View()               # view
        self.state = GameState.E_TURN  # state of game
        self.block_graph = []

    def Start(self):
        while not self.state == GameState.GAME_OVER:
            self.UpdateView()
            raw_input("Are you ready for the next turn?")
            if self.state == GameState.E_TURN: # Starts with evader
                self.bg.MoveEvader()
                self.state = GameState.P_TURN
                continue
            if self.state == GameState.P_TURN:
                if AlgoState.K_PART:
                    # self.block_graph = k_partition # TODO must: get this to work with k block code (need cut edges)
                    self.block_graph = 0
                    self.bg.Be = LocalizeEvader() # give Be to pursuers
                    # TODO: determine where to place pursuers on cut edges
                    self.bg.MovePursuers()
                if AlgoState.SWEEP:
                    """
                    for p in self.bg.pursuers:
                        # is e in p line-of-sight?
                        los = True
                        line = Line2D(p.pose, self.bg.evader.pose)
                        for edge in self.bg.polygon.edges:
                            if line.intersects(edge):
                                los = False
                    """
                    # if evader is trapped in B+
                    # TODO
                if AlgoState.CAPTURE:
                    # evader is confined to an extended k-block
                    # need O(k) pursuers

                    # phase 1: 
                    # triangulate kP (polygon of k-block)
                    boundaries = triangulate(kP)
                    # assign one pursuer to each edge of triangulation at projection
                    self.bg.ClearPursuers()
                    for line in boundaries:
                        p = self.bg.e.pose.ProjectionOnLine(line)
                        self.bg.AddPursuer(p.x, p.y)

                    # phase 2:
                    # move triangles inward


                    # GameState.GAME_OVER
                    pass
                self.state = GameState.E_TURN
                continue

    def UpdateView(self):
        self.view.PrintBoard(self.bg)

    def IsCriticalMove(self):
        pass

    def LocalizeEvader(self):
        pass


class BattleGround:
    """ Represents the state of the room in terms of the algorithm """
    def __init__(self, polygon):
        self.speed = SPEED
        self.polygon = polygon #
        self.pursuers = []     # list of Pursuers obj
        self.evader = []       # a single Evader obj
        self.Be = 0            # partition containing evader - TODO maybe: move this to pursuers
        # right now we initialize evader to point that works with Input1.txt
        self.evader = Evader(15, 0)
        

    def AddPursuer(self, x, y):
        self.pursuers.append(Pursuer(x, y))

    def ClearPursuers(self):
        self.pursuers = []
        
    def MovePursuers(self, destinations):
        for p in self.pursuers:
            p.Move(x, y)

    def MoveEvader(self):
        oldX = newX = self.evader.x
        oldY = newY = self.evader.y
        collision = True
        while collision:
            dir = random.randint(0, 4) # random north, south, east west
            if dir == 0: newY = oldY + 1
            if dir == 1: newY = oldY - 1
            if dir == 2: newX = oldX + 1
            if dir == 3: newX = oldX - 1
            eprime = Point2D(newX, newY)
            collision = False
            for edge in self.polygon.edges:
                # check to see if new move would collide with polygon edge
                if eprime.DistanceTo(edge.a) + eprime.DistanceTo(edge.b) == edge.length:
                    collision = True
        self.evader.Move(newX, newY)
        # TODO: if evader moves across cut edge, update Be (Lemma 2)

class View:
    """ The view of the board """
    @staticmethod
    def PrintBoard(board):
        print "Evader at ({0}, {1})".format(board.evader.x, board.evader.y)
        print "Pursuers at",
        for p in board.pursuers:
            print "({0}, {1})".format(p.x, p.y),
        print "\n"

class Evader:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.pose = Point2D(x, y)
    def Move(self, x, y):
        self.x = x
        self.y = y
        self.pose = Point2D(x, y)
        
class Pursuer:
    def __init__(self, x, y, polygon):
        self.x = x
        self.y = y
        self.pose = Point2D(x, y)
    def Move(self, x, y):
        self.x = x
        self.y = y
        self.pose = Point2D(x, y)
        
######################################### Testing #########################################
def read_file(filename):
    try:
        fo = open(str(filename), 'r')
        data = fo.readlines()
    # TODO: add custom exceptions for invalid file format (ex: first line is not T or P)
    except IOError as e:
        print "I/O error({0}): {1}".format(e.errno, e.strerror)    
    # strip whitespace from right side (newlines and carriage returns)
    for i in range(len(data)):
        data[i] = data[i].rstrip()
    return data

# TODO-optional: use regex's here to figure out form of each line (esp color vs pt)
def parse_polygon(lines):
    """
    messy way to read in file for homework
    TODO: clean this up, maybe use regex and more eval methods
    """
    ps = []
    if lines[0] == 'P':
        i = 1
        while i < len(lines):
            if lines[i][0] == '(':
                s = lines[i].strip()
                s = s.replace('(', '').replace(')', '')
                pt = s.split(',')
                p = Point2D( int(pt[0]) , int(pt[1]) )
                ps.append(p)
            i = i + 1
            poly = Polygon(ps)
    return poly

def main(argv):
    P = parse_polygon(read_file(argv[0]))
    game = Game(P)
    game.Start()

if __name__ == '__main__':
    main(sys.argv[1:])
