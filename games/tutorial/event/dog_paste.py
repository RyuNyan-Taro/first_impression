import pygame
from pygame.locals import *
import sys

SCREEN_SIZE = (640, 480)


def main():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption(u'dogs_stamp')

    # image
    backimg = pygame.image.load('../image/moriyama.jpg').convert()
    sielimg = pygame.image.load('../image/siel.png').convert_alpha()
    nagiimg = pygame.image.load('../image/nagi.png').convert_alpha()

    cur_pos = (0, 0)
    siels_pos = []
    nagis_pos = []

    while True:
        screen.blit(backimg, (0, 0))

        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos
                x -= sielimg.get_width() / 2
                y -= sielimg.get_width() / 2
                siels_pos.append((x, y))
            if event.type == MOUSEBUTTONDOWN and event.button == 3:
                x, y = event.pos
                x -= nagiimg.get_width() / 2
                y -= nagiimg.get_width() / 2
                nagis_pos.append((x, y))
            # if event.type == MOUSEMOTION:
            #     x, y = event.pos
            #     x -= sielimg.get_width() / 2
            #     y -= sielimg.get_width() / 2
            #     cur_pos = (x, y)
            # screen.blit(sielimg, cur_pos)

            for _pos_list, _img in [(siels_pos, sielimg), (nagis_pos, nagiimg)]:
                for i, j in _pos_list:
                    screen.blit(_img, (i, j))

            pygame.display.update()


if __name__ == '__main__':
    main()
