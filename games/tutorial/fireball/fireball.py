import pygame
from pygame.locals import *
import math
import sys

SCR_RECT = Rect(0, 0, 640, 480)
START = (320, 240)


class Fireball(pygame.sprite.Sprite):
    speed = 10

    def __init__(self, start, target):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.rect = self.image.get_rect()
        self.start = start
        self.target = target
        self.rect.center = self.start
        self.direction = math.atan2(target[1] - start[1], target[0] - start[0])
        self.vx = math.cos(self.direction) * self.speed
        self.vy = math.sin(self.direction) * self.speed

    def update(self):
        self.rect.move_ip(self.vx, self.vy)
        if not SCR_RECT.contains(self.rect):
            self.kill()


def mouse_handler():
    mouse_pressed = pygame.mouse.get_pressed()
    if mouse_pressed[0]:
        x, y = pygame.mouse.get_pos()
        Fireball(START, (x, y))


def load_image(filename, colorkey = None):
    try:
        image = pygame.image.load(filename)
    except pygame.error as message:
        print('Can not load image', filename)
        raise SystemExit(message)
    image = image.convert()
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey, RLEACCEL)

    return image


def main():
    pygame.init()
    screen = pygame.display.set_mode(SCR_RECT.size)
    pygame.display.set_caption(u'fireball')

    all_sprite = pygame.sprite.RenderUpdates()
    Fireball.containers = all_sprite
    Fireball.image = load_image('../image/fireball.png')

    clock = pygame.time.Clock()
    while True:
        clock.tick(60)
        screen.fill((0, 0, 0))
        mouse_handler()
        all_sprite.update()
        all_sprite.draw(screen)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()


if __name__ == '__main__':
    main()
