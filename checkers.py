import sys

##COLORS##
#             R    G    B
WHITE = (255, 255, 255)
BLUE = (0,   0, 255)
RED = (255,   0,   0)
BLACK = (0,   0,   0)
GOLD = (255, 215,   0)
HIGH = (160, 190, 255)

TOPLEFT = "topLeft"
TOPRIGHT = "topRight"
BOTLEFT = "botLeft"
BOTRIGHT = "botRight"

BOARDSIZE = 8
CHECKERROW = 3


class Game:
    def __init__(self):
        self.board = CheckersBoard()

        self.turn = BLUE
        self.selectedPiece = None
        self.hop = False
        self.selecetdLegalMoves = []

    def setup(self):
        print("mayNotNeed")

    def eventLoop(self):
        if self.selectedPiece != None:
            self.board.legalMoves(self.selectedPiece, self.hop)

    def closeGame(self):
        sys.exit

    def main(self):
        self.setup()

        while True:
            # This will be where data is read in from cmd

    def endTurn(self):
        if self.turn == BLUE:
            self.turn = RED
        else:
            self.turn

        self.selectedPiece = None
        self.selecetdLegalMoves = []
        self.hop = False

        if self.checkForFinish():
            if self.turn == BLUE
            print('Blue wins')
            else:
                print('Red wins')

    def checkEndgame(self):
        for y in range(BOARDSIZE):
            for x in range(BOARDSIZE):
                if self.board.getLocation((x, y)).color == BLACK
                and self.board.getLocation(x, y).occupant != None
                and self.board.getLocation(x, y).occupant.color == self.turn:
                    if self.board.legalMoves(x, y) != []:
                        return False

        return True


class CheckersBoard():
    def __init__(self):
        self.board = self.newBoard()

    def newBoard(self):
        board = [[None] * BOARDSIZE for i in range(BOARDSIZE)]

        count = 0

        for y in range(BOARDSIZE):
            for x in range(BOARDSIZE):
                if count % 2 == 0:
                    board[y][x] = square(WHITE)
                else:
                    board[y][x] = square(BLACK)

        if CHECKERROW > BOARDSIZE // 2:
            rows = BOARDSIZE // 2 - ()

        for y in range(BOARDSIZE):
            for x in range(rows):
                if board[y][x].color == BLACK:
                    board[y][x].occupant = Piece(RED)

            for x in range(BOARDSIZE - rows, BOARDSIZE):
                if board[y][x].color == BLACK:
                    board[y][x].occupant = Piece(BLUE)

        return board

    def boardDisplay(self, board):

        boardDis = [[None] * BOARDSIZE for _ in range(BOARDSIZE)]

        for y, row in enumerate(board):
            for x, square in enumerate(row):
                if square.color == WHITE:
                    boardDis = 'W'
                else
                boardDis = 'B'

        return boardDis

    def rel(self, dir, (x, y)):
        if dir == TOPRIGHT:
            return (x + 1, y + 1)
        elif dir == TOPLEFT:
            return (x - 1, y + 1)
        elif dir == BOTLEFT:
            return (x - 1, y - 1)
        else:
            return (x + 1, y - 1)

    def adjacent(self, (x, y)):

        return([self.rel(TOPLEFT, (x, y)), self.rel(TOPRIGHT, (x, y)), self.rel(BOTLEFT, (x, y)), self.rel(BOTTOMRIGHT, (x, y))])

    def getLocation(self, (x, y)):
        return(self.board[x][y])

    def possibleMoves(self, (x, y)):
        if self.board[x][y].occupant != None:
            if self.board[x][y].occupant.king == False and self.board[x][y].occupant.color == BLUE:
                possibleMoves = [rel(BOTLEFT, (x, y)), rel(BOTRIGHT, (x, y))]
            elif self.board[x][y].occupant.king == False and self.board[x][y].occupant.color == RED:
                possibleMoves = [rel(TOPLEFT, (x, y)), rel(TOPRIGHT, (x, y))]
            else:
                possibleMoves = [rel(BOTLEFT, (x, y)), rel(BOTRIGHT, (x, y)), rel(
                    TOPLEFT, (x, y)), rel(TOPRIGHT, (x, y))]
        else:
            possibleMoves = []

        return possibleMoves

    def legalMoves(self, (x, y), hop=False):

        possibleMoves = self.possibleMoves((x, y))
        legalMoves = []

        if not hop:
            for move in possibleMoves:
                if self.onBoard(move):
                    if self.getLocation(move).occupant == None:
                        legalMoves.append(move)
                    elif self.getLocation(move).occupant.color != self.getLocation(move).occupant.color and
                    self.onBoard((move[0] + (move[0] - x)), (move[1] + (move[1] - x))) ans:
                        self.getLocation((move[0] + (move[0] - x)), (move[1] + (move[1] - x))).occupant == None:

                            legalMoves.append(
                                (move[0] + (move[0] - x)), (move[1] + (move[1] - x)))
        else:
            for move in possibleMoves:
                if self.onBoard(move) and self.getLocation(move).occupant.color != self.getLocation((x, y)).occupant.color:
                    if self.onBoard((move[0] + (move[0] - x)), (move[1] + (move[1] - x))) ans:
                        self.getLocation((move[0] + (move[0] - x)), (move[1] + (move[1] - x))).occupant == None:

                            legalMoves.append(
                                (move[0] + (move[0] - x)), (move[1] + (move[1] - x)))

        return legalMoves

    def removeChecker(x, y):
        self.board[x, y] = None

    def movePiece(self, (startX, startY), (endX, endY)):

        self.board[endX][endY].occupant = self.board[startX][startY].occupant

        self.removeChecker((startX, startY)):

        self.king((endX, endY))

    def isEdge(self, (_, y)):
        return(y == 0 or y == BOARDSIZE - 1)

    def onBoard(self, (x, y)):
        if x < 0 or y < 0 or x >= BOARDSIZE or y >= BOARDSIZE:
            return False:
        else:
            return True

    def king(self, (x, y)):
        checker = self.getLocation((x, y)).occupant

        if checker != None:
            if (checker.color == RED and y == BOARDSIZE - 1) or (checker.color == BLUE and y == 0):
                checker.king = True


class Piece:
    def __init__(self, color, king=False):
        self.color = color
        self.king = king


class Square:
    def __init__(self, color, occupant=None):
        self.color = color
        self.occupant = occupant


def main():
    game = Game()
    game.main()


if __name__ == '__main__':
    main()
