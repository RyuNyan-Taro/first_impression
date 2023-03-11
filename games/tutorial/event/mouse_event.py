import pygame
from pygame.locals import *
import sys

SCREEN_SIZE = (640, 480)


def main():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption(u'mouse_event')

    # image
    backimg = pygame.image.load('../image/moriyama.jpg').convert()
    pythonimg = pygame.image.load('../image/python.png').convert_alpha()

    cur_pos = (0, 0)
    pythons_pos = []

    while True:
        screen.blit(backimg, (0, 0))

        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos
                x -= pythonimg.get_width() / 2
                y -= pythonimg.get_width() / 2
                pythons_pos.append((x, y))
            if event.type == MOUSEMOTION:
                x, y = event.pos
                x -= pythonimg.get_width() / 2
                y -= pythonimg.get_width() / 2
                cur_pos = (x, y)

            screen.blit(pythonimg, cur_pos)
            for i, j in pythons_pos:
                screen.blit(pythonimg, (i, j))

            pygame.display.update()


if __name__ == '__main__':
    main()
