'''
https://leetcode.com/problems/word-search/?envType=daily-question&envId=2024-04-02

DFS based approach 

1. Run the DFS on all nodes to find which is the starting point 
'''


class Solution(object):
    
    
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        from collections import deque
        directions = [ (-1,0), (1,0), (0,1), (0,-1)]
        M = len(board)
        N = len(board[0])
        print("M, N", M, N)
        
        def DFS(row, col, word_start):
            
            
            # edge conditions , order is important 
            
            #  All words found, don't backtrack now 
            if word_start >= len(word):
                return True 
            
            # if not found , check if the valid indexes are passed 
            
            if not (0<= row < M and 0<= col < N):
                return False 
        
            # check if mismatch occured     
            if board[row][col] != word[word_start]:
                return False 
            
            
            chr = board[row][col]
            
            board[row][col]  = "~" # marking this with this character ensures we don't revisit this (loop condition)
            
            # check for all possible x and y 
            
            for dx, dy in directions :
                if DFS(row+dx, col+dy, word_start+1):
                    return True 
                
            board[row][col] = chr 
            return False 
            
                            
                    
            
        
        for i in range(M):
            for j in range(N):
                if board[i][j] == word[0]:
                    answer = DFS(i, j, 0)
                    if answer:
                        print(i, j, answer)
                        return True
        return False 
    
    
obj = Solution()

board, word = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"
board , word = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],"SEE"
board, word = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]] , "ABCB"
board, word = [["C","A","A"],["A","A","A"],["B","C","D"]], "AAB"
board , word = [["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]], "ABCESEEEFS"
print(obj.exist(board, word))