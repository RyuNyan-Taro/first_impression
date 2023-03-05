# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
import math
import sys
import pygame.mixer
SCREEN = Rect(0, 0, 400, 400)


class Paddle(pygame.sprite.Sprite):
    def __int__(self, filename):
        # todo: fix RecursionError of which below line is case
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = pygame.image.load(filename).convert()
        self.rect = self.image.get_rect()
        self.rect.bottom = SCREEN.bottom - 20

    def update(self):
        self.rect.centerx = pygame.mouse.get_pos()[0]
        self.rect.clamp_ip(SCREEN)


# ブロックのクラス
class Block(pygame.sprite.Sprite):
    def __init__(self, filename, x, y):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = pygame.image.load(filename).convert()
        self.rect = self.image.get_rect()
        # ブロックの左上座標
        self.rect.left = SCREEN.left + x * self.rect.width
        self.rect.top = SCREEN.top + y * self.rect.height


def main():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN.size)
    # 描画用のスプライトグループ
    group = pygame.sprite.RenderUpdates()

    # 衝突判定用のスプライトグループ
    blocks = pygame.sprite.Group()

    # add to sprite group
    Paddle.containers = group
    Block.containers = group, blocks

    # create paddle and blocks
    paddle = Paddle("paddle.png")
    for x in range(1, 15):
        for y in range(1, 11):
            Block("block.png", x, y)
    clock = pygame.time.Clock()

    while (1):
        clock.tick(30)
        screen.fill((0, 20, 0))
        group.update()
        group.draw(screen)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()


if __name__ == "__main__":
    main()

