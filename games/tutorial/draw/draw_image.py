import pygame
from pygame.locals import *
import sys

SCREEN_SIZE = (640, 480)


def main():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption('draw_image')

    backimg = pygame.image.load('../image/moriyama.jpg')
    pythonimg = pygame.image.load('../image/python.png').convert_alpha()

    while True:
        screen.blit(backimg, (0, 0))
        screen.blit(pythonimg, (320, 400))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()


if __name__ == '__main__':
    main()
