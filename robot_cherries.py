'''
https://leetcode.com/problems/cherry-pickup-ii/description/?envType=daily-question&envId=2024-02-08

- Approach is use of DFS 
- Key to use DFS here is: traverse all directions for each robot 


To use memoisaiton 
variables params of the functions are 
- current row , robot_a_column, robot_b_column 
so we would need 3D matrix which stores on current row, for robot 1 position, for robot 2 position, how much can we collected 
ex: dp[0][1][3]  = 10 --> in 0th row, when robot1 was at 1st column, robot2 at 3rd column, max cherries collected would be 10 
'''

class Solution(object):
    UNKNOWN = -1 
    def __init__(self) -> None:
        self.directions = [-1, 0, 1] # columnar directions
        


    def DFS(self, grid, current_row, robot_a_column, robot_b_column):
        
        # what is invalid answer ? when it is out of bounds 
        
        if current_row == len(grid): 
            return 0 
        
        cols = len(grid[0])
        # either of one gone out of bounds
        if robot_a_column >= cols or robot_b_column >= cols or robot_a_column < 0 or robot_b_column < 0:
            return 0
        
        if self.memo[current_row][robot_a_column][robot_b_column] != Solution.UNKNOWN:
            return self.memo[current_row][robot_a_column][robot_b_column]

        
        # in this iteration, max collected cheries would be total of both robots, unless both are on same column, so choose only
        total_cherries = grid[current_row][robot_a_column] + grid[current_row][robot_b_column] if robot_b_column != robot_a_column  else grid[current_row][robot_b_column]
        max_cherries_from_next_level=   0
        for robotA_dir in self.directions:
            for robotB_dir in self.directions:
                #explore all possibilites in next row 
                sub_max_collected_cheries = self.DFS(grid, current_row+1, robot_a_column+robotA_dir, robot_b_column+robotB_dir)
                max_cherries_from_next_level = max(max_cherries_from_next_level, sub_max_collected_cheries)

        self.memo[current_row][robot_a_column][robot_b_column] = max_cherries_from_next_level + total_cherries
        return self.memo[current_row][robot_a_column][robot_b_column]

    
    def cherryPickup(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        robot_a_column = 0 
        robot_b_column = len(grid[0])-1
        current_row = 0 
        self.memo = [[[Solution.UNKNOWN for col in range(len(grid[0]))] for col in range(len(grid[0]))] for row in range(len(grid))]
        print(self.memo)
        return self.DFS(grid,current_row, robot_a_column, robot_b_column)
    

grid = [[3,1,1],[2,5,1],[1,5,5],[2,1,1]]
obj = Solution()
print(obj.cherryPickup(grid))
