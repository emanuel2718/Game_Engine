import pygame


# Created by Emanuel Ramirez Alsina on 03/23/2020
UP = pygame.K_w
DOWN = pygame.K_s
LEFT = pygame.K_d
RIGHT = pygame.K_a

# Event keys for w, a, s, d, e and f respectevely
player_keys = [119, 97, 100, 115, 101, 102 ]
# Event keys for p and d
game_keys = [112, 102]

class Getkey:
    def __init__(self, game):
        self.game = game
        self.key_map = {
            'UP'    :   pygame.K_w,
            'DOWN'  :   pygame.K_s,
            'LEFT'  :   pygame.K_a,
            'RIGHT' :   pygame.K_d
        }
