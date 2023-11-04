"""

"""

import pygame as p
import ChessEngine

p.init() # initalising the pygamr

WIDTH = HEIGHT = 768        # size of the window            
DIMENSION = 8
SQ_SIZE = HEIGHT//DIMENSION 
MAX_FPS = 15                #for animation fps

IMAGES = {}

# using our png images to make a dictinary that would be having the piece name as a key and the image as its value

def loadingImages():
    
    pieces = ["wR", "wN", "wB", "wQ", "wK", "wp", "bR", "bN", "bB", "bQ", "bK", "bp"]
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("chess/images/" + piece + ".png"), (SQ_SIZE,SQ_SIZE))

    #now we can access an image by saying IMAGES['wR']

def main():

    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color('white'))
    gs = ChessEngine.gameState()

    loadingImages() 
    running = True
    
    selSquare = ()      # keep track of the last clicked sq
    playerClicks = []   # list of selectedSquares (would look like list of tuples)

    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            elif e.type == p.MOUSEBUTTONDOWN:
                location = p.mouse.get_pos()  #(rows, coloumns)
                col = location[0]//SQ_SIZE    # check this!!!
                row = location[1]//SQ_SIZE

                if selSquare == (row, col):   # the case where we would be selecting the same square for the seconf time say pawn e2->e2
                    selSquare = ()            # if that would be the case we would simply delect the click 
                    playerClicks = []
                else :
                    selSquare = (row, col)          # if that is not the case we would be storing the selected click as a tuple in the PlayerClicks
                    playerClicks.append(selSquare)
                
                if len(playerClicks) == 2:          #if 2 clicks have been made (e2 -> e4)[(5,2) -> (5,4)]
                    move = ChessEngine.Move(playerClicks[0], playerClicks[1], gs.board)
                    print(move.getChessNotation())
                    gs.makeMove(move)
                    selSquare = ()
                    playerClicks = []               
        
        drawGameState(screen,gs)
        clock.tick(MAX_FPS)
        p.display.flip()
    

#drawing the game board and the pieces using the images we loaded above

def drawGameState(screen ,gs):
    colors = [p.Color("light yellow"), p.Color("orangered4")]
    board = gs.board

    for row in range(DIMENSION):
        for coloumn in range(DIMENSION):
            color = colors[(row + coloumn) % 2]
            p.draw.rect(screen, color, p.Rect(coloumn*SQ_SIZE, row*SQ_SIZE, SQ_SIZE, SQ_SIZE))
            piece = board[row][coloumn]
            if piece != "..":
                screen.blit(IMAGES[piece], p.Rect(coloumn*SQ_SIZE, row*SQ_SIZE, SQ_SIZE, SQ_SIZE))


main()