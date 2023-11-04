"""

This is a basic chess engine (wanna be Stockfish)
functionality and validity of moves are determined by this engine

"""

class gameState():

    def __init__(self) -> None:
        self.board = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
            ["..", "..", "..", "..", "..", "..", "..", ".."],
            ["..", "..", "..", "..", "..", "..", "..", ".."],
            ["..", "..", "..", "..", "..", "..", "..", ".."],
            ["..", "..", "..", "..", "..", "..", "..", ".."],
            ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"],
        ]

        self.whiteToMove = True
        self.moveLog = []
    
    
    def makeMove(self, move):
        
        self.board[move.startRow][move.startCol] = ".."         #moved the piece from the pos it was so now the square is empty 
        self.board[move.endRow][move.endCol] = move.pieceMoved  
        self.moveLog.append(move)                               #keeping the log
        self.whiteToMove = not self.whiteToMove                 #change the bool to not indicating turn of the other color (switching turns)


class Move():

    #we have to convert our rows and coloumn of the board into chessnotations so we would be making dictionaries where we can convert them however we want

    ranksToRows = { "1": 7, "2": 6, "3": 5, "4": 4, "5": 3, "6": 2, "7": 1, "8": 0}
    rowsToRanks = {v: k for k, v in ranksToRows.items()}
    filesToCols = { "h": 7, "g": 6, "f": 5, "e": 4, "d": 3, "c": 2, "b": 1, "a": 0}
    colsToFiles = {v: k for k, v in filesToCols.items()}

    def __init__ (self, startSq, endSq, board):
        self.startRow = startSq[0]
        self.startCol = startSq[1]
        self.endRow = endSq[0]
        self.endCol = endSq[1]
        
        self.pieceMoved = board[self.startRow][self.startCol]
        self.pieceCaptured = board[self.endRow][self.endCol]

    def getRankFile(self, rows, coloumns):
        return self.colsToFiles[coloumns] + self.rowsToRanks[rows]

    '''
    just wwriting a basic ches notation where the sq the piece was on and sq it moved to would be recorded 
    probably would improve this afterwards with proper notation like Nf3
    '''

    def getChessNotation(self):
        return self.getRankFile(self.startRow, self.startCol) + self.getRankFile(self.endRow, self.endCol)
        


