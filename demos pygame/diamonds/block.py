import os
import pygame

BLOCK_IMAGES = 'blocks.png'     # 792 x 480
IMAGES_DIRECTORY = 'images'

class Block(pygame.sprite.Sprite):

    WIDTH = 66
    HEIGHT = 40

    BLOCK_DEFS = {'l': {'type': 'block', 'crop_offset': 0, 'color': 'lightblue'},
                  'b': {'type': 'block', 'crop_offset': 1, 'color': 'blue'},
                  'r': {'type': 'block', 'crop_offset': 2, 'color': 'red'},
                  'g': {'type': 'block', 'crop_offset': 3, 'color': 'green'},
                  'w': {'type': 'block', 'crop_offset': 4, 'color': 'brown'},
                  'p': {'type': 'block', 'crop_offset': 5, 'color': 'purple'},
                  'B': {'type': 'brush', 'crop_offset': 10, 'color': 'blue'},
                  'R': {'type': 'brush', 'crop_offset': 11, 'color': 'red'},
                  'G': {'type': 'brush', 'crop_offset': 12, 'color': 'green'},
                  'W': {'type': 'brush', 'crop_offset': 13, 'color': 'brown'},
                  'P': {'type': 'brush', 'crop_offset': 14, 'color': 'purple'},
                  'O': {'type': 'brush', 'crop_offset': 15, 'color': 'orange'},
                  'd': {'type': 'diamond', 'crop_offset': 19, 'color': None},
                  'k': {'type': 'key', 'crop_offset': 20, 'color': 'orange'},
                  'L': {'type': 'lock', 'crop_offset': 21, 'color': 'orange'},
                  'S': {'type': 'solid', 'crop_offset': 22, 'color': None},
                  's': {'type': 'skull', 'crop_offset': 23, 'color': None},
                  'v': {'type': 'reverse', 'crop_offset': 24, 'color': None},
                  }

    def __init__(self, colnr, rownr, code='S'):
        pygame.sprite.Sprite.__init__(self)

        try:
            self.image = pygame.image.load(os.path.join(IMAGES_DIRECTORY, BLOCK_IMAGES))
        except:
            print('Cannot load block image')

        block_def = Block.BLOCK_DEFS.get(code)
        if block_def:
            self.type = block_def['type']
            self.crop_offset = block_def['crop_offset']
            self.color = block_def['color']

        self.rownr = rownr
        self.colnr = colnr

        self.rect = self.image.get_rect()

        size = [Block.WIDTH, Block.HEIGHT]

        self.rect.x = colnr * Block.WIDTH
        self.rect.y = rownr * Block.HEIGHT
        self.rect.w = Block.WIDTH
        self.rect.h = Block.HEIGHT

    def draw(self, surface):
        surface.blit(self.image, self.rect, (0, self.crop_offset * Block.HEIGHT, Block.WIDTH, Block.HEIGHT))

    def is_on_same_row(self, other):
        return self.rownr == other.rownr

    def is_on_same_column(self, other):
        return self.colnr == other.colnr

    def has_common_horizontal_side(self, other):
        return self.colnr == other.colnr and abs(self.rownr - other.rownr) == 1

    def has_common_vertical_side(self, other):
        return self.rownr == other.rownr and abs(self.colnr - other.colnr) == 1

    def has_common_side(self, other):
        return self.has_common_horizontal_side(other) or \
               self.has_common_vertical_side(other)

