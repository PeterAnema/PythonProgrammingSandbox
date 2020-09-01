import os
import pygame

BACKGROUND_IMAGE = 'background.png'     # 792 x 480
IMAGES_DIRECTORY = 'images'

class Background:

    def __init__(self, rect):
        try:
            self.surface = pygame.image.load(os.path.join(IMAGES_DIRECTORY, BACKGROUND_IMAGE))
        except:
            print('Cannot load background image')

    def draw(self, target_surface, area_to_update = None):
        if area_to_update is None:
            target_surface.blit(self.surface, (0, 0))
        else:
            target_surface.blit(self.surface, area_to_update, area_to_update)
