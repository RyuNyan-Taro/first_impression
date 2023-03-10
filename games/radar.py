import pygame
from pygame.locals import *
import math
import sys


def main():
    (x, y) = (400, 400)
    deg = 0
    pygame.init()
    pygame.display.set_mode((x, y), 0, 32)
    screen = pygame.display.get_surface()

    while 1:
        deg += 2
        if deg >= 360:
            deg = 0

        # background of radar
        pygame.draw.circle(screen, (0, 200, 0), (int(x/2), int(y/2)), int(x/2), 1)
        pygame.draw.circle(screen, (0, 200, 0), (int(x/2), int(y/2)), int(x/4), 1)
        pygame.draw.line(screen, (0, 200, 0), (0, int(y/2)), (x, int(y/2)))
        pygame.draw.line(screen, (0, 200, 0), (int(x/2), 0), (int(x/2), y))

        # locus of radar
        for i in range(1, 30):
            dx = x/2 + x/2 * math.cos(math.radians(deg-i))
            dy = y/2 + x/2 * math.sin(math.radians(deg-i))
            pygame.draw.aaline(screen, (0, int(255/i), 0), (int(x/2), int(y/2)), (dx, dy),5)

        pygame.display.update()
        pygame.time.wait(30)
        screen.fill((0, 20, 0, 0))

        # イベント
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()


if __name__ == '__main__':
    main()
