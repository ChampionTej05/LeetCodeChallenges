'''
https://leetcode.com/problems/n-queens/description/
'''

class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.N = n
        self.answers = []
        self.board = [['.' for _ in range(n)] for _ in range(n)]  # Correctly initialize the board
        self.solve(0)
        return self.answers

    def solve(self, col):
        if col == self.N:
            # Convert the board configuration to the required format before adding to answers
            self.answers.append([''.join(row) for row in self.board])
            return

        for row in range(self.N):
            if self.isValidToPlaceQueen(row, col):
                self.board[row][col] = 'Q'
                self.solve(col + 1)  # Recurse to the next column
                self.board[row][col] = '.'  # Reset state during backtracking

    def isValidToPlaceQueen(self, row, col):
        # Check vertically up        
        j = col 
        
        while j>=0:
            if self.board[row][j] == 'Q':
                return False 
            j-=1;

        # Check diagonal left up
        i, j = row, col
        while i >= 0 and j >= 0:
            if self.board[i][j] == 'Q':
                return False
            i -= 1
            j -= 1

        # Check diagonal right up
        i, j = row, col
        while i <self.N and j >=0:
            if self.board[i][j] == 'Q':
                return False
            i += 1
            j -= 1

        return True

        
        
        
        
board = [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]] 
obj = Solution()

print(obj.solveNQueens(n=4))