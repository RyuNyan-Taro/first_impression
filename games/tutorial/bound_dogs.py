import pygame
from pygame.locals import *
import sys

SCR_WIDTH, SCR_HEIGHT = 640, 480


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCR_WIDTH, SCR_HEIGHT))
    pygame.display.set_caption('move image and reflection')

    sielimg = pygame.image.load('image/siel.png').convert_alpha()
    nagiimg = pygame.image.load('image/nagi.png').convert_alpha()
    dog_images = (sielimg, nagiimg)
    img_rect = sielimg.get_rect()

    vx = vy = 2
    clock = pygame.time.Clock()
    img_switch = 0
    
    while True:
        clock.tick(60)

        img_rect.move_ip(vx, vy)
        if img_rect.left < 0 or img_rect.right > SCR_WIDTH:
            vx = -vx
            img_switch = 1
        if img_rect.top < 0 or img_rect.bottom > SCR_HEIGHT:
            vy = -vy
            img_switch = 0

        screen.fill((0, 0, 255))
        screen.blit(dog_images[img_switch], img_rect)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == QUIT: sys.exit()
            if event.type == KEYDOWN and event.key == K_ESCAPE: sys.exit()


if __name__ == '__main__':
    main()
