import pygame
from pygame.locals import *
import sys

SCREEN_SIZE = (640, 480)


def main():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption('Hello, World')
    sysfont = pygame.font.SysFont(None, 80)
    hello1 = sysfont.render('Hello, World!!', False, (0, 0, 0))
    hello2 = sysfont.render('Hello, World!!', True, (0, 0, 0))
    hello3 = sysfont.render('Hello, World!!', False, (255, 0, 0), (255, 255, 0))

    while True:
        screen.fill((0, 0, 255))
        screen.blit(hello1, (20, 50))
        screen.blit(hello2, (20, 150))
        screen.blit(hello3, (20, 250))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()


if __name__ == '__main__':
    main()