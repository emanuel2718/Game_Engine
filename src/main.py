import pygame

import config
import controller as control
import player


# Created by Emanuel Ramirez Alsina on 03/22/2020

class Game:
    '''Main game driver.'''

    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Game Engine')

        self.screen = pygame.display.set_mode(config.SCREEN_SIZE)

        # Background
        self.background = pygame.image.load('../assets/images/background.jpg')
        self.playerSprite = pygame.image\
            .load('../assets/images/spaceship_normal.png')
        self.player = player.Player()

        #self.background_height = background.get_rect().height



    # Main loop of the game.
    def main(self):
        self.running = True
        while self.running:
            #self.screen.fill(config.BLUE)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                #if event.type == pygame.KEYDOWN:
                #    if event.key in control.player_keys:
                #        self.player.move_player(event.key)
                #if event.type == pygame.KEYUP:
                #    if event.key in control.player_keys:
                #        self.player.move_player(event.key)


                pygame.display.update()
            self.screen.blit(self.background, (0, 0))
            self.screen.blit(self.playerSprite,
                             (self.player.get_player_x(),
                              self.player.get_player_y()))
