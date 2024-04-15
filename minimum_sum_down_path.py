'''
https://leetcode.com/problems/minimum-falling-path-sum/?envType=daily-question&envId=2024-01-19

Seems like explore DFS Problems 


# def checkRow():
#     i = 0 
#     memo[i][0]  = 0
#     minSum = 0 
#     for j in cols:
#         temp = explore(memo, i, j, sum=0) 
#         if temp < minSum:
#             minSum = temp 

# def explore(memo, i, j, sum):
    
#     if isValid(i, j):
#         sum+=arr[i][j]
#         if memo[i][j] !=0:
#             memo[i][j] = min(sum, memo[i][j])
#             return memo[i][j]
        
#         #down 
#         down = explore(memo, row+1, col, sum)
#         #left 
#         left = explore(memo, row+1, col-1, sum)
#         #right 
#         right = explore(memo, row+1, col+1, sum)

#         memo[i][j] = min(down,left,right)
#         return memo[i][j]       
#     else:
#         return sum

It would make sense to build this bottom up 

We start with last row and then go on calculating paths for each element in that row 

#initialise the memo 
memo[N-1][j] = arr[N-1][j] for j in col 

#skipping last row 
for i in reversed(N-1):
    for j in range(N):
        memo[i][j] = min( F(i+1, j), F(i+1, j-1), F(i+1, j+1))

return min(memo[0])

F(i,j):
    if isValid(i,j):
        return memo[i][j]
    else:
        return INT_MAX
'''

class Solution:
    

    def __init__(self,matrix):
        self.matrix = matrix
        self.N = len(self.matrix)
        self.memo =[ [ 0 for j in range(self.N)] for i in range(self.N)]
        self.INT_MAX = 10**8

    def isValid(self, i, j):
        if 0<=i<self.N and 0<=j<self.N:
            return True
        return False 



    def get_sub_path_sum(self, i, j):
        if self.isValid(i,j):
            return self.memo[i][j]
        else:
            return self.INT_MAX


    def get_path_sum(self):
        #initialise for last row 

        for j in range(self.N):
            self.memo[self.N-1][j] = self.matrix[self.N-1][j]

        print(self.memo)
        
        # recur for others 
        
        for i in range(self.N-2, -1, -1):
            for j in range(self.N):
                temp = [self.get_sub_path_sum(i+1, j), self.get_sub_path_sum(i+1, j+1), self.get_sub_path_sum(i+1, j-1)]
                print("Temp: {}, for i: {}, j: {}".format(temp,i, j))
                self.memo[i][j] = min(temp) + self.matrix[i][j]
                print("memo after the update: {}".format(self.memo))

        
        return min(self.memo[0])
    
matrix = [[2,1,3],[6,5,4],[7,8,9]]
matrix = [[-19,57],[-40,-5]]

obj = Solution(matrix)

print(obj.get_path_sum())