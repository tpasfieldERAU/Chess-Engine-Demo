import numpy as np

class Board:
    def __init__(self):
        self.black   = np.uint64(0b1111111111111111000000000000000000000000000000000000000000000000)
        self.rooks   = np.uint64(0b1000000100000000000000000000000000000000000000000000000010000001)
        self.pawns   = np.uint64(0b0000000011111111000000000000000000000000000000001111111100000000)
        self.kings   = np.uint64(0b0000100000000000000000000000000000000000000000000000000000001000)
        self.queens  = np.uint64(0b0001000000000000000000000000000000000000000000000000000000010000)
        self.bishops = np.uint64(0b0010010000000000000000000000000000000000000000000000000000100100)
        self.knights = np.uint64(0b0100001000000000000000000000000000000000000000000000000001000010)
    
    def makeMove(self, lgnString):
        pass

    def __coords2bits(self,x,y):
        if x>7 or x<0 or y>7 or y<0:
            raise IndexError("Index out of bounds.")
        index = x*8 + y
        val = 1 << (63-index)
        return np.uint64(val)

    def fromFEN(self, fenString):
        self.black   = np.uint64(0)
        self.rooks   = np.uint64(0)
        self.pawns   = np.uint64(0)
        self.kings   = np.uint64(0)
        self.queens  = np.uint64(0)
        self.bishops = np.uint64(0)
        self.knights = np.uint64(0)
        lines = fenString.split('/')
        binfo = lines.pop().split(' ')
        lines = lines+binfo
        for i in range(8):
            line = lines[i]
            k=0
            for j in range(len(line)):
                char = line[j]
                piece = self.__coords2bits(i, k)
                match char:
                    case 'r': 
                        self.rooks += piece
                        self.black += piece
                    case 'n':
                        self.knights += piece
                        self.black += piece
                    case 'b':
                        self.bishops += piece
                        self.black += piece
                    case 'q': 
                        self.queens += piece
                        self.black += piece
                    case 'k':
                        self.kings += piece
                        self.black += piece
                    case 'p':
                        self.pawns += piece
                        self.black += piece
                    case 'R': 
                        self.rooks += piece
                    case 'N':
                        self.knights += piece
                    case 'B':
                        self.bishops += piece
                    case 'Q': 
                        self.queens += piece
                    case 'K':
                        self.kings += piece
                    case 'P':
                        self.pawns += piece
                    case _:
                        k+=int(char)
                        continue
                k += 1

test = Board()
test.fromFEN("rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq e3 0 1")
print(bin(test.pawns))

test.fromFEN("rnbqkbnr/pp1ppppp/8/2p5/4P3/8/PPPP1PPP/RNBQKBNR w KQkq c6 0 2")
print(bin(test.pawns))
