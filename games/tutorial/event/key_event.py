import pygame
from pygame.locals import *
import sys

SCREEN_SIZE = (640, 480)


def main():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption(u'key_event')

    img = pygame.image.load('../image/python.png').convert_alpha()
    img_rect = img.get_rect()
    img_rect.center = (320, 240)

    vx = vy = 20

    while True:
        screen.fill((0, 0, 255))
        screen.blit(img, img_rect)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    sys.exit()
                if event.key == K_LEFT:
                    img_rect.move_ip(-vx, 0)
                if event.key == K_RIGHT:
                    img_rect.move_ip(vx, 0)
                if event.key == K_UP:
                    img_rect.move_ip(0, -vy)
                if event.key == K_DOWN:
                    img_rect.move_ip(0, vy)


if __name__ == '__main__':
    main()

