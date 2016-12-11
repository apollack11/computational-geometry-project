#!/usr/bin/env python


import sys
from GZ_geometry import Polygon as Polygon
from GZ_geometry import Line2D as Line

MAX_MOVE = 10

# Enum like structures
class GameState:
    P_TURN, E_TURN, GAME_OVER = range(3)

class Game:
    """ Controls the state of the BattleGround through turn based interaction """
    def __init__(self):
        self.bg = BattleGround()
        self.view = View()
        self.state == GameState.E_TURN
    
    def Start():
        while not self.state == GameState.GAME_OVER:
            self.UpdateView()
            # evader's turn
            if self.state == GameState.E_TURN:
                self.state = GameState.P_TURN
            # pursuers' turn
            if self.state == GameState.P_TURN:
                self.state = GameState.E_TURN

    def UpdateView(self):
        self.view.PrintBoard(self.bg)

class BattleGround:
    """ Represents the state of the room in terms of the algorithm """
    def __init__(self, polygon):
        self.speed = MAX_MOVE
        self.P = polygon
        self.pursuers = []
        self.evader = []
        
class View:
    """ The view of the board """
    @staticmethod
    def PrintBoard(board):
        print board


######################################### Testing #########################################
# TODO-optional: use regex's here to figure out form of each line (esp color vs pt)
def parse_polygons(lines):
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
            i += 1
            poly = Polygon(ps)
    return ps

def main(argv):
    game = Game()
    game.Start()

if __name__ == '__main__':
    main(sys.argv[1:])

