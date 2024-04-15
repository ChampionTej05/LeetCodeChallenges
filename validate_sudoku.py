'''
https://leetcode.com/problems/valid-sudoku/

# validate rows 

# validate columns 

# validate each sudoku block 

i 0, 3, 6
j 0, 3, 6 

for row in range(0, 9, 3):
    for col in range(0, 9, 3):
        for k in range(3):
            i = k + row 
            j = k + col 
            print(i, j )
        

'''

def validate_rows(board):
    for row in range(0, 9):
        aset = set()
        for col in range(0,9):
            if board[row][col]!="." and  board[row][col] in aset:
                return False 
            
    return True 

def validate_columns(board):
    for col in range(0, 9):
        aset = set()
        for row in range(0,9):
            if board[row][col]!="." and  board[row][col] in aset:
                return False 
            
    return True 

def validate_cube(board):


    for row in range(0, 9, 3):
        for col in range(0, 9, 3):
            print(".......")
            aset = set()
            for k in range(3):
                i = k + row 
                for m in range(3):
                    j = m + col 
                    print(i, j )
                    if board[i][j]!="." and board[i][j] in aset:
                        print("INVALID Sudoku")
                        return
                    else:
                        aset.add(board[i][j])
                    
            print("......")
            
    print("Sudoku is valid ")
    
    
board =  [["5","3","1",".","7",".",".",".","."]
    ,["6","1",".","1","9","5",".",".","."]
    ,[".","9","8",".",".",".",".","6","."]
    ,["8",".",".",".","6",".",".",".","3"]
    ,["4",".",".","8",".","3",".",".","1"]
    ,["7",".",".",".","2",".",".",".","6"]
    ,[".","6",".",".",".",".","2","8","."]
    ,[".",".",".","4","1","9",".",".","5"]
    ,[".",".",".",".","8",".",".","7","9"]]


validate_cube(board)

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
        def validate_rows(board):
            for row in range(0, 9):
                aset = set()
                for col in range(0,9):
                    if board[row][col]!="." and  board[row][col] in aset:
                        return False 
                    aset.add(board[row][col])
                    
            return True 

        def validate_columns(board):
            for col in range(0, 9):
                aset = set()
                for row in range(0,9):
                    if board[row][col]!="." and  board[row][col] in aset:
                        return False 
                    aset.add(board[row][col])
            return True 

        def validate_cube(board):
            for row in range(0, 9, 3):
                for col in range(0, 9, 3):
                    print(".......")
                    aset = set()
                    for k in range(3):
                        i = k + row 
                        for m in range(3):
                            j = m + col 
                            print(i, j )
                            if board[i][j]!="." and board[i][j] in aset:
                                print("INVALID Sudoku")
                                return False 
                            else:
                                aset.add(board[i][j])
                            
                    print("......")
                    
            print("Sudoku is valid ")
            return True 
        

        
        if not validate_rows(board):
            return False 
        
        if not validate_columns(board):
            return False
        
        if not validate_cube(board):
            return False 
        
        return True 