import sys
import os
import pygame

from background import *
from blocks import *
from ball import *

WINDOW_SIZE = 12 * Block.WIDTH, 12 * Block.HEIGHT
BACKGROUND_IMAGE = 'background.png'
IMAGES_DIRECTORY = 'images'

class Game:

    def __init__(self, title = 'Diamonds', levelset = 'Simpleton'):
        pygame.init()

        self.screen = pygame.display.set_mode(WINDOW_SIZE, pygame.DOUBLEBUF)
        pygame.display.set_caption('%s - %s' % (title, levelset))

        pygame.event.set_allowed([pygame.QUIT])

        __, __, *window_size = self.screen.get_rect()

        self.background = Background(self.screen.get_rect())
        self.blocks = Blocks(levelset_name = 'Simpleton', background = self.background)
        self.ball = Ball(750, 450)

        self.draw()

    def draw(self, area_to_update = None):
        # self.background.draw(self.screen, area_to_update)
        self.blocks.draw(self.screen, area_to_update)
        self.ball.draw(self.screen)
        pygame.display.update()

    def play(self):

        while True:

            # Handle events
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    sys.exit()

                pygame.event.clear()

            keys_pressed = pygame.key.get_pressed()
            if keys_pressed[pygame.K_RIGHT]:
                sideways = 'right'
            elif keys_pressed[pygame.K_LEFT]:
                sideways = 'left'
            else:
                sideways = None

            last_rect, new_rect = self.ball.move(sideways)

            # Detect collisions with window borders
            if new_rect.top < 0:
                if self.ball.upwards:
                    rect_ball = self.ball.rect
                    d = - rect_ball.top
                    self.ball.move_down(2 * d)
                    self.ball.upwards = not self.ball.upwards

            elif new_rect.bottom > WINDOW_SIZE[1]:
                if not self.ball.upwards:
                    rect_ball = self.ball.rect
                    d = rect_ball.bottom - WINDOW_SIZE[1]
                    self.ball.move_up(2 * d)
                    self.ball.upwards = not self.ball.upwards

            if new_rect.left < 0:
                d = - new_rect.left
                self.ball.move_right(d)
                sideways = None

            elif new_rect.right > WINDOW_SIZE[0]:
                d = new_rect.right - WINDOW_SIZE[0]
                self.ball.move_left(d)
                sideways = None

            # collisions
            collided_blocks = pygame.sprite.spritecollide(self.ball, self.blocks.group, False)

            if collided_blocks:
                if len(collided_blocks) == 1:
                    pass

                elif len(collided_blocks) == 2:
                    b1 = collided_blocks.pop()
                    b2 = collided_blocks.pop()
                    if b1.has_common_side(b2):
                        pass

                elif len(collided_blocks) == 3:
                    pass

                for collided_block in collided_blocks:
                    block_rect = collided_block.rect

                    color_block = collided_block.color
                    color_ball = self.ball.color

                    # Determine exact collision
                    top_left_corner_hit = False
                    top_side_hit = False
                    top_right_corner_hit = False
                    if not self.ball.upwards:
                        slope = (new_rect.x - last_rect.x)/(new_rect.y - last_rect.y)
                        cx = round((new_rect.top - block_rect.bottom) * slope + new_rect.centerx)
                        top_left_corner_hit = block_rect.left - Ball.WIDTH/2 <= cx <= block_rect.left
                        top_side_hit = block_rect.left < cx < block_rect.right
                        top_right_corner_hit = block_rect.right <= cx <= block_rect.right + Ball.WIDTH/2

                    bottom_left_corner_hit = False
                    bottom_side_hit = False
                    bottom_right_corner_hit = False
                    if self.ball.upwards:
                        slope = (new_rect.x - last_rect.x)/(new_rect.y - last_rect.y)
                        cx = round((new_rect.bottom - block_rect.top) * slope + new_rect.centerx)
                        bottom_left_corner_hit = block_rect.left - Ball.WIDTH/2 <= cx <= block_rect.left
                        bottom_side_hit = block_rect.left < cx < block_rect.right
                        bottom_right_corner_hit = block_rect.right <= cx <= block_rect.right + Ball.WIDTH/2

                    left_bottom_corner_hit = False
                    left_side_hit = False
                    left_top_corner_hit = False
                    if sideways == 'right':
                        slope = (new_rect.y - last_rect.y)/(new_rect.x - last_rect.x)
                        cy = round((new_rect.right - block_rect.left) * slope + new_rect.centery)
                        left_top_corner_hit = block_rect.top - Ball.WIDTH/2 <= cy <= block_rect.top
                        left_side_hit = block_rect.top < cy < block_rect.bottom
                        left_bottom_corner_hit = block_rect.bottom <= cy <= block_rect.bottom + Ball.WIDTH/2

                    right_bottom_corner_hit = False
                    right_side_hit = False
                    right_top_corner_hit = False
                    if sideways == 'left':
                        slope = (new_rect.y - last_rect.y)/(new_rect.x - last_rect.x)
                        cy = round((new_rect.left - block_rect.right) * slope + new_rect.centery)
                        right_top_corner_hit = block_rect.top - Ball.WIDTH/2 <= cy <= block_rect.top
                        right_side_hit = block_rect.top < cy < block_rect.bottom
                        right_bottom_corner_hit = block_rect.bottom <= cy <= block_rect.bottom + Ball.WIDTH/2

                    # Fix movement after collision
                    if bottom_side_hit or bottom_left_corner_hit or bottom_right_corner_hit:
                        d = block_rect.bottom - new_rect.top
                        self.ball.move_down(2 * d)
                        self.ball.upwards = not self.ball.upwards

                    elif top_side_hit or top_left_corner_hit or top_right_corner_hit:
                        d = new_rect.bottom - block_rect.top
                        self.ball.move_up(2 * d)
                        self.ball.upwards = not self.ball.upwards

                    elif right_side_hit or right_bottom_corner_hit or right_top_corner_hit:
                        d = block_rect.right - new_rect.left
                        self.ball.move_right(2 * d)

                    elif left_side_hit or left_bottom_corner_hit or left_top_corner_hit:
                        d = new_rect.right - block_rect.left
                        self.ball.move_left(2 * d)

                    # Action after collision
                    if collided_block.type == 'block':
                        if color_block == color_ball:
                            self.blocks.remove(collided_block)

                    elif collided_block.type == 'brush':
                        if color_block:
                            self.ball.set_color(color_block)

                    elif collided_block.type == 'key':
                        if color_block == color_ball:
                            self.blocks.remove(collided_block)

                    elif collided_block.type == 'lock':
                        if color_block == color_ball:
                            if not self.blocks.any_key():
                                self.blocks.remove(collided_block)

                    elif collided_block.type == 'reverse':
                        pass # ?????

                    elif collided_block.type == 'skull':
                        print("You lost!!!!")
                        sys.exit()

                    elif collided_block.type == 'diamond':
                        if not self.blocks.any_blocks():
                            self.blocks.remove(collided_block)

                        if not self.blocks.any_diamonds():
                            print("You won!!!!")
                            sys.exit()

            # Repaint
            margin = 25
            area_to_update = pygame.Rect(self.ball.rect.x - Block.WIDTH  - margin,
                                         self.ball.rect.y - Block.HEIGHT - margin,
                                         3 * Block.WIDTH + 2 * margin,
                                         3 * Block.HEIGHT + 2 * margin)
            self.draw(area_to_update)


# =============================================================================

# Simpleton
# Old Favorite
# Plus Signs
# Ring
# Bank Shot
# Locked Vault
# Quicksand
# Brackets
# Middle Wall
# Zig Zag
# Key Wall
# Super Blocks
# Locksmith
# Jail
# Switch Back
# Blockhead
# Full House
# Flag
# Diamonds R 4-Ever
# Diamonds 3
# Symmetry
# 4 Blocks
# Nerves of Steel
# Insanity
# U-Shape
# Flip Flop
# Spinners
# Maze
# Nooks
# Death Alley

if __name__ == '__main__':
    game = Game(levelset = 'Simpleton').play()
