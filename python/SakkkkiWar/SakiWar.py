import pygame
from pygame.locals import MOUSEBUTTONDOWN, MOUSEBUTTONUP
import Helper
import Constants
import GamePiece
from Helper import *


from tkinter import Tk, messagebox


# noinspection PyUnusedLocal
def game():
    # The Game loop
    SHOW_END_GAME = 1
    Mousedown = False
    Mousereleased = False
    TargetPiece = None
    checkmate = False
    check_message = False
    check = False
    teams = ['USA', 'RUSS']
    score = [0,0]
    colors = [dark_brown, light_brown]
    drawboard(colors)

    while True:
        turn = teams[0]
        checkquitgame()
        pieceholder = None

        # --------      CHECK FOR CHECKMATE AND CHECK CONDITIONS --------

        if checkmate:
            colors = [gray, violet]
            drawboard(colors)
            if SHOW_END_GAME:
                show_checkmate(teams)
                SHOW_END_GAME = 0

        elif check and not check_message:
            show_check(teams)
            check_message = True
            continue

        # ----- END CHECKING ----

        drawboard(colors)

        # get cursor
        Cursor = pygame.mouse.get_pos()

        # ---- BLOCKING CALL ----
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                Mousedown = True
            if event.type == MOUSEBUTTONUP:
                Mousedown = False
                Mousereleased = True

        # ---- Events on MouseDown -----
        # pickup the nearest piece if a piece is not selected
        if Mousedown and not TargetPiece:
            TargetPiece = nearest_piece(Cursor, Constants.PIECES)
            if TargetPiece:
                OriginalPlace = TargetPiece.square

        if Mousedown and TargetPiece:
            TargetPiece.drag(Cursor)

        # ---- MouseReleased Events -----
        if Mousereleased:
            Mousereleased = False

            # ----- validate turn -----
            if TargetPiece and TargetPiece.team != turn:  # check your turn
                TargetPiece.update(OriginalPlace)
                TargetPiece = None
                print('check your turn')

            # ---- set closest piece that can be taken ----
            elif TargetPiece:
                pos1 = TargetPiece.rect.center
                for Square in squareCenters:
                    if distance_formula(pos1, Square.center) < Helper.BoardWidth / 16:  # half width of square
                        newspot = Square
                        otherpiece = nearest_piece(Square.center, Constants.PIECES)
                        break

                if otherpiece and otherpiece != TargetPiece and otherpiece.team == TargetPiece.team:

                    # check if space is occupied by team
                    TargetPiece.update(OriginalPlace)

                elif newspot not in TargetPiece.movelist():

                    # check if you can move there
                    TargetPiece.update(OriginalPlace)

                elif otherpiece and otherpiece != TargetPiece and type(otherpiece) != GamePiece.General:
                    # take enemy piece
                    if otherpiece.level <= TargetPiece.level:
                        pieceholder = piece
                        Constants.PIECES.remove(otherpiece)
                        TargetPiece.update(newspot)
                    #calculate score
                    teams = teams[::-1]  # switch teams
                    if turn == 'USA':
                        score[0] += 1
                    else:
                        score[1] += 1
                else:
                    # move
                    TargetPiece.update(newspot)
                    if type(TargetPiece) == GamePiece.Destroyer or type(TargetPiece) == GamePiece.RUSSSubmarine or type(TargetPiece) == GamePiece.USASubmarine:
                        TargetPiece.bool += 1
                    teams = teams[::-1]  # switch teams

                if True:  # always check every turn at end
                    check = False
                    for piece in Constants.PIECES:
                        if type(piece) == None and piece.team == turn:
                            check = piece.undercheck()
                if check:
                    # if still under check revert back
                    TargetPiece.update(OriginalPlace)
                    if pieceholder and pieceholder.team != TargetPiece.team:
                        Constants.PIECES.append(pieceholder)
                        # noinspection PyUnusedLocal
                        pieceholder = None

                    teams = teams[::-1]  # switch back
            TargetPiece = None

        for piece in Constants.PIECES:
            piece.draw(screen)
            scoreString = 'USA: ' + str(score[0]) + 'ROOOOKIE: '+ str(score[1])
            draw_text(screen, scoreString , 18, ScreenWidth / 2, 10)
        pygame.display.flip()


pygame.display.set_caption('SakiWar')
FPS = pygame.time.Clock()
FPS.tick(30)

if __name__ == '__main__':
    game()
