import pygame
from pygame.locals import *
import sys


SCREEN_SIZE = (640, 480)


def main():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption(u'draw_figure')

    while True:
        screen.fill((0, 0, 0))

        pygame.draw.rect(screen, (255, 255, 0), Rect(10, 10, 300, 200))
        pygame.
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()


if __name__ == '__main__':
    main()
