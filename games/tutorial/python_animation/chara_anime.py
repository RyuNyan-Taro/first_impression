import pygame
from pygame.locals import *
import sys

SCR_RECT = Rect(0, 0, 640, 480)


def load_image(filename, colorkey=None):
    try:
        image = pygame.image.load(filename)
    except pygame.error as message:
        print('Can not load image.', filename)
        raise SystemExit(message)
    image = image.convert()
    if colorkey is not None:
        if colorkey == 1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey, RLEACCEL)

    return image


def split_image(image):
    imageList = list()
    for i in range(0, 128, 32):
        surface = pygame.Surface((32, 32))
        surface.blit(image, (0, 0), (i, 0, 32, 32))
        surface.set_colorkey(surface.get_at((0, 0)), RLEACCEL)
        surface.convert()
        imageList.append(surface)

    return imageList


class Character(pygame.sprite.Sprite):
    animcycle = 12
    frame = 0

    def __init__(self, filename, x, y):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.images = split_image(load_image(filename))
        self.image = self.images[0]
        self.rect = self.image.get_rect(topleft=(x, y))

    def update(self):
        self.frame += 1
        self.image = self.images[int(self.frame/self.animcycle % 4)]


def main():
    pygame.init()
    screen = pygame.display.set_mode(SCR_RECT.size)
    pygame.display.set_caption(u'character_animation')

    all_sprite = pygame.sprite.RenderUpdates()
    Character.containers = all_sprite

    player = Character('../image/player4.png', 0, 0)
    king = Character('../image/king4.png', 32, 0)
    soldier = Character('../image/soldier4.png', 64, 0)

    clock = pygame.time.Clock()
    while True:
        clock.tick(60)
        screen.fill((0, 0, 255))
        all_sprite.update()
        all_sprite.draw(screen)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()


if __name__ == '__main__':
    main()
