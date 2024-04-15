

class Position:
    def __init__(self,x,y) -> None:
        self.x = x 
        self.y = y

    def __str__(self) -> str:
        return "x: {}, y: {}".format(self.x, self.y)


def on_diagonal(position1, position2):

    return abs(position1.x-position2.x) == abs(position1.y-position2.y)

def on_same_level(position1, position2):
    return position1.x == position2.x or position1.y == position2.y 

def check_piece_in_between(position1, piece, position2):
    minX = min(position1.x, position2.x)
    minY = min(position1.y, position2.y)

    maxX = max(position1.x, position2.x)
    maxY = max(position1.y, position2.y)

    return minX <= piece.x <= maxX and minY <= piece.y  <=  maxY

def minMovesToCaptureTheQueen(a: int, b: int, c: int, d: int, e: int, f: int):

    rookPosition = Position(a,b)
    bishopPosition = Position(c,d)
    queenPosition = Position(e,f)

    # check_if_bishop_in_line_with_queen
    if on_diagonal(queenPosition, bishopPosition):
        # if rook in between queen and bishop 
        # check_if_rook_in_line_with_queen
        if on_diagonal(queenPosition, rookPosition) and check_piece_in_between(queenPosition, rookPosition, bishopPosition):
            return 2
        else:
            return 1
        
    
    if on_same_level(queenPosition, rookPosition):
        # if bishop in between queen and rook 
        if on_same_level(queenPosition, bishopPosition) and check_piece_in_between(queenPosition, bishopPosition, rookPosition):
            return 2
        return 1
    
    return 2 


a , b = 3,5 
c, d = 1,8
e, f = 8,1 

print(minMovesToCaptureTheQueen(a,b,c,d,e,f))