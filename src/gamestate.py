import pygame

class State(object):
    '''Parent class of all game states'''

    def __init__(self, game):
        #TODO: Need to rethink this maybe?
        # The idea here is to eventually be able to control different states
        # For now it will be Main Menu -> Game -> Pause
        self.game = game
        self.done = False
        self.prev_state = None
        self.next_state = None

class Game_State(State):
    def __init__(self, game):
        State.__init__(self, game)
        # next state? Could be Pause or Menu

class Pause_State(State):
    def __init__(self, game):
        State.__init__(self, game)
        # next state? Could be Game or Menu

class Menu_State(State):
    def __init__(self, game):
        State.__init__(self, game)
        self.next_state = 'Game_State'

