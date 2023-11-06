"""

This is a basic chess engine (wanna be Stockfish)
functionality and validity of moves are determined by this engine

"""

class gameState():

    def __init__(self) -> None:
        self.board = [
            ["wB", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bp", "..", "bp", "bp", "bp", "bp", "bp", "bp"],
            ["..", "..", "..", "..", "..", "..", "..", ".."],
            ["..", "..", "..", "..", "..", "..", "..", ".."],
            ["..", "..", "..", "..", "..", "bB", "..", ".."],
            ["..", "..", "..", "..", "..", "..", "..", ".."],
            ["wp", "wp", "wp", "wp", "wp", "wp", "..", "wp"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", ".."],
        ]

        self.whiteToMove = True
        self.moveLog = []
    
    
    def makeMove(self, move):
        
        self.board[move.startRow][move.startCol] = ".."         #moved the piece from the pos it was so now the square is empty 
        self.board[move.endRow][move.endCol] = move.pieceMoved  
        self.moveLog.append(move)                               #keeping the log
        self.whiteToMove = not self.whiteToMove                 #change the bool to not indicating turn of the other color (switching turns)

    def undoMove(self):

        if len(self.moveLog) != 0:
            move = self.moveLog.pop()
            self.board[move.startRow][move.startCol] = move.pieceMoved
            self.board[move.endRow][move.endCol] = move.pieceCaptured
            self.whiteToMove = not self.whiteToMove

    def getValidMoves(self):
        return self.getAllPossibleMoves()


    def getAllPossibleMoves(self):

        moves = []

        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                
                wb = self.board[row][col][0]  #the color of the piece ie the first letter of the string 
                piece = self.board[row][col][1]

                if (wb == 'w' and self.whiteToMove) or (wb == 'b' and not self.whiteToMove):
                    
                    if piece == 'p':
                        self.getPawnMoves(row, col, moves)
                    elif piece == 'N':
                        self.getKnightMoves(row, col, moves)
                    elif piece == 'B':
                        self.getBishopMoves(row, col, moves)
                    elif piece == 'R':
                        self.getRookMoves(row, col, moves)
                    elif piece == 'Q':
                        self.getBishopMoves(row, col, moves)
                        self.getRookMoves(row, col, moves)
                    elif piece == 'K':
                        self.getKingMoves(row, col, moves)
                    
        return moves


    "Move function for each piece"

    def getPawnMoves(self,row, col, moves):
        
        if self.whiteToMove:                            #white moves
            if self.board[row - 1][col] == "..":        #if there is nothing infront of it
                moves.append(Move((row, col), (row-1, col), self.board))
                if row == 6 and self.board[row - 2][col] == "..":
                    moves.append(Move((row, col), (row-2, col), self.board)) #2 pawn move

            # CAPTURES for white

            if col-1 >= 0:
                if self.board[row-1][col-1][0] == 'b':      
                    moves.append(Move((row, col), (row-1, col-1), self.board))
            if col+1 <=7:
                if self.board[row-1][col+1][0] == 'b':
                    moves.append(Move((row, col), (row-1, col+1), self.board)) 
        
        elif not self.whiteToMove:                      #black moves
            if self.board[row + 1][col] == "..":        #if there is nothing infront of it
                moves.append(Move((row, col), (row+1, col), self.board))
                if row == 1 and self.board[row + 2][col] == "..":
                    moves.append(Move((row, col), (row+2, col), self.board)) #2 pawn move
            
            #CAPTURES for black

            if col-1 >= 0:
                if self.board[row+1][col-1][0] == 'w':
                    moves.append(Move((row, col), (row+1, col-1), self.board))
            if col+1 <=7:
                if self.board[row+1][col+1][0] == 'w':
                    moves.append(Move((row, col), (row+1, col+1), self.board)) 
                

    def getKnightMoves(self, row, col, moves):

        # NOT the best coded moves but ill see into it when debugging now the thing is to get them to work

        #improved the way it was coded (less hardcoded can be better ig)

        t = [[-2,-1], [-2,1], [-1,-2], [-1,2], [1,-2], [1,2], [2,-1], [2,1]] #these are all the possible sq that knight can acsess at best (from say a d4 square)
            
        for i in range(len(t)):
            
            if row+(t[i][0]) <= 7 and row+(t[i][0]) >= 0 and col+(t[i][1]) <=7 and col+(t[i][1]) >= 0:  #check all the moves that are in the range of the board
        
                if self.whiteToMove:                 #WhiteMoves                            
                
                    if self.board[row+(t[i][0])][col+(t[i][1])][0] != "w":                                  #check if there is a white peice already standing there
                        moves.append(Move((row, col), (row+(t[i][0]), col+(t[i][1])), self.board))          # if not then it is a legal move(actually possible legal we would be deciding afterwards)

            
                elif not self.whiteToMove:          # BlackMoves    Same as white 

                    if self.board[row+(t[i][0])][col+(t[i][1])][0] != "b":
                        moves.append(Move((row, col), (row+(t[i][0]), col+(t[i][1])), self.board))

        pass

    def getBishopMoves(self, row, col, moves):

        dir = [[-1,-1], [-1,1], [1,-1], [1,1]] #all the direction the bishop can move

        enemyColor = "b" if self.whiteToMove else "w"

        for d in dir:                           #iternating through all the directions

            for i in range(1,8):                #iterating through 1 to 8 

                lastRow = row + d[0] * i        #multipling i to the x coordinate and y coordinate
                lastCol = col + d[1] * i

                if 0 <= lastRow <= 7 and 0 <= lastCol <= 7:     #checking if they are on the board

                    if self.board[lastRow][lastCol] == "..":                            #if the sq is empty then we can append the move
                        moves.append(Move((row, col), (lastRow,lastCol), self.board))   
                    elif self.board[lastRow][lastCol][0] == enemyColor:                 #if the sq is of an enemy color 
                        moves.append(Move((row, col), (lastRow,lastCol), self.board))   #we append the move but we can not go further 
                        break                                                           #hence a break also put at the end
                    else:               #if we see an alley piece we also break cant go further 
                        break
                
                else:       #if off board we will simply break 
                    break
                
        pass
    
    def getRookMoves(self, row, col, moves):
        
        #Same as Bishop just directions has changed

        dir = [[0,-1], [0,1], [1,0], [-1,0]] #all the direction the rook can move

        enemyColor = "b" if self.whiteToMove else "w"

        for d in dir:

            for i in range(1,8):

                lastRow = row + d[0] * i
                lastCol = col + d[1] * i

                if 0 <= lastRow <= 7 and 0 <= lastCol <= 7:

                    if self.board[lastRow][lastCol] == "..":
                        moves.append(Move((row, col), (lastRow,lastCol), self.board))
                    elif self.board[lastRow][lastCol][0] == enemyColor:
                        moves.append(Move((row, col), (lastRow,lastCol), self.board))
                        break
                    else:
                        break
                
                else:
                    break


    def getKingMoves(self, row, col, moves):

        #Again using basic modifications it is similar to what we did for Bishop just changes the directions

        dir = [[-1,-1], [-1,0], [-1,1],[0,-1], [0,1],[1,-1], [1,0], [1,1]]

        enemyColor = "b" if self.whiteToMove else "w"


        for d in dir:

            for i in range(1,8):

                lastRow = row + d[0] 
                lastCol = col + d[1] 

                if 0 <= lastRow <= 7 and 0 <= lastCol <= 7:

                    if self.board[lastRow][lastCol] == "..":
                        moves.append(Move((row, col), (lastRow,lastCol), self.board))
                    elif self.board[lastRow][lastCol][0] == enemyColor:
                        moves.append(Move((row, col), (lastRow,lastCol), self.board))
                        break
                    else:
                        break
                
                else:
                    break

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

        self.moveID = self.startRow*1000 + self.startCol*100 + self.endRow*10 + self.endCol # e2 -> e4 would be 6444

    def __eq__(self, other) :
        if isinstance(other, Move):
            return self.moveID == other.moveID
        return False

    def getRankFile(self, rows, coloumns):
        return self.colsToFiles[coloumns] + self.rowsToRanks[rows]

    '''
    just wwriting a basic ches notation where the sq the piece was on and sq it moved to would be recorded 
    probably would improve this afterwards with proper notation like Nf3
    '''

    def getChessNotation(self):
        return self.getRankFile(self.startRow, self.startCol) + self.getRankFile(self.endRow, self.endCol)



