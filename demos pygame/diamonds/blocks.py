import os
import pygame

from block import Block

SETTINGS_DIRECTORY = 'settings'
SETTINGS_FILE = 'Diamonds.txt'

class Blocks:

    def __init__(self, levelset_name = 'Simpleton', background = None):
        self.background = background
        self.surface = background.surface.copy()
        self.group = Blocks.get_levelset(levelset_name = levelset_name)
        self.type_counts = self.type_counter()
        self.draw_blocks()

    def type_counter(self):
        return {t: len(set(filter(lambda b: b.type == t, self.group))) for t in {b.type for b in self.group}}

    def remove(self, block):
        self.group.remove(block)
        self.type_counts[block.type] -= 1
        self.surface.blit(self.background.surface, block.rect, block.rect)

    def draw_blocks(self):
        self.surface.blit(self.background.surface, (0, 0))
        for block in self.group:
            block.draw(self.surface)

    def draw(self, target_surface, area_to_update = None):
        if area_to_update is None:
            target_surface.blit(self.surface, (0, 0))
        else:
            target_surface.blit(self.surface, area_to_update, area_to_update)

    def any_blocks(self):
        return self.type_counts['block'] != 0

    def any_diamonds(self):
        return self.type_counts['diamond'] != 0

    @staticmethod
    def read_settings_file(filename = SETTINGS_FILE):

        full_filename = os.path.join(SETTINGS_DIRECTORY, filename)

        levelsets = {}

        try:
            with open(full_filename) as f:
                for line in f:
                    if line.startswith('name='):
                        name = line[5:].strip()
                        levelset = ''
                        for _ in range(12):
                            levelset += f.readline()
                        levelsets[name] = levelset.strip()

        except:
            print('Error reading settings file: %s' % filename)

        return levelsets


    @staticmethod
    def build_levelset(levelset):

        blocks = pygame.sprite.Group()

        for row, line in enumerate(levelset.split()):
            for col, code in enumerate(list(line)):
                if code in Block.BLOCK_DEFS:
                    block = Block(col, row, code)
                    blocks.add(block)

        return blocks

    @staticmethod
    def get_levelset(filename = SETTINGS_FILE, levelset_name = 'Simpleton'):

        levelsets = Blocks.read_settings_file(filename = filename)
        levelset = levelsets[levelset_name]

        return Blocks.build_levelset(levelset)






