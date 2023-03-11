import pygame
from pygame.locals import *
import sys

SCREEN_SIZE = (640, 480)


def main():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption(u'mouse_event2')

    backimg = pygame.image.load('../image/moriyama.jpg').convert()
    pythonimg = pygame.image.load('../image/python.png').convert_alpha()

    cur_pos = (0, 0)
    pythons_pos = list()

    while True:
        screen.blit(backimg, (0, 0))

        mouse_pressed = pygame.mouse.get_pressed()

        if mouse_pressed[0]:
            x, y = pygame.mouse.get_pos()
            x, y = center_xy(pythonimg, x, y)
            pythons_pos.append((x, y))

        x, y = pygame.mouse.get_pos()
        x, y = center_xy(pythonimg, x, y)
        cur_pos = (x, y)

        screen.blit(pythonimg, cur_pos)
        for i, j in pythons_pos:
            screen.blit(pythonimg, (i, j))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()


def center_xy(pythonimg, x, y):
    x -= pythonimg.get_width() / 2
    y -= pythonimg.get_width() / 2

    return x, y


if __name__ == '__main__':
    main()
