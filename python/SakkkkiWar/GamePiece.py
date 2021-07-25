import pygame
import math
from Helper import *
import Constants

class GamePieces(pygame.sprite.Sprite):
    #Class for stratego pieces
    def __init__(self, image, position, team):
        pygame.sprite.Sprite.__init__(self)
        self.team = team
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (int(BoardWidth / 8 - BoardWidth / 21), int(BoardWidth / 8 - BoardWidth / 21)))
        self.square = position
        self.rect = pygame.Rect(self.image.get_rect())
        self.rect.topleft = position.topleft
        self.rect.center = position.center
        self.level = None

    def draw(self, surface):
        surface.blit(self.image, self.rect.topleft)

    def drag(self, cursor):
        self.rect.center = cursor

    def update(self, position):
        self.square = position
        self.rect.center = position.center

    def movelist(self):
        return squareCenters

class USASubmarine(GamePieces):
    def __init__(self, image, position, team):
        GamePieces.__init__(self, image, position, team)
        self.bool = 0
        self.level = 5

    def movelist(self):
        move_list = []
        removeupto = []
        noblocks = make_lines(self.square, squareCenters, [math.pi / 2])
        takeblocks = make_lines(self.square, squareCenters, [math.pi / 4, 3 * math.pi / 4])
        if self.bool <= 0:
            for (x, y) in noblocks:
                move_list.append(x)
            move_list = move_list[len(move_list) - 2:len(move_list)]
        else:
            for (x, y) in noblocks:
                move_list.append(x)
            move_list = move_list[len(move_list) - 1:len(move_list)]

        for piece in Constants.PIECES:
            for item in noblocks:
                if piece.square == item[0]:
                    removeupto.append(item)
                    if item[0] in move_list:
                        move_list.remove(item[0])

        for x in move_list:
            for (a, b) in removeupto:
                if isfarther(self.square, a, x):
                    move_list.remove(x)

        for (block, angle) in takeblocks:
            if block.colliderect(self.square):
                for piece in Constants.PIECES:
                    if piece.square == block:
                        move_list.append(block)
        return move_list

class RUSSSubmarine(GamePieces):
    def __init__(self, image, position, team):
        GamePieces.__init__(self, image, position, team)
        self.bool = 0
        self.level = 5

    def movelist(self):
        move_list = []
        removeupto = []
        noblocks = make_lines(self.square, squareCenters, [-math.pi / 2])
        takeblocks = make_lines(self.square, squareCenters, [-math.pi / 4, -3 * math.pi / 4])
        if self.bool <= 0:
            for (x, y) in noblocks:
                move_list.append(x)
            move_list = move_list[0:2]
        else:
            for (x, y) in noblocks:
                move_list.append(x)
            move_list = move_list[0:1]

        for piece in Constants.PIECES:
            for item in noblocks:
                if piece.square == item[0]:
                    removeupto.append(item)
                    if item[0] in move_list:
                        move_list.remove(item[0])

        for x in move_list:
            for (a, b) in removeupto:
                if isfarther(self.square, a, x):
                    move_list.remove(x)

        for (block, angle) in takeblocks:
            if block.colliderect(self.square):
                for piece in Constants.PIECES:
                    if piece.square == block:
                        move_list.append(block)
        return move_list

class General(GamePieces):
    def __init__(self, image, position, team):
        GamePieces.__init__(self, image, position, team)
        self.bool = 0
        self.level = 10

    def movelist(self):
        move_list = []
        removeupto = []
        noblocks = make_lines(self.square, squareCenters, [math.pi / 2])
        takeblocks = make_lines(self.square, squareCenters, [math.pi / 4, 3 * math.pi / 4])
        if self.bool <= 0:
            for (x, y) in noblocks:
                move_list.append(x)
            move_list = move_list[len(move_list) - 2:len(move_list)]
        else:
            for (x, y) in noblocks:
                move_list.append(x)
            move_list = move_list[len(move_list) - 1:len(move_list)]

        for piece in Constants.PIECES:
            for item in noblocks:
                if piece.square == item[0]:
                    removeupto.append(item)
                    if item[0] in move_list:
                        move_list.remove(item[0])

        for x in move_list:
            for (a, b) in removeupto:
                if isfarther(self.square, a, x):
                    move_list.remove(x)

        for (block, angle) in takeblocks:
            if block.colliderect(self.square):
                for piece in Constants.PIECES:
                    if piece.square == block:
                        move_list.append(block)
        return move_list


class Destroyer(GamePieces):
    def __init__(self, image, position, team):
        GamePieces.__init__(self, image, position, team)
        self.bool = 0
        self.level = 3

    def movelist(self):
        removeupto = []
        noblocks = make_lines(self.square, squareCenters, [math.pi / 4,3 * math.pi / 4, -math.pi / 4, -3 * math.pi / 4])
        move_list = []

        for piece in Constants.PIECES:
            for item in noblocks:
                if piece.square == item[0]:
                    removeupto.append(item)

        for item in noblocks:
            move_list.append(item[0])

        for (x, y) in noblocks:
            for (a, b) in removeupto:
                if isfarther(self.square, a, x) and y == b and x in move_list:
                    move_list.remove(x)
        return move_list

class NUKE(GamePieces):
    def __init__(self, image, position, team):
        GamePieces.__init__(self, image, position, team)
        self.bool = 0
        self.level = 11 #nothing survives a tactical nuke, 3 nukes per team

    def movelist(self):
        removeupto=[]
        noblocks = make_lines(self.square, squareCenters, [math.pi/2, 3*math.pi/2, -math.pi/2, -3*math.pi/2])
        move_list = []
        for piece in Constants.PIECES:
            for item in noblocks:
                if piece.square == item[0]:
                    removeupto.append(item)

        for item in noblocks:
            move_list.append(item[0])

        for (x, y) in noblocks:
            for (a, b) in removeupto:
                if isfarther(self.square, a, x) and y == b and x in move_list:
                    move_list.remove(x)
        return move_list
