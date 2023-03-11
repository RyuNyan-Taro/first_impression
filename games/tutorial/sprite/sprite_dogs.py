import pygame
from pygame.locals import *
import sys

SCR_RECT = Rect(0, 0, 640, 480)


class MySprite(pygame.sprite.Sprite):
    def __init__(self, x, y, vx, vy, img_num):
        pygame.sprite.Sprite.__init__(self)
        sielimg = pygame.image.load('../image/siel.png').convert_alpha()
        nagiimg = pygame.image.load('../image/nagi.png').convert_alpha()
        self.images = (sielimg, nagiimg)
        width = self.images[0].get_width()
        height = self.images[0].get_height()
        self.rect = Rect(x, y, width, height)
        self.vx = vx
        self.vy = vy
        self.img_num = img_num

    def update(self):
        self.rect.move_ip(self.vx, self.vy)
        if self.rect.left < 0 or self.rect.right > SCR_RECT.width:
            self.vx = -self.vx
            self.img_num = 0
        if self.rect.top < 0 or self.rect.bottom > SCR_RECT.height:
            self.vy = -self.vy
            self.img_num = 1
        self.rect = self.rect.clamp(SCR_RECT)

    def draw(self, screen):
        screen.blit(self.images[self.img_num], self.rect)


def main():
    pygame.init()
    screen = pygame.display.set_mode(SCR_RECT.size)
    pygame.display.set_caption(u'using of sprite')
    sprites_list = list()
    sprites_list.append(MySprite(0, 0, 2, 2, 0))
    sprites_list.append(MySprite(10, 10, 5, 5, 1))
    sprites_list.append(MySprite(320, 240, -2, 3, 0))
    sprites_list.append(MySprite(320, 240, -2, 3, 0))
    sprites_list.append(MySprite(5, 47, 4, 5, 0))
    sprites_list.append(MySprite(300, 1, 6, 10, 0))
    sprites_list.append(MySprite(22, 440, -2, 3, 0))

    clock = pygame.time.Clock()

    while True:
        clock.tick(60)

        screen.fill((0, 0, 255))

        for _sprite in sprites_list:
            _sprite.update()
        for _sprite in sprites_list:
            _sprite.draw(screen)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()


if __name__ == '__main__':
    main()