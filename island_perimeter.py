'''
https://leetcode.com/problems/island-perimeter/?envType=daily-question&envId=2024-04-15


For each land cell cell(i,j), we add 4 to perimeter as 4 sides will be added 
Now, we can come to cell(i,j)  from either 
    - cell(i-1,j) or cell(i, j-1) 
    - if either of them is land, that means one edge would be same for them and hence that edge would be removed 
    - So if cell(i-1,j) or cell(i, j-1) == 1 , then perimeter = perimeter-2 
'''



class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        LAND = 1 
        WATER = 0  
        R = len(grid)
        C = len(grid[0])
        perimeter = 0 
        for row in range(R):
            for col in range(C):
                if grid[row][col] == LAND:
                    perimeter +=4 
                    
                    # did we come from left cell to this ?
                    if col>0 and grid[row][col-1] == LAND:
                        perimeter-=2 
                        
                    # did we come from above cell to this ?
                    if row>0 and grid[row-1][col] == LAND:
                        perimeter-=2 
                    
        return perimeter
        
        # # assuming this is starting with one land cell 
        # def DFS(  row, col, perimeter, visited):
        #     if row >=N or row <0 or col >=N or col <0:
        #         return 
            
        #     if grid[row][col] == WATER:
        #         return 
            
        #     if visited[row][col] :
        #         return 
            
        #     perimeter[0] = perimeter[0] + 4 
        #     visited[row][col] = True 
        #     print("For Cell ({}, {}), the perimeter added {}".format(row, col, perimeter))
            
        #     if row >=1 and grid[row-1][col] == LAND:
        #         perimeter[0] = perimeter[0] - 2 
        #         print("For Cell ({}, {}), the perimeter for row updated to {}".format(row, col, perimeter))
        #     if col >=1 and grid[row][col-1] == LAND:
               
        #         perimeter[0] = perimeter[0] -2 
        #         print("For Cell ({}, {}), the perimeter for col updated to {}".format(row, col, perimeter))
                
        #     DFS( row+1, col, perimeter, visited)
        #     DFS( row, col+1, perimeter, visited) 
                
                
        
        # for i in range(N):
        #     for j in range(N):
        #         if grid[i][j] == LAND:
        #             perimeter = [0]
        #             visited = [[False for _ in range(N)] for _ in range(N)] 
        #             print("Startign with row {}, col {}".format(i, j) )
        #             DFS(i, j, perimeter, visited) 
        #             print("Perimeter: ", perimeter)
        #             return perimeter[0]
            
                
                
                
                
obj = Solution()

grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]


print(obj.islandPerimeter(grid))
            
            
            