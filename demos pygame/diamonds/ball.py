import os
import pygame

BALL_IMAGES = 'balls.png'     # 792 x 480
IMAGES_DIRECTORY = 'images'

class Ball(pygame.sprite.Sprite):

    WIDTH = 20
    HEIGHT = 20
    STEP_SIZE = 5

    crop_offsets = {'lightblue': 0,
                    'blue': 1,
                    'red': 2,
                    'green': 3,
                    'brown': 4,
                    'purple': 5,
                    'orange': 6,
                    'yellow': 7,
                    'black': 8,
                    'white': 9
                    }

    def __init__(self, x=750, y=460):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(os.path.join(IMAGES_DIRECTORY, BALL_IMAGES)).convert_alpha()

        self.rect = self.image.get_rect()
        size = [Ball.WIDTH, Ball.HEIGHT]

        self.rect.x = x
        self.rect.y = y
        self.rect.width = Ball.WIDTH
        self.rect.height = Ball.HEIGHT

        self.color = 'lightblue'
        self.crop_offset = Ball.crop_offsets[self.color]

        self.upwards = True

    def move_left(self, dx):
        self.rect.x -= dx

    def move_right(self, dx):
        self.rect.x += dx

    def move_up(self, dy):
        self.rect.y -= dy

    def move_down(self, dy):
        self.rect.y += dy

    def move(self, sideways = None):
        last_rect = self.rect.copy()

        if self.upwards:
            self.move_up(Ball.STEP_SIZE)
        else:
            self.move_down(Ball.STEP_SIZE)

        if sideways == 'left':
            self.move_left(Ball.STEP_SIZE)
        elif sideways == 'right':
            self.move_right(Ball.STEP_SIZE)

        new_rect = self.rect.copy()

        return last_rect, new_rect

    def draw(self, target_surface):
        target_surface.blit(self.image, self.rect, (0, self.crop_offset * Ball.HEIGHT, Ball.WIDTH, Ball.HEIGHT))

    def set_color(self, color):
        self.color = color
        self.crop_offset = Ball.crop_offsets[color]
