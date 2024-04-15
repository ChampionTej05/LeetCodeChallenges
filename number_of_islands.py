'''
https://leetcode.com/problems/number-of-islands/

We can use DFS to span our search 
- We start with cell of Land(1) and then search all its parts till we hit 0 on all sides 
    a. We could this as one island and mark current cell as 0 (so that it is not counted as 1 again )
    b. Repeat the process for all 
'''

def numIslands(grid):
    rows = len(grid)
    cols = len(grid[0])

    print(rows, cols)

    num_islands = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == "1":
                num_islands = num_islands +  1
                print("Incremented")
                mark_islands(grid, i, j)

    return num_islands

def mark_islands(grid, row, col):
    rows = len(grid)
    cols = len(grid[0])

    if 0 <= row < rows and 0 <= col < cols and grid[row][col] !="0":
        #mark the current cell as water 
        grid[row][col] = "0" 

        #explore now 
        mark_islands(grid, row, col-1)
        mark_islands(grid, row, col+1)
        mark_islands(grid, row-1, col)
        mark_islands(grid, row+1, col)




grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
print(numIslands(grid))