import sys
import pygame
from collections import deque

BACKGROUND_COLOR = 150, 200, 150
SEGMENT_COLOR = 200, 0, 0
SEGMENT_SIZE = 16
GROW_COUNTER_THRESHOLD = 10

class Segment(pygame.sprite.Sprite):

    def __init__(self,
                 x = 0,
                 y = 0,
                 color = SEGMENT_COLOR,
                 width = SEGMENT_SIZE,
                 height = SEGMENT_SIZE):

        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        self.rect = self.image.get_rect()

        self.position(x, y)

    def position(self, x = 0, y = 0):
        self.rect.x = x
        self.rect.y = y

    def move(self, dx = 0, dy = 0):
        self.rect.x += dx
        self.rect.y += dy


class Snake:

    def __init__(self, max_length = 10, x = 0, y = 0):
        self.max_length = max_length
        self.body = deque()
        self.sprites = pygame.sprite.Group()
        self.head = Segment(x = x, y = y)

    def add(self, segment):
        self.body.append(self.head)
        self.sprites.add(self.head)
        self.head = segment
        if len(self.body) > self.max_length:
            self.sprites.remove(self.body[0])
            del self.body[0]

    def increment_max_length(self, increment = 1):
        self.max_length += increment

    def move(self, dx = 0, dy = 0):
        head = Segment(x = self.head.rect.x + dx,
                       y = self.head.rect.y + dy)
        self.add(head)

    def draw(self, surface):
        surface.blit(self.head.image, self.head.rect)
        self.sprites.draw(surface)


# =============================================================================

pygame.init()

step_size = SEGMENT_SIZE + 1
size = width, height = 30 * step_size, 20 * step_size
movement = step_size, 0

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Demo pygame - snake")

snake = Snake()

grow_counter = 0
started = False
while True:

    # Handle events
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            started = True

            if event.key == pygame.K_RIGHT:
                movement = abs(step_size), 0
            elif event.key == pygame.K_LEFT:
                movement = -abs(step_size), 0
            elif event.key == pygame.K_DOWN:
                movement = 0, abs(step_size)
            elif event.key == pygame.K_UP:
                movement = 0, -abs(step_size)

    if started:
        grow_counter += 1
        if grow_counter >= GROW_COUNTER_THRESHOLD:
            snake.increment_max_length()
            grow_counter = 0

        # Move snake
        snake.move(*movement)

        # Detect collisions
        if snake.head.rect.left < 0 or snake.head.rect.right > width:
            break
        if snake.head.rect.top < 0 or snake.head.rect.bottom > height:
            break

        if pygame.sprite.spritecollideany(snake.head, snake.sprites):
            break

    # Paint screen
    screen.fill(BACKGROUND_COLOR)
    snake.draw(screen)

    pygame.display.flip()

    # Wait
    pygame.time.wait(100)


# Collision occurred
while True:

    # Handle events
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            sys.exit()
