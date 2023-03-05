import pygame
from pygame.locals import *
import datetime
import sys


def main():
    pygame.init()
    screen = pygame.display.set_mode((300, 200))
    pygame.display.set_caption('GAME')
    font = pygame.font.Font(None, 25)
    while 1:
        screen.fill((0, 0, 0))
        text = font.render(str(datetime.datetime.now()), True, (255, 255, 255))
        screen.blit(text, [20, 100])
        pygame.display.update()
        # event
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()


if __name__ == "__main__":
    main()
