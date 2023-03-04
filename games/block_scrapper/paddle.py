import pygame
from pygame.locals import *
import math
import sys
import pygame.mixer
SCREEN = Rect(0, 0, 400, 400)


class Paddle(pygame.sprite.Sprite):
    def __int__(self, filename):
        # todo: fix RecursionError of which below line is case
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = pygame.image.load(filename).convert()
        self.rect = self.image.get_rect()
        self.rect.bottom = SCREEN.bottom - 20

    def update(self):
        self.rect.centerx = pygame.mouse.get_pos()[0]
        self.rect.clamp_ip(SCREEN)


def main():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN.size)
    group = pygame.sprite.RenderUpdates()
    Paddle.containers = group
    print('a')
    paddle = Paddle("paddle.png")
    clock = pygame.time.Clock()

    while (1):
        clock.tick(30)
        screen.fill((0, 20, 0))
        group.update()
        group.draw(screen)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()


if __name__ == "__main__":
    main()

