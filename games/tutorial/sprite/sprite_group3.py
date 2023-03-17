import pygame
from pygame.locals import *
import sys

SCR_RECT = Rect(0, 0, 640, 480)


class MySprite(pygame.sprite.Sprite):
    def __init__(self, filename, x, y, vx, vy):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = pygame.image.load(filename).convert_alpha()
        self.rect = Rect(x, y, self.image.get_width(), self.image.get_height())
        self.vx = vx
        self.vy = vy

    def update(self):
        self.rect.move_ip(self.vx, self.vy)
        if self.rect.left < 0 or self.rect.right > SCR_RECT.width:
            self.vx = -self.vx
        if self.rect.top < 0 or self.rect.bottom > SCR_RECT.height:
            self.vy = -self.vy
        self.rect = self.rect.clamp(SCR_RECT)


def main():
    pygame.init()
    screen = pygame.display.set_mode(SCR_RECT.size)
    pygame.display.set_caption(u'How to use sprite group 3')

    group = pygame.sprite.RenderUpdates()
    MySprite.containers = group


    python1 = MySprite('../image/python.png', 0, 0, 2, 2)
    python2 = MySprite('../image/python.png', 10, 10, 5, 5)
    python3 = MySprite('../image/python.png', 0, 0, 5, 5)

    clock = pygame.time.Clock()

    background = pygame.Surface(SCR_RECT.size)
    background.fill((0, 0, 255))
    screen.blit(background, (0, 0))
    pygame.display.update()

    while True:
        clock.tick(60)
        group.clear(screen, background)
        group.update()
        print(python1.rect)

        dirty_rects = group.draw(screen)
        print(dirty_rects)

        pygame.display.update(dirty_rects)
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()


if __name__ == '__main__':
    main()
