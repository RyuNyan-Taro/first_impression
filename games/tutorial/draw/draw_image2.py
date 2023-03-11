import pygame
from pygame.locals import *
import sys

SCREEN_SIZE = (640, 480)


def main():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption('clear_backscreen')

    planeimg = pygame.image.load('../image/plane.png').convert()

    planeimg2 = pygame.image.load('../image/plane.png').convert()
    colorkey = planeimg2.get_at((0, 0))
    planeimg2.set_colorkey(colorkey, RLEACCEL)

    while True:
        screen.fill((0, 0, 0))
        screen.blit(planeimg, (100, 100))
        screen.blit(planeimg2, (200, 100))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()


if __name__ == '__main__':
    main()
