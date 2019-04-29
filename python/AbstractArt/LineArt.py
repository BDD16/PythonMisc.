import sys
import pygame
from pygame.locals import *

HEIGHT = 500
WIDTH = 500
SCREEN_COLOR = (0,0,0)
LINE_COLOR = (255,255,255)
LINE_WIDTH = 5

me = '[LineArt]'

class LineArt:

    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.screen.fill(SCREEN_COLOR)
        pygame.display.flip()
        print(me +'Welcome to LineArt')

    def DrawFromLeftCorner(self):
        LINE_COLOR = (0,255,0)
        for i in range(WIDTH):
            if i %15 == 0:
                pygame.draw.line(self.screen, LINE_COLOR,(0, i + 15), ((WIDTH-i -15), 0), LINE_WIDTH)

        pygame.display.flip()

    def DrawFromRightCorner(self):
        for i in range(WIDTH):
            LINE_COLOR = (abs(255 + i) % 255, abs((255 +i)) % 255,  255)
            if i %15 == 0:
                pygame.draw.line(self.screen, LINE_COLOR,(WIDTH-i -15, 0), (WIDTH,HEIGHT-i -15), LINE_WIDTH)

        pygame.display.flip()

    def DrawFromLowerRight(self):
        LINE_COLOR = (255,0,0)
        for i in range(WIDTH):
            if i %15 == 0:
                pygame.draw.line(self.screen, LINE_COLOR,(0, HEIGHT - i - 15), (WIDTH-i- 15,(HEIGHT)), LINE_WIDTH)

        pygame.display.flip()

    def DrawFromLowerLeft(self):
        LINE_COLOR = (0,0,155)
        for i in range(WIDTH):
            if i %15 == 0:
                pygame.draw.line(self.screen, LINE_COLOR,(i, HEIGHT), (WIDTH,(HEIGHT-i-15)), LINE_WIDTH)

        pygame.display.flip()

    def DrawAllFourCorners(self):
        self.DrawFromLeftCorner()
        self.DrawFromRightCorner()
        self.DrawFromLowerLeft()
        self.DrawFromLowerRight()




if __name__ == '__main__':
    x = LineArt()
    x.DrawAllFourCorners()
    while True:
        for events in pygame.event.get():
            if events.type == QUIT:
                sys.exit(0)
