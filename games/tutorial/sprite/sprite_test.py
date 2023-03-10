import pygame
from pygame.locals import *
import sys

SCR_RECT = Rect(0, 0, 640, 480)


class MySprite(pygame.sprite.Sprite):
    def __init__(self, filename, x, y, vx, vy):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert_alpha()
        width = self.image.get_width()
        height = self.image.get_height()
        self.rect = Rect(x, y, width, height)
        self.vx = vx
        self.vy = vy

    def update(self):
        self.rect.move_ip(self.vx, self.vy)
        if self.rect.left < 0 or self.rect.right > SCR_RECT.width:
            self.vx = -self.vx
        if self.rect.top < 0 or self.rect.bottom > SCR_RECT.height:
            self.vy = -self.vy
        self.rect = self.rect.clamp(SCR_RECT)

    def draw(self, screen):
        screen.blit(self.image, self.rect)


def main():
    pygame.init()
    screen = pygame.display.set_mode(SCR_RECT.size)
    pygame.display.set_caption(u'using of splite')

    python1 = MySprite('../image/python.png', 0, 0, 2, 2)
    python2 = MySprite('../image/python.png', 10, 10, 5, 5)
    python3 = MySprite('../image/python.png', 320, 240, -2, 3)

    clock = pygame.time.Clock()

    while True:
        clock.tick(60)

        screen.fill((0, 0, 255))

        python1.update()
        python2.update()
        python3.update()

        python1.draw(screen)
        python2.draw(screen)
        python3.draw(screen)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()


if __name__ == '__main__':
    main()