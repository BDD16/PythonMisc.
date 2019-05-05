from Helper import *
from GamePiece import *

NAME = 'SakiWar'

PIECES_NAME = {
    "USA": './SubmarineUSA.png',
    "RUSS": './SubmarineRussian.png',
    "DEST": './GMDWater.png',
    "NUKE": './Nuke2.png',
    "TRUMP": './MasterChief.png',
    "QUEEN": './QueenPutin.jpg'
}

light_brown = (251, 196, 117)
gray = (100, 100, 100)
violet = (238, 130, 238)
dark_brown = (139, 69, 0)
colors = [dark_brown, light_brown]
drawboard(colors)
LIFE = {
    'PLAYER_ONE': 10,
    'PLAYER_TWO': 10
}

PIECES = [
    USASubmarine(PIECES_NAME['USA'], squareCenters[48], 'USA'),
    USASubmarine(PIECES_NAME['USA'], squareCenters[49], 'USA'),
    USASubmarine(PIECES_NAME['USA'], squareCenters[50], 'USA'),
    USASubmarine(PIECES_NAME['USA'], squareCenters[51], 'USA'),
    USASubmarine(PIECES_NAME['USA'], squareCenters[52], 'USA'),
    USASubmarine(PIECES_NAME['USA'], squareCenters[53], 'USA'),
    USASubmarine(PIECES_NAME['USA'], squareCenters[54], 'USA'),
    USASubmarine(PIECES_NAME['USA'], squareCenters[55], 'USA'),
    RUSSSubmarine(PIECES_NAME['RUSS'], squareCenters[8], 'RUSS'),
    RUSSSubmarine(PIECES_NAME['RUSS'], squareCenters[9], 'RUSS'),
    RUSSSubmarine(PIECES_NAME['RUSS'], squareCenters[10], 'RUSS'),
    RUSSSubmarine(PIECES_NAME['RUSS'], squareCenters[11], 'RUSS'),
    RUSSSubmarine(PIECES_NAME['RUSS'], squareCenters[12], 'RUSS'),
    RUSSSubmarine(PIECES_NAME['RUSS'], squareCenters[13], 'RUSS'),
    RUSSSubmarine(PIECES_NAME['RUSS'], squareCenters[14], 'RUSS'),
    RUSSSubmarine(PIECES_NAME['RUSS'], squareCenters[15], 'RUSS'),
    Destroyer(PIECES_NAME['DEST'], squareCenters[56], 'USA'),
    Destroyer(PIECES_NAME['DEST'], squareCenters[57], 'USA'),
    Destroyer(PIECES_NAME['DEST'], squareCenters[58], 'USA'),
    Destroyer(PIECES_NAME['DEST'], squareCenters[59], 'USA'),
    NUKE(PIECES_NAME['NUKE'], squareCenters[60],'USA'),
    NUKE(PIECES_NAME['NUKE'], squareCenters[62],'USA'),
    NUKE(PIECES_NAME['NUKE'], squareCenters[63],'USA'),
    NUKE(PIECES_NAME['NUKE'], squareCenters[1],'RUSS'),
    NUKE(PIECES_NAME['NUKE'], squareCenters[7],'RUSS'),
    NUKE(PIECES_NAME['NUKE'], squareCenters[3],'RUSS'),
    General(PIECES_NAME['TRUMP'], squareCenters[61],'USA'),
    General(PIECES_NAME['QUEEN'], squareCenters[5], 'RUSS')
]
