import pygame

import config
import controller as control
import main

# Created by Emanuel Ramirez Alsina on 03/23/2020

'''Starter code for the player.'''

# TODO: finish this.
class Player:

    def __init__(self):
        self.player_x = int(config.SCREEN_WIDTH / 2) - 30
        self.player_y = int(600 / 1.25)
        self.delta_player_x = 0
        self.delta_player_y = 0

    def get_player_x(self):
        return self.player_x

    def get_player_y(self):
        return self.player_y

    def get_playersprite(self):
        return self.playerSprite

    def update_player(self, x, y):
        self.player_x = x
        self.player_y = y


# TODO: Change the player to it's own class.
# Player spawn
# Xill update the movement of the player

#print('Player x: {} || Width: {}'.format(player_x, SCREEN_WIDTH))
#print('Player y: {} || Height: {}'.format(player_y, SCREEN_HEIGHT))
# Player movement
#if event.type == pygame.KEYDOWN:
#    if event.key == config.get('UP'):
#        self.delta_player_y = -3
#    elif event.key == config.get('DOWN'):
#        self.delta_player_y = 3
#    elif event.key == config.get('LEFT'):
#        self.delta_player_x = -3
#    elif event.key == config.get('RIGHT'):
#        self.delta_player_x = 3
#if event.type == pygame.KEYUP:
#    if event.key == config.get('UP') or event.key == config.get('DOWN'):
#        self.delta_player_y = 0
#    elif event.key == config.get('LEFT') or event.key == config.get('RIGHT'):
#        self.delta_player_x = 0
#
## Keep the player in the scene. 
## Account for the size of the player image.
#
## Update player positions.
#self.player_x += self.delta_player_x
#self.player_y += self.delta_player_y
#self.update_player(self.player_x, self.player_y)
