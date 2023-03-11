import random

import pygame
from pygame.locals import *
import sys

SCR_RECT = Rect(0, 0, 640*2, 480*2)


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


def initial_pos_speed() -> tuple[int, int, float, float]:
    """Return random x and y pos, and vx and vy speed"""

    def initial_speed():
        speed = round(random.triangular(1, 5, 1), 2)
        multiply = random.randint(0, 1)
        speed = speed * ((-1) ** multiply)

        return speed

    x_pos = random.randint(0, SCR_RECT.size[0])
    y_pos = random.randint(0, SCR_RECT.size[1])
    vx_speed = initial_speed()
    vy_speed = initial_speed()

    return x_pos, y_pos, vx_speed, vy_speed


def main():
    pygame.init()
    screen = pygame.display.set_mode(SCR_RECT.size)
    pygame.display.set_caption(u'How to use sprite group')

    group = pygame.sprite.RenderUpdates()
    for _i in range(20):
        my_sprite = MySprite('image/python.png', *initial_pos_speed())
        group.add(my_sprite)

    clock = pygame.time.Clock()

    while True:
        clock.tick(60)
        screen.fill((0, 0, 255))

        group.update()
        group.draw(screen)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()


if __name__ == '__main__':
    main()
