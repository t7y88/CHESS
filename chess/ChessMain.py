"""

"""

import pygame as p
import ChessEngine

p.init()

WIDTH = HEIGHT = 400 
DIMENSION = 8
SQ_SIZE = HEIGHT//DIMENSION
MAX_FPS = 15 #for animation later on

IMAGES = {}

'''
loading images
'''


def loadingImages():
    
    pieces = ["wR", "wN", "wB", "wQ", "wK", "wp", "bR", "bN", "bB", "bQ", "bK", "bp"]
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("images/" + piece + ".png"), (SQ_SIZE,SQ_SIZE))

    #now we can access an image by saying IMAGES['wR']

def main():

    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color('white'))
    gs = ChessEngine.gameState()
    print(gs.board)

main()